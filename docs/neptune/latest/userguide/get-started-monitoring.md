---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/get-started-monitoring.html
---

# Monitoring an Amazon Neptune cluster
<a name="get-started-monitoring"></a>

Amazon Neptune supports the following monitoring methods.
+ **Amazon CloudWatch** – Amazon Neptune automatically sends metrics to CloudWatch and also supports CloudWatch Alarms. For more information, see [Monitoring Neptune Using Amazon CloudWatch](cloudwatch.md).
+ **AWS CloudTrail** – Amazon Neptune supports API logging using CloudTrail. For more information, see [Logging Amazon Neptune API Calls with AWS CloudTrail](cloudtrail.md).
+ **Tagging** – Use tags to add metadata to your Neptune resources and track usage based on tags. For more information, see [Tagging Amazon Neptune resources](tagging.md).
+ **Audit log files** – View, download, or watch database log files using the Neptune console. For more information, see [Using Audit Logs with Amazon Neptune Clusters](auditing.md).
+ **Instance status** – Check the health of a Neptune instance's graph database engine, find out what version of the engine is installed, and obtain other engine status information using the [instance status API](access-graph-status.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
