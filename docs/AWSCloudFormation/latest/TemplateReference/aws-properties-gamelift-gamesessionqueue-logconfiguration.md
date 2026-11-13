---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-gamesessionqueue-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::GameSessionQueue LogConfiguration
<a name="aws-properties-gamelift-gamesessionqueue-logconfiguration"></a>

An optional configuration that delivers game session placement insight logs to one or more destinations of your choice. Use these logs to diagnose why a game session placement is `FULFILLED`, `CANCELLED`, `TIMED_OUT`, or `FAILED`, which locations were evaluated, and the latency and cost factors that influenced each decision.

 **Related data type: ** [GameSessionQueueLogConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameSessionQueueLogConfiguration.html)

## Syntax
<a name="aws-properties-gamelift-gamesessionqueue-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-gamesessionqueue-logconfiguration-syntax.json"></a>

```
{
  "[DeliveryDestinations](#cfn-gamelift-gamesessionqueue-logconfiguration-deliverydestinations)" : {{[ DeliveryDestination, ... ]}}
}
```

### YAML
<a name="aws-properties-gamelift-gamesessionqueue-logconfiguration-syntax.yaml"></a>

```
  [DeliveryDestinations](#cfn-gamelift-gamesessionqueue-logconfiguration-deliverydestinations): {{
    - DeliveryDestination}}
```

## Properties
<a name="aws-properties-gamelift-gamesessionqueue-logconfiguration-properties"></a>

`DeliveryDestinations`  <a name="cfn-gamelift-gamesessionqueue-logconfiguration-deliverydestinations"></a>
The destinations that receive game session placement insight logs for the queue. You can specify up to 3 destinations. Each destination must have a unique ARN.
*Required*: Yes
*Type*: Array of [DeliveryDestination](aws-properties-gamelift-gamesessionqueue-deliverydestination.md)
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-gamelift-gamesessionqueue-logconfiguration--seealso"></a>
+ [ Create Amazon GameLift Servers resources using AWS CloudFormation](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Servers Developer Guide*
+ [ Create a queue](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-creating.html) in the *Amazon GameLift Servers Developer Guide*
+ [GameSessionQueueLogConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameSessionQueueLogConfiguration.html) in the *Amazon GameLift Servers API Reference*
