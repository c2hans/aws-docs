---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-defaulttextareacontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DefaultTextAreaControlOptions
<a name="aws-properties-quicksight-analysis-defaulttextareacontroloptions"></a>

The default options that correspond to the `TextArea` filter control type.

## Syntax
<a name="aws-properties-quicksight-analysis-defaulttextareacontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-defaulttextareacontroloptions-syntax.json"></a>

```
{
  "[Delimiter](#cfn-quicksight-analysis-defaulttextareacontroloptions-delimiter)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-analysis-defaulttextareacontroloptions-displayoptions)" : {{TextAreaControlDisplayOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-defaulttextareacontroloptions-syntax.yaml"></a>

```
  [Delimiter](#cfn-quicksight-analysis-defaulttextareacontroloptions-delimiter): {{String}}
  [DisplayOptions](#cfn-quicksight-analysis-defaulttextareacontroloptions-displayoptions): {{
    TextAreaControlDisplayOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-defaulttextareacontroloptions-properties"></a>

`Delimiter`  <a name="cfn-quicksight-analysis-defaulttextareacontroloptions-delimiter"></a>
The delimiter that is used to separate the lines in text.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-analysis-defaulttextareacontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [TextAreaControlDisplayOptions](aws-properties-quicksight-analysis-textareacontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
