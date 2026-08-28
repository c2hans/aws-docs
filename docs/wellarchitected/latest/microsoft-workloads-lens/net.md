---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/net.html
---

# .NET
<a name="net"></a>

 Optimizing .NET applications for cost-efficiency in the cloud involves leveraging the latest advancements in cross-platform .NET technologies. By migrating from traditional .NET Framework to modern, cross-platform .NET versions, organizations can take advantage of Linux-based deployments, including cost-effective ARM64 instances like AWS Graviton2. This shift not only reduces licensing costs but also opens up opportunities for serverless architectures and improved performance. AWS provides tools like AWS Transform to facilitate this modernization process, enabling .NET applications to fully exploit cloud benefits and achieve significant cost savings while enhancing scalability and maintainability.

|  MSFTCOST08: How do you save on .NET for your Microsoft workload?  |
| --- |
|   |

 While .NET Framework applications often utilize AWS virtual machines or containers, cross-platform .NET's introduction enables modern applications to fully exploit cloud benefits, including serverless environments. Cross-platform .NET further expands possibilities by offering performant hosting on ARM64 EC2 instances, like Graviton2 families. This advancement allows access to specialized compute options on Amazon EC2, optimizing performance for diverse workloads such as video encoding, web serving, and high-performance computing. Thus, .NET applications can now harness the latest processor technologies, adapting to specific task requirements and maximizing efficiency in the cloud environment.

**Topics**
+ [MSFTCOST08-BP01 Refactor to cross-platform .NET and move to Linux](msftcost08-bp01.net-and-move-to-linux.md)
+ [MSFTCOST08-BP02 Consider serverless architecture for your Microsoft .NET applications](msftcost08-bp02.net-applications.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
