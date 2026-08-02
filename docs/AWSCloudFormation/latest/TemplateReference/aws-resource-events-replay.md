---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-replay.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Replay
<a name="aws-resource-events-replay"></a>

A `Replay` object that contains details about a replay.

## Syntax
<a name="aws-resource-events-replay-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-events-replay-syntax.json"></a>

```
{
  "Type" : "AWS::Events::Replay",
  "Properties" : {
      "[Destination](#cfn-events-replay-destination)" : {{Destination}},
      "[EventEndTime](#cfn-events-replay-eventendtime)" : {{String}},
      "[EventSourceArn](#cfn-events-replay-eventsourcearn)" : {{String}},
      "[EventStartTime](#cfn-events-replay-eventstarttime)" : {{String}},
      "[ReplayName](#cfn-events-replay-replayname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-events-replay-syntax.yaml"></a>

```
Type: AWS::Events::Replay
Properties:
  [Destination](#cfn-events-replay-destination): {{
    Destination}}
  [EventEndTime](#cfn-events-replay-eventendtime): {{String}}
  [EventSourceArn](#cfn-events-replay-eventsourcearn): {{String}}
  [EventStartTime](#cfn-events-replay-eventstarttime): {{String}}
  [ReplayName](#cfn-events-replay-replayname): {{String}}
```

## Properties
<a name="aws-resource-events-replay-properties"></a>

`Destination`  <a name="cfn-events-replay-destination"></a>
Property description not available.
*Required*: Yes
*Type*: [Destination](aws-properties-events-replay-destination.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventEndTime`  <a name="cfn-events-replay-eventendtime"></a>
A time stamp for the time to start replaying events. Any event with a creation time prior to the `EventEndTime` specified is replayed.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventSourceArn`  <a name="cfn-events-replay-eventsourcearn"></a>
The ARN of the archive to replay event from.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventStartTime`  <a name="cfn-events-replay-eventstarttime"></a>
A time stamp for the time to start replaying events. This is determined by the time in the event as described in [Time](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEventsRequestEntry.html#eventbridge-Type-PutEventsRequestEntry-Time).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReplayName`  <a name="cfn-events-replay-replayname"></a>
The name of the replay.
*Required*: Yes
*Type*: String
*Pattern*: `^[\.\-_A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-events-replay-return-values"></a>

### Ref
<a name="aws-resource-events-replay-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-events-replay-return-values-fn--getatt"></a>

####
<a name="aws-resource-events-replay-return-values-fn--getatt-fn--getatt"></a>

`ReplayArn`  <a name="ReplayArn-fn::getatt"></a>
Property description not available.

`ReplayStartTime`  <a name="ReplayStartTime-fn::getatt"></a>
A time stamp for the time that the replay started.

`State`  <a name="State-fn::getatt"></a>
The current state of the replay.
