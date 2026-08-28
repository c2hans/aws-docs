---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-s3-performance.html
---

# Improve Hive performance
<a name="emr-hive-s3-performance"></a>

Amazon EMR offers features to help optimize performance when using Hive to query, read and write data saved in Amazon S3.

S3 Select can improve query performance for CSV and JSON files in some applications by “pushing down” processing to Amazon S3.

The EMRFS S3 optimized committer is an alternative to the [OutputCommitter](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/OutputCommitter.html) class, that eliminates list and rename operations to improve performance when writing files Amazon S3 using EMRFS.

**Topics**
+ [Enabling Hive EMRFS S3 optimized committer](hive-optimized-committer.md)
+ [Using S3 Select with Hive to improve performance](emr-hive-s3select.md)
+ [MSCK Optimization](emr-msck-optimization.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
