---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/security-foundations.html
---

# Security foundations
<a name="security-foundations"></a>

| DRHCSEC01: Have you updated and validated your control objectives to address data residency compliance requirements? |
| --- |
|   |

 Based on your requirements and risks identified from your data residency compliance requirements, update and validate the control objectives and controls that apply to the workload. Ongoing validation of control objectives and controls help you measure the effectiveness of risk mitigation.

| DRHCSEC02: Does your account management strategy separate workloads that have different data residency requirements? |
| --- |
|   |

 Separating workloads at the AWS account level is recommended, as it provides a strong separation boundary and simplifies the implementation of preventative controls, such as Identity and Access Management (IAM) policies and service control policies (SCPs), as well as detective controls.

**Topics**
+ [DRHCSEC01-BP01 Update your control objectives to address your data residency compliance requirements](drhcsec01-bp01.md)
+ [DRHCSEC01-BP02 Document any differences in the treatment of log data into the control objectives](drhcsec01-bp02.md)
+ [DRHCSEC02-BP01 Separate workloads that have different data residency requirements](drhcsec02.md)
+ [DRHCSEC02-BP02 Manage workloads with similar data residency requirements efficiently](drhcsec02-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
