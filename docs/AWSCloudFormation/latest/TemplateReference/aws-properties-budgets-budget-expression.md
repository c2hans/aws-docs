---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-expression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget Expression
<a name="aws-properties-budgets-budget-expression"></a>

Use Expression to filter in various Budgets APIs.

## Syntax
<a name="aws-properties-budgets-budget-expression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-expression-syntax.json"></a>

```
{
  "[And](#cfn-budgets-budget-expression-and)" : {{[ Expression, ... ]}},
  "[CostCategories](#cfn-budgets-budget-expression-costcategories)" : {{CostCategoryValues}},
  "[Dimensions](#cfn-budgets-budget-expression-dimensions)" : {{ExpressionDimensionValues}},
  "[Not](#cfn-budgets-budget-expression-not)" : {{Expression}},
  "[Or](#cfn-budgets-budget-expression-or)" : {{[ Expression, ... ]}},
  "[Tags](#cfn-budgets-budget-expression-tags)" : {{TagValues}}
}
```

### YAML
<a name="aws-properties-budgets-budget-expression-syntax.yaml"></a>

```
  [And](#cfn-budgets-budget-expression-and): {{
    - Expression}}
  [CostCategories](#cfn-budgets-budget-expression-costcategories): {{
    CostCategoryValues}}
  [Dimensions](#cfn-budgets-budget-expression-dimensions): {{
    ExpressionDimensionValues}}
  [Not](#cfn-budgets-budget-expression-not): {{
    Expression}}
  [Or](#cfn-budgets-budget-expression-or): {{
    - Expression}}
  [Tags](#cfn-budgets-budget-expression-tags): {{
    TagValues}}
```

## Properties
<a name="aws-properties-budgets-budget-expression-properties"></a>

`And`  <a name="cfn-budgets-budget-expression-and"></a>
Return results that match both Dimension objects.
*Required*: No
*Type*: Array of [Expression](#aws-properties-budgets-budget-expression)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CostCategories`  <a name="cfn-budgets-budget-expression-costcategories"></a>
The filter that's based on CostCategoryValues.
*Required*: No
*Type*: [CostCategoryValues](aws-properties-budgets-budget-costcategoryvalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dimensions`  <a name="cfn-budgets-budget-expression-dimensions"></a>
The specific Dimension to use for Expression.
*Required*: No
*Type*: [ExpressionDimensionValues](aws-properties-budgets-budget-expressiondimensionvalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Not`  <a name="cfn-budgets-budget-expression-not"></a>
Return results that don't match a Dimension object.
*Required*: No
*Type*: [Expression](#aws-properties-budgets-budget-expression)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Or`  <a name="cfn-budgets-budget-expression-or"></a>
Return results that match either Dimension object.
*Required*: No
*Type*: Array of [Expression](#aws-properties-budgets-budget-expression)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-budgets-budget-expression-tags"></a>
The specific Tag to use for Expression.
*Required*: No
*Type*: [TagValues](aws-properties-budgets-budget-tagvalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
