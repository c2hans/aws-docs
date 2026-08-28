---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-httpactionheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule HttpActionHeader
<a name="aws-properties-iot-topicrule-httpactionheader"></a>

The HTTP action header.

## Syntax
<a name="aws-properties-iot-topicrule-httpactionheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-httpactionheader-syntax.json"></a>

```
{
  "[Key](#cfn-iot-topicrule-httpactionheader-key)" : {{String}},
  "[Value](#cfn-iot-topicrule-httpactionheader-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-httpactionheader-syntax.yaml"></a>

```
  [Key](#cfn-iot-topicrule-httpactionheader-key): {{String}}
  [Value](#cfn-iot-topicrule-httpactionheader-value): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-httpactionheader-properties"></a>

`Key`  <a name="cfn-iot-topicrule-httpactionheader-key"></a>
The HTTP header key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iot-topicrule-httpactionheader-value"></a>
The HTTP header value. Substitution templates are supported.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
