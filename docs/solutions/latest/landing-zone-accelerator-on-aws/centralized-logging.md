---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/centralized-logging.html
---

# Centralized logging
<a name="centralized-logging"></a>

 **AWS log archiving architecture with EventBridge, Lambda, Kinesis, and S3 components.**

![image5](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/image5.png)

1. A CloudWatch log group update workflow runs during the **Logging** stage of the pipeline. A CloudFormation custom resource invokes a Lambda function that updates existing log groups to the increase log retention if it’s less than the solution log retention period, CloudWatch AWS KMS key, and subscription filter. The destination for the subscription filter is an Amazon Kinesis Data Stream deployed to the **Log Archive** account. For example, before solution is installed if there are existing log groups `LogGroupA` with 5 years retention and `LogGroupB` with 1 week retention. The solution is deployed with 1 year retention in global-config.yaml under `cloudwatchLogRetentionInDays`. Then `LogGroupA` will be unaffected with the update since 5 years is greater than 1 year but `LogGroupB` retention will change to 1 year. If in a subsequent update or initial update, solution is deployed with 10 years retention in global-config.yaml under `cloudwatchLogRetentionInDays`, then both log groups will change retention to 10 years.

1. An EventBridge rule monitors for new CloudWatch log groups created in core and workload accounts.

1. When new log groups are created, the EventBridge rule invokes a Lambda function that updates the log group with the configured log retention period, CloudWatch AWS KMS key, and subscription filter. The destination for the subscription filter is the Kinesis Data Stream deployed to the **Log Archive** account. Since log replication to s3 is active, any CreateLogGroup API call will get the retention specified in global-config.yaml under `cloudwatchLogRetentionInDays`. So if `cloudwatchLogRetentionInDays` is set to 1 week and new log group is created with 5 year retention then it will change to 1 week. The solution ensures that entire organization’s CloudWatch retention for any new log group is compliant under the value specified in global-config.yaml under `cloudwatchLogRetentionInDays`.

1. Log groups stream their logs to the Kinesis Data Stream. The data stream is encrypted at rest with the replication AWS KMS key.

1. A delivery stream is configured with the Kinesis Data Stream and Firehose, allowing the logs to be transformed and replicated to Amazon S3.

1. The destination of the Firehose delivery stream is the `aws-accelerator-central-logs` Amazon S3 bucket. This bucket is encrypted at rest with the central logging AWS KMS key. In addition, the `aws-accelerator-s3-access-logs` and `aws-accelerator-elb-access-logs` buckets are encrypted at rest with Amazon S3-managed server-side encryption (SSE-S3) because these services don’t support customer-managed AWS KMS keys. Logs delivered to the `aws-accelerator-elb-access-logs` bucket replicate to the central logs bucket with Amazon S3 replication.
