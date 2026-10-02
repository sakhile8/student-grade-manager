"""
Lab 4 - Requirements Traceability and Test Management

Library System Test Cases

These tests document the 16 test cases designed from the
eight supplied functional requirements.

The actual Library System implementation is not part of
the current project, so these tests are currently skipped.
They serve as executable test specifications.
"""

import pytest


# ============================================================
# REQ-001: User Registration
# ============================================================

def test_tc001_successful_user_registration():
    """REQ-001: Register with unique email and password >= 8 characters."""
    pytest.skip("Library System implementation not available")


def test_tc002_registration_with_short_password():
    """REQ-001: Reject password shorter than 8 characters."""
    pytest.skip("Library System implementation not available")


# ============================================================
# REQ-002: Duplicate Email Registration
# ============================================================

def test_tc003_registration_with_unique_email():
    """REQ-002: Allow registration with a unique email address."""
    pytest.skip("Library System implementation not available")


def test_tc004_registration_with_existing_email():
    """REQ-002: Reject registration when email is already in use."""
    pytest.skip("Library System implementation not available")


# ============================================================
# REQ-003: Book Search
# ============================================================

def test_tc005_search_book_by_title():
    """REQ-003: Search catalogue by title and return results within 2 seconds."""
    pytest.skip("Library System implementation not available")


def test_tc006_search_using_nonexistent_isbn():
    """REQ-003: Search using an ISBN with no matching book."""
    pytest.skip("Library System implementation not available")


# ============================================================
# REQ-004: No Search Results
# ============================================================

def test_tc007_search_with_no_matching_results():
    """REQ-004: Display 'No results found' when there are no matches."""
    pytest.skip("Library System implementation not available")


def test_tc008_search_with_matching_book():
    """REQ-004: Display matching results instead of 'No results found'."""
    pytest.skip("Library System implementation not available")


# ============================================================
# REQ-005: Book Borrowing
# ============================================================

def test_tc009_borrow_available_book():
    """REQ-005: Registered user can borrow an available book."""
    pytest.skip("Library System implementation not available")


def test_tc010_borrow_unavailable_book():
    """REQ-005: User cannot borrow an unavailable book."""
    pytest.skip("Library System implementation not available")


# ============================================================
# REQ-006: Borrowing Restrictions
# ============================================================

def test_tc011_borrow_third_book():
    """REQ-006: User with two books can borrow a third book."""
    pytest.skip("Library System implementation not available")


def test_tc012_attempt_to_borrow_fourth_book():
    """REQ-006: User with three books cannot borrow a fourth book."""
    pytest.skip("Library System implementation not available")


# ============================================================
# REQ-007: Return Processing
# ============================================================

def test_tc013_return_book_on_time():
    """REQ-007: Record return and calculate zero overdue fine."""
    pytest.skip("Library System implementation not available")


def test_tc014_return_overdue_book():
    """REQ-007: Calculate overdue fine at P2.00 per day."""
    pytest.skip("Library System implementation not available")


# ============================================================
# REQ-008: Overdue Notifications
# ============================================================

def test_tc015_two_day_due_date_notification():
    """REQ-008: Email user two days before the due date."""
    pytest.skip("Library System implementation not available")


def test_tc016_no_early_due_date_notification():
    """REQ-008: Do not send the two-day reminder too early."""
    pytest.skip("Library System implementation not available")