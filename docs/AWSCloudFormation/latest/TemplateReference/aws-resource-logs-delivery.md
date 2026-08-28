---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-delivery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Delivery
<a name="aws-resource-logs-delivery"></a>

This structure contains information about one *delivery* in your account.

A delivery is a connection between a logical *delivery source* and a logical *delivery destination*.

For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

To update an existing delivery configuration, use [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html).

## Syntax
<a name="aws-resource-logs-delivery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-delivery-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::Delivery",
  "Properties" : {
      "[DeliveryDestinationArn](#cfn-logs-delivery-deliverydestinationarn)" : {{String}},
      "[DeliverySourceName](#cfn-logs-delivery-deliverysourcename)" : {{String}},
      "[FieldDelimiter](#cfn-logs-delivery-fielddelimiter)" : {{String}},
      "[RecordFields](#cfn-logs-delivery-recordfields)" : {{[ String, ... ]}},
      "[S3EnableHiveCompatiblePath](#cfn-logs-delivery-s3enablehivecompatiblepath)" : {{Boolean}},
      "[S3SuffixPath](#cfn-logs-delivery-s3suffixpath)" : {{String}},
      "[Tags](#cfn-logs-delivery-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-logs-delivery-syntax.yaml"></a>

```
Type: AWS::Logs::Delivery
Properties:
  [DeliveryDestinationArn](#cfn-logs-delivery-deliverydestinationarn): {{String}}
  [DeliverySourceName](#cfn-logs-delivery-deliverysourcename): {{String}}
  [FieldDelimiter](#cfn-logs-delivery-fielddelimiter): {{String}}
  [RecordFields](#cfn-logs-delivery-recordfields): {{
    - String}}
  [S3EnableHiveCompatiblePath](#cfn-logs-delivery-s3enablehivecompatiblepath): {{Boolean}}
  [S3SuffixPath](#cfn-logs-delivery-s3suffixpath): {{String}}
  [Tags](#cfn-logs-delivery-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-logs-delivery-properties"></a>

`DeliveryDestinationArn`  <a name="cfn-logs-delivery-deliverydestinationarn"></a>
The ARN of the delivery destination that is associated with this delivery.
*Required*: Yes
*Type*: String
*Pattern*: `[\w#+=/:,.@-]*\*?`
*Minimum*: `16`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeliverySourceName`  <a name="cfn-logs-delivery-deliverysourcename"></a>
The name of the delivery source that is associated with this delivery.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]*$`
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FieldDelimiter`  <a name="cfn-logs-delivery-fielddelimiter"></a>
The field delimiter that is used between record fields when the final output format of a delivery is in `Plain`, `W3C`, or `Raw` format.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordFields`  <a name="cfn-logs-delivery-recordfields"></a>
The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3EnableHiveCompatiblePath`  <a name="cfn-logs-delivery-s3enablehivecompatiblepath"></a>
Use this parameter to cause the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3SuffixPath`  <a name="cfn-logs-delivery-s3suffixpath"></a>
Use this to reconfigure the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path will vary by each log source. To find the values supported for the suffix path for each log source, use the [DescribeConfigurationTemplates](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html) operation and check the `allowedSuffixPathFields` field in the response.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-logs-delivery-tags"></a>
An array of key-value pairs to apply to the delivery.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-logs-delivery-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-delivery-return-values"></a>

### Ref
<a name="aws-resource-logs-delivery-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-logs-delivery-return-values-fn--getatt"></a>

####
<a name="aws-resource-logs-delivery-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) that uniquely identifies this delivery.

`DeliveryDestinationType`  <a name="DeliveryDestinationType-fn::getatt"></a>
Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, or Firehose.

`DeliveryId`  <a name="DeliveryId-fn::getatt"></a>
The unique ID that identifies this delivery in your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
