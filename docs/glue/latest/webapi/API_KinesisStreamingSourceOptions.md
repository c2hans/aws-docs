---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_KinesisStreamingSourceOptions.html
---

# KinesisStreamingSourceOptions
<a name="API_KinesisStreamingSourceOptions"></a>

Additional options for the Amazon Kinesis streaming data source.

## Contents
<a name="API_KinesisStreamingSourceOptions_Contents"></a>

 ** AddIdleTimeBetweenReads **   <a name="Glue-Type-KinesisStreamingSourceOptions-AddIdleTimeBetweenReads"></a>
Adds a time delay between two consecutive getRecords operations. The default value is `"False"`. This option is only configurable for AWS Glue version 2.0 and above.
Type: Boolean
Required: No

 ** AddRecordTimestamp **   <a name="Glue-Type-KinesisStreamingSourceOptions-AddRecordTimestamp"></a>
When this option is set to 'true', the data output will contain an additional column named "\_\_src\_timestamp" that indicates the time when the corresponding record received by the stream. The default value is 'false'. This option is supported in AWS Glue version 4.0 or later.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** AvoidEmptyBatches **   <a name="Glue-Type-KinesisStreamingSourceOptions-AvoidEmptyBatches"></a>
Avoids creating an empty microbatch job by checking for unread data in the Kinesis data stream before the batch is started. The default value is `"False"`.
Type: Boolean
Required: No

 ** Classification **   <a name="Glue-Type-KinesisStreamingSourceOptions-Classification"></a>
An optional classification.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** Delimiter **   <a name="Glue-Type-KinesisStreamingSourceOptions-Delimiter"></a>
Specifies the delimiter character.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** DescribeShardInterval **   <a name="Glue-Type-KinesisStreamingSourceOptions-DescribeShardInterval"></a>
The minimum time interval between two ListShards API calls for your script to consider resharding. The default value is `1s`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** EmitConsumerLagMetrics **   <a name="Glue-Type-KinesisStreamingSourceOptions-EmitConsumerLagMetrics"></a>
When this option is set to 'true', for each batch, it will emit the metrics for the duration between the oldest record received by the stream and the time it arrives in AWS Glue to CloudWatch. The metric's name is "glue.driver.streaming.maxConsumerLagInMs". The default value is 'false'. This option is supported in AWS Glue version 4.0 or later.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** EndpointUrl **   <a name="Glue-Type-KinesisStreamingSourceOptions-EndpointUrl"></a>
The URL of the Kinesis endpoint.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** FanoutConsumerARN **   <a name="Glue-Type-KinesisStreamingSourceOptions-FanoutConsumerARN"></a>
The Amazon Resource Name (ARN) of the Kinesis Data Streams enhanced fan-out consumer. When specified, enables enhanced fan-out for dedicated throughput and lower latency data consumption.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** IdleTimeBetweenReadsInMs **   <a name="Glue-Type-KinesisStreamingSourceOptions-IdleTimeBetweenReadsInMs"></a>
The minimum time delay between two consecutive getRecords operations, specified in ms. The default value is `1000`. This option is only configurable for AWS Glue version 2.0 and above.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** MaxFetchRecordsPerShard **   <a name="Glue-Type-KinesisStreamingSourceOptions-MaxFetchRecordsPerShard"></a>
The maximum number of records to fetch per shard in the Kinesis data stream per microbatch. Note: The client can exceed this limit if the streaming job has already read extra records from Kinesis (in the same get-records call). If `MaxFetchRecordsPerShard` needs to be strict then it needs to be a multiple of `MaxRecordPerRead`. The default value is `100000`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** MaxFetchTimeInMs **   <a name="Glue-Type-KinesisStreamingSourceOptions-MaxFetchTimeInMs"></a>
The maximum time spent for the job executor to read records for the current batch from the Kinesis data stream, specified in milliseconds (ms). Multiple `GetRecords` API calls may be made within this time. The default value is `1000`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** MaxRecordPerRead **   <a name="Glue-Type-KinesisStreamingSourceOptions-MaxRecordPerRead"></a>
The maximum number of records to fetch from the Kinesis data stream in each getRecords operation. The default value is `10000`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** MaxRetryIntervalMs **   <a name="Glue-Type-KinesisStreamingSourceOptions-MaxRetryIntervalMs"></a>
The maximum cool-off time period (specified in ms) between two retries of a Kinesis Data Streams API call. The default value is `10000`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** NumRetries **   <a name="Glue-Type-KinesisStreamingSourceOptions-NumRetries"></a>
The maximum number of retries for Kinesis Data Streams API requests. The default value is `3`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** RetryIntervalMs **   <a name="Glue-Type-KinesisStreamingSourceOptions-RetryIntervalMs"></a>
The cool-off time period (specified in ms) before retrying the Kinesis Data Streams API call. The default value is `1000`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** RoleArn **   <a name="Glue-Type-KinesisStreamingSourceOptions-RoleArn"></a>
The Amazon Resource Name (ARN) of the role to assume using AWS Security Token Service (AWS STS). This role must have permissions for describe or read record operations for the Kinesis data stream. You must use this parameter when accessing a data stream in a different account. Used in conjunction with `"awsSTSSessionName"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** RoleSessionName **   <a name="Glue-Type-KinesisStreamingSourceOptions-RoleSessionName"></a>
An identifier for the session assuming the role using AWS STS. You must use this parameter when accessing a data stream in a different account. Used in conjunction with `"awsSTSRoleARN"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** StartingPosition **   <a name="Glue-Type-KinesisStreamingSourceOptions-StartingPosition"></a>
The starting position in the Kinesis data stream to read data from. The possible values are `"latest"`, `"trim_horizon"`, `"earliest"`, or a timestamp string in UTC format in the pattern `yyyy-mm-ddTHH:MM:SSZ` (where `Z` represents a UTC timezone offset with a \+/-. For example: "2023-04-04T08:00:00-04:00"). The default value is `"latest"`.
Note: Using a value that is a timestamp string in UTC format for "startingPosition" is supported only for AWS Glue version 4.0 or later.
Type: String
Valid Values: `latest | trim_horizon | earliest | timestamp`
Required: No

 ** StartingTimestamp **   <a name="Glue-Type-KinesisStreamingSourceOptions-StartingTimestamp"></a>
The timestamp of the record in the Kinesis data stream to start reading data from. The possible values are a timestamp string in UTC format of the pattern `yyyy-mm-ddTHH:MM:SSZ` (where Z represents a UTC timezone offset with a \+/-. For example: "2023-04-04T08:00:00\+08:00").
Type: Timestamp
Required: No

 ** StreamArn **   <a name="Glue-Type-KinesisStreamingSourceOptions-StreamArn"></a>
The Amazon Resource Name (ARN) of the Kinesis data stream.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** StreamName **   <a name="Glue-Type-KinesisStreamingSourceOptions-StreamName"></a>
The name of the Kinesis data stream.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_KinesisStreamingSourceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/KinesisStreamingSourceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/KinesisStreamingSourceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/KinesisStreamingSourceOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
