---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf-tradeoffs.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# Tradeoffs
<a name="perf-tradeoffs"></a>

 When you architect solutions, think about tradeoffs to validate a more efficient approach. Depending on your situation, you could trade consistency, durability, and space for time or latency, to deliver higher performance.

 Using AWS, you can go global in minutes and deploy resources in multiple locations across the globe to be closer to your end users. You can also dynamically add read only replicas to information stores (such as database systems) to reduce the load on the primary database.

 The following question focuses on these considerations for performance efficiency.

| PERF 8:  How do you use tradeoffs to improve performance? |
| --- |
|  When architecting solutions, determining tradeoffs permits you to select an more efficient approach. Often you can improve performance by trading consistency, durability, and space for time and latency.  |

 As you make changes to the workload, collect and evaluate metrics to determine the impact of those changes. Measure the impacts to the system and to the end user to understand how your trade-oﬀs impact your workload. Use a systematic approach, such as load testing, to explore whether the tradeoff improves performance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
