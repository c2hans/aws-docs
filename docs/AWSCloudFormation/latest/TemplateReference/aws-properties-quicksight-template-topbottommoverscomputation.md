---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-topbottommoverscomputation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TopBottomMoversComputation
<a name="aws-properties-quicksight-template-topbottommoverscomputation"></a>

The top movers and bottom movers computation setup.

## Syntax
<a name="aws-properties-quicksight-template-topbottommoverscomputation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-topbottommoverscomputation-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-template-topbottommoverscomputation-category)" : {{DimensionField}},
  "[ComputationId](#cfn-quicksight-template-topbottommoverscomputation-computationid)" : {{String}},
  "[MoverSize](#cfn-quicksight-template-topbottommoverscomputation-moversize)" : {{Number}},
  "[Name](#cfn-quicksight-template-topbottommoverscomputation-name)" : {{String}},
  "[SortOrder](#cfn-quicksight-template-topbottommoverscomputation-sortorder)" : {{String}},
  "[Time](#cfn-quicksight-template-topbottommoverscomputation-time)" : {{DimensionField}},
  "[Type](#cfn-quicksight-template-topbottommoverscomputation-type)" : {{String}},
  "[Value](#cfn-quicksight-template-topbottommoverscomputation-value)" : {{MeasureField}}
}
```

### YAML
<a name="aws-properties-quicksight-template-topbottommoverscomputation-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-template-topbottommoverscomputation-category): {{
    DimensionField}}
  [ComputationId](#cfn-quicksight-template-topbottommoverscomputation-computationid): {{String}}
  [MoverSize](#cfn-quicksight-template-topbottommoverscomputation-moversize): {{Number}}
  [Name](#cfn-quicksight-template-topbottommoverscomputation-name): {{String}}
  [SortOrder](#cfn-quicksight-template-topbottommoverscomputation-sortorder): {{String}}
  [Time](#cfn-quicksight-template-topbottommoverscomputation-time): {{
    DimensionField}}
  [Type](#cfn-quicksight-template-topbottommoverscomputation-type): {{String}}
  [Value](#cfn-quicksight-template-topbottommoverscomputation-value): {{
    MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-topbottommoverscomputation-properties"></a>

`Category`  <a name="cfn-quicksight-template-topbottommoverscomputation-category"></a>
The category field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputationId`  <a name="cfn-quicksight-template-topbottommoverscomputation-computationid"></a>
The ID for a computation.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MoverSize`  <a name="cfn-quicksight-template-topbottommoverscomputation-moversize"></a>
The mover size setup of the top and bottom movers computation.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-template-topbottommoverscomputation-name"></a>
The name of a computation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortOrder`  <a name="cfn-quicksight-template-topbottommoverscomputation-sortorder"></a>
The sort order setup of the top and bottom movers computation.
*Required*: No
*Type*: String
*Allowed values*: `PERCENT_DIFFERENCE | ABSOLUTE_DIFFERENCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Time`  <a name="cfn-quicksight-template-topbottommoverscomputation-time"></a>
The time field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-template-topbottommoverscomputation-type"></a>
The computation type. Choose from the following options:
+ TOP: Top movers computation.
+ BOTTOM: Bottom movers computation.
*Required*: Yes
*Type*: String
*Allowed values*: `TOP | BOTTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-template-topbottommoverscomputation-value"></a>
The value field that is used in a computation.
*Required*: No
*Type*: [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
