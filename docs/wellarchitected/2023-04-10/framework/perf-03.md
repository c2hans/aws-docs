---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf-03.html
---

This whitepaper is for historical reference only.

All updated guidance and best practices now live in the [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) whitepaper.

# PERF 3. How do you select your storage solution?

 The most effective storage solution for a system varies based on the kind of access operation (block, file, or object), patterns of access (random or sequential), required throughput, frequency of access (online, offline, archival), frequency of update (WORM, dynamic), and availability and durability constraints. Well-architected systems use multiple storage solutions and activates different features to improve performance and use resources efficiently.

**Topics**
+ [PERF03-BP01 Understand storage characteristics and requirements](perf_right_storage_solution_understand_char.md)
+ [PERF03-BP02 Evaluate available configuration options](perf_right_storage_solution_evaluated_options.md)
+ [PERF03-BP03 Make decisions based on access patterns and metrics](perf_right_storage_solution_optimize_patterns.md)
