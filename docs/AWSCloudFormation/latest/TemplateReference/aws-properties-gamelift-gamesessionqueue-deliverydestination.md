---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-gamesessionqueue-deliverydestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::GameSessionQueue DeliveryDestination
<a name="aws-properties-gamelift-gamesessionqueue-deliverydestination"></a>

A destination that receives game session placement insight logs for a game session queue. Amazon GameLift Servers delivers the logs to the resource identified by `DestinationArn`. For `CLOUDWATCH` and `S3` destinations, Amazon GameLift Servers creates a resource of the specified `LogDestination` type on your behalf when you omit the ARN; `FIREHOSE` destinations require the ARN.

**Note**
Amazon CloudWatch Logs vended log charges apply to each destination. Amazon S3 and Amazon Data Firehose destinations also incur their own service charges. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

 **Related data type: ** [LogDeliveryDestination](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LogDeliveryDestination.html)

## Syntax
<a name="aws-properties-gamelift-gamesessionqueue-deliverydestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-gamesessionqueue-deliverydestination-syntax.json"></a>

```
{
  "[DestinationArn](#cfn-gamelift-gamesessionqueue-deliverydestination-destinationarn)" : {{String}},
  "[LogDestination](#cfn-gamelift-gamesessionqueue-deliverydestination-logdestination)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-gamesessionqueue-deliverydestination-syntax.yaml"></a>

```
  [DestinationArn](#cfn-gamelift-gamesessionqueue-deliverydestination-destinationarn): {{String}}
  [LogDestination](#cfn-gamelift-gamesessionqueue-deliverydestination-logdestination): {{String}}
```

## Properties
<a name="aws-properties-gamelift-gamesessionqueue-deliverydestination-properties"></a>

`DestinationArn`  <a name="cfn-gamelift-gamesessionqueue-deliverydestination-destinationarn"></a>
The Amazon Resource Name (ARN) of the resource that receives the game session placement insight logs. This resource must match the type that you specify in `LogDestination`. This value is required for `FIREHOSE` destinations. For `CLOUDWATCH` and `S3`, you can omit this value; Amazon GameLift Servers then creates a destination resource of the specified type on your behalf.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-zA-Z0-9:/*._#-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogDestination`  <a name="cfn-gamelift-gamesessionqueue-deliverydestination-logdestination"></a>
The type of AWS resource that receives the game session placement insight logs.
Valid values:
+ `CLOUDWATCH` -- An Amazon CloudWatch Logs log group. Amazon GameLift Servers creates it for you if you omit `DestinationArn`.
+ `S3` -- An Amazon S3 bucket. Amazon GameLift Servers creates it for you if you omit `DestinationArn`.
+ `FIREHOSE` -- An existing Amazon Data Firehose delivery stream. `DestinationArn` is required.
*Required*: Yes
*Type*: String
*Allowed values*: `CLOUDWATCH | S3 | FIREHOSE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-gamelift-gamesessionqueue-deliverydestination--seealso"></a>
+ [ Create Amazon GameLift Servers resources using AWS CloudFormation](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Servers Developer Guide*
+ [ Create a queue](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-creating.html) in the *Amazon GameLift Servers Developer Guide*
+ [LogDeliveryDestination](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LogDeliveryDestination.html) in the *Amazon GameLift Servers API Reference*
