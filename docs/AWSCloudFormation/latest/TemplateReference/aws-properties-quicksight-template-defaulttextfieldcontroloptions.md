---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-defaulttextfieldcontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DefaultTextFieldControlOptions
<a name="aws-properties-quicksight-template-defaulttextfieldcontroloptions"></a>

The default options that correspond to the `TextField` filter control type.

## Syntax
<a name="aws-properties-quicksight-template-defaulttextfieldcontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-defaulttextfieldcontroloptions-syntax.json"></a>

```
{
  "[DisplayOptions](#cfn-quicksight-template-defaulttextfieldcontroloptions-displayoptions)" : {{TextFieldControlDisplayOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-defaulttextfieldcontroloptions-syntax.yaml"></a>

```
  [DisplayOptions](#cfn-quicksight-template-defaulttextfieldcontroloptions-displayoptions): {{
    TextFieldControlDisplayOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-defaulttextfieldcontroloptions-properties"></a>

`DisplayOptions`  <a name="cfn-quicksight-template-defaulttextfieldcontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [TextFieldControlDisplayOptions](aws-properties-quicksight-template-textfieldcontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
