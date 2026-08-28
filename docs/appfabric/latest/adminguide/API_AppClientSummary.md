---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/API_AppClientSummary.html
---

# AppClientSummary
<a name="API_AppClientSummary"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Contains information about an AppClient.

**Topics**

| Parameter | Description |
| --- | --- |
| **arn** | The Amazon Resource Name (ARN) of the AppClient.<br />Type: String<br />Length Constraints: Minimum length of 1. Maximum length of 1011.<br />Pattern: `arn:.+`<br />Required: Yes |
| **verificationStatus** | The AppClient verification status.<br />Type: String<br />Valid Values: `pending_verification \| verified \| rejected`<br />Required: Yes |
| **appClientId** | The ID of the AppClient. Meant to be used in o-auth flows for the app-client.<br />Type: String<br />Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br />Required: No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
