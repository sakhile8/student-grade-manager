from playwright.sync_api import Page


class StudentPage:
    def __init__(self, page: Page):
        self.page = page

        self.student_name = page.locator("#student-name")
        self.student_grade = page.locator("#student-grade")
        self.add_student_button = page.locator("#submit-student")
        self.student_rows = page.locator("#student-list tr")

    def open(self, url):
        self.page.goto(url)

    def add_student(self, name, grade):
        self.student_name.fill(name)
        self.student_grade.fill(str(grade))
        self.add_student_button.click()

    def get_student_count(self):
        return self.student_rows.count()

    def get_student(self, index):
        row = self.student_rows.nth(index)

        return {
            "name": row.locator("td").nth(0).inner_text(),
            "grade": row.locator("td").nth(1).inner_text()
        }