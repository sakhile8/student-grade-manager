from pathlib import Path

import pytest
from playwright.sync_api import Page

from pages.student_page import StudentPage


@pytest.fixture
def student_page(page: Page):
    student_page = StudentPage(page)

    app_url = (Path(__file__).resolve().parent / "app" / "index.html").as_uri()
    student_page.open(app_url)

    return student_page