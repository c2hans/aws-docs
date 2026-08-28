---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-deliverysource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::DeliverySource
<a name="aws-resource-logs-deliverysource"></a>

Creates or updates one *delivery source* in your account. A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Firehose.

Only some AWS services support being configured as a delivery source. These services are listed as **Supported [V2 Permissions]** in the table at [Enabling logging from AWS services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)

To configure logs delivery between a supported AWS service and a destination, you must do the following:
+ Create a delivery source, which is a logical object that represents the resource that is actually sending the logs.
+ Create a *delivery destination*, which is a logical object that represents the actual delivery destination. For more information, see [AWS::Logs::DeliveryDestination](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html) or [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html).
+ Create a *delivery* by pairing exactly one delivery source and one delivery destination. For more information, see [AWS::Logs::Delivery](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html) or [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

## Syntax
<a name="aws-resource-logs-deliverysource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-deliverysource-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::DeliverySource",
  "Properties" : {
      "[DeliverySourceConfiguration](#cfn-logs-deliverysource-deliverysourceconfiguration)" : {{{{{Key}}: {{Value}}, ...}}},
      "[LogType](#cfn-logs-deliverysource-logtype)" : {{String}},
      "[Name](#cfn-logs-deliverysource-name)" : {{String}},
      "[ResourceArn](#cfn-logs-deliverysource-resourcearn)" : {{String}},
      "[Tags](#cfn-logs-deliverysource-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-logs-deliverysource-syntax.yaml"></a>

```
Type: AWS::Logs::DeliverySource
Properties:
  [DeliverySourceConfiguration](#cfn-logs-deliverysource-deliverysourceconfiguration): {{
    {{Key}}: {{Value}}}}
  [LogType](#cfn-logs-deliverysource-logtype): {{String}}
  [Name](#cfn-logs-deliverysource-name): {{String}}
  [ResourceArn](#cfn-logs-deliverysource-resourcearn): {{String}}
  [Tags](#cfn-logs-deliverysource-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-logs-deliverysource-properties"></a>

`DeliverySourceConfiguration`  <a name="cfn-logs-deliverysource-deliverysourceconfiguration"></a>
The map of key-value pairs that configure the delivery source.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{1,255}$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogType`  <a name="cfn-logs-deliverysource-logtype"></a>
The type of log that the source is sending. For valid values for this parameter, see the documentation for the source service.
*Required*: No
*Type*: String
*Pattern*: `[\w-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-logs-deliverysource-name"></a>
The unique name of the delivery source.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]*$`
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceArn`  <a name="cfn-logs-deliverysource-resourcearn"></a>
The ARN of the AWS resource that is generating and sending logs. For example, `arn:aws:workmail:us-east-1:123456789012:organization/m-1234EXAMPLEabcd1234abcd1234abcd1234`
*Required*: No
*Type*: String
*Pattern*: `[\w#+=/:,.@-]*\*?`
*Minimum*: `16`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-logs-deliverysource-tags"></a>
An array of key-value pairs to apply to the delivery source.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-logs-deliverysource-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-deliverysource-return-values"></a>

### Ref
<a name="aws-resource-logs-deliverysource-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-logs-deliverysource-return-values-fn--getatt"></a>

####
<a name="aws-resource-logs-deliverysource-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) that uniquely identifies this delivery source.

`ResourceArns`  <a name="ResourceArns-fn::getatt"></a>
This array contains the ARN of the AWS resource that sends logs and is represented by this delivery source. Currently, only one ARN can be in the array.

`Service`  <a name="Service-fn::getatt"></a>
The AWS service that is sending logs.

`Status`  <a name="Status-fn::getatt"></a>
The status of the delivery source. A delivery source can have the status `ACTIVE` or `INACTIVE`. Note: This value is defined for selective log types.

`StatusReason`  <a name="StatusReason-fn::getatt"></a>
The reason for the status of the delivery source. A status reason of `RESOURCE_DELETED` indicates that the resource associated with the delivery source has been deleted. Note: This value is defined for selective log types.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
