---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/storage.html
---

# Storage
<a name="storage"></a>

 Optimizing storage costs is essential for Microsoft workloads on AWS, as storage represents a significant portion of infrastructure expenses. AWS offers various cost-effective storage solutions, from newer generation EBS volumes (gp3) to fully managed services like Amazon FSx for Windows File Server and FSx for ONTAP. By implementing proper lifecycle management for volumes and snapshots, and choosing the right storage solutions for specific workload requirements, organizations can significantly reduce storage costs while maintaining or improving performance.

|  MSFTCOST05: How do you save on storage for your Microsoft workload?  |
| --- |
|   |

 The storage layer is a critical architecture component for most applications, including Microsoft workloads. Exploring the compatible Amazon storage offers can help you provide the required performance to your workloads and save costs. Constantly managing storage resources avoids unused resources, over-provisioning, and keeps the workloads performant.

**Topics**
+ [MSFTCOST05-BP01 Migrate Amazon EBS volumes from gp2 to gp3](msftcost05-bp01.md)
+ [MSFTCOST05-BP02 Control Amazon EBS volumes or snapshots lifecycle](msftcost05-bp02.md)
+ [MSFTCOST05-BP03 Use Amazon FSx for NetApp ONTAP](msftcost05-bp03.md)
+ [MSFTCOST05-BP04 Use Amazon FSx for Windows File Server](msftcost05-bp04.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
