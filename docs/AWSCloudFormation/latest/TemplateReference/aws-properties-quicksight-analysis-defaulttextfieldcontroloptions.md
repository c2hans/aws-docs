---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-defaulttextfieldcontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DefaultTextFieldControlOptions
<a name="aws-properties-quicksight-analysis-defaulttextfieldcontroloptions"></a>

The default options that correspond to the `TextField` filter control type.

## Syntax
<a name="aws-properties-quicksight-analysis-defaulttextfieldcontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-defaulttextfieldcontroloptions-syntax.json"></a>

```
{
  "[DisplayOptions](#cfn-quicksight-analysis-defaulttextfieldcontroloptions-displayoptions)" : {{TextFieldControlDisplayOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-defaulttextfieldcontroloptions-syntax.yaml"></a>

```
  [DisplayOptions](#cfn-quicksight-analysis-defaulttextfieldcontroloptions-displayoptions): {{
    TextFieldControlDisplayOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-defaulttextfieldcontroloptions-properties"></a>

`DisplayOptions`  <a name="cfn-quicksight-analysis-defaulttextfieldcontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [TextFieldControlDisplayOptions](aws-properties-quicksight-analysis-textfieldcontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
