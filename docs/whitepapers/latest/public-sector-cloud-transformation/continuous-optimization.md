---
source_url: https://docs.aws.amazon.com/whitepapers/latest/public-sector-cloud-transformation/continuous-optimization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Continuous optimization
<a name="continuous-optimization"></a>

 [Continuous optimization](https://aws.amazon.com/blogs/enterprise-strategy/continuous-optimization/) is an iterative process where we implement a set of simple, high-impact cost reduction methods across all applications, and then measure and report the cost savings results. The process is then repeated on a regular cadence. Following are two essential tenets of continuous optimization:
+  **Tenet 1: Cost optimization is not a project, it’s a way of life**.

  AWS is never finished with continuous optimization. It is integrated into existing operating procedures, and AWS works to improve the process every cycle. The process is designed to be low-cost and low-overhead. Within those limitations, continuous optimization is designed to find out exactly what level of super-optimization is possible. How inexpensively can we run each application? is the question to be answered
+  **Tenet 2: Focus on big impact / low effort**.

  Each optimization idea should be ranked by its impact/effort ratio, and ideas should be implemented starting from the top of the list and progress downward until reaching a point where the effort exceeds the impact. This line will be drawn in a different place by different organizations, and can change over time to suit the business priorities.

## The continuous optimization process
<a name="the-continuous-optimization-process"></a>

 The following are three categories of optimization along with several examples of each.

### Category 1: Remove
<a name="category-1-remove"></a>

 These are the easiest ideas that produce the most cost savings.

1.  **Remove unused applications** — Determine whether the application is really needed. If not, delete all infrastructure and data associated with it.

1.  **Remove unused instances** — Look for instances that are no longer used, and then shut them down. [AWS CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) can be a useful starting point to discover idle instances.

1.  **Remove unused storage volumes** — Volumes unattached from instances (orphan volumes) are almost never needed any longer. A helpful policy is to require that needed orphan volumes have a tag specifying who needs it and why it is needed. Verify that they’re not needed and remove them.

1.  **Remove unused snapshots** — Storage and instance snapshots accumulate when there isn’t an active process to remove them. Determine what is needed and remove the rest.

1.  **Reallocate or sell unutilized reserved instances** — AWS Cost Explorer is a great tool for finding unused RIs. Either move an on-demand instance to an instance type that is covered by an RI or resell them on the [Amazon EC2 Reserved Instance Marketplace](https://aws.amazon.com/ec2/purchasing-options/reserved-instances/marketplace/).

### Category 2: Resize
<a name="category-2-resize"></a>

Everything that can’t be deleted should be evaluated to ensure it isn’t over-provisioned.

1.  **Resize instances** — Use Amazon CloudWatch Metrics to determine which instances can be downsized.

1.  **Resize storage volumes** — Look at storage volume utilization and reduce any unnecessary free space. Re-evaluate any overgenerous free space policies that were carried over from on-premises. It’s possible to be far more efficient with storage in AWS.

1. **Reduce performance of storage volumes** — Use Amazon CloudWatch Metrics to determine if Provisioned Input/Output Operations Per Second (PIOPS) volumes can be detuned or moved to less expensive non-PIOPS volumes.

### Category 3: Refactor
<a name="category-3-refactor"></a>

This category should be done less frequently, as it takes more effort and is less likely to produce results after the first pass. However, the first pass will likely produce significant results, so this step should be done at least once. After that a quarterly or annual review is a reasonable cadence. Look at each application and ensure that the architecture is as efficient as possible. If needed, ask your AWS account team to perform an AWS Well Architected Review.

Managing costs in AWS can be a simple and productive process. Experiment with these ideas and invent new ones.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
