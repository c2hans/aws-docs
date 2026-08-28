---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsus01-bp01.html
---

# HNSUS01-BP01 Decommission unused assets and consolidate redundant resources
<a name="hnsus01-bp01"></a>

 Regularly audit your workload to identify and remove unused or redundant assets (for example, orphaned storage volumes, inactive EC2 instances, and outdated datasets). Consolidate overlapping resources (for example, duplicate reports and redundant databases) to eliminate waste.

 **Desired outcome:** Reduced resource consumption and minimized environmental footprint by eliminating unnecessary infrastructure.

 **Level of risk exposed if this best practice is not established:** Low

 **Benefits of establishing this best practice:**
+  Frees up compute, storage, and network resources
+  Lowers energy consumption and costs
+  Simplifies architecture and improves maintainability

## Implementation guidance
<a name="implementation-guidance-60"></a>
+  Identify underutilized resources. For example, you can achieve this using AWS Trusted Advisor Cost Optimization Checks
+  Use policies to automate deletion of unused assets. For example, you can achieve this using Amazon S3 Lifecycle Policies and Amazon Data Lifecycle Manager

## Resources
<a name="resources-49"></a>
+  [AWS Trusted Advisor: Cost Optimization Checks](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
+  [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
+  [Delete Amazon Data Lifecycle Manager policies](https://docs.aws.amazon.com/ebs/latest/userguide/delete.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
