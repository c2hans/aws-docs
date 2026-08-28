---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-visualsubtitlelabeloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard VisualSubtitleLabelOptions
<a name="aws-properties-quicksight-dashboard-visualsubtitlelabeloptions"></a>

The subtitle label options for a visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-visualsubtitlelabeloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-visualsubtitlelabeloptions-syntax.json"></a>

```
{
  "[FormatText](#cfn-quicksight-dashboard-visualsubtitlelabeloptions-formattext)" : {{LongFormatText}},
  "[Visibility](#cfn-quicksight-dashboard-visualsubtitlelabeloptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-visualsubtitlelabeloptions-syntax.yaml"></a>

```
  [FormatText](#cfn-quicksight-dashboard-visualsubtitlelabeloptions-formattext): {{
    LongFormatText}}
  [Visibility](#cfn-quicksight-dashboard-visualsubtitlelabeloptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-visualsubtitlelabeloptions-properties"></a>

`FormatText`  <a name="cfn-quicksight-dashboard-visualsubtitlelabeloptions-formattext"></a>
The long text format of the subtitle label, such as plain text or rich text.
*Required*: No
*Type*: [LongFormatText](aws-properties-quicksight-dashboard-longformattext.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-dashboard-visualsubtitlelabeloptions-visibility"></a>
The visibility of the subtitle label.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
