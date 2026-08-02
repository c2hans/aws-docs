---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_KafkaStreamingSourceOptions.html
---

# KafkaStreamingSourceOptions
<a name="API_KafkaStreamingSourceOptions"></a>

Additional options for streaming.

## Contents
<a name="API_KafkaStreamingSourceOptions_Contents"></a>

 ** AddRecordTimestamp **   <a name="Glue-Type-KafkaStreamingSourceOptions-AddRecordTimestamp"></a>
When this option is set to 'true', the data output will contain an additional column named "\_\_src\_timestamp" that indicates the time when the corresponding record received by the topic. The default value is 'false'. This option is supported in AWS Glue version 4.0 or later.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** Assign **   <a name="Glue-Type-KafkaStreamingSourceOptions-Assign"></a>
The specific `TopicPartitions` to consume. You must specify at least one of `"topicName"`, `"assign"` or `"subscribePattern"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** BootstrapServers **   <a name="Glue-Type-KafkaStreamingSourceOptions-BootstrapServers"></a>
A list of bootstrap server URLs, for example, as `b-1.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094`. This option must be specified in the API call or defined in the table metadata in the Data Catalog.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** Classification **   <a name="Glue-Type-KafkaStreamingSourceOptions-Classification"></a>
An optional classification.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** ConnectionName **   <a name="Glue-Type-KafkaStreamingSourceOptions-ConnectionName"></a>
The name of the connection.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** Delimiter **   <a name="Glue-Type-KafkaStreamingSourceOptions-Delimiter"></a>
Specifies the delimiter character.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** EmitConsumerLagMetrics **   <a name="Glue-Type-KafkaStreamingSourceOptions-EmitConsumerLagMetrics"></a>
When this option is set to 'true', for each batch, it will emit the metrics for the duration between the oldest record received by the topic and the time it arrives in AWS Glue to CloudWatch. The metric's name is "glue.driver.streaming.maxConsumerLagInMs". The default value is 'false'. This option is supported in AWS Glue version 4.0 or later.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** EndingOffsets **   <a name="Glue-Type-KafkaStreamingSourceOptions-EndingOffsets"></a>
The end point when a batch query is ended. Possible values are either `"latest"` or a JSON string that specifies an ending offset for each `TopicPartition`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** IncludeHeaders **   <a name="Glue-Type-KafkaStreamingSourceOptions-IncludeHeaders"></a>
Whether to include the Kafka headers. When the option is set to "true", the data output will contain an additional column named "glue\_streaming\_kafka\_headers" with type `Array[Struct(key: String, value: String)]`. The default value is "false". This option is available in AWS Glue version 3.0 or later only.
Type: Boolean
Required: No

 ** MaxOffsetsPerTrigger **   <a name="Glue-Type-KafkaStreamingSourceOptions-MaxOffsetsPerTrigger"></a>
The rate limit on the maximum number of offsets that are processed per trigger interval. The specified total number of offsets is proportionally split across `topicPartitions` of different volumes. The default value is null, which means that the consumer reads all offsets until the known latest offset.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** MinPartitions **   <a name="Glue-Type-KafkaStreamingSourceOptions-MinPartitions"></a>
The desired minimum number of partitions to read from Kafka. The default value is null, which means that the number of spark partitions is equal to the number of Kafka partitions.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** NumRetries **   <a name="Glue-Type-KafkaStreamingSourceOptions-NumRetries"></a>
The number of times to retry before failing to fetch Kafka offsets. The default value is `3`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PollTimeoutMs **   <a name="Glue-Type-KafkaStreamingSourceOptions-PollTimeoutMs"></a>
The timeout in milliseconds to poll data from Kafka in Spark job executors. The default value is `512`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** RetryIntervalMs **   <a name="Glue-Type-KafkaStreamingSourceOptions-RetryIntervalMs"></a>
The time in milliseconds to wait before retrying to fetch Kafka offsets. The default value is `10`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** SecurityProtocol **   <a name="Glue-Type-KafkaStreamingSourceOptions-SecurityProtocol"></a>
The protocol used to communicate with brokers. The possible values are `"SSL"` or `"PLAINTEXT"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** StartingOffsets **   <a name="Glue-Type-KafkaStreamingSourceOptions-StartingOffsets"></a>
The starting position in the Kafka topic to read data from. The possible values are `"earliest"` or `"latest"`. The default value is `"latest"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** StartingTimestamp **   <a name="Glue-Type-KafkaStreamingSourceOptions-StartingTimestamp"></a>
The timestamp of the record in the Kafka topic to start reading data from. The possible values are a timestamp string in UTC format of the pattern `yyyy-mm-ddTHH:MM:SSZ` (where Z represents a UTC timezone offset with a \+/-. For example: "2023-04-04T08:00:00\+08:00").
Only one of `StartingTimestamp` or `StartingOffsets` must be set.
Type: Timestamp
Required: No

 ** SubscribePattern **   <a name="Glue-Type-KafkaStreamingSourceOptions-SubscribePattern"></a>
A Java regex string that identifies the topic list to subscribe to. You must specify at least one of `"topicName"`, `"assign"` or `"subscribePattern"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** TopicName **   <a name="Glue-Type-KafkaStreamingSourceOptions-TopicName"></a>
The topic name as specified in Apache Kafka. You must specify at least one of `"topicName"`, `"assign"` or `"subscribePattern"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_KafkaStreamingSourceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/KafkaStreamingSourceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/KafkaStreamingSourceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/KafkaStreamingSourceOptions)
