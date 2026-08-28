---
source_url: https://docs.aws.amazon.com/appstudio/latest/userguide/quotas.html
---

# Quotas for AWS App Studio
<a name="quotas"></a>

The following table describes quotas and limits for AWS App Studio.

|  |  |
| --- |--- |
| Maximum number of apps in an App Studio instance | 20 |
| Maximum number of applications published to the Testing or Production environment in an App Studio instance. A single application published to both Testing and Production counts as two published applications. | 6 |
| Maximum number of managed entities per app | 20 |
| Maximum number of rows returned per query | 3000 |
| Maximum number of rows of sample data per entity | 500 |
| Maximum run time of an automation | 2 minutes. Automations that run longer than 2 minute will fail. |
| Maximum automation input and output size | 5GB per input or output. |
| Maximum data size used by an automation or data action | 450MB per automation or data action run. |
| Page names and component names | Must be non-empty and unique. Must contain only letters, numbers underscores (\_) and dollar signs ($). Cannot contain spaces. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstudio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
