---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf-04.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF 4. How do you select your database solution?
<a name="perf-04"></a>

 The most effective database solution for a system varies based on requirements for availability, consistency, partition tolerance, latency, durability, scalability, and query capability. Many systems use different database solutions for various subsystems and activate different features to improve performance. Selecting the wrong database solution and features for a system can lead to lower performance efficiency.

**Topics**
+ [PERF04-BP01 Understand data characteristics](perf_right_database_solution_understand_char.md)
+ [PERF04-BP02 Evaluate the available options](perf_right_database_solution_evaluate_options.md)
+ [PERF04-BP03 Collect and record database performance metrics](perf_right_database_solution_collect_metrics.md)
+ [PERF04-BP04 Choose data storage based on access patterns](perf_right_database_solution_access_patterns.md)
+ [PERF04-BP05 Optimize data storage based on access patterns and metrics](perf_right_database_solution_optimize_metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
