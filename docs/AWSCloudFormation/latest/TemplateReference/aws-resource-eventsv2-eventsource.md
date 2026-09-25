---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eventsv2-eventsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource
<a name="aws-resource-eventsv2-eventsource"></a>

Resource schema for `AWS::EventsV2::EventSource`. A managed event source that forwards AWS service events or partner events onto a custom event bus.

## Syntax
<a name="aws-resource-eventsv2-eventsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-eventsv2-eventsource-syntax.json"></a>

```
{
  "Type" : "AWS::EventsV2::EventSource",
  "Properties" : {
      "[Configuration](#cfn-eventsv2-eventsource-configuration)" : {{EventSourceConfiguration}},
      "[Description](#cfn-eventsv2-eventsource-description)" : {{String}},
      "[EventBusArn](#cfn-eventsv2-eventsource-eventbusarn)" : {{String}},
      "[Name](#cfn-eventsv2-eventsource-name)" : {{String}},
      "[Tags](#cfn-eventsv2-eventsource-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-eventsv2-eventsource-syntax.yaml"></a>

```
Type: AWS::EventsV2::EventSource
Properties:
  [Configuration](#cfn-eventsv2-eventsource-configuration): {{
    EventSourceConfiguration}}
  [Description](#cfn-eventsv2-eventsource-description): {{String}}
  [EventBusArn](#cfn-eventsv2-eventsource-eventbusarn): {{String}}
  [Name](#cfn-eventsv2-eventsource-name): {{String}}
  [Tags](#cfn-eventsv2-eventsource-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-eventsv2-eventsource-properties"></a>

`Configuration`  <a name="cfn-eventsv2-eventsource-configuration"></a>
The event source configuration. Specify exactly one of AwsServiceEventsConfiguration or PartnerEventsConfiguration.
*Required*: Yes
*Type*: [EventSourceConfiguration](aws-properties-eventsv2-eventsource-eventsourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-eventsv2-eventsource-description"></a>
A description of the event source. Control characters and Unicode line separators are not allowed.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F-\u009F\u2028\u2029]*(?![\s\S])`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventBusArn`  <a name="cfn-eventsv2-eventsource-eventbusarn"></a>
The ARN of the custom event bus the event source forwards onto.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-eventsv2-eventsource-name"></a>
The name of the event source. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '\_'. Names cannot begin with the reserved aws. prefix.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws\.)[A-Za-z0-9][\.\-_A-Za-z0-9]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-eventsv2-eventsource-tags"></a>
An array of key-value pairs to apply to the event source. You can apply a maximum of 50 tags.
For more information about tagging, see [Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-eventsv2-eventsource-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-eventsv2-eventsource-return-values"></a>

### Ref
<a name="aws-resource-eventsv2-eventsource-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the event source Amazon Resource Name (ARN), such as `arn:aws:events:us-east-1:123456789012:event-sourcev2/aws.service/s3-events/a1b2c3d4e5f6g7h8i9j0k1l2m`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-eventsv2-eventsource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-eventsv2-eventsource-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the event source was created, as an ISO 8601 timestamp.

`EventSourceArn`  <a name="EventSourceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the event source.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time the event source was last modified, as an ISO 8601 timestamp.

`Revoked`  <a name="Revoked-fn::getatt"></a>
Whether the event bus owner has revoked this event source. Revocation is permanent. You can delete a revoked event source, but you can't update it.

`State`  <a name="State-fn::getatt"></a>
The current lifecycle state of the event source, such as `ACTIVE`. The `Revoked` attribute, not the state, indicates whether the event bus owner has revoked the event source.

## Examples
<a name="aws-resource-eventsv2-eventsource--examples"></a>

The following examples forward events to a custom event bus.

**Topics**
+ [Forward all events from an Amazon EventBridge service source](#aws-resource-eventsv2-eventsource--examples--Forward_all_events_from_an_Amazon_EventBridge_service_source)
+ [Filter forwarded events and set a failure destination](#aws-resource-eventsv2-eventsource--examples--Filter_forwarded_events_and_set_a_failure_destination)
+ [Forward a partner event source](#aws-resource-eventsv2-eventsource--examples--Forward_a_partner_event_source)

### Forward all events from an Amazon EventBridge service source
<a name="aws-resource-eventsv2-eventsource--examples--Forward_all_events_from_an_Amazon_EventBridge_service_source"></a>

The following example forwards all Amazon S3 events from the account's default event bus to a custom event bus.

#### JSON
<a name="aws-resource-eventsv2-eventsource--examples--Forward_all_events_from_an_Amazon_EventBridge_service_source--json"></a>

```
{
  "Resources": {
    "S3EventSource": {
      "Type": "AWS::EventsV2::EventSource",
      "Properties": {
        "Name": "s3-events",
        "EventBusArn": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
        "Configuration": {
          "AwsServiceEventsConfiguration": {
            "AwsService": "aws.s3"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-eventsource--examples--Forward_all_events_from_an_Amazon_EventBridge_service_source--yaml"></a>

```
Resources:
  S3EventSource:
    Type: AWS::EventsV2::EventSource
    Properties:
      Name: s3-events
      EventBusArn: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
      Configuration:
        AwsServiceEventsConfiguration:
          AwsService: aws.s3
```

### Filter forwarded events and set a failure destination
<a name="aws-resource-eventsv2-eventsource--examples--Filter_forwarded_events_and_set_a_failure_destination"></a>

The following example forwards only matching Amazon S3 events and sends undeliverable events to an Amazon SQS queue.

#### JSON
<a name="aws-resource-eventsv2-eventsource--examples--Filter_forwarded_events_and_set_a_failure_destination--json"></a>

```
{
  "Resources": {
    "S3EventSource": {
      "Type": "AWS::EventsV2::EventSource",
      "Properties": {
        "Name": "s3-object-created",
        "EventBusArn": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
        "Configuration": {
          "AwsServiceEventsConfiguration": {
            "AwsService": "aws.s3",
            "Pattern": "{\"detail-type\":[\"Object Created\"]}",
            "OnFailureConfiguration": {
              "Arn": "arn:aws:sqs:us-east-1:123456789012:event-source-dlq"
            }
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-eventsource--examples--Filter_forwarded_events_and_set_a_failure_destination--yaml"></a>

```
Resources:
  S3EventSource:
    Type: AWS::EventsV2::EventSource
    Properties:
      Name: s3-object-created
      EventBusArn: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
      Configuration:
        AwsServiceEventsConfiguration:
          AwsService: aws.s3
          Pattern: '{"detail-type":["Object Created"]}'
          OnFailureConfiguration:
            Arn: arn:aws:sqs:us-east-1:123456789012:event-source-dlq
```

### Forward a partner event source
<a name="aws-resource-eventsv2-eventsource--examples--Forward_a_partner_event_source"></a>

The following example forwards events from a partner event source through a managed partner event bus.

#### JSON
<a name="aws-resource-eventsv2-eventsource--examples--Forward_a_partner_event_source--json"></a>

```
{
  "Resources": {
    "PartnerEventSource": {
      "Type": "AWS::EventsV2::EventSource",
      "Properties": {
        "Name": "example-partner-source",
        "EventBusArn": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
        "Configuration": {
          "PartnerEventsConfiguration": {
            "PartnerEventSourceArn": "arn:aws:events:us-east-1::event-source/aws.partner/examplepartner.com/1234567890/example-source"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-eventsource--examples--Forward_a_partner_event_source--yaml"></a>

```
Resources:
  PartnerEventSource:
    Type: AWS::EventsV2::EventSource
    Properties:
      Name: example-partner-source
      EventBusArn: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
      Configuration:
        PartnerEventsConfiguration:
          PartnerEventSourceArn: arn:aws:events:us-east-1::event-source/aws.partner/examplepartner.com/1234567890/example-source
```
