---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-tagvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget TagValues
<a name="aws-properties-budgets-budget-tagvalues"></a>

The values that are available for a tag.

## Syntax
<a name="aws-properties-budgets-budget-tagvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-tagvalues-syntax.json"></a>

```
{
  "[Key](#cfn-budgets-budget-tagvalues-key)" : {{String}},
  "[MatchOptions](#cfn-budgets-budget-tagvalues-matchoptions)" : {{[ String, ... ]}},
  "[Values](#cfn-budgets-budget-tagvalues-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-budgets-budget-tagvalues-syntax.yaml"></a>

```
  [Key](#cfn-budgets-budget-tagvalues-key): {{String}}
  [MatchOptions](#cfn-budgets-budget-tagvalues-matchoptions): {{
    - String}}
  [Values](#cfn-budgets-budget-tagvalues-values): {{
    - String}}
```

## Properties
<a name="aws-properties-budgets-budget-tagvalues-properties"></a>

`Key`  <a name="cfn-budgets-budget-tagvalues-key"></a>
The key for the tag.
*Required*: No
*Type*: String
*Pattern*: `[\S\s]*`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchOptions`  <a name="cfn-budgets-budget-tagvalues-matchoptions"></a>
The match options that you can use to filter your results.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-budgets-budget-tagvalues-values"></a>
The specific value of the tag.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
