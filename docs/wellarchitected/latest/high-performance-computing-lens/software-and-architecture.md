---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/software-and-architecture.html
---

# Software and architecture
<a name="software-and-architecture"></a>

| HPCSUS02: Have you complemented your architecture with a remote desktop solution? |
| --- |
|   |

 By enabling remote visualization of simulation results, rather than transferring and storing large datasets locally, organizations can minimize network traffic, optimize resource usage, and improve overall sustainability of their HPC operations.

## HPCSUS02-BP01 Use a VDI solution to reduce data movement
<a name="hpcsus02-bp01"></a>

 In [SUS03-BP05 Use software patterns and architectures that best support data access and storage patterns](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a6.html), you understand how data is used within your workload, consumed by your users, transferred, and stored. For HPC workloads, Virtual Desktop Infrastructure (VDI) technologies help you reduce network traffic between the end-users' clients rather than transferring the entire data set and duplicating storage on-premises. In addition, optimizing data movement across the network reduces the total networking resources required for the workload and lowers its environmental impact.

### Implementation guidance
<a name="implementation-guidance-24"></a>

 Use a remote visualization technology, such as Amazon DCV or Amazon AppStream 2.0, to visualize the results of your simulations without the need of copying back the results.

## Key AWS services
<a name="key-aws-services-10"></a>
+  [Amazon DCV](https://aws.amazon.com/hpc/dcv/)
+  [Amazon AppStream 2.0](https://aws.amazon.com/appstream2/)
+  [Research and Engineering Studio on AWS](https://aws.amazon.com/hpc/res/)

## Resources
<a name="resources-10"></a>
+  [Empowering Researchers to Run HPC Workloads on AWS with Research Gateway](https://aws.amazon.com/blogs/apn/empowering-researchers-to-run-hpc-workloads-on-aws-with-research-gateway/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
