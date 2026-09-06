---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-totalaggregationcomputation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TotalAggregationComputation
<a name="aws-properties-quicksight-analysis-totalaggregationcomputation"></a>

The total aggregation computation configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-totalaggregationcomputation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-totalaggregationcomputation-syntax.json"></a>

```
{
  "[ComputationId](#cfn-quicksight-analysis-totalaggregationcomputation-computationid)" : {{String}},
  "[Name](#cfn-quicksight-analysis-totalaggregationcomputation-name)" : {{String}},
  "[Value](#cfn-quicksight-analysis-totalaggregationcomputation-value)" : {{MeasureField}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-totalaggregationcomputation-syntax.yaml"></a>

```
  [ComputationId](#cfn-quicksight-analysis-totalaggregationcomputation-computationid): {{String}}
  [Name](#cfn-quicksight-analysis-totalaggregationcomputation-name): {{String}}
  [Value](#cfn-quicksight-analysis-totalaggregationcomputation-value): {{
    MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-totalaggregationcomputation-properties"></a>

`ComputationId`  <a name="cfn-quicksight-analysis-totalaggregationcomputation-computationid"></a>
The ID for a computation.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-analysis-totalaggregationcomputation-name"></a>
The name of a computation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-analysis-totalaggregationcomputation-value"></a>
The value field that is used in a computation.
*Required*: No
*Type*: [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
