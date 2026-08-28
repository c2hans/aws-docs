---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-s3-optimized-commit-protocol.html
---

# Use the EMRFS S3-optimized commit protocol
<a name="emr-spark-s3-optimized-commit-protocol"></a>

The EMRFS S3-optimized commit protocol is an alternative [FileCommitProtocol](https://downloads.apache.org/spark/docs/2.4.1/api/java/org/apache/spark/internal/io/FileCommitProtocol.html) implementation that is optimized for writing files with Spark dynamic partition overwrite to Amazon S3 when using EMRFS. The protocol improves application performance by avoiding rename operations in Amazon S3 during the Spark dynamic partition overwrite job commit phase.

Note that the [EMRFS S3-optimized committer](emr-spark-s3-optimized-committer.html) also improves performance by avoiding rename operations. However, it doesn't work for dynamic partition overwrite cases, while the commit protocol’s improvements only target dynamic partition overwrite cases.

The commit protocol is available with Amazon EMR release 5.30.0 and later and 6.2.0 and later and is enabled by default. Amazon EMR added a parallelism improvement starting with release 5.31.0. The protocol is used for Spark jobs that use Spark, DataFrames, or Datasets. There are circumstances under which the commit protocol is not used. For more information, see [Requirements for the EMRFS S3-optimized commit protocol](emr-spark-committer-reqs.md).

**Topics**
+ [Requirements for the EMRFS S3-optimized commit protocol](emr-spark-commit-protocol-reqs.md)
+ [The EMRFS S3-optimized commit protocol and multipart uploads](emr-spark-commit-protocol-multipart.md)
+ [Job tuning considerations](emr-spark-commit-protocol-tuning.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
