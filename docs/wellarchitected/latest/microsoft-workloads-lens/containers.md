---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/containers.html
---

# Containers
<a name="containers"></a>

 Containerizing Windows workloads represents a significant opportunity to optimize infrastructure costs and improve operational efficiency. AWS provides comprehensive tools and services to support this transformation, such as advanced optimization tools like AWS Compute Optimizer for Fargate tasks and Kubecost for EKS environments. By leveraging these solutions along with modern scaling strategies like Karpenter, organizations can reduce their Windows Server footprint while gaining the benefits of containerized deployments, including improved resource utilization and automated scaling.

|  MSFTCOST07: How do you save on Windows Server footprint moving to Windows Containers?  |
| --- |
|   |

 Containers can help optimize the infrastructure and also promote agility for your workloads. If compatible, applications that require components from the Windows OS may leverage the infrastructure modernization of running on Windows containers.

**Topics**
+ [MSFTCOST07-BP01 Optimize AWS Fargate tasks with AWS Compute Optimizer](msftcost07-bp01.md)
+ [MSFTCOST07-BP02 Improve Amazon Elastic Kubernetes Service cost tracking with Kubecost](msftcost07-bp02.md)
+ [MSFTCOST07-BP03 Change your scale strategy for Windows Containers on Kubernetes using Karpenter](msftcost07-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
