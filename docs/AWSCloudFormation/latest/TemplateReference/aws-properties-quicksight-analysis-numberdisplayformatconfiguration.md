---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-numberdisplayformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis NumberDisplayFormatConfiguration
<a name="aws-properties-quicksight-analysis-numberdisplayformatconfiguration"></a>

The options that determine the number display format configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-numberdisplayformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-numberdisplayformatconfiguration-syntax.json"></a>

```
{
  "[DecimalPlacesConfiguration](#cfn-quicksight-analysis-numberdisplayformatconfiguration-decimalplacesconfiguration)" : {{DecimalPlacesConfiguration}},
  "[NegativeValueConfiguration](#cfn-quicksight-analysis-numberdisplayformatconfiguration-negativevalueconfiguration)" : {{NegativeValueConfiguration}},
  "[NullValueFormatConfiguration](#cfn-quicksight-analysis-numberdisplayformatconfiguration-nullvalueformatconfiguration)" : {{NullValueFormatConfiguration}},
  "[NumberScale](#cfn-quicksight-analysis-numberdisplayformatconfiguration-numberscale)" : {{String}},
  "[Prefix](#cfn-quicksight-analysis-numberdisplayformatconfiguration-prefix)" : {{String}},
  "[SeparatorConfiguration](#cfn-quicksight-analysis-numberdisplayformatconfiguration-separatorconfiguration)" : {{NumericSeparatorConfiguration}},
  "[Suffix](#cfn-quicksight-analysis-numberdisplayformatconfiguration-suffix)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-numberdisplayformatconfiguration-syntax.yaml"></a>

```
  [DecimalPlacesConfiguration](#cfn-quicksight-analysis-numberdisplayformatconfiguration-decimalplacesconfiguration): {{
    DecimalPlacesConfiguration}}
  [NegativeValueConfiguration](#cfn-quicksight-analysis-numberdisplayformatconfiguration-negativevalueconfiguration): {{
    NegativeValueConfiguration}}
  [NullValueFormatConfiguration](#cfn-quicksight-analysis-numberdisplayformatconfiguration-nullvalueformatconfiguration): {{
    NullValueFormatConfiguration}}
  [NumberScale](#cfn-quicksight-analysis-numberdisplayformatconfiguration-numberscale): {{String}}
  [Prefix](#cfn-quicksight-analysis-numberdisplayformatconfiguration-prefix): {{String}}
  [SeparatorConfiguration](#cfn-quicksight-analysis-numberdisplayformatconfiguration-separatorconfiguration): {{
    NumericSeparatorConfiguration}}
  [Suffix](#cfn-quicksight-analysis-numberdisplayformatconfiguration-suffix): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-numberdisplayformatconfiguration-properties"></a>

`DecimalPlacesConfiguration`  <a name="cfn-quicksight-analysis-numberdisplayformatconfiguration-decimalplacesconfiguration"></a>
The option that determines the decimal places configuration.
*Required*: No
*Type*: [DecimalPlacesConfiguration](aws-properties-quicksight-analysis-decimalplacesconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NegativeValueConfiguration`  <a name="cfn-quicksight-analysis-numberdisplayformatconfiguration-negativevalueconfiguration"></a>
The options that determine the negative value configuration.
*Required*: No
*Type*: [NegativeValueConfiguration](aws-properties-quicksight-analysis-negativevalueconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullValueFormatConfiguration`  <a name="cfn-quicksight-analysis-numberdisplayformatconfiguration-nullvalueformatconfiguration"></a>
The options that determine the null value format configuration.
*Required*: No
*Type*: [NullValueFormatConfiguration](aws-properties-quicksight-analysis-nullvalueformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberScale`  <a name="cfn-quicksight-analysis-numberdisplayformatconfiguration-numberscale"></a>
Determines the number scale value of the number format.
*Required*: No
*Type*: String
*Allowed values*: `NONE | AUTO | THOUSANDS | MILLIONS | BILLIONS | TRILLIONS | LAKHS | CRORES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-quicksight-analysis-numberdisplayformatconfiguration-prefix"></a>
Determines the prefix value of the number format.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SeparatorConfiguration`  <a name="cfn-quicksight-analysis-numberdisplayformatconfiguration-separatorconfiguration"></a>
The options that determine the numeric separator configuration.
*Required*: No
*Type*: [NumericSeparatorConfiguration](aws-properties-quicksight-analysis-numericseparatorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Suffix`  <a name="cfn-quicksight-analysis-numberdisplayformatconfiguration-suffix"></a>
Determines the suffix value of the number format.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
