---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-numericseparatorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template NumericSeparatorConfiguration
<a name="aws-properties-quicksight-template-numericseparatorconfiguration"></a>

The options that determine the numeric separator configuration.

## Syntax
<a name="aws-properties-quicksight-template-numericseparatorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-numericseparatorconfiguration-syntax.json"></a>

```
{
  "[DecimalSeparator](#cfn-quicksight-template-numericseparatorconfiguration-decimalseparator)" : {{String}},
  "[ThousandsSeparator](#cfn-quicksight-template-numericseparatorconfiguration-thousandsseparator)" : {{ThousandSeparatorOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-numericseparatorconfiguration-syntax.yaml"></a>

```
  [DecimalSeparator](#cfn-quicksight-template-numericseparatorconfiguration-decimalseparator): {{String}}
  [ThousandsSeparator](#cfn-quicksight-template-numericseparatorconfiguration-thousandsseparator): {{
    ThousandSeparatorOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-numericseparatorconfiguration-properties"></a>

`DecimalSeparator`  <a name="cfn-quicksight-template-numericseparatorconfiguration-decimalseparator"></a>
Determines the decimal separator.
*Required*: No
*Type*: String
*Allowed values*: `COMMA | DOT | SPACE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThousandsSeparator`  <a name="cfn-quicksight-template-numericseparatorconfiguration-thousandsseparator"></a>
The options that determine the thousands separator configuration.
*Required*: No
*Type*: [ThousandSeparatorOptions](aws-properties-quicksight-template-thousandseparatoroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
