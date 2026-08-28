---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoopmetrics_Ganglia.html
---

# Hadoop and Spark metrics in Ganglia
<a name="Hadoopmetrics_Ganglia"></a>

**Note**
The last release of Amazon EMR to include Ganglia was Amazon EMR 6.15.0. To monitor your cluster, releases higher than 6.15.0 include the [Amazon CloudWatch agent](emr-AmazonCloudWatchAgent.md).

 Ganglia reports Hadoop metrics for each instance. The various types of metrics are prefixed by category: distributed file system (dfs.\*), Java virtual machine (jvm.\*), MapReduce (mapred.\*), and remote procedure calls (rpc.\*).

YARN-based Ganglia metrics such as Spark and Hadoop are not available for EMR release versions 4.4.0 and 4.5.0. Use a later version to use these metrics.

Ganglia metrics for Spark generally have prefixes for YARN application ID and Spark DAGScheduler. So prefixes follow this form:
+ DAGScheduler.\*
+ application\_xxxxxxxxxx\_xxxx.driver.\*
+ application\_xxxxxxxxxx\_xxxx.executor.\*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
