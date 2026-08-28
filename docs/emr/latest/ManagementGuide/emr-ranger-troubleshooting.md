---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-troubleshooting.html
---

# Apache Ranger troubleshooting
<a name="emr-ranger-troubleshooting"></a>

Here are some commonly diagnosed issues related to using Apache Ranger.

## Recommendations
<a name="emr-ranger-troubleshooting-recommendations"></a>
+ **Test using a single main node cluster:** Single node master clusters provision quicker than a multi-node cluster which can decrease the time for each testing iteration.
+ **Set development mode on the cluster.** When starting your EMR cluster, set the `--additional-info"` parameter to:

  `'{"clusterType":"development"}'`

  This parameter can only be set through the AWS CLI or AWS SDK and is not available through the Amazon EMR console. When this flag is set, and the master fails to provision, the Amazon EMR service keeps the cluster alive for some time before it decommissions it. This time is very useful for probing various log files before the cluster is terminated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
