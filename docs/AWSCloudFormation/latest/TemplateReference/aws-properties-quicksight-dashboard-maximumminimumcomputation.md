---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-maximumminimumcomputation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard MaximumMinimumComputation
<a name="aws-properties-quicksight-dashboard-maximumminimumcomputation"></a>

The maximum and minimum computation configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-maximumminimumcomputation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-maximumminimumcomputation-syntax.json"></a>

```
{
  "[ComputationId](#cfn-quicksight-dashboard-maximumminimumcomputation-computationid)" : {{String}},
  "[Name](#cfn-quicksight-dashboard-maximumminimumcomputation-name)" : {{String}},
  "[Time](#cfn-quicksight-dashboard-maximumminimumcomputation-time)" : {{DimensionField}},
  "[Type](#cfn-quicksight-dashboard-maximumminimumcomputation-type)" : {{String}},
  "[Value](#cfn-quicksight-dashboard-maximumminimumcomputation-value)" : {{MeasureField}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-maximumminimumcomputation-syntax.yaml"></a>

```
  [ComputationId](#cfn-quicksight-dashboard-maximumminimumcomputation-computationid): {{String}}
  [Name](#cfn-quicksight-dashboard-maximumminimumcomputation-name): {{String}}
  [Time](#cfn-quicksight-dashboard-maximumminimumcomputation-time): {{
    DimensionField}}
  [Type](#cfn-quicksight-dashboard-maximumminimumcomputation-type): {{String}}
  [Value](#cfn-quicksight-dashboard-maximumminimumcomputation-value): {{
    MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-maximumminimumcomputation-properties"></a>

`ComputationId`  <a name="cfn-quicksight-dashboard-maximumminimumcomputation-computationid"></a>
The ID for a computation.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dashboard-maximumminimumcomputation-name"></a>
The name of a computation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Time`  <a name="cfn-quicksight-dashboard-maximumminimumcomputation-time"></a>
The time field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dashboard-maximumminimumcomputation-type"></a>
The type of computation. Choose one of the following options:
+ MAXIMUM: A maximum computation.
+ MINIMUM: A minimum computation.
*Required*: Yes
*Type*: String
*Allowed values*: `MAXIMUM | MINIMUM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-dashboard-maximumminimumcomputation-value"></a>
The value field that is used in a computation.
*Required*: No
*Type*: [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
