---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-costcategoryvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget CostCategoryValues
<a name="aws-properties-budgets-budget-costcategoryvalues"></a>

The cost category values used for filtering the costs.

## Syntax
<a name="aws-properties-budgets-budget-costcategoryvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-costcategoryvalues-syntax.json"></a>

```
{
  "[Key](#cfn-budgets-budget-costcategoryvalues-key)" : {{String}},
  "[MatchOptions](#cfn-budgets-budget-costcategoryvalues-matchoptions)" : {{[ String, ... ]}},
  "[Values](#cfn-budgets-budget-costcategoryvalues-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-budgets-budget-costcategoryvalues-syntax.yaml"></a>

```
  [Key](#cfn-budgets-budget-costcategoryvalues-key): {{String}}
  [MatchOptions](#cfn-budgets-budget-costcategoryvalues-matchoptions): {{
    - String}}
  [Values](#cfn-budgets-budget-costcategoryvalues-values): {{
    - String}}
```

## Properties
<a name="aws-properties-budgets-budget-costcategoryvalues-properties"></a>

`Key`  <a name="cfn-budgets-budget-costcategoryvalues-key"></a>
The unique name of the cost category.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchOptions`  <a name="cfn-budgets-budget-costcategoryvalues-matchoptions"></a>
The match options that you can use to filter your results.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-budgets-budget-costcategoryvalues-values"></a>
The specific value of the cost category.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
