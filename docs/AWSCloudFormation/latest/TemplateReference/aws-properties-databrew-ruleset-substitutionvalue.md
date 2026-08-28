---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-ruleset-substitutionvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Ruleset SubstitutionValue
<a name="aws-properties-databrew-ruleset-substitutionvalue"></a>

A key-value pair to associate an expression's substitution variable names with their values.

## Syntax
<a name="aws-properties-databrew-ruleset-substitutionvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-ruleset-substitutionvalue-syntax.json"></a>

```
{
  "[Value](#cfn-databrew-ruleset-substitutionvalue-value)" : {{String}},
  "[ValueReference](#cfn-databrew-ruleset-substitutionvalue-valuereference)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-ruleset-substitutionvalue-syntax.yaml"></a>

```
  [Value](#cfn-databrew-ruleset-substitutionvalue-value): {{String}}
  [ValueReference](#cfn-databrew-ruleset-substitutionvalue-valuereference): {{String}}
```

## Properties
<a name="aws-properties-databrew-ruleset-substitutionvalue-properties"></a>

`Value`  <a name="cfn-databrew-ruleset-substitutionvalue-value"></a>
Value or column name.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueReference`  <a name="cfn-databrew-ruleset-substitutionvalue-valuereference"></a>
Variable name.
*Required*: Yes
*Type*: String
*Pattern*: `^:[A-Za-z0-9_]+$`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
