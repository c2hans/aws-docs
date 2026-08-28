---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/access-management.html
---

# Access management
<a name="access-management"></a>

 Controlling access to Microsoft workloads involves implementing proper authentication, authorization, and auditing mechanisms that integrate with both Microsoft and AWS identity services. This focus area addresses how to establish centralized identity management, implement least privilege principles, and maintain comprehensive access monitoring across your Microsoft environment.

|  MSFTSEC02: How do you manage and regulate user access to your Microsoft workload environment?  |
| --- |
|   |

 To control access to your Microsoft workload, utilize the authentication and authorization tools provided by AWS, Microsoft, and trusted third-party vendors. Implement a least-privilege approach, verifying that users and systems have only the permissions necessary for their roles.

**Topics**
+ [MSFTSEC02-BP01 Align your Microsoft workload access with organizational identity strategy](msftsec02-bp01.md)
+ [MSFTSEC02-BP02 Implement logging to track access and authorization changes](msftsec02-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
