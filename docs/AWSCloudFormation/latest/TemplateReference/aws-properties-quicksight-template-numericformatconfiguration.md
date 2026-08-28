---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-numericformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template NumericFormatConfiguration
<a name="aws-properties-quicksight-template-numericformatconfiguration"></a>

The options that determine the numeric format configuration.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-template-numericformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-numericformatconfiguration-syntax.json"></a>

```
{
  "[CurrencyDisplayFormatConfiguration](#cfn-quicksight-template-numericformatconfiguration-currencydisplayformatconfiguration)" : {{CurrencyDisplayFormatConfiguration}},
  "[NumberDisplayFormatConfiguration](#cfn-quicksight-template-numericformatconfiguration-numberdisplayformatconfiguration)" : {{NumberDisplayFormatConfiguration}},
  "[PercentageDisplayFormatConfiguration](#cfn-quicksight-template-numericformatconfiguration-percentagedisplayformatconfiguration)" : {{PercentageDisplayFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-numericformatconfiguration-syntax.yaml"></a>

```
  [CurrencyDisplayFormatConfiguration](#cfn-quicksight-template-numericformatconfiguration-currencydisplayformatconfiguration): {{
    CurrencyDisplayFormatConfiguration}}
  [NumberDisplayFormatConfiguration](#cfn-quicksight-template-numericformatconfiguration-numberdisplayformatconfiguration): {{
    NumberDisplayFormatConfiguration}}
  [PercentageDisplayFormatConfiguration](#cfn-quicksight-template-numericformatconfiguration-percentagedisplayformatconfiguration): {{
    PercentageDisplayFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-numericformatconfiguration-properties"></a>

`CurrencyDisplayFormatConfiguration`  <a name="cfn-quicksight-template-numericformatconfiguration-currencydisplayformatconfiguration"></a>
The options that determine the currency display format configuration.
*Required*: No
*Type*: [CurrencyDisplayFormatConfiguration](aws-properties-quicksight-template-currencydisplayformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberDisplayFormatConfiguration`  <a name="cfn-quicksight-template-numericformatconfiguration-numberdisplayformatconfiguration"></a>
The options that determine the number display format configuration.
*Required*: No
*Type*: [NumberDisplayFormatConfiguration](aws-properties-quicksight-template-numberdisplayformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PercentageDisplayFormatConfiguration`  <a name="cfn-quicksight-template-numericformatconfiguration-percentagedisplayformatconfiguration"></a>
The options that determine the percentage display format configuration.
*Required*: No
*Type*: [PercentageDisplayFormatConfiguration](aws-properties-quicksight-template-percentagedisplayformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
