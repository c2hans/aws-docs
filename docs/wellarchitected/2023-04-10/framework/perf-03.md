---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf-03.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF 3. How do you select your storage solution?
<a name="perf-03"></a>

 The most effective storage solution for a system varies based on the kind of access operation (block, file, or object), patterns of access (random or sequential), required throughput, frequency of access (online, offline, archival), frequency of update (WORM, dynamic), and availability and durability constraints. Well-architected systems use multiple storage solutions and activates different features to improve performance and use resources efficiently.

**Topics**
+ [PERF03-BP01 Understand storage characteristics and requirements](perf_right_storage_solution_understand_char.md)
+ [PERF03-BP02 Evaluate available configuration options](perf_right_storage_solution_evaluated_options.md)
+ [PERF03-BP03 Make decisions based on access patterns and metrics](perf_right_storage_solution_optimize_patterns.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
