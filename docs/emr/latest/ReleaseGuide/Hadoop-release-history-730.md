---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-730.html
---

# Amazon EMR 7.3.0 - Hadoop release notes
<a name="Hadoop-release-history-730"></a>

## Amazon EMR 7.3.0 - Hadoop changes
<a name="Hadoop-release-history-730-changes"></a>

| Type | Description |
| --- | --- |
| New Feature | [HADOOP-19197](https://issues.apache.org/jira/browse/HADOOP-18850): S3A Support AWS KMS Encryption Context |
| New Feature | [HADOOP-18980](https://issues.apache.org/jira/browse/HADOOP-18980): S3A credential provider remapping: make extensible |
| Improvement | [HADOOP-18808](https://issues.apache.org/jira/browse/HADOOP-18808): LogExactlyOnce to add a debug() method |

## Amazon EMR 7.3.0 - Hadoop features
<a name="Hadoop-release-history-730-features"></a>

See the following list for new Hadoop features in Amazon EMR 7.3.0.
+ By default, clusters with in-transit encryption enabled through the security configuration will run TLS 1.3 for Hadoop YARN (Resource Manager, Node Manager, Timeline Server and WebApplicationProxy), HDFS (NameNode, DataNode, Journal Node and DFSZKFailoverController), and Map Reduce (JobHistory Server and MapReduce Shuffle ports).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
