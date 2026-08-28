---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-timestamp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule Timestamp
<a name="aws-properties-iot-topicrule-timestamp"></a>

Describes how to interpret an application-defined timestamp value from an MQTT message payload and the precision of that value.

## Syntax
<a name="aws-properties-iot-topicrule-timestamp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-timestamp-syntax.json"></a>

```
{
  "[Unit](#cfn-iot-topicrule-timestamp-unit)" : {{String}},
  "[Value](#cfn-iot-topicrule-timestamp-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-timestamp-syntax.yaml"></a>

```
  [Unit](#cfn-iot-topicrule-timestamp-unit): {{String}}
  [Value](#cfn-iot-topicrule-timestamp-value): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-timestamp-properties"></a>

`Unit`  <a name="cfn-iot-topicrule-timestamp-unit"></a>
The precision of the timestamp value that results from the expression described in `value`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iot-topicrule-timestamp-value"></a>
An expression that returns a long epoch time value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
