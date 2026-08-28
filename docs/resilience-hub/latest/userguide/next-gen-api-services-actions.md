---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-services-actions.html
---

# Services
<a name="next-gen-api-services-actions"></a>

| Action | Method | Description |
| --- | --- | --- |
| CreateService | POST | Create a service with regions, permission model, report configuration, and dependency discovery settings. |
| UpdateService | POST | Update service configuration including permission model and dependency discovery. |
| GetService | GET | Retrieve full service details including effective policy values and resilience score. |
| ListServices | GET | List services, filterable by systemId, userJourneyId, organizationId, ouId, accountId, assessmentStatus, and policyArn. |
| DeleteService | POST | Delete a service. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
