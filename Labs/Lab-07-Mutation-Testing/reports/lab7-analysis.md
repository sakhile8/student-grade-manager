# Lab 7 - Mutation testing report

## Experiment

Cosmic Ray 8.7.0 was used on `grade_manager.py`. Each run uses the Lab 6
AI-generated tests, the manual tests, or both. The original AI-only and
manual-only run databases are `cosmic-ai.sqlite` and `cosmic-manual.sqlite`;
their configuration files are in the Lab 7 folder. The combined run uses
`cosmic-combined.toml`.

| Suite | Mutants | Killed | Survived | Mutation score |
|---|---:|---:|---:|---:|
| AI-generated, before targeted tests | 114 | 41 | 73 | 35.96% |
| Manual, before targeted tests | 114 | 41 | 73 | 35.96% |
| Combined, before targeted tests | 114 | 41 | 73 | 35.96% |
| AI-generated, after targeted tests | 114 | 58 | 56 | 50.88% |
| Combined, after targeted tests | 114 | 58 | 56 | 50.88% |

The initial combined result is the mutant-by-mutant union of the stored AI and
manual runs. Both suites killed the same 41 mutants, so combining them did not
increase the initial score. The final AI-only and combined runs were rerun with
Cosmic Ray after the new tests. The manual suite did not change. See the
suite-specific JSON reports and `lab7-final-results.json` for the recorded
totals.

Mutation score is `killed / (killed + survived) * 100`. Invalid and skipped
mutants are excluded. The Lab 6 coverage logs report 69% statement coverage
for the AI and manual suites and 69% for combined. High coverage alone did not
mean assertions distinguished correct from incorrect behavior.

## Three AI-run survivors and the added tests

| Surviving mutant | Why the old assertions did not kill it | Test added |
|---|---|---|
| `add_grade`: change `student["name"] == name` to `<=` | The AI suite checked an unknown student only against an empty roster, so the comparison was never evaluated for a nonmatching existing student. | `test_add_grade_does_not_match_a_different_existing_student` |
| `get_average`: change `/` to `//` | Existing grades had whole-number averages, for which normal and floor division return the same value. | `test_get_average_preserves_fractional_averages` |
| `get_passing_students`: change `>= 60` to `> 60` | The AI suite had no passing-student boundary assertion at exactly 60. | `test_get_passing_students_includes_exactly_sixty` |

These tests are in
`../../Lab-06-Test-Design/tests/ai_generated/test_ai_generated.py`. Together,
they exercise the comparisons and result values that the original assertions
missed. See `lab7-final-results.json` for the measured final score.

## Reproduction

From `Labs/Lab-07-Mutation-Testing`:

```powershell
cosmic-ray baseline cosmic-ai.toml
cosmic-ray init cosmic-ai.toml $env:TEMP\grade-ai.sqlite
cosmic-ray exec cosmic-ai.toml $env:TEMP\grade-ai.sqlite
cosmic-ray baseline cosmic-manual.toml
cosmic-ray init cosmic-manual.toml $env:TEMP\grade-manual.sqlite
cosmic-ray exec cosmic-manual.toml $env:TEMP\grade-manual.sqlite
cosmic-ray baseline cosmic-combined.toml
cosmic-ray init cosmic-combined.toml $env:TEMP\grade-combined.sqlite
cosmic-ray exec cosmic-combined.toml $env:TEMP\grade-combined.sqlite
```
