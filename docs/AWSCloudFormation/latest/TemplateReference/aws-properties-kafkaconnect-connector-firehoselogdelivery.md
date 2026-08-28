---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-firehoselogdelivery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector FirehoseLogDelivery
<a name="aws-properties-kafkaconnect-connector-firehoselogdelivery"></a>

The settings for delivering logs to Amazon Kinesis Data Firehose.

## Syntax
<a name="aws-properties-kafkaconnect-connector-firehoselogdelivery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-firehoselogdelivery-syntax.json"></a>

```
{
  "[DeliveryStream](#cfn-kafkaconnect-connector-firehoselogdelivery-deliverystream)" : {{String}},
  "[Enabled](#cfn-kafkaconnect-connector-firehoselogdelivery-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-firehoselogdelivery-syntax.yaml"></a>

```
  [DeliveryStream](#cfn-kafkaconnect-connector-firehoselogdelivery-deliverystream): {{String}}
  [Enabled](#cfn-kafkaconnect-connector-firehoselogdelivery-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-firehoselogdelivery-properties"></a>

`DeliveryStream`  <a name="cfn-kafkaconnect-connector-firehoselogdelivery-deliverystream"></a>
The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Enabled`  <a name="cfn-kafkaconnect-connector-firehoselogdelivery-enabled"></a>
Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
