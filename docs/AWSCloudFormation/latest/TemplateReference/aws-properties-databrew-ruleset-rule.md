---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-ruleset-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Ruleset Rule
<a name="aws-properties-databrew-ruleset-rule"></a>

Represents a single data quality requirement that should be validated in the scope of this dataset.

## Syntax
<a name="aws-properties-databrew-ruleset-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-ruleset-rule-syntax.json"></a>

```
{
  "[CheckExpression](#cfn-databrew-ruleset-rule-checkexpression)" : {{String}},
  "[ColumnSelectors](#cfn-databrew-ruleset-rule-columnselectors)" : {{[ ColumnSelector, ... ]}},
  "[Disabled](#cfn-databrew-ruleset-rule-disabled)" : {{Boolean}},
  "[Name](#cfn-databrew-ruleset-rule-name)" : {{String}},
  "[SubstitutionMap](#cfn-databrew-ruleset-rule-substitutionmap)" : {{[ SubstitutionValue, ... ]}},
  "[Threshold](#cfn-databrew-ruleset-rule-threshold)" : {{Threshold}}
}
```

### YAML
<a name="aws-properties-databrew-ruleset-rule-syntax.yaml"></a>

```
  [CheckExpression](#cfn-databrew-ruleset-rule-checkexpression): {{String}}
  [ColumnSelectors](#cfn-databrew-ruleset-rule-columnselectors): {{
    - ColumnSelector}}
  [Disabled](#cfn-databrew-ruleset-rule-disabled): {{Boolean}}
  [Name](#cfn-databrew-ruleset-rule-name): {{String}}
  [SubstitutionMap](#cfn-databrew-ruleset-rule-substitutionmap): {{
    - SubstitutionValue}}
  [Threshold](#cfn-databrew-ruleset-rule-threshold): {{
    Threshold}}
```

## Properties
<a name="aws-properties-databrew-ruleset-rule-properties"></a>

`CheckExpression`  <a name="cfn-databrew-ruleset-rule-checkexpression"></a>
The expression which includes column references, condition names followed by variable references, possibly grouped and combined with other conditions. For example, `(:col1 starts_with :prefix1 or :col1 starts_with :prefix2) and (:col1 ends_with :suffix1 or :col1 ends_with :suffix2)`. Column and value references are substitution variables that should start with the ':' symbol. Depending on the context, substitution variables' values can be either an actual value or a column name. These values are defined in the SubstitutionMap. If a CheckExpression starts with a column reference, then ColumnSelectors in the rule should be null. If ColumnSelectors has been defined, then there should be no columnn reference in the left side of a condition, for example, `is_between :val1 and :val2`.
*Required*: Yes
*Type*: String
*Pattern*: `^[><0-9A-Za-z_.,:)(!= ]+$`
*Minimum*: `4`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnSelectors`  <a name="cfn-databrew-ruleset-rule-columnselectors"></a>
List of column selectors. Selectors can be used to select columns using a name or regular expression from the dataset. Rule will be applied to selected columns.
*Required*: No
*Type*: Array of [ColumnSelector](aws-properties-databrew-ruleset-columnselector.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Disabled`  <a name="cfn-databrew-ruleset-rule-disabled"></a>
A value that specifies whether the rule is disabled. Once a rule is disabled, a profile job will not validate it during a job run. Default value is false.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-databrew-ruleset-rule-name"></a>
The name of the rule.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubstitutionMap`  <a name="cfn-databrew-ruleset-rule-substitutionmap"></a>
The map of substitution variable names to their values used in a check expression. Variable names should start with a ':' (colon). Variable values can either be actual values or column names. To differentiate between the two, column names should be enclosed in backticks, for example, `":col1": "`Column A`".`
*Required*: No
*Type*: Array of [SubstitutionValue](aws-properties-databrew-ruleset-substitutionvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-databrew-ruleset-rule-threshold"></a>
The threshold used with a non-aggregate check expression. Non-aggregate check expressions will be applied to each row in a specific column, and the threshold will be used to determine whether the validation succeeds.
*Required*: No
*Type*: [Threshold](aws-properties-databrew-ruleset-threshold.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
