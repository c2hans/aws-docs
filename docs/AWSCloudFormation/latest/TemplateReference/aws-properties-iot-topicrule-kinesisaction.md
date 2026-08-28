---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-kinesisaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule KinesisAction
<a name="aws-properties-iot-topicrule-kinesisaction"></a>

Describes an action to write data to an Amazon Kinesis stream.

## Syntax
<a name="aws-properties-iot-topicrule-kinesisaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-kinesisaction-syntax.json"></a>

```
{
  "[PartitionKey](#cfn-iot-topicrule-kinesisaction-partitionkey)" : {{String}},
  "[RoleArn](#cfn-iot-topicrule-kinesisaction-rolearn)" : {{String}},
  "[StreamName](#cfn-iot-topicrule-kinesisaction-streamname)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-kinesisaction-syntax.yaml"></a>

```
  [PartitionKey](#cfn-iot-topicrule-kinesisaction-partitionkey): {{String}}
  [RoleArn](#cfn-iot-topicrule-kinesisaction-rolearn): {{String}}
  [StreamName](#cfn-iot-topicrule-kinesisaction-streamname): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-kinesisaction-properties"></a>

`PartitionKey`  <a name="cfn-iot-topicrule-kinesisaction-partitionkey"></a>
The partition key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-topicrule-kinesisaction-rolearn"></a>
The ARN of the IAM role that grants access to the Amazon Kinesis stream.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamName`  <a name="cfn-iot-topicrule-kinesisaction-streamname"></a>
The name of the Amazon Kinesis stream.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
