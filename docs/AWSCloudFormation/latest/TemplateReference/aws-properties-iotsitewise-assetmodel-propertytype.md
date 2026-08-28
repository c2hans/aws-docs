---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-propertytype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel PropertyType
<a name="aws-properties-iotsitewise-assetmodel-propertytype"></a>

Contains a property type, which can be one of `attribute`, `measurement`, `metric`, or `transform`.

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-propertytype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-propertytype-syntax.json"></a>

```
{
  "[Attribute](#cfn-iotsitewise-assetmodel-propertytype-attribute)" : {{Attribute}},
  "[Metric](#cfn-iotsitewise-assetmodel-propertytype-metric)" : {{Metric}},
  "[Transform](#cfn-iotsitewise-assetmodel-propertytype-transform)" : {{Transform}},
  "[TypeName](#cfn-iotsitewise-assetmodel-propertytype-typename)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-propertytype-syntax.yaml"></a>

```
  [Attribute](#cfn-iotsitewise-assetmodel-propertytype-attribute): {{
    Attribute}}
  [Metric](#cfn-iotsitewise-assetmodel-propertytype-metric): {{
    Metric}}
  [Transform](#cfn-iotsitewise-assetmodel-propertytype-transform): {{
    Transform}}
  [TypeName](#cfn-iotsitewise-assetmodel-propertytype-typename): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-propertytype-properties"></a>

`Attribute`  <a name="cfn-iotsitewise-assetmodel-propertytype-attribute"></a>
Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an [IIoT](https://en.wikipedia.org/wiki/Internet_of_things#Industrial_applications) wind turbine.
*Required*: No
*Type*: [Attribute](aws-properties-iotsitewise-assetmodel-attribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metric`  <a name="cfn-iotsitewise-assetmodel-propertytype-metric"></a>
Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.
*Required*: No
*Type*: [Metric](aws-properties-iotsitewise-assetmodel-metric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Transform`  <a name="cfn-iotsitewise-assetmodel-propertytype-transform"></a>
Specifies an asset transform property. A transform contains a mathematical expression that maps a property's data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.
*Required*: No
*Type*: [Transform](aws-properties-iotsitewise-assetmodel-transform.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeName`  <a name="cfn-iotsitewise-assetmodel-propertytype-typename"></a>
The type of property type, which can be one of `Attribute`, `Measurement`, `Metric`, or `Transform`.
*Required*: Yes
*Type*: String
*Allowed values*: `Measurement | Attribute | Transform | Metric`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
