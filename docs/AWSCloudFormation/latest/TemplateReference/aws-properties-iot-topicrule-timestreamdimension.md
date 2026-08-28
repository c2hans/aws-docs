---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-timestreamdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule TimestreamDimension
<a name="aws-properties-iot-topicrule-timestreamdimension"></a>

Metadata attributes of the time series that are written in each measure record.

## Syntax
<a name="aws-properties-iot-topicrule-timestreamdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-timestreamdimension-syntax.json"></a>

```
{
  "[Name](#cfn-iot-topicrule-timestreamdimension-name)" : {{String}},
  "[Value](#cfn-iot-topicrule-timestreamdimension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-timestreamdimension-syntax.yaml"></a>

```
  [Name](#cfn-iot-topicrule-timestreamdimension-name): {{String}}
  [Value](#cfn-iot-topicrule-timestreamdimension-value): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-timestreamdimension-properties"></a>

`Name`  <a name="cfn-iot-topicrule-timestreamdimension-name"></a>
The metadata dimension name. This is the name of the column in the Amazon Timestream database table record.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iot-topicrule-timestreamdimension-value"></a>
The value to write in this column of the database record.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
