---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-750.html
---

# Amazon EMR 7.5.0 - Hadoop release notes
<a name="Hadoop-release-history-750"></a>

## Amazon EMR 7.5.0 - Hadoop changes
<a name="Hadoop-release-history-750-changes"></a>

| Type | Description |
| --- | --- |
| Bug Fix | Commented out fs.file.impl to empty value. |
| Backport |  [HADOOP-19286](https://issues.apache.org/jira/browse/HADOOP-19286): Support S3A cross region access when S3 region/endpoint is set |
| Improvement | Automatic S3 region configuration setting for S3A connector on EMR-EC2 |
| Improvement | Reduce the number of HeadObject calls in S3A |

With the release of Amazon EMR 7.5, Spark's S3A connector demonstrates read performance comparable to EMRFS, as evidenced by benchmarks using a 3TB TPC-DS parquet dataset.

## Amazon EMR 7.5.0 - Hadoop features
<a name="Hadoop-release-history-750-features"></a>
+ S3 region configuration `fs.s3a.endpoint.region` is automatically set to the region where the EMR cluster is launched with S3A connector for EMR-EC2 deployment.
+ Amazon S3 cross-bucket region access is enabled by default for the S3A connector. It can be modified by setting `fs.s3a.cross.region.access.enabled={{true or false}}`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
