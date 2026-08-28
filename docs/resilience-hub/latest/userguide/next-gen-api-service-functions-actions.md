---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-service-functions-actions.html
---

# Service functions
<a name="next-gen-api-service-functions-actions"></a>

| Action | Method | Description |
| --- | --- | --- |
| CreateServiceFunction | POST | Create a service function with criticality (PRIMARY/SUPPLEMENTAL). |
| UpdateServiceFunction | POST | Update service function properties. |
| ListServiceFunctions | GET | List service functions for a service. |
| DeleteServiceFunction | POST | Delete a service function. |
| AddServiceFunctionResources | POST | Associate resources with a service function (up to 10 per call). |
| DeleteServiceFunctionResources | POST | Remove resource associations (up to 10 per call). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
