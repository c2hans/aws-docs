---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.3---choose-the-optimal-storage-based-on-access-patterns-data-growth-and-the-performance-metrics..html
---

# Best practice 9.3 – Choose the optimal storage based on access patterns, data growth, and the performance requirements
<a name="best-practice-9.3---choose-the-optimal-storage-based-on-access-patterns-data-growth-and-the-performance-metrics."></a>

 Storage options for data analytics can have performance tradeoffs based on access patterns and data size. For example, in Amazon S3, can be much more efficient to retrieve a smaller number of larger objects, as opposed to a larger number of smaller objects.

 Evaluate your workload needs and usage patterns to determine if the method or location of storing your data can improve the overall efficiency of your solution.

## Suggestion 9.3.1 – Identify available solution options for the performance improvement
<a name="suggestion-9.3.1-identify-available-solution-options-for-the-performance-improvement."></a>

 When data I/O is limiting performance and business requirements are not being met, improve I/O through the options available within that service. For example, with EBS volumes of GP3 type, increase Provisioned IOPS or throughput, or for Amazon Redshift, increase the number of nodes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
