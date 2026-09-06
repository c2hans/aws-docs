---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_user_a4.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS02-BP03 Stop the creation and maintenance of unused assets
<a name="sus_sus_user_a4"></a>

 Analyze application assets (such as pre-compiled reports, datasets, and static images) and asset access patterns to identify redundancy, underutilization, and potential decommission targets. Consolidate generated assets with redundant content (for example, monthly reports with overlapping or common datasets and outputs) to remove the resources consumed when duplicating outputs. Decommission unused assets (for example, images of products that are no longer sold) to free consumed resources and reduce the number of resources used to support the workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Manage static assets and remove assets that are no longer required.
+  Manage generated assets and stop generating and remove assets that are no longer required.
+  Consolidate overlapping generated assets to remove redundant processing.
+  Instruct third parties to stop producing and storing assets managed on your behalf that are no longer required.
+  Instruct third parties to consolidate redundant assets produced on your behalf.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/)

 **Related videos:**
+  [Building Sustainably on AWS](https://www.youtube.com/watch?v=ARAitMSIxc8)
