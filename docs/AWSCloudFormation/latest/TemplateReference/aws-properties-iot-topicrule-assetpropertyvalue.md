---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-assetpropertyvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule AssetPropertyValue
<a name="aws-properties-iot-topicrule-assetpropertyvalue"></a>

An asset property value entry containing the following information.

## Syntax
<a name="aws-properties-iot-topicrule-assetpropertyvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-assetpropertyvalue-syntax.json"></a>

```
{
  "[Quality](#cfn-iot-topicrule-assetpropertyvalue-quality)" : {{String}},
  "[Timestamp](#cfn-iot-topicrule-assetpropertyvalue-timestamp)" : {{AssetPropertyTimestamp}},
  "[Value](#cfn-iot-topicrule-assetpropertyvalue-value)" : {{AssetPropertyVariant}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-assetpropertyvalue-syntax.yaml"></a>

```
  [Quality](#cfn-iot-topicrule-assetpropertyvalue-quality): {{String}}
  [Timestamp](#cfn-iot-topicrule-assetpropertyvalue-timestamp): {{
    AssetPropertyTimestamp}}
  [Value](#cfn-iot-topicrule-assetpropertyvalue-value): {{
    AssetPropertyVariant}}
```

## Properties
<a name="aws-properties-iot-topicrule-assetpropertyvalue-properties"></a>

`Quality`  <a name="cfn-iot-topicrule-assetpropertyvalue-quality"></a>
Optional. A string that describes the quality of the value. Accepts substitution templates. Must be `GOOD`, `BAD`, or `UNCERTAIN`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timestamp`  <a name="cfn-iot-topicrule-assetpropertyvalue-timestamp"></a>
The asset property value timestamp.
*Required*: Yes
*Type*: [AssetPropertyTimestamp](aws-properties-iot-topicrule-assetpropertytimestamp.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iot-topicrule-assetpropertyvalue-value"></a>
The value of the asset property.
*Required*: Yes
*Type*: [AssetPropertyVariant](aws-properties-iot-topicrule-assetpropertyvariant.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
