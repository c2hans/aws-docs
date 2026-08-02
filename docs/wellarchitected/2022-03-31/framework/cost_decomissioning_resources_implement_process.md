---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_decomissioning_resources_implement_process.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST04-BP02 Implement a decommissioning process
<a name="cost_decomissioning_resources_implement_process"></a>

 Implement a process to identify and decommission orphaned resources.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Implement a standardized process across your organization to identify and remove unused resources. The process should define the frequency searches are performed, and the processes to remove the resource to ensure that all organization requirements are met.

**Implementation steps**
+  **Create and implement a decommissioning process: **Working with the workload developers and owners, build a decommissioning process for the workload and its resources. The process should cover the method to verify if the workload is in use, and also if each of the workload resources are in use. The process should also cover the steps necessary to decommission the resource, removing them from service while ensuring compliance with any regulatory requirements. Any associated resources are also covered, such as licenses or attached storage. The process should provide notification to the workload owners that the decommissioning process has been executed.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/)
