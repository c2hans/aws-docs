---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-efs.html
---

# Amazon Elastic File System (Amazon EFS)
<a name="component-configuration-examples-efs"></a>

The following example shows a component configuration in JSON format for Amazon EFS.

```
{
   "alarmMetrics": [
     {
       "alarmMetricName": "BurstCreditBalance",
       "monitor": true
     },
     {
       "alarmMetricName": "PercentIOLimit",
       "monitor": true
     },
     {
       "alarmMetricName": "PermittedThroughput",
       "monitor": true
     },
     {
       "alarmMetricName": "MeteredIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "TotalIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "DataWriteIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "DataReadIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "MetadataIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "ClientConnections",
       "monitor": true
     },
     {
       "alarmMetricName": "TimeSinceLastSync",
       "monitor": true
     },
     {
       "alarmMetricName": "Throughput",
       "monitor": true
     },
     {
       "alarmMetricName": "PercentageOfPermittedThroughputUtilization",
       "monitor": true
     },
     {
       "alarmMetricName": "ThroughputIOPS",
       "monitor": true
     },
     {
       "alarmMetricName": "PercentThroughputDataReadIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "PercentThroughputDataWriteIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "PercentageOfIOPSDataReadIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "PercentageOfIOPSDataWriteIOBytes",
       "monitor": true
     },
     {
       "alarmMetricName": "AverageDataReadIOBytesSize",
       "monitor": true
     },
     {
       "alarmMetricName": "AverageDataWriteIOBytesSize",
       "monitor": true
     }
   ],
   "logs": [
    {
    "logGroupName": "/aws/efs/utils",
    "logType": "EFS_MOUNT_STATUS",
    "monitor": true,
    }
   ]
 }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
