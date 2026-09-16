---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html
---

# UpdateEventSourceMapping
<a name="API_UpdateEventSourceMapping"></a>

Updates an event source mapping. You can change the function that AWS Lambda invokes, or pause invocation and resume later from the same location.

For details about how to configure different event sources, see the following topics.
+  [ Amazon DynamoDB Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping)
+  [ Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping)
+  [ Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource)
+  [ Amazon MQ and RabbitMQ](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping)
+  [ Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html)
+  [ Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html)
+  [ Amazon DocumentDB](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html)

The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka):
+  `BisectBatchOnFunctionError` – If the function returns an error, split the batch in two and retry.
+  `MaximumRecordAgeInSeconds` – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires
+  `MaximumRetryAttempts` – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.
+  `OnFailure` – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see [Adding a destination](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations).

The following option is available only for DynamoDB and Kinesis event sources:
+  `ParallelizationFactor` – Process multiple batches from each shard concurrently.

For information about which configuration parameters apply to each event source, see the following topics.
+  [ Amazon DynamoDB Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-params)
+  [ Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-params)
+  [ Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-params)
+  [ Amazon MQ and RabbitMQ](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-params)
+  [ Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-parms)
+  [ Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-kafka-parms)
+  [ Amazon DocumentDB](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html#docdb-configuration)

## Request Syntax
<a name="API_UpdateEventSourceMapping_RequestSyntax"></a>

```
PUT /2015-03-31/event-source-mappings/{{UUID}} HTTP/1.1
Content-type: application/json

{
   "AmazonManagedKafkaEventSourceConfig": {
      "ConsumerGroupId": "{{string}}",
      "SchemaRegistryConfig": {
         "AccessConfigs": [
            {
               "Type": "{{string}}",
               "URI": "{{string}}"
            }
         ],
         "EventRecordFormat": "{{string}}",
         "SchemaRegistryURI": "{{string}}",
         "SchemaValidationConfigs": [
            {
               "Attribute": "{{string}}"
            }
         ]
      }
   },
   "BatchSize": {{number}},
   "BisectBatchOnFunctionError": {{boolean}},
   "DestinationConfig": {
      "OnFailure": {
         "Destination": "{{string}}"
      },
      "OnSuccess": {
         "Destination": "{{string}}"
      }
   },
   "DocumentDBEventSourceConfig": {
      "CollectionName": "{{string}}",
      "DatabaseName": "{{string}}",
      "FullDocument": "{{string}}"
   },
   "Enabled": {{boolean}},
   "FilterCriteria": {
      "Filters": [
         {
            "Pattern": "{{string}}"
         }
      ]
   },
   "FunctionName": "{{string}}",
   "FunctionResponseTypes": [ "{{string}}" ],
   "KMSKeyArn": "{{string}}",
   "LoggingConfig": {
      "SystemLogLevel": "{{string}}"
   },
   "MaximumBatchingWindowInSeconds": {{number}},
   "MaximumRecordAgeInSeconds": {{number}},
   "MaximumRetryAttempts": {{number}},
   "MetricsConfig": {
      "Metrics": [ "{{string}}" ]
   },
   "ParallelizationFactor": {{number}},
   "ProvisionedPollerConfig": {
      "MaximumPollers": {{number}},
      "MinimumPollers": {{number}},
      "PollerGroupName": "{{string}}"
   },
   "ScalingConfig": {
      "MaximumConcurrency": {{number}}
   },
   "SelfManagedKafkaEventSourceConfig": {
      "ConsumerGroupId": "{{string}}",
      "SchemaRegistryConfig": {
         "AccessConfigs": [
            {
               "Type": "{{string}}",
               "URI": "{{string}}"
            }
         ],
         "EventRecordFormat": "{{string}}",
         "SchemaRegistryURI": "{{string}}",
         "SchemaValidationConfigs": [
            {
               "Attribute": "{{string}}"
            }
         ]
      }
   },
   "SourceAccessConfigurations": [
      {
         "Type": "{{string}}",
         "URI": "{{string}}"
      }
   ],
   "TumblingWindowInSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateEventSourceMapping_RequestParameters"></a>

The request uses the following URI parameters.

 ** [UUID](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-uri-UUID"></a>
The identifier of the event source mapping.
Required: Yes

## Request Body
<a name="API_UpdateEventSourceMapping_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AmazonManagedKafkaEventSourceConfig](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-AmazonManagedKafkaEventSourceConfig"></a>
Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.
Type: [AmazonManagedKafkaEventSourceConfig](API_AmazonManagedKafkaEventSourceConfig.md) object
Required: No

 ** [BatchSize](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-BatchSize"></a>
The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).
+  **Amazon Kinesis** – Default 100. Max 10,000.
+  **Amazon DynamoDB Streams** – Default 100. Max 10,000.
+  **Amazon Simple Queue Service** – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.
+  **Amazon Managed Streaming for Apache Kafka** – Default 100. Max 10,000.
+  **Self-managed Apache Kafka** – Default 100. Max 10,000.
+  **Amazon MQ (ActiveMQ and RabbitMQ)** – Default 100. Max 10,000.
+  **DocumentDB** – Default 100. Max 10,000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [BisectBatchOnFunctionError](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-BisectBatchOnFunctionError"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.
Type: Boolean
Required: No

 ** [DestinationConfig](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-DestinationConfig"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.
Type: [DestinationConfig](API_DestinationConfig.md) object
Required: No

 ** [DocumentDBEventSourceConfig](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-DocumentDBEventSourceConfig"></a>
Specific configuration settings for a DocumentDB event source.
Type: [DocumentDBEventSourceConfig](API_DocumentDBEventSourceConfig.md) object
Required: No

 ** [Enabled](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-Enabled"></a>
When true, the event source mapping is active. When false, Lambda pauses polling and invocation.
Default: True
Type: Boolean
Required: No

 ** [FilterCriteria](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-FilterCriteria"></a>
An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see [Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html).
Type: [FilterCriteria](API_FilterCriteria.md) object
Required: No

 ** [FunctionName](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `MyFunction`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
+  **Version or Alias ARN** – `arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`.
+  **Partial ARN** – `123456789012:function:MyFunction`.
The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: No

 ** [FunctionResponseTypes](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-FunctionResponseTypes"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `ReportBatchItemFailures`
Required: No

 ** [KMSKeyArn](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-KMSKeyArn"></a>
 The ARN of the AWS Key Management Service (AWS KMS) customer managed key that Lambda uses to encrypt your function's [filter criteria](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics). By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key.
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
Required: No

 ** [LoggingConfig](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-LoggingConfig"></a>
(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. Use this configuration object to define the level of logs for your event source mapping.
Type: [EventSourceMappingLoggingConfig](API_EventSourceMappingLoggingConfig.md) object
Required: No

 ** [MaximumBatchingWindowInSeconds](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-MaximumBatchingWindowInSeconds"></a>
The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure `MaximumBatchingWindowInSeconds` to any value from 0 seconds to 300 seconds in increments of seconds.
For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change `MaximumBatchingWindowInSeconds` in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.
Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

 ** [MaximumRecordAgeInSeconds](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-MaximumRecordAgeInSeconds"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 604800.
Required: No

 ** [MaximumRetryAttempts](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-MaximumRetryAttempts"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 10000.
Required: No

 ** [MetricsConfig](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-MetricsConfig"></a>
The metrics configuration for your event source. For more information, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics).
Type: [EventSourceMappingMetricsConfig](API_EventSourceMappingMetricsConfig.md) object
Required: No

 ** [ParallelizationFactor](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-ParallelizationFactor"></a>
(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [ProvisionedPollerConfig](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-ProvisionedPollerConfig"></a>
(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see [provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode).
Type: [ProvisionedPollerConfig](API_ProvisionedPollerConfig.md) object
Required: No

 ** [ScalingConfig](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-ScalingConfig"></a>
(Amazon SQS only) The scaling configuration for the event source. For more information, see [Configuring maximum concurrency for Amazon SQS event sources](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency).
Type: [ScalingConfig](API_ScalingConfig.md) object
Required: No

 ** [SelfManagedKafkaEventSourceConfig](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-SelfManagedKafkaEventSourceConfig"></a>
Specific configuration settings for a self-managed Apache Kafka event source.
Type: [SelfManagedKafkaEventSourceConfig](API_SelfManagedKafkaEventSourceConfig.md) object
Required: No

 ** [SourceAccessConfigurations](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-SourceAccessConfigurations"></a>
An array of authentication protocols or VPC components required to secure your event source.
Type: Array of [SourceAccessConfiguration](API_SourceAccessConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 22 items.
Required: No

 ** [TumblingWindowInSeconds](#API_UpdateEventSourceMapping_RequestSyntax) **   <a name="lambda-UpdateEventSourceMapping-request-TumblingWindowInSeconds"></a>
(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 900.
Required: No

## Response Syntax
<a name="API_UpdateEventSourceMapping_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "AmazonManagedKafkaEventSourceConfig": {
      "ConsumerGroupId": "string",
      "SchemaRegistryConfig": {
         "AccessConfigs": [
            {
               "Type": "string",
               "URI": "string"
            }
         ],
         "EventRecordFormat": "string",
         "SchemaRegistryURI": "string",
         "SchemaValidationConfigs": [
            {
               "Attribute": "string"
            }
         ]
      }
   },
   "BatchSize": number,
   "BisectBatchOnFunctionError": boolean,
   "DestinationConfig": {
      "OnFailure": {
         "Destination": "string"
      },
      "OnSuccess": {
         "Destination": "string"
      }
   },
   "DocumentDBEventSourceConfig": {
      "CollectionName": "string",
      "DatabaseName": "string",
      "FullDocument": "string"
   },
   "EventSourceArn": "string",
   "EventSourceMappingArn": "string",
   "FilterCriteria": {
      "Filters": [
         {
            "Pattern": "string"
         }
      ]
   },
   "FilterCriteriaError": {
      "ErrorCode": "string",
      "Message": "string"
   },
   "FunctionArn": "string",
   "FunctionResponseTypes": [ "string" ],
   "KMSKeyArn": "string",
   "LastModified": number,
   "LastProcessingResult": "string",
   "LoggingConfig": {
      "SystemLogLevel": "string"
   },
   "MaximumBatchingWindowInSeconds": number,
   "MaximumRecordAgeInSeconds": number,
   "MaximumRetryAttempts": number,
   "MetricsConfig": {
      "Metrics": [ "string" ]
   },
   "ParallelizationFactor": number,
   "ProvisionedPollerConfig": {
      "MaximumPollers": number,
      "MinimumPollers": number,
      "PollerGroupName": "string"
   },
   "Queues": [ "string" ],
   "ScalingConfig": {
      "MaximumConcurrency": number
   },
   "SelfManagedEventSource": {
      "Endpoints": {
         "string" : [ "string" ]
      }
   },
   "SelfManagedKafkaEventSourceConfig": {
      "ConsumerGroupId": "string",
      "SchemaRegistryConfig": {
         "AccessConfigs": [
            {
               "Type": "string",
               "URI": "string"
            }
         ],
         "EventRecordFormat": "string",
         "SchemaRegistryURI": "string",
         "SchemaValidationConfigs": [
            {
               "Attribute": "string"
            }
         ]
      }
   },
   "SourceAccessConfigurations": [
      {
         "Type": "string",
         "URI": "string"
      }
   ],
   "StartingPosition": "string",
   "StartingPositionTimestamp": number,
   "State": "string",
   "StateTransitionReason": "string",
   "Topics": [ "string" ],
   "TumblingWindowInSeconds": number,
   "UUID": "string"
}
```

## Response Elements
<a name="API_UpdateEventSourceMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [AmazonManagedKafkaEventSourceConfig](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-AmazonManagedKafkaEventSourceConfig"></a>
Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.
Type: [AmazonManagedKafkaEventSourceConfig](API_AmazonManagedKafkaEventSourceConfig.md) object

 ** [BatchSize](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-BatchSize"></a>
The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).
Default value: Varies by service. For Amazon SQS, the default is 10. For all other services, the default is 100.
Related setting: When you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [BisectBatchOnFunctionError](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-BisectBatchOnFunctionError"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry. The default value is false.
Type: Boolean

 ** [DestinationConfig](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-DestinationConfig"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.
Type: [DestinationConfig](API_DestinationConfig.md) object

 ** [DocumentDBEventSourceConfig](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-DocumentDBEventSourceConfig"></a>
Specific configuration settings for a DocumentDB event source.
Type: [DocumentDBEventSourceConfig](API_DocumentDBEventSourceConfig.md) object

 ** [EventSourceArn](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-EventSourceArn"></a>
The Amazon Resource Name (ARN) of the event source.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

 ** [EventSourceMappingArn](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-EventSourceMappingArn"></a>
The Amazon Resource Name (ARN) of the event source mapping.
Type: String
Length Constraints: Minimum length of 85. Maximum length of 120.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:event-source-mapping:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [FilterCriteria](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-FilterCriteria"></a>
An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see [Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html).
If filter criteria is encrypted, this field shows up as `null` in the response of ListEventSourceMapping API calls. You can view this field in plaintext in the response of GetEventSourceMapping and DeleteEventSourceMapping calls if you have `kms:Decrypt` permissions for the correct AWS KMS key.
Type: [FilterCriteria](API_FilterCriteria.md) object

 ** [FilterCriteriaError](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-FilterCriteriaError"></a>
An object that contains details about an error related to filter criteria encryption.
Type: [FilterCriteriaError](API_FilterCriteriaError.md) object

 ** [FunctionArn](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-FunctionArn"></a>
The ARN of the Lambda function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`

 ** [FunctionResponseTypes](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-FunctionResponseTypes"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `ReportBatchItemFailures`

 ** [KMSKeyArn](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-KMSKeyArn"></a>
 The ARN of the AWS Key Management Service (AWS KMS) customer managed key that Lambda uses to encrypt your function's [filter criteria](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics).
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`

 ** [LastModified](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-LastModified"></a>
The date that the event source mapping was last updated or that its state changed, in Unix time seconds.
Type: Timestamp

 ** [LastProcessingResult](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-LastProcessingResult"></a>
The result of the event source mapping's last processing attempt.
Type: String

 ** [LoggingConfig](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-LoggingConfig"></a>
(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see [Event source mapping logging](https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html).
Type: [EventSourceMappingLoggingConfig](API_EventSourceMappingLoggingConfig.md) object

 ** [MaximumBatchingWindowInSeconds](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-MaximumBatchingWindowInSeconds"></a>
The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure `MaximumBatchingWindowInSeconds` to any value from 0 seconds to 300 seconds in increments of seconds.
For streams and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change `MaximumBatchingWindowInSeconds` in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.
Related setting: For streams and Amazon SQS event sources, when you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.

 ** [MaximumRecordAgeInSeconds](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-MaximumRecordAgeInSeconds"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, Lambda never discards old records.
The minimum valid value for maximum record age is 60s. Although values less than 60 and greater than -1 fall within the parameter's absolute range, they are not allowed
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 604800.

 ** [MaximumRetryAttempts](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-MaximumRetryAttempts"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, Lambda retries failed records until the record expires in the event source.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 10000.

 ** [MetricsConfig](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-MetricsConfig"></a>
The metrics configuration for your event source. For more information, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics).
Type: [EventSourceMappingMetricsConfig](API_EventSourceMappingMetricsConfig.md) object

 ** [ParallelizationFactor](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-ParallelizationFactor"></a>
(Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [ProvisionedPollerConfig](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-ProvisionedPollerConfig"></a>
(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see [provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode).
Type: [ProvisionedPollerConfig](API_ProvisionedPollerConfig.md) object

 ** [Queues](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-Queues"></a>
 (Amazon MQ) The name of the Amazon MQ broker destination queue to consume.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\s\S]*`

 ** [ScalingConfig](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-ScalingConfig"></a>
(Amazon SQS only) The scaling configuration for the event source. For more information, see [Configuring maximum concurrency for Amazon SQS event sources](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency).
Type: [ScalingConfig](API_ScalingConfig.md) object

 ** [SelfManagedEventSource](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-SelfManagedEventSource"></a>
The self-managed Apache Kafka cluster for your event source.
Type: [SelfManagedEventSource](API_SelfManagedEventSource.md) object

 ** [SelfManagedKafkaEventSourceConfig](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-SelfManagedKafkaEventSourceConfig"></a>
Specific configuration settings for a self-managed Apache Kafka event source.
Type: [SelfManagedKafkaEventSourceConfig](API_SelfManagedKafkaEventSourceConfig.md) object

 ** [SourceAccessConfigurations](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-SourceAccessConfigurations"></a>
An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.
Type: Array of [SourceAccessConfiguration](API_SourceAccessConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 22 items.

 ** [StartingPosition](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-StartingPosition"></a>
The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. `AT_TIMESTAMP` is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.
Type: String
Valid Values: `TRIM_HORIZON | LATEST | AT_TIMESTAMP`

 ** [StartingPositionTimestamp](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-StartingPositionTimestamp"></a>
With `StartingPosition` set to `AT_TIMESTAMP`, the time from which to start reading, in Unix time seconds. `StartingPositionTimestamp` cannot be in the future.
Type: Timestamp

 ** [State](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-State"></a>
The state of the event source mapping. It can be one of the following: `Creating`, `Enabling`, `Enabled`, `Disabling`, `Disabled`, `Updating`, or `Deleting`.
Type: String

 ** [StateTransitionReason](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-StateTransitionReason"></a>
Indicates whether a user or Lambda made the last change to the event source mapping.
Type: String

 ** [Topics](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-Topics"></a>
The name of the Kafka topic.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 249.
Pattern: `[^.]([a-zA-Z0-9\-_.]+)`

 ** [TumblingWindowInSeconds](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-TumblingWindowInSeconds"></a>
(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 900.

 ** [UUID](#API_UpdateEventSourceMapping_ResponseSyntax) **   <a name="lambda-UpdateEventSourceMapping-response-UUID"></a>
The identifier of the event source mapping.
Type: String

## Errors
<a name="API_UpdateEventSourceMapping_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** ResourceInUseException **
The operation conflicts with the resource's availability. For example, you tried to update an event source mapping in the CREATING state, or you tried to delete an event source mapping currently UPDATING.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_UpdateEventSourceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/UpdateEventSourceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/UpdateEventSourceMapping)
