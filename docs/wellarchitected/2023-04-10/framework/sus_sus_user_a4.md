---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sus_sus_user_a4.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS02-BP03 Stop the creation and maintenance of unused assets
<a name="sus_sus_user_a4"></a>

Decommission unused assets in your workload to reduce the number of cloud resources required to support your demand and minimize waste.

 **Common anti-patterns:**
+  You do not analyze your application for assets that are redundant or no longer required.
+  You do not remove assets that are redundant or no longer required.

 **Benefits of establishing this best practice:** Removing unused assets frees resources and improves the overall efficiency of the workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Unused assets consume cloud resources like storage space and compute power. By identifying and eliminating these assets, you can free up these resources, resulting in a more efficient cloud architecture. Perform regular analysis on application assets such as pre-compiled reports, datasets, static images, and asset access patterns to identify redundancy, underutilization, and potential decommission targets. Remove those redundant assets to reduce the resource waste in your workload.

 **Implementation steps**
+  Use monitoring tools to identify static assets that are no longer required.
+  Before removing any asset, evaluate the impact of removing it on the architecture.
+  Develop a plan and remove assets that are no longer required.
+  Consolidate overlapping generated assets to remove redundant processing.
+  Update your applications to no longer produce and store assets that are not required.
+  Instruct third parties to stop producing and storing assets managed on your behalf that are no longer required.
+  Instruct third parties to consolidate redundant assets produced on your behalf.
+  Regularly review your workload to identify and remove unused assets.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/)
+ [ How do I terminate active resources that I no longer need on my AWS account? ](https://aws.amazon.com/premiumsupport/knowledge-center/terminate-resources-account-closure/)

 **Related videos:**
+ [ How do I check for and then remove active resources that I no longer need on my AWS account? ](https://www.youtube.com/watch?v=pqg9AqESRlg)
