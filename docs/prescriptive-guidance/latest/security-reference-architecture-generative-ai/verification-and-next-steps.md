---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/verification-and-next-steps.html
---

# Verification and next steps

The architecture review brings together the selected controls, evidence that they work, and decisions that still need an owner. Complete the same four steps introduced at the start of the guide and capture the results in one implementation record.

## Complete the four steps
<a name="complete-the-four-steps"></a>

1. **Establish account boundaries and choose a path.** Confirm the [development and production boundaries](https://dp8l2mfblnx2f.cloudfront.net/architecture/), including protected training within the production security boundary. Record the account owners, model service, and any knowledge bases, training jobs, tools, or agents. Use [AI models](https://dp8l2mfblnx2f.cloudfront.net/answers/) for **AI that answers**, [knowledge bases](https://dp8l2mfblnx2f.cloudfront.net/connects/) for **AI that connects**, and [agents and their tools](https://dp8l2mfblnx2f.cloudfront.net/acts/) for **AI that acts**.

1. **Threat model the workload.** Record the team that owns each deployment path and cross-account permission. Check the threat model against these boundaries and use its threat scenarios to guide verification.

1. **Apply the relevant controls.** Check the [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) or [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) guidance for the service in use. Add retrieval, tool, and action protections for the paths present in the workload. Reuse the organization's security foundation and assign any missing controls to an owner.

1. **Verify and record decisions.** Test allowed and denied behavior, retain evidence, and record remaining risks. Reassess when a model, dataset, tool, permission, or deployment changes.

## Test the boundaries that apply
<a name="test-the-boundaries-that-apply"></a>

|
|
| **Workload component** | **Test** | **Expected result** |
| --- |--- |--- |
| Model inference | Use an application role to invoke an unapproved model or endpoint. Try each exposed API without its required content checks. | IAM denies the unapproved resource. The application rejects requests that bypass required checks. |
| Application access | Request another user's session or result. Revoke access, wait for the configured session invalidation to complete, and then repeat the request. | The application denies access and returns no protected content. |
| Custom application and tool code | Reproduce a reported vulnerability in an approved test environment, apply the reviewed fix, and rerun that test and the affected authorization tests. | The exploit fails, permitted behavior still works, and the release record identifies the tested revision and remaining gaps. |
| Knowledge bases and retrieval | Submit another tenant's identifier to the application, omit retrieval scope, and request a document after you remove its source permission. | The application derives scope from verified identity or rejects the request. Unauthorized documents do not appear in results, citations, or caches. |
| Model customization | Run a job against an unrelated dataset and attempt to release a model that lacks independent approval. | The job can't access the dataset, and the release workflow blocks deployment. |
| Read-only tools | Attempt a write with the tool's actual downstream credentials. Call with missing or forged user context. | The downstream service denies the write and the authorization layer rejects invalid context. |
| Agent actions | Attempt self-approval through the agent and its tools. Test an independently approved request, changed parameters, replay, revoked permission, and a retry after partial failure. | Only the unchanged, valid, independently approved request proceeds. The record identifies the approver, decision, and time. The application rejects invalid approval, and retries prevent duplicate effects. |

For agents, run containment, recovery, and adversarial scenarios in an approved test environment. Verify that each test leaves usable evidence for the response team.

## Implementation record
<a name="implementation-record"></a>

|
|
| **Record** | **Include** |
| --- |--- |
| Workload and owner | Components, technology choices, data classification, and accountable teams |
| Architecture and permissions | Accounts, data flows, principals, tools, and downstream effects |
| Threat model | Workload data-flow diagram, assets, trust boundaries, plausible attacks, selected mitigations, and verification scenarios |
| Implemented controls | Owner, acceptance criteria, covered paths, configuration records, and applicable rule evaluations or security findings |
| Governance | Acceptable use policies, model approval criteria, applicable impact assessments, and the owners and review dates for these records |
| Verification | Expected allowed and denied behavior, test results, and audit records |
| Code vulnerability remediation | Code and context reviewed, known coverage gaps, available proof, finding dispositions, patch approvals, tests, and deployed revisions from the [application code review workflow](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/#review-custom-application-code-with-aws-continuum) |
| Remaining risk | Gap, consequence, owner, target decision date, and remediation or accepted risk |
| Reassessment | Changes that require a new review and the date of the next review |

Keep technical evidence and governance records in the organization's approved evidence repository. Map each requirement to its owner, implemented controls, evidence, and remaining gaps. Identify the workload version and review date so reviewers can determine whether the evidence still applies. Restrict access to sensitive records and track follow-up decisions to completion.

For AI workloads, retain the reviewed model or agent version, training and knowledge-source provenance, approval decisions, evaluation results, and exceptions. Update the record after a material change and at the scheduled review. Use these records in the organization's compliance and assurance reviews.

Your AWS account team can help you explore a [Security Health Improvement Program (SHIP)](https://aws.amazon.com/security/security-health-improvement-program/) engagement to assess the implementation and prioritize improvements.
