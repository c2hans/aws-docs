---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/pipeline-alarms-monitoring-and-logs.html
---

# Pipeline alarms, monitoring, and logs
<a name="pipeline-alarms-monitoring-and-logs"></a>

## Pipeline alarms
<a name="pipeline-alarms"></a>

There are different types of pipeline alarms: log processor alarms, buffer layer alarms, and source alarms (only for application log pipeline). The alarms will be triggered when the defined condition is met.

| Log alarm type | Log alarm condition | Description |
| --- | --- | --- |
| Log processor alarms | Error invocation \# >= 10 for 5 minutes, 1 consecutive time | When the number of log processor Lambda error calls is greater than or equal to 10 within 5 minutes (including 5 minutes), an email alarm will be triggered. |
| Log processor alarms | Failed record \# >= 1 for 1 minute, 1 consecutive time | When the number of failed records is greater than or equal to 1 within a 1-minute window, an alarm will be triggered. |
| Log processor alarms | Average execution duration in last 5 minutes >= 60000 milliseconds | In the last 5 minutes, when the average execution time of log processor Lambda is greater than or equal to 60 seconds, an email alarm will be triggered. |
| Buffer layer alarms | SQS Oldest Message Age >= 30 minutes | When the age of the oldest Amazon SQS message is greater than or equal to 30 minutes, it means that the message has not been consumed for at least 30 minutes, an email alarm will be triggered. |
| Source alarms (only for application log pipeline) | Fluent Bit output\_retried\_record\_total >= 100 for last 5 minutes | When the total number of retry records output by Fluent Bit in the past 5 minutes is greater than or equal to 100, an email alarm will be triggered. |

You can choose to enable log alarms or disable them according to your needs.

### Enable log alarms
<a name="enable-log-alarms"></a>

1. Sign in to the Centralized Logging with OpenSearch console.

1. In the left navigation bar, under Log Analytics Pipelines, choose AWS Service Log or Application Log.

1. Select the log pipeline created and choose **View details**.

1. Select the **Alarm** tab.

1. Switch on **Alarms** if needed and select an existing SNS topic.

1. If you choose **Create a new SNS topic**, you must provide email address for the newly created SNS topic to notify.

### Disable log alarms
<a name="disable-log-alarms"></a>

1. Sign in to the Centralized Logging with OpenSearch console.

1. In the left navigation bar, under Log Analytics Pipelines, choose Application Log or Service Log.Select the log pipeline created and choose View details.

1. Select the Alarm tab.

1. Switch off Alarms.

## Monitoring
<a name="monitoring"></a>

The following types of metrics are available on the Centralized Logging with OpenSearch console.

### Log source metrics
<a name="log-source-metrics"></a>

 **Fluent Bit**
+ FluentBitOutputProcRecords - The number of log records that this output instance has successfully sent. This is the total record count of all unique chunks sent by this output. If a record is not successfully sent, it does not count towards this metric.
+ FluentBitOutputProcBytes - The number of bytes of log records that this output instance has successfully sent. This is the total byte size of all unique chunks sent by this output. If a record is not sent due to some error, then it will not count towards this metric.
+ FluentBitOutputDroppedRecords - The number of log records that have been dropped by the output. This means they met an unrecoverable error or retries expired for their chunk.
+ FluentBitOutputErrors - The number of chunks that have faced an error (either unrecoverable or retrievable). This is the number of times a chunk has failed, and does not correspond with the number of error messages you see in the Fluent Bit log output.
+ FluentBitOutputRetriedRecords - The number of log records that experienced a retry. Note that this is calculated at the chunk level, and the count is increased when an entire chunk is marked for retry. An output plugin may or may not perform multiple actions that generate many error messages when uploading a single chunk.
+ FluentBitOutputRetriesFailed - The number of times that retries expired for a chunk. Each plugin configures a Retry\_Limit, which applies to chunks. Once the Retry\_Limit has been reached for a chunk, it is discarded and this metric is incremented.
+ FluentBitOutputRetries - The number of times this output instance requested a retry for a chunk.

 **Network Load Balancer**
+ SyslogNLBActiveFlowCount - The total number of concurrent flows (or connections) from clients to targets. This metric includes connections in the SYN\_SENT and ESTABLISHED states. TCP connections are not terminated at the load balancer, so a client opening a TCP connection to a target counts as a single flow.
+ SyslogNLBProcessedBytes - The total number of bytes processed by the load balancer, including TCP/IP headers. This count includes traffic to and from targets, minus health check traffic.

### Buffer metrics
<a name="buffer-metrics"></a>

Log Buffer is a buffer layer between the Log Agent and OpenSearch clusters. The agent uploads logs into the buffer layer before being processed and delivered into the OpenSearch clusters. A buffer layer is a way to protect OpenSearch clusters from overwhelming.

 **Kinesis Data Stream**
+ KDSIncomingBytes - The number of bytes successfully put to the Kinesis stream over the specified time period. This metric includes bytes from PutRecord and PutRecords operations. Minimum, Maximum, and Average statistics represent the bytes in a single put operation for the stream in the specified time period.
+ KDSIncomingRecords - The number of records successfully put to the Kinesis stream over the specified time period. This metric includes record counts from PutRecord and PutRecords operations. Minimum, Maximum, and Average statistics represent the records in a single put operation for the stream in the specified time period.
+ KDSPutRecordBytes - The number of bytes put to the Kinesis stream using the PutRecord operation over the specified time period.
+ KDSThrottledRecords - The number of records rejected due to throttling in a PutRecords operation per Kinesis data stream, measured over the specified time period.
+ KDSWriteProvisionedThroughputExceeded - The number of records rejected due to throttling for the stream over the specified time period. This metric includes throttling from PutRecord and PutRecords operations. The most commonly used statistic for this metric is Average.

When the Minimum statistic has a non-zero value, records will be throttled for the stream during the specified time period.

When the Maximum statistic has a value of 0 (zero), no records will be throttled for the stream during the specified time period.

 **Amazon SQS**
+ SQSNumberOfMessagesSent - The number of messages added to a queue.
+ SQSNumberOfMessagesDeleted - The number of messages deleted from the queue.

Amazon SQS emits the NumberOfMessagesDeleted metric for every successful deletion operation that uses a valid receipt handle, including duplicate deletions. The following scenarios might cause the value of the NumberOfMessagesDeleted metric to be higher than expected: - Calling the DeleteMessage action on different receipt handles that belong to the same message: If the message is not processed before the visibility timeout expires, the message becomes available to other consumers that can process it and delete it again, increasing the value of the NumberOfMessagesDeleted metric.
+ Calling the DeleteMessage action on the same receipt handle: If the message is processed and deleted, but you call the DeleteMessage action again using the same receipt handle, a success status is returned, increasing the value of the NumberOfMessagesDeleted metric.
+ SQSApproximateNumberOfMessagesVisible - The number of messages available for retrieval from the queue.
+ SQSApproximateAgeOfOldestMessage - The approximate age of the oldest non-deleted message in the queue.
+ After a message is received three times (or more) and not processed, the message is moved to the back of the queue and the ApproximateAgeOfOldestMessage metric points at the second-oldest message that hasn’t been received more than three times. This action occurs even if the queue has a redrive policy.
+ Because a single poison-pill message (received multiple times but never deleted) can distort this metric, the age of a poison-pill message isn’t included in the metric until the poison-pill message is consumed successfully.
+ When the queue has a redrive policy, the message is moved to a dead-letter queue after the configured **Maximum Receives**. When the message is moved to the dead-letter queue, the ApproximateAgeOfOldestMessage metric of the dead-letter queue represents the time when the message was moved to the dead-letter queue (not the original time the message was sent).

### Log processor metrics
<a name="log-processor-metrics"></a>

The Log Processor Lambda is responsible for performing final processing on the data and bulk writing it to OpenSearch.
+ TotalLogs - The total number of log records or events processed by the Lambda function.
+ ExcludedLogs - The number of log records or events that were excluded from processing, which could be due to filtering or other criteria.
+ LoadedLogs - The number of log records or events that were successfully processed and loaded into OpenSearch.
+ FailedLogs - The number of log records or events that failed to be processed or loaded into OpenSearch.
+ ConcurrentExecutions - The number of function instances that are processing events. If this number reaches your [concurrent executions quota](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#compute-and-storage) for the Region, or the [reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) limit on the function, then Lambda throttles additional invocation requests.
+ Duration - The amount of time that your function code spends processing an event. The billed duration for an invocation is the value of Duration rounded up to the nearest millisecond.
+ Throttles - The number of invocation requests that are throttled. When all function instances are processing requests and no concurrency is available to scale up, Lambda rejects additional requests with a TooManyRequestsException error. Throttled requests and other invocation errors don’t count as either Invocations or Errors.
+ Invocations - The number of times that your function code is invoked, including successful invocations and invocations that result in a function error. Invocations aren’t recorded if the invocation request is throttled or otherwise results in an invocation error. The value of Invocations equals the number of requests billed.
