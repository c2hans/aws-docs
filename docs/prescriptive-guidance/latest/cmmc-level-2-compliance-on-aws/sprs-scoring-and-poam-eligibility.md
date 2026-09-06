---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/sprs-scoring-and-poam-eligibility.html
---

# SPRS scoring and POA&M eligibility
<a name="sprs-scoring-and-poam-eligibility"></a>

Understanding the SPRS scoring model is essential for prioritizing your remediation efforts and understanding what is required for certification.

## Scoring model
<a name="scoring-model"></a>

Your SPRS score starts at 110 (one point per requirement) and decreases based on unmet requirements. The deduction depends on whether the requirement is classified as Basic or Derived:

|
|
| Requirement type | Count | Deduction if NOT MET | Maximum deduction |
| --- |--- |--- |--- |
| Basic | 30 | 5 points | 150 points |
| Derived | 80 | 1 point | 80 points |

The minimum possible score is -120 (all requirements NOT MET). The deduction can exceed the starting score because Basic requirements deduct 5 points each. You must submit your SPRS score to the DoD SPRS portal and keep it current.

To achieve Conditional CMMC Status, your score must be 88 or higher (equivalent to 80 percent of the maximum 110), with all NOT MET items on eligible POA&Ms. To achieve Final CMMC Status, all 110 requirements must be MET and all POA&Ms closed. The 88-point threshold is the number that matters most when you are planning remediation: prioritize the POA&M-ineligible requirements first (no certification is possible if any are NOT MET), then close enough Basic and Derived gaps to reach 88.

## POA&M eligibility
<a name="poam-eligibility"></a>

Of the 110 requirements, 84 are POA&M-eligible (can be deferred with a remediation plan) and 26 are POA&M-ineligible (must be MET at the time of assessment). If any POA&M-ineligible requirement is NOT MET, your organization cannot achieve even Conditional status regardless of overall score. Each POA&M must be closed within 180 days of the initial assessment, and the C3PAO performs a closeout assessment using the same evidence standards.

The 26 POA&M-ineligible requirements span these control families:

|
|
| Family | POA&M-ineligible requirements |
| --- |--- |
| Access Control (AC) | 3.1.1, 3.1.2, 3.1.20, 3.1.22 |
| Audit and Accountability (AU) | 3.3.1, 3.3.2 |
| Configuration Management (CM) | 3.4.1, 3.4.2 |
| Identification and Authentication (IA) | 3.5.1, 3.5.2 |
| Media Protection (MP) | 3.8.3 |
| Personnel Security (PS) | 3.9.1, 3.9.2 |
| Physical Protection (PE) | 3.10.1, 3.10.2 |
| Risk Assessment (RA) | 3.11.1 |
| Security Assessment (CA) | 3.12.1, 3.12.3, 3.12.4 |
| System and Comm. Protection (SC) | 3.13.1, 3.13.2, 3.13.5 |
| System and Info. Integrity (SI) | 3.14.1, 3.14.2, 3.14.4, 3.14.5 |

## Remediation prioritization
<a name="remediation-prioritization"></a>

When building your remediation roadmap, prioritize in this order:

1. POA&M-ineligible requirements first, as these are blockers. If any are NOT MET, no certification is possible.

1. 5-point Basic requirements next, as they have the highest score impact per remediation effort.

1. 1-point Derived requirements last, addressed in descending order of implementation complexity (easy wins first).

Calculate your projected SPRS score after each planned remediation to track progress toward the 88-point Conditional threshold.
