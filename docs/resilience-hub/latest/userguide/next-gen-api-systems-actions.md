---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-systems-actions.html
---

# Systems
<a name="next-gen-api-systems-actions"></a>

| Action | Method | Description |
| --- | --- | --- |
| CreateSystem | POST | Create a system with optional dependency discovery enablement. |
| UpdateSystem | POST | Update system description, dependency discovery, and KMS key. |
| GetSystem | GET | Retrieve system details. |
| ListSystems | GET | List systems, filterable by organizationId, ouId, and accountId. |
| DeleteSystem | POST | Delete a system (must have no associated services). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
