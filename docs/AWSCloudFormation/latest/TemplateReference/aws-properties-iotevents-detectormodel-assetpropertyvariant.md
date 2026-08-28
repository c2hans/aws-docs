---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-assetpropertyvariant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel AssetPropertyVariant
<a name="aws-properties-iotevents-detectormodel-assetpropertyvariant"></a>

A structure that contains an asset property value. For more information, see [Variant](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Variant.html) in the *AWS IoT SiteWise API Reference*.

You must use expressions for all parameters in `AssetPropertyVariant`. The expressions accept literals, operators, functions, references, and substitution templates.

**Examples**
+ For literal values, the expressions must contain single quotes. For example, the value for the `integerValue` parameter can be `'100'`.
+ For references, you must specify either variables or parameters. For example, the value for the `booleanValue` parameter can be `$variable.offline`.
+ For a substitution template, you must use `${}`, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

  In the following example, the value for the `doubleValue` parameter uses a substitution template.

   `'${$input.TemperatureInput.sensorData.temperature * 6 / 5 + 32}'`

For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *AWS IoT Events Developer Guide*.

You must specify one of the following value types, depending on the `dataType` of the specified asset property. For more information, see [AssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetProperty.html) in the *AWS IoT SiteWise API Reference*.

## Syntax
<a name="aws-properties-iotevents-detectormodel-assetpropertyvariant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-assetpropertyvariant-syntax.json"></a>

```
{
  "[BooleanValue](#cfn-iotevents-detectormodel-assetpropertyvariant-booleanvalue)" : {{String}},
  "[DoubleValue](#cfn-iotevents-detectormodel-assetpropertyvariant-doublevalue)" : {{String}},
  "[IntegerValue](#cfn-iotevents-detectormodel-assetpropertyvariant-integervalue)" : {{String}},
  "[StringValue](#cfn-iotevents-detectormodel-assetpropertyvariant-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-assetpropertyvariant-syntax.yaml"></a>

```
  [BooleanValue](#cfn-iotevents-detectormodel-assetpropertyvariant-booleanvalue): {{String}}
  [DoubleValue](#cfn-iotevents-detectormodel-assetpropertyvariant-doublevalue): {{String}}
  [IntegerValue](#cfn-iotevents-detectormodel-assetpropertyvariant-integervalue): {{String}}
  [StringValue](#cfn-iotevents-detectormodel-assetpropertyvariant-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-assetpropertyvariant-properties"></a>

`BooleanValue`  <a name="cfn-iotevents-detectormodel-assetpropertyvariant-booleanvalue"></a>
The asset property value is a Boolean value that must be `'TRUE'` or `'FALSE'`. You must use an expression, and the evaluated result should be a Boolean value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DoubleValue`  <a name="cfn-iotevents-detectormodel-assetpropertyvariant-doublevalue"></a>
The asset property value is a double. You must use an expression, and the evaluated result should be a double.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerValue`  <a name="cfn-iotevents-detectormodel-assetpropertyvariant-integervalue"></a>
The asset property value is an integer. You must use an expression, and the evaluated result should be an integer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-iotevents-detectormodel-assetpropertyvariant-stringvalue"></a>
The asset property value is a string. You must use an expression, and the evaluated result should be a string.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
