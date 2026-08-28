---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/API_VerificationDetails.html
---

# VerificationDetails
<a name="API_VerificationDetails"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Contains the status and reason for the AppClient verification.

**Topics**

| Parameter | Description |
| --- | --- |
| **verificationStatus** | The AppClient verification status.<br />Type: String<br />Valid Values: `pending_verification \| verified \| rejected`<br />Required: Yes |
| **statusReason** | The AppClient verification status reason.<br />Type: String<br />Length Constraints: Minimum length of 1. Maximum length of 1024.<br />Required: No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
