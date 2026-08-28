---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-userproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule UserProperty
<a name="aws-properties-iot-topicrule-userproperty"></a>

A key-value pair that you define in the header.

## Syntax
<a name="aws-properties-iot-topicrule-userproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-userproperty-syntax.json"></a>

```
{
  "[Key](#cfn-iot-topicrule-userproperty-key)" : {{String}},
  "[Value](#cfn-iot-topicrule-userproperty-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-userproperty-syntax.yaml"></a>

```
  [Key](#cfn-iot-topicrule-userproperty-key): {{String}}
  [Value](#cfn-iot-topicrule-userproperty-value): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-userproperty-properties"></a>

`Key`  <a name="cfn-iot-topicrule-userproperty-key"></a>
A key to be specified in `UserProperty`.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iot-topicrule-userproperty-value"></a>
A value to be specified in `UserProperty`.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
