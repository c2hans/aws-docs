---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/data-export-cloudwatch-logs.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Monitoring with Amazon CloudWatch Logs
<a name="data-export-cloudwatch-logs"></a>

You can monitor Amazon Monitron live data export using Amazon CloudWatch Logs. When a measurement fails to export, Amazon Monitron will send a log event to your CloudWatch Logs. You can also set up a metric filter on the error log to generate metrics and set up alarms. An alarm can watch for certain thresholds and send notifications or take actions when those thresholds are met. For more information, see [the CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

Amazon Monitron sends log events to the /aws/monitron/data-export/{HASH\_ID} log group.

The log event has the following JSON format:

```
{
    "assetDisplayName": "string",
    "destination": "string",
    "errorCode": "string",
    "errorMessage": "string",
    "eventId": "string",
    "positionDisplayName": "string",
    "projectDisplayName": "string",
    "projectName": "string",
    "sensorId": "string",
    "siteDisplayName": "string",
    "timestamp": "string"
}
```

assetDisplayName
+ The asset name displayed in the App
+ Type: String

destination
+ The ARN of the Kinesis data stream
+ Type: String
+ Pattern: arn:aws:kinesis:{{REGION}}:{{AWS\_ACCOUNT\_ID}}:stream/{{STREAM\_NAME}}

errorCode
+ The error code
+ Type: String
+ Valid Values: `INTERNAL_SEVER_ERROR | KINESIS_RESOURCE_NOT_FOUND | KINESIS_PROVISIONED_THROUGHPUT_EXCEEDED | KMS_ACCESS_DENIED | KMS_NOT_FOUND | KMS_DISABLED | KMS_INVALID_STATE | KMS_THROTTLING`

errorMessage
+ The detailed error message
+ Type: String

eventId
+ The unique event ID corresponding to each measurement export
+ Type: String

positionDisplayName
+ The sensor position name displayed in the App
+ Type: String

sensorId
+ The physical ID of the sensor from which the measurement is sent
+ Type: String

siteDisplayName
+ The site name displayed in the App
+ Type: String

timestamp
+ The timestamp when the measurement is received by Amazon Monitron service in UTC
+ Type: String
+ Pattern: yyyy-mm-dd hh:mm:ss.SSS

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
