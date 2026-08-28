---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-topbottommoverscomputation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TopBottomMoversComputation
<a name="aws-properties-quicksight-analysis-topbottommoverscomputation"></a>

The top movers and bottom movers computation setup.

## Syntax
<a name="aws-properties-quicksight-analysis-topbottommoverscomputation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-topbottommoverscomputation-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-analysis-topbottommoverscomputation-category)" : {{DimensionField}},
  "[ComputationId](#cfn-quicksight-analysis-topbottommoverscomputation-computationid)" : {{String}},
  "[MoverSize](#cfn-quicksight-analysis-topbottommoverscomputation-moversize)" : {{Number}},
  "[Name](#cfn-quicksight-analysis-topbottommoverscomputation-name)" : {{String}},
  "[SortOrder](#cfn-quicksight-analysis-topbottommoverscomputation-sortorder)" : {{String}},
  "[Time](#cfn-quicksight-analysis-topbottommoverscomputation-time)" : {{DimensionField}},
  "[Type](#cfn-quicksight-analysis-topbottommoverscomputation-type)" : {{String}},
  "[Value](#cfn-quicksight-analysis-topbottommoverscomputation-value)" : {{MeasureField}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-topbottommoverscomputation-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-analysis-topbottommoverscomputation-category): {{
    DimensionField}}
  [ComputationId](#cfn-quicksight-analysis-topbottommoverscomputation-computationid): {{String}}
  [MoverSize](#cfn-quicksight-analysis-topbottommoverscomputation-moversize): {{Number}}
  [Name](#cfn-quicksight-analysis-topbottommoverscomputation-name): {{String}}
  [SortOrder](#cfn-quicksight-analysis-topbottommoverscomputation-sortorder): {{String}}
  [Time](#cfn-quicksight-analysis-topbottommoverscomputation-time): {{
    DimensionField}}
  [Type](#cfn-quicksight-analysis-topbottommoverscomputation-type): {{String}}
  [Value](#cfn-quicksight-analysis-topbottommoverscomputation-value): {{
    MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-topbottommoverscomputation-properties"></a>

`Category`  <a name="cfn-quicksight-analysis-topbottommoverscomputation-category"></a>
The category field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputationId`  <a name="cfn-quicksight-analysis-topbottommoverscomputation-computationid"></a>
The ID for a computation.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MoverSize`  <a name="cfn-quicksight-analysis-topbottommoverscomputation-moversize"></a>
The mover size setup of the top and bottom movers computation.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-analysis-topbottommoverscomputation-name"></a>
The name of a computation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortOrder`  <a name="cfn-quicksight-analysis-topbottommoverscomputation-sortorder"></a>
The sort order setup of the top and bottom movers computation.
*Required*: No
*Type*: String
*Allowed values*: `PERCENT_DIFFERENCE | ABSOLUTE_DIFFERENCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Time`  <a name="cfn-quicksight-analysis-topbottommoverscomputation-time"></a>
The time field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-analysis-topbottommoverscomputation-type"></a>
The computation type. Choose from the following options:
+ TOP: Top movers computation.
+ BOTTOM: Bottom movers computation.
*Required*: Yes
*Type*: String
*Allowed values*: `TOP | BOTTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-analysis-topbottommoverscomputation-value"></a>
The value field that is used in a computation.
*Required*: No
*Type*: [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
