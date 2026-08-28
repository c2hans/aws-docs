---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/preparing-for-the-c3pao-assessment.html
---

# Preparing for the C3PAO assessment
<a name="preparing-for-the-c3pao-assessment"></a>

The CMMC Assessment Process (CAP) v2.0 defines a structured lifecycle for your assessment. Understanding what happens in each phase helps you prepare effectively.

## Assessment phases
<a name="assessment-phases"></a>

|
|
| Phase | Key activities | What you should prepare |
| --- |--- |--- |
| Preliminary Proceedings | C3PAO receives your assessment request, confirms your legal entity (CAGE code), frames the assessment scope, identifies conflicts of interest, and executes the contractual agreement. | Your CAGE code, SPRS UID from any prior self-assessment, and a clear definition of your assessment scope. |
| Phase 1: Pre-Assessment | Lead CCA reviews your SSP for completeness and accuracy. Assessment scope is validated per 32 CFR § 170.19(c). CRM availability and ESP personnel participation are confirmed. The Lead CCA determines if you are prepared to proceed. | A complete, final-form SSP. CRM documentation for all ESPs. Evidence that your controls are implemented and operating. ESP contacts available for interviews. |
| Phase 2: Assess Conformity | Assessment Team evaluates implementation of all 110 requirements using examine, interview, and test methods per NIST SP 800-171A. Depth and coverage sampling is performed. Daily checkpoint meetings occur between the Assessment Team and your organization. | Personnel who can explain control implementation during interviews. Live demonstrations of controls in operation. Access to your evidence repository and compliance dashboards. |
| Phase 3: Report Results | Results compiled per requirement (MET, NOT MET, NOT APPLICABLE). Final SPRS score calculated. POA&Ms documented for eligible NOT MET requirements. Results uploaded to CMMC eMASS. | Understanding of your projected score and any remaining gaps. POA&M documentation ready for any controls not yet fully implemented. |

## Preparing for assessor questions
<a name="preparing-for-assessor-questions"></a>

During Phase 2, your C3PAO assessors will ask specific questions mapped to assessment objectives. The CMMC Assessment Guide Level 2 v2.13 includes potential assessment considerations for each control. Preparing your team to answer these questions is as important as having the technical controls in place.

To prepare effectively:
+ Identify which personnel will be interviewed for each control family. Typical interviewees include system and network administrators, personnel with information security responsibilities, personnel with account management responsibilities, incident response team members, and management leads.
+ For each control, review the assessment objectives from NIST SP 800-171A and confirm that your team can explain how each objective is satisfied.
+ Map each assessor question to the evidence artifact that answers it. When the assessor asks "How do you enforce least privilege?", your team should be able to point to specific IAM policies, IAM Access Analyzer findings, and IAM Identity Center permission sets.
+ Conduct mock interviews before the assessment. Have someone unfamiliar with the implementation ask the assessor questions and evaluate whether the responses are clear, specific, and supported by evidence.

## Assessment findings
<a name="assessment-findings"></a>

Per the Assessment Guide and 32 CFR § 170.24, each requirement results in one of three findings:

|
|
| Finding | Meaning |
| --- |--- |
| MET | All assessment objectives are satisfied. Evidence must be in final form. Drafts, working guides, and unapproved policies are not accepted. |
| NOT MET | One or more objectives are not satisfied. If the requirement is POA&M-eligible, it can be placed on a POA&M for remediation within 180 days. |
| NOT APPLICABLE | The requirement does not apply to the system as scoped. Must be justified in the SSP. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
