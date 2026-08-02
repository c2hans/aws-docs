---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-transform.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel Transform
<a name="aws-properties-iotsitewise-assetmodel-transform"></a>

Contains an asset transform property. A transform is a one-to-one mapping of a property's data points from one form to another. For example, you can use a transform to convert a Celsius data stream to Fahrenheit by applying the transformation expression to each data point of the Celsius stream. A transform can only have a data type of `DOUBLE` and consume properties with data types of `INTEGER` or `DOUBLE`.

For more information, see [Transforms](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html#transforms) in the *AWS IoT SiteWise User Guide*.

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-transform-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-transform-syntax.json"></a>

```
{
  "[Expression](#cfn-iotsitewise-assetmodel-transform-expression)" : {{String}},
  "[Variables](#cfn-iotsitewise-assetmodel-transform-variables)" : {{[ ExpressionVariable, ... ]}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-transform-syntax.yaml"></a>

```
  [Expression](#cfn-iotsitewise-assetmodel-transform-expression): {{String}}
  [Variables](#cfn-iotsitewise-assetmodel-transform-variables): {{
    - ExpressionVariable}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-transform-properties"></a>

`Expression`  <a name="cfn-iotsitewise-assetmodel-transform-expression"></a>
The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the *AWS IoT SiteWise User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Variables`  <a name="cfn-iotsitewise-assetmodel-transform-variables"></a>
The list of variables used in the expression.
*Required*: Yes
*Type*: Array of [ExpressionVariable](aws-properties-iotsitewise-assetmodel-expressionvariable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
