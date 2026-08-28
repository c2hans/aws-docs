---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/firehose-cloudwatch-metrics-best-practices.html
---

# Implement best practices with CloudWatch Alarms
<a name="firehose-cloudwatch-metrics-best-practices"></a>

Add CloudWatch alarms for when the following metrics exceed the buffering limit (a maximum of 15 minutes).
+ `DeliveryToS3.DataFreshness`
+ `DeliveryToIceberg.DataFreshness`
+ `DeliveryToSplunk.DataFreshness`
+ `DeliveryToAmazonOpenSearchService.DataFreshness`
+ `DeliveryToAmazonOpenSearchServerless.DataFreshness`
+ `DeliveryToHttpEndpoint.DataFreshness`

Also, create alarms based on the following metric math expressions.
+ `IncomingBytes (Sum per 5 Minutes) / 300` approaches a percentage of `BytesPerSecondLimit`.
+ `IncomingRecords (Sum per 5 Minutes) / 300` approaches a percentage of `RecordsPerSecondLimit`.
+ `IncomingPutRequests (Sum per 5 Minutes) / 300` approaches a percentage of `PutRequestsPerSecondLimit`.

Another metric for which we recommend an alarm is `ThrottledRecords`.

For information about troubleshooting when alarms go to the `ALARM` state, see [Troubleshoot errors in Amazon Data Firehose](troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
