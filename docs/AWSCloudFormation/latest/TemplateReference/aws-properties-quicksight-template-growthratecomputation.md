---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-growthratecomputation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GrowthRateComputation
<a name="aws-properties-quicksight-template-growthratecomputation"></a>

The growth rate computation configuration.

## Syntax
<a name="aws-properties-quicksight-template-growthratecomputation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-growthratecomputation-syntax.json"></a>

```
{
  "[ComputationId](#cfn-quicksight-template-growthratecomputation-computationid)" : {{String}},
  "[Name](#cfn-quicksight-template-growthratecomputation-name)" : {{String}},
  "[PeriodSize](#cfn-quicksight-template-growthratecomputation-periodsize)" : {{Number}},
  "[Time](#cfn-quicksight-template-growthratecomputation-time)" : {{DimensionField}},
  "[Value](#cfn-quicksight-template-growthratecomputation-value)" : {{MeasureField}}
}
```

### YAML
<a name="aws-properties-quicksight-template-growthratecomputation-syntax.yaml"></a>

```
  [ComputationId](#cfn-quicksight-template-growthratecomputation-computationid): {{String}}
  [Name](#cfn-quicksight-template-growthratecomputation-name): {{String}}
  [PeriodSize](#cfn-quicksight-template-growthratecomputation-periodsize): {{Number}}
  [Time](#cfn-quicksight-template-growthratecomputation-time): {{
    DimensionField}}
  [Value](#cfn-quicksight-template-growthratecomputation-value): {{
    MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-growthratecomputation-properties"></a>

`ComputationId`  <a name="cfn-quicksight-template-growthratecomputation-computationid"></a>
The ID for a computation.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-template-growthratecomputation-name"></a>
The name of a computation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeriodSize`  <a name="cfn-quicksight-template-growthratecomputation-periodsize"></a>
The period size setup of a growth rate computation.
*Required*: No
*Type*: Number
*Minimum*: `2`
*Maximum*: `52`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Time`  <a name="cfn-quicksight-template-growthratecomputation-time"></a>
The time field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-template-growthratecomputation-value"></a>
The value field that is used in a computation.
*Required*: No
*Type*: [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
