---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-labeloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis LabelOptions
<a name="aws-properties-quicksight-analysis-labeloptions"></a>

The share label options for the labels.

## Syntax
<a name="aws-properties-quicksight-analysis-labeloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-labeloptions-syntax.json"></a>

```
{
  "[CustomLabel](#cfn-quicksight-analysis-labeloptions-customlabel)" : {{String}},
  "[FontConfiguration](#cfn-quicksight-analysis-labeloptions-fontconfiguration)" : {{FontConfiguration}},
  "[Visibility](#cfn-quicksight-analysis-labeloptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-labeloptions-syntax.yaml"></a>

```
  [CustomLabel](#cfn-quicksight-analysis-labeloptions-customlabel): {{String}}
  [FontConfiguration](#cfn-quicksight-analysis-labeloptions-fontconfiguration): {{
    FontConfiguration}}
  [Visibility](#cfn-quicksight-analysis-labeloptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-labeloptions-properties"></a>

`CustomLabel`  <a name="cfn-quicksight-analysis-labeloptions-customlabel"></a>
The text for the label.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontConfiguration`  <a name="cfn-quicksight-analysis-labeloptions-fontconfiguration"></a>
The font configuration of the label.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-analysis-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-labeloptions-visibility"></a>
Determines whether or not the label is visible.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
