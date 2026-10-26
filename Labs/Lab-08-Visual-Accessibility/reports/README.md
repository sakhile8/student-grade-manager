# Lab 8 evidence

`visual_baseline.png` is the original unstyled page and `visual_after.png` is the
updated layout, both captured at 1280 x 900. `visual_diff_report.json` records
the changed-pixel percentage; a pixel counts when any RGB channel differs by
more than 16. The measured difference is 1.61%.

| Report | Finding | WCAG level | Impact |
|---|---|---|---|
| `accessibility_before.json` | `landmark-one-main`; missing main landmark | Best practice (not mapped to A/AA by axe) | Moderate |
| `accessibility_before.json` | `region`; page content outside landmarks | Best practice (not mapped to A/AA by axe) | Moderate |
| `accessibility_after.json` | No violations; 32 passing rules | N/A | N/A |

The two best-practice findings were fixed by adding a `<main>` landmark and
placing the student form and roster in landmarks. The after report is produced
by `tests/test_lab8_visual_accessibility.py`, which loads axe-core 4.10.3 from
cdnjs, writes the scan JSON, and fails on any violation. That scan requires
network access to the CDN.

**Reflection:** A pixel-diff test would not detect missing landmarks, inaccessible
keyboard navigation, an unlabeled control, or incorrect screen-reader
semantics when the pixels remain unchanged. This is why visual comparison and
an accessibility rules scan complement rather than replace each other.
