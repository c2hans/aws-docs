---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-deliverydestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::DeliveryDestination
<a name="aws-resource-logs-deliverydestination"></a>

This structure contains information about one *delivery destination* in your account. A delivery destination is an AWS resource that represents an AWS service that logs can be sent to. CloudWatch Logs, Amazon S3, Firehose, and X-Ray are supported as delivery destinations.

To configure logs delivery between a supported AWS service and a destination, you must do the following:
+ Create a delivery source, which is a logical object that represents the resource that is actually sending the logs. For more information, see [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html).
+ Create a *delivery destination*, which is a logical object that represents the actual delivery destination.
+ If you are delivering logs cross-account, you must use [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination.
+ Create a *delivery* by pairing exactly one delivery source and one delivery destination. For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

## Syntax
<a name="aws-resource-logs-deliverydestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-deliverydestination-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::DeliveryDestination",
  "Properties" : {
      "[DeliveryDestinationPolicy](#cfn-logs-deliverydestination-deliverydestinationpolicy)" : {{DestinationPolicy}},
      "[DeliveryDestinationType](#cfn-logs-deliverydestination-deliverydestinationtype)" : {{String}},
      "[DestinationResourceArn](#cfn-logs-deliverydestination-destinationresourcearn)" : {{String}},
      "[Name](#cfn-logs-deliverydestination-name)" : {{String}},
      "[OutputFormat](#cfn-logs-deliverydestination-outputformat)" : {{String}},
      "[Tags](#cfn-logs-deliverydestination-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-logs-deliverydestination-syntax.yaml"></a>

```
Type: AWS::Logs::DeliveryDestination
Properties:
  [DeliveryDestinationPolicy](#cfn-logs-deliverydestination-deliverydestinationpolicy): {{
    DestinationPolicy}}
  [DeliveryDestinationType](#cfn-logs-deliverydestination-deliverydestinationtype): {{String}}
  [DestinationResourceArn](#cfn-logs-deliverydestination-destinationresourcearn): {{String}}
  [Name](#cfn-logs-deliverydestination-name): {{String}}
  [OutputFormat](#cfn-logs-deliverydestination-outputformat): {{String}}
  [Tags](#cfn-logs-deliverydestination-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-logs-deliverydestination-properties"></a>

`DeliveryDestinationPolicy`  <a name="cfn-logs-deliverydestination-deliverydestinationpolicy"></a>
An IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account. For examples of this policy, see [Examples](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html#API_PutDeliveryDestinationPolicy_Examples) in the CloudWatch Logs API Reference.
*Required*: No
*Type*: [DestinationPolicy](aws-properties-logs-deliverydestination-destinationpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliveryDestinationType`  <a name="cfn-logs-deliverydestination-deliverydestinationtype"></a>
Displays whether this delivery destination is CloudWatch Logs, Amazon S3, Firehose, or X-Ray.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z]+$`
*Minimum*: `1`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationResourceArn`  <a name="cfn-logs-deliverydestination-destinationresourcearn"></a>
The ARN of the AWS destination that this delivery destination represents. That AWS destination can be a log group in CloudWatch Logs, an Amazon S3 bucket, or a Firehose stream.
*Required*: No
*Type*: String
*Pattern*: `[\w#+=/:,.@-]*\*?`
*Minimum*: `16`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-logs-deliverydestination-name"></a>
The name of this delivery destination.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]*$`
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputFormat`  <a name="cfn-logs-deliverydestination-outputformat"></a>
The format of the logs that are sent to this delivery destination.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z]+$`
*Minimum*: `1`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-logs-deliverydestination-tags"></a>
An array of key-value pairs to apply to the delivery destination.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-logs-deliverydestination-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-deliverydestination-return-values"></a>

### Ref
<a name="aws-resource-logs-deliverydestination-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-logs-deliverydestination-return-values-fn--getatt"></a>

####
<a name="aws-resource-logs-deliverydestination-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
