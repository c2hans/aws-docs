---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-eventsourcemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping
<a name="aws-resource-lambda-eventsourcemapping"></a>

The `AWS::Lambda::EventSourceMapping` resource creates a mapping between an event source and an AWS Lambda function. Lambda reads items from the event source and triggers the function.

For details about each event source type, see the following topics. In particular, each of the topics describes the required and optional parameters for the specific event source.
+  [ Configuring a Dynamo DB stream as an event source](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping)
+  [ Configuring a Kinesis stream as an event source](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping)
+  [ Configuring an SQS queue as an event source](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource)
+  [ Configuring an MQ broker as an event source](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping)
+  [ Configuring MSK as an event source](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html)
+  [ Configuring Self-Managed Apache Kafka as an event source](https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html)
+  [ Configuring Amazon DocumentDB as an event source](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html)

## Syntax
<a name="aws-resource-lambda-eventsourcemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-eventsourcemapping-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::EventSourceMapping",
  "Properties" : {
      "[AmazonManagedKafkaEventSourceConfig](#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig)" : {{AmazonManagedKafkaEventSourceConfig}},
      "[BatchSize](#cfn-lambda-eventsourcemapping-batchsize)" : {{Integer}},
      "[BisectBatchOnFunctionError](#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror)" : {{Boolean}},
      "[DestinationConfig](#cfn-lambda-eventsourcemapping-destinationconfig)" : {{DestinationConfig}},
      "[DocumentDBEventSourceConfig](#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig)" : {{DocumentDBEventSourceConfig}},
      "[Enabled](#cfn-lambda-eventsourcemapping-enabled)" : {{Boolean}},
      "[EventSourceArn](#cfn-lambda-eventsourcemapping-eventsourcearn)" : {{String}},
      "[FilterCriteria](#cfn-lambda-eventsourcemapping-filtercriteria)" : {{FilterCriteria}},
      "[FunctionName](#cfn-lambda-eventsourcemapping-functionname)" : {{String}},
      "[FunctionResponseTypes](#cfn-lambda-eventsourcemapping-functionresponsetypes)" : {{[ String, ... ]}},
      "[KmsKeyArn](#cfn-lambda-eventsourcemapping-kmskeyarn)" : {{String}},
      "[LoggingConfig](#cfn-lambda-eventsourcemapping-loggingconfig)" : {{LoggingConfig}},
      "[MaximumBatchingWindowInSeconds](#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds)" : {{Integer}},
      "[MaximumRecordAgeInSeconds](#cfn-lambda-eventsourcemapping-maximumrecordageinseconds)" : {{Integer}},
      "[MaximumRetryAttempts](#cfn-lambda-eventsourcemapping-maximumretryattempts)" : {{Integer}},
      "[MetricsConfig](#cfn-lambda-eventsourcemapping-metricsconfig)" : {{MetricsConfig}},
      "[ParallelizationFactor](#cfn-lambda-eventsourcemapping-parallelizationfactor)" : {{Integer}},
      "[ProvisionedPollerConfig](#cfn-lambda-eventsourcemapping-provisionedpollerconfig)" : {{ProvisionedPollerConfig}},
      "[Queues](#cfn-lambda-eventsourcemapping-queues)" : {{[ String, ... ]}},
      "[ScalingConfig](#cfn-lambda-eventsourcemapping-scalingconfig)" : {{ScalingConfig}},
      "[SelfManagedEventSource](#cfn-lambda-eventsourcemapping-selfmanagedeventsource)" : {{SelfManagedEventSource}},
      "[SelfManagedKafkaEventSourceConfig](#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig)" : {{SelfManagedKafkaEventSourceConfig}},
      "[SourceAccessConfigurations](#cfn-lambda-eventsourcemapping-sourceaccessconfigurations)" : {{[ SourceAccessConfiguration, ... ]}},
      "[StartingPosition](#cfn-lambda-eventsourcemapping-startingposition)" : {{String}},
      "[StartingPositionTimestamp](#cfn-lambda-eventsourcemapping-startingpositiontimestamp)" : {{Number}},
      "[Tags](#cfn-lambda-eventsourcemapping-tags)" : {{[ Tag, ... ]}},
      "[Topics](#cfn-lambda-eventsourcemapping-topics)" : {{[ String, ... ]}},
      "[TumblingWindowInSeconds](#cfn-lambda-eventsourcemapping-tumblingwindowinseconds)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-lambda-eventsourcemapping-syntax.yaml"></a>

```
Type: AWS::Lambda::EventSourceMapping
Properties:
  [AmazonManagedKafkaEventSourceConfig](#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig): {{
    AmazonManagedKafkaEventSourceConfig}}
  [BatchSize](#cfn-lambda-eventsourcemapping-batchsize): {{Integer}}
  [BisectBatchOnFunctionError](#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror): {{Boolean}}
  [DestinationConfig](#cfn-lambda-eventsourcemapping-destinationconfig): {{
    DestinationConfig}}
  [DocumentDBEventSourceConfig](#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig): {{
    DocumentDBEventSourceConfig}}
  [Enabled](#cfn-lambda-eventsourcemapping-enabled): {{Boolean}}
  [EventSourceArn](#cfn-lambda-eventsourcemapping-eventsourcearn): {{String}}
  [FilterCriteria](#cfn-lambda-eventsourcemapping-filtercriteria): {{
    FilterCriteria}}
  [FunctionName](#cfn-lambda-eventsourcemapping-functionname): {{String}}
  [FunctionResponseTypes](#cfn-lambda-eventsourcemapping-functionresponsetypes): {{
    - String}}
  [KmsKeyArn](#cfn-lambda-eventsourcemapping-kmskeyarn): {{String}}
  [LoggingConfig](#cfn-lambda-eventsourcemapping-loggingconfig): {{
    LoggingConfig}}
  [MaximumBatchingWindowInSeconds](#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds): {{Integer}}
  [MaximumRecordAgeInSeconds](#cfn-lambda-eventsourcemapping-maximumrecordageinseconds): {{Integer}}
  [MaximumRetryAttempts](#cfn-lambda-eventsourcemapping-maximumretryattempts): {{Integer}}
  [MetricsConfig](#cfn-lambda-eventsourcemapping-metricsconfig): {{
    MetricsConfig}}
  [ParallelizationFactor](#cfn-lambda-eventsourcemapping-parallelizationfactor): {{Integer}}
  [ProvisionedPollerConfig](#cfn-lambda-eventsourcemapping-provisionedpollerconfig): {{
    ProvisionedPollerConfig}}
  [Queues](#cfn-lambda-eventsourcemapping-queues): {{
    - String}}
  [ScalingConfig](#cfn-lambda-eventsourcemapping-scalingconfig): {{
    ScalingConfig}}
  [SelfManagedEventSource](#cfn-lambda-eventsourcemapping-selfmanagedeventsource): {{
    SelfManagedEventSource}}
  [SelfManagedKafkaEventSourceConfig](#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig): {{
    SelfManagedKafkaEventSourceConfig}}
  [SourceAccessConfigurations](#cfn-lambda-eventsourcemapping-sourceaccessconfigurations): {{
    - SourceAccessConfiguration}}
  [StartingPosition](#cfn-lambda-eventsourcemapping-startingposition): {{String}}
  [StartingPositionTimestamp](#cfn-lambda-eventsourcemapping-startingpositiontimestamp): {{Number}}
  [Tags](#cfn-lambda-eventsourcemapping-tags): {{
    - Tag}}
  [Topics](#cfn-lambda-eventsourcemapping-topics): {{
    - String}}
  [TumblingWindowInSeconds](#cfn-lambda-eventsourcemapping-tumblingwindowinseconds): {{Integer}}
```

## Properties
<a name="aws-resource-lambda-eventsourcemapping-properties"></a>

`AmazonManagedKafkaEventSourceConfig`  <a name="cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig"></a>
Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.
*Required*: No
*Type*: [AmazonManagedKafkaEventSourceConfig](aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BatchSize`  <a name="cfn-lambda-eventsourcemapping-batchsize"></a>
The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).
+ **Amazon Kinesis** – Default 100. Max 10,000.
+ **Amazon DynamoDB Streams** – Default 100. Max 10,000.
+ **Amazon Simple Queue Service** – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.
+ **Amazon Managed Streaming for Apache Kafka** – Default 100. Max 10,000.
+ **Self-managed Apache Kafka** – Default 100. Max 10,000.
+ **Amazon MQ (ActiveMQ and RabbitMQ)** – Default 100. Max 10,000.
+ **DocumentDB** – Default 100. Max 10,000.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BisectBatchOnFunctionError`  <a name="cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror"></a>
(Kinesis and DynamoDB Streams only) If the function returns an error, split the batch in two and retry. The default value is false.
When using `BisectBatchOnFunctionError`, check the `BatchSize` parameter in the `OnFailure` destination message's metadata. The `BatchSize` could be greater than 1 since Lambda consolidates failed messages metadata when writing to the `OnFailure` destination.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationConfig`  <a name="cfn-lambda-eventsourcemapping-destinationconfig"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.
*Required*: No
*Type*: [DestinationConfig](aws-properties-lambda-eventsourcemapping-destinationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentDBEventSourceConfig`  <a name="cfn-lambda-eventsourcemapping-documentdbeventsourceconfig"></a>
Specific configuration settings for a DocumentDB event source.
*Required*: No
*Type*: [DocumentDBEventSourceConfig](aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-lambda-eventsourcemapping-enabled"></a>
When true, the event source mapping is active. When false, Lambda pauses polling and invocation.
Default: True
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventSourceArn`  <a name="cfn-lambda-eventsourcemapping-eventsourcearn"></a>
The Amazon Resource Name (ARN) of the event source.
+ **Amazon Kinesis** – The ARN of the data stream or a stream consumer.
+ **Amazon DynamoDB Streams** – The ARN of the stream.
+ **Amazon Simple Queue Service** – The ARN of the queue.
+ **Amazon Managed Streaming for Apache Kafka** – The ARN of the cluster or the ARN of the VPC connection (for [cross-account event source mappings](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc)).
+ **Amazon MQ** – The ARN of the broker.
+ **Amazon DocumentDB** – The ARN of the DocumentDB change stream.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
*Minimum*: `12`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterCriteria`  <a name="cfn-lambda-eventsourcemapping-filtercriteria"></a>
An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see [Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html).
*Required*: No
*Type*: [FilterCriteria](aws-properties-lambda-eventsourcemapping-filtercriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionName`  <a name="cfn-lambda-eventsourcemapping-functionname"></a>
The name or ARN of the Lambda function.

**Name formats**
+ **Function name** – `MyFunction`.
+ **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
+ **Version or Alias ARN** – `arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`.
+ **Partial ARN** – `123456789012:function:MyFunction`.
The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.
*Required*: Yes
*Type*: String
*Pattern*: `(arn:(aws[a-zA-Z-]*)?:lambda:)?((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionResponseTypes`  <a name="cfn-lambda-eventsourcemapping-functionresponsetypes"></a>
(Kinesis, DynamoDB Streams, and SQS) A list of current response type enums applied to the event source mapping.
Valid Values: `ReportBatchItemFailures`
*Required*: No
*Type*: Array of String
*Allowed values*: `ReportBatchItemFailures`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-lambda-eventsourcemapping-kmskeyarn"></a>
 The ARN of the AWS Key Management Service (AWS KMS) customer managed key that Lambda uses to encrypt your function's [filter criteria](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics).
*Required*: No
*Type*: String
*Pattern*: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
*Minimum*: `12`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingConfig`  <a name="cfn-lambda-eventsourcemapping-loggingconfig"></a>
(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see [Event source mapping logging](https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html).
*Required*: No
*Type*: [LoggingConfig](aws-properties-lambda-eventsourcemapping-loggingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBatchingWindowInSeconds`  <a name="cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds"></a>
The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function.
**Default (Kinesis, DynamoDB, Amazon SQS event sources)**: 0
**Default (Amazon MSK, Kafka, Amazon MQ, Amazon DocumentDB event sources)**: 500 ms
**Related setting: ** For Amazon SQS event sources, when you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumRecordAgeInSeconds`  <a name="cfn-lambda-eventsourcemapping-maximumrecordageinseconds"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, Lambda never discards old records.
The minimum valid value for maximum record age is 60s. Although values less than 60 and greater than -1 fall within the parameter's absolute range, they are not allowed
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `604800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumRetryAttempts`  <a name="cfn-lambda-eventsourcemapping-maximumretryattempts"></a>
(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, Lambda retries failed records until the record expires in the event source.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricsConfig`  <a name="cfn-lambda-eventsourcemapping-metricsconfig"></a>
The metrics configuration for your event source. For more information, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics).
*Required*: No
*Type*: [MetricsConfig](aws-properties-lambda-eventsourcemapping-metricsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParallelizationFactor`  <a name="cfn-lambda-eventsourcemapping-parallelizationfactor"></a>
(Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProvisionedPollerConfig`  <a name="cfn-lambda-eventsourcemapping-provisionedpollerconfig"></a>
(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see [provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode).
*Required*: No
*Type*: [ProvisionedPollerConfig](aws-properties-lambda-eventsourcemapping-provisionedpollerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Queues`  <a name="cfn-lambda-eventsourcemapping-queues"></a>
 (Amazon MQ) The name of the Amazon MQ broker destination queue to consume.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `1000 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingConfig`  <a name="cfn-lambda-eventsourcemapping-scalingconfig"></a>
This property is for Amazon SQS event sources only. You cannot use `ProvisionedPollerConfig` while using `ScalingConfig`. These options are mutually exclusive. To remove the scaling configuration, pass an empty value.
*Required*: No
*Type*: [ScalingConfig](aws-properties-lambda-eventsourcemapping-scalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfManagedEventSource`  <a name="cfn-lambda-eventsourcemapping-selfmanagedeventsource"></a>
The self-managed Apache Kafka cluster for your event source.
*Required*: No
*Type*: [SelfManagedEventSource](aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SelfManagedKafkaEventSourceConfig`  <a name="cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig"></a>
Specific configuration settings for a self-managed Apache Kafka event source.
*Required*: No
*Type*: [SelfManagedKafkaEventSourceConfig](aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceAccessConfigurations`  <a name="cfn-lambda-eventsourcemapping-sourceaccessconfigurations"></a>
An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.
*Required*: No
*Type*: Array of [SourceAccessConfiguration](aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.md)
*Minimum*: `1`
*Maximum*: `22`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartingPosition`  <a name="cfn-lambda-eventsourcemapping-startingposition"></a>
The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB.
+ **LATEST** - Read only new records.
+ **TRIM\_HORIZON** - Process all available records.
+ **AT\_TIMESTAMP** - Specify a time from which to start reading records.
*Required*: No
*Type*: String
*Pattern*: `(LATEST|TRIM_HORIZON|AT_TIMESTAMP)+`
*Minimum*: `6`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartingPositionTimestamp`  <a name="cfn-lambda-eventsourcemapping-startingpositiontimestamp"></a>
With `StartingPosition` set to `AT_TIMESTAMP`, the time from which to start reading, in Unix time seconds. `StartingPositionTimestamp` cannot be in the future.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lambda-eventsourcemapping-tags"></a>
A list of tags to add to the event source mapping.
You must have the `lambda:TagResource`, `lambda:UntagResource`, and `lambda:ListTags` permissions for your [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) to manage the CloudFormation stack. If you don't have these permissions, there might be unexpected behavior with stack-level tags propagating to the resource during resource creation and update.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-eventsourcemapping-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Topics`  <a name="cfn-lambda-eventsourcemapping-topics"></a>
The name of the Kafka topic.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `249 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TumblingWindowInSeconds`  <a name="cfn-lambda-eventsourcemapping-tumblingwindowinseconds"></a>
(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-eventsourcemapping-return-values"></a>

### Ref
<a name="aws-resource-lambda-eventsourcemapping-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the mapping's ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-eventsourcemapping-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lambda-eventsourcemapping-return-values-fn--getatt-fn--getatt"></a>

`EventSourceMappingArn`  <a name="EventSourceMappingArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the event source mapping.

`Id`  <a name="Id-fn::getatt"></a>
The event source mapping's ID.

## Examples
<a name="aws-resource-lambda-eventsourcemapping--examples"></a>

### Event Source Mapping
<a name="aws-resource-lambda-eventsourcemapping--examples--Event_Source_Mapping"></a>

Create an event source mapping that reads events from Amazon Kinesis and invokes a Lambda function in the same template.

#### JSON
<a name="aws-resource-lambda-eventsourcemapping--examples--Event_Source_Mapping--json"></a>

```
"EventSourceMapping": {
    "Type": "AWS::Lambda::EventSourceMapping",
    "Properties": {
        "EventSourceArn": {
            "Fn::Join": [
                "",
                [
                    "arn:aws:kinesis:",
                    {
                        "Ref": "AWS::Region"
                    },
                    ":",
                    {
                        "Ref": "AWS::AccountId"
                    },
                    ":stream/",
                    {
                        "Ref": "KinesisStream"
                    }
                ]
            ]
        },
        "FunctionName": {
            "Fn::GetAtt": [
                "LambdaFunction",
                "Arn"
            ]
        },
        "StartingPosition": "TRIM_HORIZON"
    }
}
```

#### YAML
<a name="aws-resource-lambda-eventsourcemapping--examples--Event_Source_Mapping--yaml"></a>

```
MyEventSourceMapping:
  Type: AWS::Lambda::EventSourceMapping
  Properties:
    EventSourceArn:
      Fn::Join:
        - ""
        -
          - "arn:aws:kinesis:"
          -
            Ref: "AWS::Region"
          - ":"
          -
            Ref: "AWS::AccountId"
          - ":stream/"
          -
            Ref: "KinesisStream"
    FunctionName:
      Fn::GetAtt:
        - "LambdaFunction"
        - "Arn"
    StartingPosition: "TRIM_HORIZON"
```
