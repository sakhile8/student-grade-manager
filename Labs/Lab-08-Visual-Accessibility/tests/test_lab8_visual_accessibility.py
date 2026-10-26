import json
from pathlib import Path

from PIL import Image, ImageChops
from playwright.sync_api import Page, expect


PROJECT_ROOT = Path(__file__).resolve().parents[1]
APP_URL = (
    PROJECT_ROOT.parent
    / "Lab-05-Test-Automation"
    / "app"
    / "index.html"
).as_uri()
REPORTS = PROJECT_ROOT / "reports"


def test_grade_manager_passes_axe_scan(page: Page):
    page.set_viewport_size({"width": 1280, "height": 900})
    page.goto(APP_URL)
    page.add_script_tag(
        url="https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.3/axe.min.js"
    )

    results = page.evaluate(
        """async () => {
            const results = await axe.run(document);
            return {
                violations: results.violations.map(({ id, impact, help, nodes }) => ({
                    id,
                    impact,
                    help,
                    targets: nodes.map(({ target }) => target)
                })),
                passes: results.passes.length
            };
        }"""
    )

    REPORTS.mkdir(exist_ok=True)
    (REPORTS / "accessibility_after.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="utf-8"
    )
    assert results["violations"] == []


def test_student_form_validates_input_and_renders_text(page: Page):
    page.set_viewport_size({"width": 1280, "height": 900})
    page.goto(APP_URL)
    name = page.get_by_label("Student Name")
    grade = page.get_by_label("Grade (0-100)")

    expect(name).to_have_attribute("required", "")
    expect(grade).to_have_attribute("required", "")
    expect(grade).to_have_attribute("min", "0")
    expect(grade).to_have_attribute("max", "100")

    name.fill("Alice")
    grade.fill("101")
    page.get_by_role("button", name="Add Student").click()
    expect(page.locator("#student-list tr")).to_have_count(0)

    name.fill("   ")
    grade.fill("85")
    page.get_by_role("button", name="Add Student").click()
    expect(page.locator("#student-list tr")).to_have_count(0)

    name.fill("<em>Alice</em>")
    grade.fill("0")
    page.get_by_role("button", name="Add Student").click()
    row = page.locator("#student-list tr").first
    expect(row.locator("td").first).to_have_text("<em>Alice</em>")
    expect(row.locator("td").nth(1)).to_have_text("0")
    expect(row.locator("em")).to_have_count(0)
    expect(page.get_by_role("status")).to_contain_text("Added <em>Alice</em>.")


def test_visual_change_has_a_measurable_pixel_diff(page: Page):
    page.set_viewport_size({"width": 1280, "height": 900})
    page.goto(APP_URL)
    screenshot = REPORTS / "visual_after.png"
    REPORTS.mkdir(exist_ok=True)
    page.screenshot(path=str(screenshot), full_page=True)

    baseline = Image.open(REPORTS / "visual_baseline.png").convert("RGB")
    current = Image.open(screenshot).convert("RGB")
    assert baseline.size == current.size

    difference = ImageChops.difference(baseline, current)
    pixel_bytes = difference.tobytes()
    changed_pixels = sum(
        1
        for offset in range(0, len(pixel_bytes), 3)
        if max(pixel_bytes[offset : offset + 3]) > 16
    )
    pixel_difference_percent = changed_pixels / (baseline.width * baseline.height) * 100

    report = {
        "baseline": "visual_baseline.png",
        "comparison": "visual_after.png",
        "viewport": {"width": 1280, "height": 900},
        "changed_pixels": changed_pixels,
        "total_pixels": baseline.width * baseline.height,
        "pixel_difference_percent": round(pixel_difference_percent, 2),
        "threshold_per_pixel": 16,
    }
    (REPORTS / "visual_diff_report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    assert changed_pixels > 0
