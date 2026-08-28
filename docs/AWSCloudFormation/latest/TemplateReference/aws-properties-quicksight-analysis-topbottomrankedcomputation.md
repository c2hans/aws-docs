---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-topbottomrankedcomputation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TopBottomRankedComputation
<a name="aws-properties-quicksight-analysis-topbottomrankedcomputation"></a>

The top ranked and bottom ranked computation configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-topbottomrankedcomputation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-topbottomrankedcomputation-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-analysis-topbottomrankedcomputation-category)" : {{DimensionField}},
  "[ComputationId](#cfn-quicksight-analysis-topbottomrankedcomputation-computationid)" : {{String}},
  "[Name](#cfn-quicksight-analysis-topbottomrankedcomputation-name)" : {{String}},
  "[ResultSize](#cfn-quicksight-analysis-topbottomrankedcomputation-resultsize)" : {{Number}},
  "[Type](#cfn-quicksight-analysis-topbottomrankedcomputation-type)" : {{String}},
  "[Value](#cfn-quicksight-analysis-topbottomrankedcomputation-value)" : {{MeasureField}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-topbottomrankedcomputation-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-analysis-topbottomrankedcomputation-category): {{
    DimensionField}}
  [ComputationId](#cfn-quicksight-analysis-topbottomrankedcomputation-computationid): {{String}}
  [Name](#cfn-quicksight-analysis-topbottomrankedcomputation-name): {{String}}
  [ResultSize](#cfn-quicksight-analysis-topbottomrankedcomputation-resultsize): {{Number}}
  [Type](#cfn-quicksight-analysis-topbottomrankedcomputation-type): {{String}}
  [Value](#cfn-quicksight-analysis-topbottomrankedcomputation-value): {{
    MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-topbottomrankedcomputation-properties"></a>

`Category`  <a name="cfn-quicksight-analysis-topbottomrankedcomputation-category"></a>
The category field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputationId`  <a name="cfn-quicksight-analysis-topbottomrankedcomputation-computationid"></a>
The ID for a computation.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-analysis-topbottomrankedcomputation-name"></a>
The name of a computation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResultSize`  <a name="cfn-quicksight-analysis-topbottomrankedcomputation-resultsize"></a>
The result size of a top and bottom ranked computation.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-analysis-topbottomrankedcomputation-type"></a>
The computation type. Choose one of the following options:
+ TOP: A top ranked computation.
+ BOTTOM: A bottom ranked computation.
*Required*: Yes
*Type*: String
*Allowed values*: `TOP | BOTTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-analysis-topbottomrankedcomputation-value"></a>
The value field that is used in a computation.
*Required*: No
*Type*: [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
