---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-visualtitlelabeloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template VisualTitleLabelOptions
<a name="aws-properties-quicksight-template-visualtitlelabeloptions"></a>

The title label options for a visual.

## Syntax
<a name="aws-properties-quicksight-template-visualtitlelabeloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-visualtitlelabeloptions-syntax.json"></a>

```
{
  "[FormatText](#cfn-quicksight-template-visualtitlelabeloptions-formattext)" : {{ShortFormatText}},
  "[Visibility](#cfn-quicksight-template-visualtitlelabeloptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-visualtitlelabeloptions-syntax.yaml"></a>

```
  [FormatText](#cfn-quicksight-template-visualtitlelabeloptions-formattext): {{
    ShortFormatText}}
  [Visibility](#cfn-quicksight-template-visualtitlelabeloptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-visualtitlelabeloptions-properties"></a>

`FormatText`  <a name="cfn-quicksight-template-visualtitlelabeloptions-formattext"></a>
The short text format of the title label, such as plain text or rich text.
*Required*: No
*Type*: [ShortFormatText](aws-properties-quicksight-template-shortformattext.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-visualtitlelabeloptions-visibility"></a>
The visibility of the title label.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
