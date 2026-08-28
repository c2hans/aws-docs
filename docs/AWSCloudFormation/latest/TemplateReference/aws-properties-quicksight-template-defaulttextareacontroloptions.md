---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-defaulttextareacontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DefaultTextAreaControlOptions
<a name="aws-properties-quicksight-template-defaulttextareacontroloptions"></a>

The default options that correspond to the `TextArea` filter control type.

## Syntax
<a name="aws-properties-quicksight-template-defaulttextareacontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-defaulttextareacontroloptions-syntax.json"></a>

```
{
  "[Delimiter](#cfn-quicksight-template-defaulttextareacontroloptions-delimiter)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-template-defaulttextareacontroloptions-displayoptions)" : {{TextAreaControlDisplayOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-defaulttextareacontroloptions-syntax.yaml"></a>

```
  [Delimiter](#cfn-quicksight-template-defaulttextareacontroloptions-delimiter): {{String}}
  [DisplayOptions](#cfn-quicksight-template-defaulttextareacontroloptions-displayoptions): {{
    TextAreaControlDisplayOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-defaulttextareacontroloptions-properties"></a>

`Delimiter`  <a name="cfn-quicksight-template-defaulttextareacontroloptions-delimiter"></a>
The delimiter that is used to separate the lines in text.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-template-defaulttextareacontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [TextAreaControlDisplayOptions](aws-properties-quicksight-template-textareacontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
