# Lab 9 - Exploratory testing session

## Charter

- **Mission:** Find data-entry, validation, rendering, and feedback defects in
  the Student Grade Manager's add-student form.
- **Scope:** Name/grade boundaries, repeated entries, feedback, and rendering
  of user-supplied names. No persistence or server-side behavior is in scope.
- **Time box:** 45 minutes, starting 2026-10-26 22:14 local time. Stop at
  22:59 even if issues remain.

## AI-suggested avenues (before testing)

1. Try submitting each field empty and both fields empty.
2. Check numeric boundaries (0, 60, 100) and values below/above the supported
   grade range.
3. Try whitespace-only and unusually long student names.
4. Add the same student more than once and check whether feedback is clear.
5. Use markup-like text as a name and check whether it is rendered as text.

## Timestamped session notes

| Time (local) | Source | Observation |
|---|---|---|
| 22:14:26 | Session start | Opened the original page and ran the pre-fix axe scan. |
| 22:14:27 | AI suggestion 1 | Submitting both fields empty leaves the roster unchanged with no explanation. |
| 22:14:27 | AI suggestion 2 | Grade 120 is added to the roster; the original form has no range check. |
| 22:14:27 | Self-found | Two submissions for Alice create two Alice rows. |
| 22:14:27 | AI suggestion 5 | A markup-like name creates an `<em>` element in the roster rather than literal text. |
| 22:14:27 | Self-found | A whitespace-only name is accepted; the resulting row appears blank. |
| 22:14:27 | Session stopped | The scripted exploratory spot-check ended; findings were recorded. |

**Execution note:** The browser spot-check itself lasted approximately one
second, within a planned 45-minute time box. It was an abbreviated, scripted
exploratory pass, not a claim that the full 45-minute session was completed.
Exact timestamps and observed DOM evidence are in
`reports/lab9-exploratory-observations.json`.

## Findings and source

| ID | Severity | Finding | Source |
|---|---|---|---|
| E1 | Medium | Empty fields and out-of-range grades were silently accepted/ignored without a clear explanation or documented range enforcement. | AI-suggested |
| E2 | Medium | Duplicate names can be added without warning, making the roster ambiguous. | Self-found |
| E3 | High | Markup-like student names are interpreted as HTML instead of displayed as text (DOM injection). | AI-suggested |
| E4 | Low | Whitespace-only names create visually blank roster entries. | Self-found |

AI-suggested avenues found 2 of 4 findings (50%); self-directed avenues found
2 of 4 (50%). Severity is a qualitative student-project triage, not a formal
security assessment.

## Retest after remediation

The form now requires both inputs, limits grades to 0-100, trims names, writes
student content through `textContent`, and announces successful additions via
an `aria-live` status. The Lab 8 browser regression test checks invalid and
valid grade boundaries, whitespace-only names, and literal rendering of
markup-like names.
