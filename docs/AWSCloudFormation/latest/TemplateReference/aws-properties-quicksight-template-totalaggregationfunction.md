---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-totalaggregationfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TotalAggregationFunction
<a name="aws-properties-quicksight-template-totalaggregationfunction"></a>

An aggregation function that aggregates the total values of a measure.

## Syntax
<a name="aws-properties-quicksight-template-totalaggregationfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-totalaggregationfunction-syntax.json"></a>

```
{
  "[SimpleTotalAggregationFunction](#cfn-quicksight-template-totalaggregationfunction-simpletotalaggregationfunction)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-totalaggregationfunction-syntax.yaml"></a>

```
  [SimpleTotalAggregationFunction](#cfn-quicksight-template-totalaggregationfunction-simpletotalaggregationfunction): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-totalaggregationfunction-properties"></a>

`SimpleTotalAggregationFunction`  <a name="cfn-quicksight-template-totalaggregationfunction-simpletotalaggregationfunction"></a>
A built in aggregation function for total values.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | SUM | AVERAGE | MIN | MAX | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
