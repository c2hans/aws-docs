---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-dimensionfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DimensionField
<a name="aws-properties-quicksight-template-dimensionfield"></a>

The dimension type field.

## Syntax
<a name="aws-properties-quicksight-template-dimensionfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-dimensionfield-syntax.json"></a>

```
{
  "[CategoricalDimensionField](#cfn-quicksight-template-dimensionfield-categoricaldimensionfield)" : {{CategoricalDimensionField}},
  "[DateDimensionField](#cfn-quicksight-template-dimensionfield-datedimensionfield)" : {{DateDimensionField}},
  "[NumericalDimensionField](#cfn-quicksight-template-dimensionfield-numericaldimensionfield)" : {{NumericalDimensionField}}
}
```

### YAML
<a name="aws-properties-quicksight-template-dimensionfield-syntax.yaml"></a>

```
  [CategoricalDimensionField](#cfn-quicksight-template-dimensionfield-categoricaldimensionfield): {{
    CategoricalDimensionField}}
  [DateDimensionField](#cfn-quicksight-template-dimensionfield-datedimensionfield): {{
    DateDimensionField}}
  [NumericalDimensionField](#cfn-quicksight-template-dimensionfield-numericaldimensionfield): {{
    NumericalDimensionField}}
```

## Properties
<a name="aws-properties-quicksight-template-dimensionfield-properties"></a>

`CategoricalDimensionField`  <a name="cfn-quicksight-template-dimensionfield-categoricaldimensionfield"></a>
The dimension type field with categorical type columns.
*Required*: No
*Type*: [CategoricalDimensionField](aws-properties-quicksight-template-categoricaldimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateDimensionField`  <a name="cfn-quicksight-template-dimensionfield-datedimensionfield"></a>
The dimension type field with date type columns.
*Required*: No
*Type*: [DateDimensionField](aws-properties-quicksight-template-datedimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumericalDimensionField`  <a name="cfn-quicksight-template-dimensionfield-numericaldimensionfield"></a>
The dimension type field with numerical type columns.
*Required*: No
*Type*: [NumericalDimensionField](aws-properties-quicksight-template-numericaldimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
