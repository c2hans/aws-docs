---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_EventSourceMappingConfiguration.html
---

# EventSourceMappingConfiguration
<a name="API_EventSourceMappingConfiguration"></a>

A mapping between an AWS resource and a Lambda function. For details, see [CreateEventSourceMapping](API_CreateEventSourceMapping.md).

## Contents
<a name="API_EventSourceMappingConfiguration_Contents"></a>

 ** AmazonManagedKafkaEventSourceConfig **   <a name="lambda-Type-EventSourceMappingConfiguration-AmazonManagedKafkaEventSourceConfig"></a>
Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.
Type: [AmazonManagedKafkaEventSourceConfig](API_AmazonManagedKafkaEventSourceConfig.md) object
Required: No

 ** BatchSize **   <a name="lambda-Type-EventSourceMappingConfiguration-BatchSize"></a>
The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).
Default value: Varies by service. For Amazon SQS, the default is 10. For all other services, the default is 100.
Related setting: When you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** BisectBatchOnFunctionError **   <a name="lambda-Type-EventSourceMappingConfiguration-BisectBatchOnFunctionError"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry. The default value is false.
Type: Boolean
Required: No

 ** DestinationConfig **   <a name="lambda-Type-EventSourceMappingConfiguration-DestinationConfig"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.
Type: [DestinationConfig](API_DestinationConfig.md) object
Required: No

 ** DocumentDBEventSourceConfig **   <a name="lambda-Type-EventSourceMappingConfiguration-DocumentDBEventSourceConfig"></a>
Specific configuration settings for a DocumentDB event source.
Type: [DocumentDBEventSourceConfig](API_DocumentDBEventSourceConfig.md) object
Required: No

 ** EventSourceArn **   <a name="lambda-Type-EventSourceMappingConfiguration-EventSourceArn"></a>
The Amazon Resource Name (ARN) of the event source.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

 ** EventSourceMappingArn **   <a name="lambda-Type-EventSourceMappingConfiguration-EventSourceMappingArn"></a>
The Amazon Resource Name (ARN) of the event source mapping.
Type: String
Length Constraints: Minimum length of 85. Maximum length of 120.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:event-source-mapping:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** FilterCriteria **   <a name="lambda-Type-EventSourceMappingConfiguration-FilterCriteria"></a>
An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see [Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html).
If filter criteria is encrypted, this field shows up as `null` in the response of ListEventSourceMapping API calls. You can view this field in plaintext in the response of GetEventSourceMapping and DeleteEventSourceMapping calls if you have `kms:Decrypt` permissions for the correct AWS KMS key.
Type: [FilterCriteria](API_FilterCriteria.md) object
Required: No

 ** FilterCriteriaError **   <a name="lambda-Type-EventSourceMappingConfiguration-FilterCriteriaError"></a>
An object that contains details about an error related to filter criteria encryption.
Type: [FilterCriteriaError](API_FilterCriteriaError.md) object
Required: No

 ** FunctionArn **   <a name="lambda-Type-EventSourceMappingConfiguration-FunctionArn"></a>
The ARN of the Lambda function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: No

 ** FunctionResponseTypes **   <a name="lambda-Type-EventSourceMappingConfiguration-FunctionResponseTypes"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `ReportBatchItemFailures`
Required: No

 ** KMSKeyArn **   <a name="lambda-Type-EventSourceMappingConfiguration-KMSKeyArn"></a>
 The ARN of the AWS Key Management Service (AWS KMS) customer managed key that Lambda uses to encrypt your function's [filter criteria](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics).
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
Required: No

 ** LastModified **   <a name="lambda-Type-EventSourceMappingConfiguration-LastModified"></a>
The date that the event source mapping was last updated or that its state changed, in Unix time seconds.
Type: Timestamp
Required: No

 ** LastProcessingResult **   <a name="lambda-Type-EventSourceMappingConfiguration-LastProcessingResult"></a>
The result of the event source mapping's last processing attempt.
Type: String
Required: No

 ** LoggingConfig **   <a name="lambda-Type-EventSourceMappingConfiguration-LoggingConfig"></a>
(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see [Event source mapping logging](https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html).
Type: [EventSourceMappingLoggingConfig](API_EventSourceMappingLoggingConfig.md) object
Required: No

 ** MaximumBatchingWindowInSeconds **   <a name="lambda-Type-EventSourceMappingConfiguration-MaximumBatchingWindowInSeconds"></a>
The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure `MaximumBatchingWindowInSeconds` to any value from 0 seconds to 300 seconds in increments of seconds.
For streams and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change `MaximumBatchingWindowInSeconds` in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.
Related setting: For streams and Amazon SQS event sources, when you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

 ** MaximumRecordAgeInSeconds **   <a name="lambda-Type-EventSourceMappingConfiguration-MaximumRecordAgeInSeconds"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, Lambda never discards old records.
The minimum valid value for maximum record age is 60s. Although values less than 60 and greater than -1 fall within the parameter's absolute range, they are not allowed
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 604800.
Required: No

 ** MaximumRetryAttempts **   <a name="lambda-Type-EventSourceMappingConfiguration-MaximumRetryAttempts"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, Lambda retries failed records until the record expires in the event source.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 10000.
Required: No

 ** MetricsConfig **   <a name="lambda-Type-EventSourceMappingConfiguration-MetricsConfig"></a>
The metrics configuration for your event source. For more information, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics).
Type: [EventSourceMappingMetricsConfig](API_EventSourceMappingMetricsConfig.md) object
Required: No

 ** ParallelizationFactor **   <a name="lambda-Type-EventSourceMappingConfiguration-ParallelizationFactor"></a>
(Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** ProvisionedPollerConfig **   <a name="lambda-Type-EventSourceMappingConfiguration-ProvisionedPollerConfig"></a>
(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see [provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode).
Type: [ProvisionedPollerConfig](API_ProvisionedPollerConfig.md) object
Required: No

 ** Queues **   <a name="lambda-Type-EventSourceMappingConfiguration-Queues"></a>
 (Amazon MQ) The name of the Amazon MQ broker destination queue to consume.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\s\S]*`
Required: No

 ** ScalingConfig **   <a name="lambda-Type-EventSourceMappingConfiguration-ScalingConfig"></a>
(Amazon SQS only) The scaling configuration for the event source. For more information, see [Configuring maximum concurrency for Amazon SQS event sources](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency).
Type: [ScalingConfig](API_ScalingConfig.md) object
Required: No

 ** SelfManagedEventSource **   <a name="lambda-Type-EventSourceMappingConfiguration-SelfManagedEventSource"></a>
The self-managed Apache Kafka cluster for your event source.
Type: [SelfManagedEventSource](API_SelfManagedEventSource.md) object
Required: No

 ** SelfManagedKafkaEventSourceConfig **   <a name="lambda-Type-EventSourceMappingConfiguration-SelfManagedKafkaEventSourceConfig"></a>
Specific configuration settings for a self-managed Apache Kafka event source.
Type: [SelfManagedKafkaEventSourceConfig](API_SelfManagedKafkaEventSourceConfig.md) object
Required: No

 ** SourceAccessConfigurations **   <a name="lambda-Type-EventSourceMappingConfiguration-SourceAccessConfigurations"></a>
An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.
Type: Array of [SourceAccessConfiguration](API_SourceAccessConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 22 items.
Required: No

 ** StartingPosition **   <a name="lambda-Type-EventSourceMappingConfiguration-StartingPosition"></a>
The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. `AT_TIMESTAMP` is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.
Type: String
Valid Values: `TRIM_HORIZON | LATEST | AT_TIMESTAMP`
Required: No

 ** StartingPositionTimestamp **   <a name="lambda-Type-EventSourceMappingConfiguration-StartingPositionTimestamp"></a>
With `StartingPosition` set to `AT_TIMESTAMP`, the time from which to start reading, in Unix time seconds. `StartingPositionTimestamp` cannot be in the future.
Type: Timestamp
Required: No

 ** State **   <a name="lambda-Type-EventSourceMappingConfiguration-State"></a>
The state of the event source mapping. It can be one of the following: `Creating`, `Enabling`, `Enabled`, `Disabling`, `Disabled`, `Updating`, or `Deleting`.
Type: String
Required: No

 ** StateTransitionReason **   <a name="lambda-Type-EventSourceMappingConfiguration-StateTransitionReason"></a>
Indicates whether a user or Lambda made the last change to the event source mapping.
Type: String
Required: No

 ** Topics **   <a name="lambda-Type-EventSourceMappingConfiguration-Topics"></a>
The name of the Kafka topic.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 249.
Pattern: `[^.]([a-zA-Z0-9\-_.]+)`
Required: No

 ** TumblingWindowInSeconds **   <a name="lambda-Type-EventSourceMappingConfiguration-TumblingWindowInSeconds"></a>
(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 900.
Required: No

 ** UUID **   <a name="lambda-Type-EventSourceMappingConfiguration-UUID"></a>
The identifier of the event source mapping.
Type: String
Required: No

## See Also
<a name="API_EventSourceMappingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/EventSourceMappingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/EventSourceMappingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/EventSourceMappingConfiguration)
