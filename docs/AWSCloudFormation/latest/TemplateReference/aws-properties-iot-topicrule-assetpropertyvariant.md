---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-assetpropertyvariant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule AssetPropertyVariant
<a name="aws-properties-iot-topicrule-assetpropertyvariant"></a>

Contains an asset property value (of a single type).

## Syntax
<a name="aws-properties-iot-topicrule-assetpropertyvariant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-assetpropertyvariant-syntax.json"></a>

```
{
  "[BooleanValue](#cfn-iot-topicrule-assetpropertyvariant-booleanvalue)" : {{String}},
  "[DoubleValue](#cfn-iot-topicrule-assetpropertyvariant-doublevalue)" : {{String}},
  "[IntegerValue](#cfn-iot-topicrule-assetpropertyvariant-integervalue)" : {{String}},
  "[StringValue](#cfn-iot-topicrule-assetpropertyvariant-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-assetpropertyvariant-syntax.yaml"></a>

```
  [BooleanValue](#cfn-iot-topicrule-assetpropertyvariant-booleanvalue): {{String}}
  [DoubleValue](#cfn-iot-topicrule-assetpropertyvariant-doublevalue): {{String}}
  [IntegerValue](#cfn-iot-topicrule-assetpropertyvariant-integervalue): {{String}}
  [StringValue](#cfn-iot-topicrule-assetpropertyvariant-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-iot-topicrule-assetpropertyvariant-properties"></a>

`BooleanValue`  <a name="cfn-iot-topicrule-assetpropertyvariant-booleanvalue"></a>
Optional. A string that contains the boolean value (`true` or `false`) of the value entry. Accepts substitution templates.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DoubleValue`  <a name="cfn-iot-topicrule-assetpropertyvariant-doublevalue"></a>
Optional. A string that contains the double value of the value entry. Accepts substitution templates.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerValue`  <a name="cfn-iot-topicrule-assetpropertyvariant-integervalue"></a>
Optional. A string that contains the integer value of the value entry. Accepts substitution templates.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-iot-topicrule-assetpropertyvariant-stringvalue"></a>
Optional. The string value of the value entry. Accepts substitution templates.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
