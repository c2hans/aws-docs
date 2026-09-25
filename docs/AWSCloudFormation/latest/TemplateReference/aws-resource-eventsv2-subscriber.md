---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eventsv2-subscriber.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber
<a name="aws-resource-eventsv2-subscriber"></a>

Resource type definition for `AWS::EventsV2::Subscriber`, an Amazon EventBridge subscription that delivers events from an event bus to a target. Canonical identity is the combination of bus, name, and target. Replacement uses delete\_then\_create.

## Syntax
<a name="aws-resource-eventsv2-subscriber-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-eventsv2-subscriber-syntax.json"></a>

```
{
  "Type" : "AWS::EventsV2::Subscriber",
  "Properties" : {
      "[BatchConfiguration](#cfn-eventsv2-subscriber-batchconfiguration)" : {{BatchConfiguration}},
      "[Description](#cfn-eventsv2-subscriber-description)" : {{String}},
      "[EventBusArn](#cfn-eventsv2-subscriber-eventbusarn)" : {{String}},
      "[FilterConfiguration](#cfn-eventsv2-subscriber-filterconfiguration)" : {{FilterConfiguration}},
      "[InvokeConfiguration](#cfn-eventsv2-subscriber-invokeconfiguration)" : {{InvokeConfiguration}},
      "[LogConfiguration](#cfn-eventsv2-subscriber-logconfiguration)" : {{LogConfiguration}},
      "[Name](#cfn-eventsv2-subscriber-name)" : {{String}},
      "[OnFailureConfiguration](#cfn-eventsv2-subscriber-onfailureconfiguration)" : {{OnFailureConfiguration}},
      "[PointInTimeConfiguration](#cfn-eventsv2-subscriber-pointintimeconfiguration)" : {{PointInTimeConfiguration}},
      "[ResumePosition](#cfn-eventsv2-subscriber-resumeposition)" : {{String}},
      "[RetryPolicy](#cfn-eventsv2-subscriber-retrypolicy)" : {{RetryPolicy}},
      "[StartingPosition](#cfn-eventsv2-subscriber-startingposition)" : {{String}},
      "[State](#cfn-eventsv2-subscriber-state)" : {{String}},
      "[Tags](#cfn-eventsv2-subscriber-tags)" : {{[ Tag, ... ]}},
      "[Transformer](#cfn-eventsv2-subscriber-transformer)" : {{Transformer}},
      "[Type](#cfn-eventsv2-subscriber-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-eventsv2-subscriber-syntax.yaml"></a>

```
Type: AWS::EventsV2::Subscriber
Properties:
  [BatchConfiguration](#cfn-eventsv2-subscriber-batchconfiguration): {{
    BatchConfiguration}}
  [Description](#cfn-eventsv2-subscriber-description): {{String}}
  [EventBusArn](#cfn-eventsv2-subscriber-eventbusarn): {{String}}
  [FilterConfiguration](#cfn-eventsv2-subscriber-filterconfiguration): {{
    FilterConfiguration}}
  [InvokeConfiguration](#cfn-eventsv2-subscriber-invokeconfiguration): {{
    InvokeConfiguration}}
  [LogConfiguration](#cfn-eventsv2-subscriber-logconfiguration): {{
    LogConfiguration}}
  [Name](#cfn-eventsv2-subscriber-name): {{String}}
  [OnFailureConfiguration](#cfn-eventsv2-subscriber-onfailureconfiguration): {{
    OnFailureConfiguration}}
  [PointInTimeConfiguration](#cfn-eventsv2-subscriber-pointintimeconfiguration): {{
    PointInTimeConfiguration}}
  [ResumePosition](#cfn-eventsv2-subscriber-resumeposition): {{String}}
  [RetryPolicy](#cfn-eventsv2-subscriber-retrypolicy): {{
    RetryPolicy}}
  [StartingPosition](#cfn-eventsv2-subscriber-startingposition): {{String}}
  [State](#cfn-eventsv2-subscriber-state): {{String}}
  [Tags](#cfn-eventsv2-subscriber-tags): {{
    - Tag}}
  [Transformer](#cfn-eventsv2-subscriber-transformer): {{
    Transformer}}
  [Type](#cfn-eventsv2-subscriber-type): {{String}}
```

## Properties
<a name="aws-resource-eventsv2-subscriber-properties"></a>

`BatchConfiguration`  <a name="cfn-eventsv2-subscriber-batchconfiguration"></a>
Configuration for batching events into a single delivery to the target.
*Required*: No
*Type*: [BatchConfiguration](aws-properties-eventsv2-subscriber-batchconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-eventsv2-subscriber-description"></a>
A description of the subscriber. Control characters and Unicode line separators are not allowed.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F-\u009F\u2028\u2029]*(?![\s\S])`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventBusArn`  <a name="cfn-eventsv2-subscriber-eventbusarn"></a>
The ARN of the event bus this subscriber belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterConfiguration`  <a name="cfn-eventsv2-subscriber-filterconfiguration"></a>
Configuration for filtering which events are delivered to the target. An event must match every filter to be delivered.
*Required*: No
*Type*: [FilterConfiguration](aws-properties-eventsv2-subscriber-filterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvokeConfiguration`  <a name="cfn-eventsv2-subscriber-invokeconfiguration"></a>
Configuration for how the subscriber invokes its target, including the target ARN, the IAM role used to invoke it, and, optionally, the target-specific parameters object that matches the target type.
*Required*: Yes
*Type*: [InvokeConfiguration](aws-properties-eventsv2-subscriber-invokeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-eventsv2-subscriber-logconfiguration"></a>
Delivery logging configuration for the subscriber.
*Required*: No
*Type*: [LogConfiguration](aws-properties-eventsv2-subscriber-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-eventsv2-subscriber-name"></a>
The name of the subscriber. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '\_'.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][\.\-_A-Za-z0-9]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OnFailureConfiguration`  <a name="cfn-eventsv2-subscriber-onfailureconfiguration"></a>
The destination for events that could not be delivered to the target.
*Required*: No
*Type*: [OnFailureConfiguration](aws-properties-eventsv2-subscriber-onfailureconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PointInTimeConfiguration`  <a name="cfn-eventsv2-subscriber-pointintimeconfiguration"></a>
The point in time to start delivering events from. Used when StartingPosition is POINT\_IN\_TIME.
*Required*: No
*Type*: [PointInTimeConfiguration](aws-properties-eventsv2-subscriber-pointintimeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResumePosition`  <a name="cfn-eventsv2-subscriber-resumeposition"></a>
Resume-time control, never returned by the service. Applied only when an update transitions State from STOPPED to RUNNING: LAST\_PROCESSED (default) resumes from the last processed event, LATEST skips to the newest. Ignored on create and on any update that does not perform that transition.
*Required*: No
*Type*: String
*Allowed values*: `LAST_PROCESSED | LATEST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryPolicy`  <a name="cfn-eventsv2-subscriber-retrypolicy"></a>
The retry policy for failed deliveries to the target.
*Required*: No
*Type*: [RetryPolicy](aws-properties-eventsv2-subscriber-retrypolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartingPosition`  <a name="cfn-eventsv2-subscriber-startingposition"></a>
Where the subscriber starts reading events: LATEST starts from the newest events; POINT\_IN\_TIME starts from the point specified in PointInTimeConfiguration.
*Required*: No
*Type*: String
*Allowed values*: `LATEST | POINT_IN_TIME`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`State`  <a name="cfn-eventsv2-subscriber-state"></a>
The run state of the subscriber. Events are delivered only while the state is RUNNING. Setting the state to STOPPED pauses delivery. When an update sets a stopped subscriber back to RUNNING, ResumePosition controls where delivery resumes.
*Required*: No
*Type*: String
*Allowed values*: `RUNNING | STOPPED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-eventsv2-subscriber-tags"></a>
An array of key-value pairs to apply to the subscriber. You can apply a maximum of 50 tags.
For more information about tagging, see [Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-eventsv2-subscriber-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Transformer`  <a name="cfn-eventsv2-subscriber-transformer"></a>
Configuration for transforming events before delivery to the target.
*Required*: No
*Type*: [Transformer](aws-properties-eventsv2-subscriber-transformer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-eventsv2-subscriber-type"></a>
The delivery ordering mode of the subscriber. FIFO delivers events in order within an event group; UNORDERED delivers without an ordering guarantee.
*Required*: No
*Type*: String
*Allowed values*: `FIFO | UNORDERED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-eventsv2-subscriber-return-values"></a>

### Ref
<a name="aws-resource-eventsv2-subscriber-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the subscriber Amazon Resource Name (ARN), such as `arn:aws:events:us-east-1:123456789012:subscriber/orders-to-queue/a1b2c3d4e5f6g7h8i9j0k1l2m`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-eventsv2-subscriber-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-eventsv2-subscriber-return-values-fn--getatt-fn--getatt"></a>

`BusName`  <a name="BusName-fn::getatt"></a>
The name of the event bus that this subscriber belongs to.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the subscriber was created, as an ISO 8601 timestamp.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time the subscriber was last modified, as an ISO 8601 timestamp.

`SubscriberArn`  <a name="SubscriberArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the subscriber.

## Examples
<a name="aws-resource-eventsv2-subscriber--examples"></a>

The following examples deliver events from an event bus to a target.

**Topics**
+ [Create a minimal subscriber](#aws-resource-eventsv2-subscriber--examples--Create_a_minimal_subscriber)
+ [Create a filtered subscriber with batching and retries](#aws-resource-eventsv2-subscriber--examples--Create_a_filtered_subscriber_with_batching_and_retries)

### Create a minimal subscriber
<a name="aws-resource-eventsv2-subscriber--examples--Create_a_minimal_subscriber"></a>

The following example delivers events to an Amazon SQS queue by using an IAM role.

#### JSON
<a name="aws-resource-eventsv2-subscriber--examples--Create_a_minimal_subscriber--json"></a>

```
{
  "Resources": {
    "OrdersSubscriber": {
      "Type": "AWS::EventsV2::Subscriber",
      "Properties": {
        "Name": "orders-to-queue",
        "EventBusArn": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
        "InvokeConfiguration": {
          "TargetArn": "arn:aws:sqs:us-east-1:123456789012:orders-queue",
          "RoleArn": "arn:aws:iam::123456789012:role/EventBridgeInvokeSqs"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-subscriber--examples--Create_a_minimal_subscriber--yaml"></a>

```
Resources:
  OrdersSubscriber:
    Type: AWS::EventsV2::Subscriber
    Properties:
      Name: orders-to-queue
      EventBusArn: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
      InvokeConfiguration:
        TargetArn: arn:aws:sqs:us-east-1:123456789012:orders-queue
        RoleArn: arn:aws:iam::123456789012:role/EventBridgeInvokeSqs
```

### Create a filtered subscriber with batching and retries
<a name="aws-resource-eventsv2-subscriber--examples--Create_a_filtered_subscriber_with_batching_and_retries"></a>

The following example delivers matching events to a Lambda function. It batches events, retries failures, sends undeliverable events to an Amazon SQS queue, and logs errors.

#### JSON
<a name="aws-resource-eventsv2-subscriber--examples--Create_a_filtered_subscriber_with_batching_and_retries--json"></a>

```
{
  "Resources": {
    "OrdersSubscriber": {
      "Type": "AWS::EventsV2::Subscriber",
      "Properties": {
        "Name": "orders-to-function",
        "EventBusArn": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
        "Type": "UNORDERED",
        "InvokeConfiguration": {
          "TargetArn": "arn:aws:lambda:us-east-1:123456789012:function:ProcessOrders",
          "RoleArn": "arn:aws:iam::123456789012:role/EventBridgeInvokeLambda",
          "LambdaParameters": {
            "InvocationType": "REQUEST_RESPONSE"
          }
        },
        "FilterConfiguration": {
          "Filters": [
            { "Pattern": "{\"detail-type\":[\"Order Placed\"]}", "Scope": "DATA" }
          ]
        },
        "BatchConfiguration": {
          "MaxBatchSize": 10,
          "MaxBatchWindowInSeconds": 5
        },
        "RetryPolicy": {
          "MaxRetryAttempts": 10,
          "MaxEventAgeInSeconds": 3600,
          "RetryStrategy": "ALL"
        },
        "OnFailureConfiguration": {
          "Arn": "arn:aws:sqs:us-east-1:123456789012:orders-dlq"
        },
        "LogConfiguration": {
          "Level": "ERROR",
          "IncludePayload": "ON_ERROR_ONLY"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-subscriber--examples--Create_a_filtered_subscriber_with_batching_and_retries--yaml"></a>

```
Resources:
  OrdersSubscriber:
    Type: AWS::EventsV2::Subscriber
    Properties:
      Name: orders-to-function
      EventBusArn: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
      Type: UNORDERED
      InvokeConfiguration:
        TargetArn: arn:aws:lambda:us-east-1:123456789012:function:ProcessOrders
        RoleArn: arn:aws:iam::123456789012:role/EventBridgeInvokeLambda
        LambdaParameters:
          InvocationType: REQUEST_RESPONSE
      FilterConfiguration:
        Filters:
          - Pattern: '{"detail-type":["Order Placed"]}'
            Scope: DATA
      BatchConfiguration:
        MaxBatchSize: 10
        MaxBatchWindowInSeconds: 5
      RetryPolicy:
        MaxRetryAttempts: 10
        MaxEventAgeInSeconds: 3600
        RetryStrategy: ALL
      OnFailureConfiguration:
        Arn: arn:aws:sqs:us-east-1:123456789012:orders-dlq
      LogConfiguration:
        Level: ERROR
        IncludePayload: ON_ERROR_ONLY
```
