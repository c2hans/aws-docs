---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ccm-and-qpm-aurora-postgresql/targeted-business-outcomes.html
---

# Targeted business outcomes
<a name="targeted-business-outcomes"></a>

You can use this guide to achieve the following business outcomes with cluster cache management (CCM):
+ In the event of a failover, recover quickly to help maintain stable and optimal workload performance.
+ Reduce business losses caused by poor workload performance after a failover.
+ Help prevent unnecessary I/O costs after a failover.

You can use this guide to achieve the following business outcomes with query plan management (QPM):
+ Improve plan stability by forcing the optimizer to choose from a small number of approved plans. This prevents the optimizer from selecting a sub-optimal plan for a given SQL statement after system or database changes.
+ Optimize plans centrally and then distribute them globally.
+ Determine which indexes aren't being used, and evaluate the effects of adding or removing an index.
+ Automatically recognize any new minimum-cost plans that the optimizer identifies.
+ Test new optimizer features with minimal risk because you can decide to accept only the plan changes that improve performance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
