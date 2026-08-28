---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-committer-tuning.html
---

# Job tuning considerations
<a name="emr-spark-committer-tuning"></a>

The EMRFS S3-optimized committer consumes a small amount of memory for each file written by a task attempt until the task gets committed or aborted. In most jobs, the amount of memory consumed is negligible. For jobs that have long-running tasks that write a large number of files, the memory that the committer consumes may be noticeable and require adjustments to the memory allocated for Spark executors. You can tune executor memory using the `spark.executor.memory` property. As a guideline, a single task writing 100,000 files would typically require an additional 100MB of memory. For more information, see [Application properties](https://spark.apache.org/docs/latest/configuration.html#application-properties) in the Apache Spark Configuration documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
