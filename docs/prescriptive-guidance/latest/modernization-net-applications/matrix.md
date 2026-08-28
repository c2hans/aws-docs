---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/matrix.html
---

# Decision matrix
<a name="matrix"></a>

The following table summarizes the migration and modernization options for legacy .NET applications, based on your use case and resources.

|  |  |
| --- |--- |
|   | Migration strategy and architecture |
| Use case | Rehost | Replatform as a Windows container  | Re-architect as a Linux container  | Re-architect as microservices in Linux containers | Re-architect as microservices without containers <br />  |
| You have resources for refactoring. | No | No | Yes | Yes | Yes |
| Your .NET legacy application is in constant use. | Yes | Yes | Yes | Yes | No |
| You can resolve .NET Framework dependencies. | No | No | Yes | Yes | Yes |
| You can remove Windows dependencies. | No | No | Yes | Yes | Yes |
| You want to run your application as a native Windows application on an Amazon Elastic Compute Cloud (Amazon EC2) instance. | Yes | No | No | No | No |
| Your code can be ported from .NET Framework to .NET Core or .NET 6. | No | No | Yes | Yes | Yes |
| You want to split your monolithic application. | No | No | No | Yes | Yes |

The following sections describe these options in detail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
