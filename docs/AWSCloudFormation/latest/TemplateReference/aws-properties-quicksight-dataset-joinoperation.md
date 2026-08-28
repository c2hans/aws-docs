---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-joinoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet JoinOperation
<a name="aws-properties-quicksight-dataset-joinoperation"></a>

A transform operation that combines data from two sources based on specified join conditions.

## Syntax
<a name="aws-properties-quicksight-dataset-joinoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-joinoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-joinoperation-alias)" : {{String}},
  "[LeftOperand](#cfn-quicksight-dataset-joinoperation-leftoperand)" : {{TransformOperationSource}},
  "[LeftOperandProperties](#cfn-quicksight-dataset-joinoperation-leftoperandproperties)" : {{JoinOperandProperties}},
  "[OnClause](#cfn-quicksight-dataset-joinoperation-onclause)" : {{String}},
  "[RightOperand](#cfn-quicksight-dataset-joinoperation-rightoperand)" : {{TransformOperationSource}},
  "[RightOperandProperties](#cfn-quicksight-dataset-joinoperation-rightoperandproperties)" : {{JoinOperandProperties}},
  "[Type](#cfn-quicksight-dataset-joinoperation-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-joinoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-joinoperation-alias): {{String}}
  [LeftOperand](#cfn-quicksight-dataset-joinoperation-leftoperand): {{
    TransformOperationSource}}
  [LeftOperandProperties](#cfn-quicksight-dataset-joinoperation-leftoperandproperties): {{
    JoinOperandProperties}}
  [OnClause](#cfn-quicksight-dataset-joinoperation-onclause): {{String}}
  [RightOperand](#cfn-quicksight-dataset-joinoperation-rightoperand): {{
    TransformOperationSource}}
  [RightOperandProperties](#cfn-quicksight-dataset-joinoperation-rightoperandproperties): {{
    JoinOperandProperties}}
  [Type](#cfn-quicksight-dataset-joinoperation-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-joinoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-joinoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LeftOperand`  <a name="cfn-quicksight-dataset-joinoperation-leftoperand"></a>
The left operand for the join operation.
*Required*: Yes
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LeftOperandProperties`  <a name="cfn-quicksight-dataset-joinoperation-leftoperandproperties"></a>
Properties that control how the left operand's columns are handled in the join result.
*Required*: No
*Type*: [JoinOperandProperties](aws-properties-quicksight-dataset-joinoperandproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnClause`  <a name="cfn-quicksight-dataset-joinoperation-onclause"></a>
The join condition that specifies how to match rows between the left and right operands.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RightOperand`  <a name="cfn-quicksight-dataset-joinoperation-rightoperand"></a>
The right operand for the join operation.
*Required*: Yes
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RightOperandProperties`  <a name="cfn-quicksight-dataset-joinoperation-rightoperandproperties"></a>
Properties that control how the right operand's columns are handled in the join result.
*Required*: No
*Type*: [JoinOperandProperties](aws-properties-quicksight-dataset-joinoperandproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dataset-joinoperation-type"></a>
The type of join to perform, such as `INNER`, `LEFT`, `RIGHT`, or `OUTER`.
*Required*: Yes
*Type*: String
*Allowed values*: `INNER | OUTER | LEFT | RIGHT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
