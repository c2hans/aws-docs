---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html
---

# Available CloudWatch metrics for Amazon SQS
<a name="sqs-available-cloudwatch-metrics"></a>

Amazon SQS sends the following metrics to CloudWatch.

**Note**
For some metrics, the result is approximate because of the distributed architecture of Amazon SQS. In most cases, the count should be close to the actual number of messages in the queue.

## Amazon SQS metrics
<a name="sqs-metrics"></a>

Amazon SQS automatically publishes operational metrics to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) under the `AWS/SQS` namespace. These metrics help you monitor queue health and performance. Due to SQS’s distributed nature, many values are approximate, but accurate enough for most operational decisions.

**Note**
All metrics emit non-negative values only when the queue is active.
Some metrics (such as `SentMessageSize`) are not emitted until at least one message is sent.

| Metric | Description | Units | Reporting behavior | Key notes |
| --- | --- | --- | --- | --- |
| ApproximateAgeOfOldestMessage | The age of the oldest unprocessed message in the queue. | Seconds | Reported if the queue contains at least one active message. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
| ApproximateNumberOfGroupsWithInflightMessages | For FIFO only. The number of message groups with one or more in-flight messages. | Count | Reported if the FIFO queue is active. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
| ApproximateNumberOfMessagesDelayed | The number of messages in the queue that are delayed and not immediately available for retrieval. | Count | Reported if delayed messages exist in the queue. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
| ApproximateNumberOfMessagesNotVisible | The number of in-flight messages that have been received but not yet deleted or expired. | Count | Reported if in-flight messages exist. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
| ApproximateNumberOfMessagesVisible | The number of messages currently available for retrieval and processing. | Count | Reported if the queue is active. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
| NumberOfEmptyReceives¹ | The number of [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) API calls that returned no messages. | Count | Reported during receive operations. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
| NumberOfDeduplicatedSentMessages | For FIFO only. The number of sent messages that were deduplicated and not added to the queue. | Count | Reported if duplicate MessageDeduplicationId values or content are detected. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
| NumberOfMessagesDeleted¹ | The number of messages successfully deleted from the queue. | Count | Reported for each delete request with a valid receipt handle. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
| NumberOfMessagesReceived¹ | The number of messages returned by the [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) API. | Count | Reported during receive operations. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html)  |
|  NumberOfMessagesSent¹ | The number of messages successfully added to a queue. | Count | Reported for each successful manual send. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
|  SentMessageSize¹  | The size of messages successfully sent to the queue. | Bytes | Not emitted until at least one message is sent. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
|  ApproximateNumberOfNoisyGroups | The number of message groups that are considered noisy in a fair queue. A noisy message group represents a noisy neighbor tenant of a multi-tenant queue. | Count | A non-negative value is reported [if the queue is active](monitoring-using-cloudwatch.md). | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
|  ApproximateNumberOfMessagesVisibleInQuietGroups | The number of messages visible excluding messages from noisy message groups. | Count | A non-negative value is reported [if the queue is active](monitoring-using-cloudwatch.md). | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
|  ApproximateNumberOfMessagesNotVisibleInQuietGroups | The number of messages in-flight excluding messages from noisy message groups. | Count | A non-negative value is reported [if the queue is active](monitoring-using-cloudwatch.md). | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
|  ApproximateNumberOfMessagesDelayedInQuietGroups | The number of messages excluding messages from noisy message groups that are delayed and not available for reading immediately. Delayed messages occur when the queue is configured as a [delay queue](sqs-delay-queues.md) or when a message has been sent with a delay parameter. | Count | A non-negative value is reported [if the queue is active](monitoring-using-cloudwatch.md). | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |
|  ApproximateAgeOfOldestMessageInQuietGroups | The age of the oldest non-deleted message in the queue excluding messages from noisy message groups. | Seconds | A non-negative value is reported [if the queue is active](monitoring-using-cloudwatch.md). | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) |

¹ These metrics reflect system-level activity and may include retries, duplicates, or delayed messages. Don’t use raw counts to estimate real-time queue state without factoring in message lifecycle behavior.

## Dead-letter queues (DLQs) and CloudWatch metrics
<a name="dlq-cloudwatch-metrics"></a>

When working with DLQs, it's important to understand how Amazon SQS metrics behave:
+ **`NumberOfMessagesSent`** – This metric behaves differently for DLQs:
  + **Manual Sending** – Messages manually sent to a DLQ are captured by this metric.
  + **Automatic Redrive** – Messages automatically moved to a DLQ due to processing failures are **not** captured by this metric. As a result, the `NumberOfMessagesSent` and `NumberOfMessagesReceived` metrics may show discrepancies for DLQs.
+ **Recommended Metric for DLQs** – To monitor the state of a DLQ, use the `ApproximateNumberOfMessagesVisible` metric. This metric indicates the number of messages currently available for processing in the DLQ.

## Fair queues and CloudWatch metrics
<a name="fair-queues-cloudwatch-metrics"></a>

When you use [fair queues](sqs-fair-queues.md), Amazon SQS emits the following additional metrics:
+ `ApproximateNumberOfNoisyGroups`
+ `ApproximateNumberOfMessagesVisibleInQuietGroups`
+ `ApproximateNumberOfMessagesNotVisibleInQuietGroups`
+ `ApproximateNumberOfMessagesDelayedInQuietGroups`
+ `ApproximateAgeOfOldestMessageInQuietGroups`

**Note**
Each `QuietGroup` metric is a subset of the equivalent standard queue-level `Approximate` metric, but excludes messages from noisy neighbor groups.

**Noisy groups**
A noisy message group represents a noisy neighbor tenant of a multi-tenant queue.

**Quiet groups**
Message groups excluding noisy groups.

**Observing SQS fair queues behavior**

To monitor the effect of Amazon SQS fair queues, you can compare `Approximate..InQuietGroups` metrics with standard queue-level metrics. During traffic surges for a specific tenant, the general queue-level metrics may reveal increasing backlogs or older message ages. However, looking at the quiet groups in isolation, you can identify that most non-noisy message groups or tenants are not impacted, and provide an estimate of the total number of impacted message groups.

 While these new metrics provide a good overview of Amazon SQS fair queues behavior, it can be beneficial to understand which specific tenant is causing the load. [Amazon CloudWatch contributor insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) allows you to see metrics about the top-N contributors, the total number of unique contributors, and their usage. This is especially helpful in scenarios where you are dealing with thousands of tenants that would otherwise lead to high-cardinality data (and cost) when emitting traditional metrics.

 For an example of monitoring configuration for fair queues, see the sample on [GitHub](https://github.com/aws-samples/sample-amazon-sqs-fair-queues).

## Dimensions for Amazon SQS metrics
<a name="sqs-metric-dimensions"></a>

Amazon SQS metrics in CloudWatch use a single dimension: **`QueueName`**. All metric data is grouped and filtered by the name of the queue.

## Monitoring tips
<a name="monitoring-tips"></a>

Monitor SQS effectively using key metrics and CloudWatch alarms to detect queue backlogs, optimize performance, and stay within service limits.
+ Set [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) based on `ApproximateNumberOfMessagesVisible` to catch backlog growth.
+ Monitor `NumberOfEmptyReceives` to tune poll frequency and reduce API cost.
+ Use `ApproximateNumberOfGroupsWithInflightMessages` in FIFO queues to diagnose throughput limits.
+ Review [SQS quotas](sqs-quotas.md) to understand metric thresholds and service limits.
