---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-parametertextareacontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ParameterTextAreaControl
<a name="aws-properties-quicksight-analysis-parametertextareacontrol"></a>

A control to display a text box that is used to enter multiple entries.

## Syntax
<a name="aws-properties-quicksight-analysis-parametertextareacontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-parametertextareacontrol-syntax.json"></a>

```
{
  "[Delimiter](#cfn-quicksight-analysis-parametertextareacontrol-delimiter)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-analysis-parametertextareacontrol-displayoptions)" : {{TextAreaControlDisplayOptions}},
  "[ParameterControlId](#cfn-quicksight-analysis-parametertextareacontrol-parametercontrolid)" : {{String}},
  "[SourceParameterName](#cfn-quicksight-analysis-parametertextareacontrol-sourceparametername)" : {{String}},
  "[Title](#cfn-quicksight-analysis-parametertextareacontrol-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-parametertextareacontrol-syntax.yaml"></a>

```
  [Delimiter](#cfn-quicksight-analysis-parametertextareacontrol-delimiter): {{String}}
  [DisplayOptions](#cfn-quicksight-analysis-parametertextareacontrol-displayoptions): {{
    TextAreaControlDisplayOptions}}
  [ParameterControlId](#cfn-quicksight-analysis-parametertextareacontrol-parametercontrolid): {{String}}
  [SourceParameterName](#cfn-quicksight-analysis-parametertextareacontrol-sourceparametername): {{String}}
  [Title](#cfn-quicksight-analysis-parametertextareacontrol-title): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-parametertextareacontrol-properties"></a>

`Delimiter`  <a name="cfn-quicksight-analysis-parametertextareacontrol-delimiter"></a>
The delimiter that is used to separate the lines in text.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-analysis-parametertextareacontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [TextAreaControlDisplayOptions](aws-properties-quicksight-analysis-textareacontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterControlId`  <a name="cfn-quicksight-analysis-parametertextareacontrol-parametercontrolid"></a>
The ID of the `ParameterTextAreaControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceParameterName`  <a name="cfn-quicksight-analysis-parametertextareacontrol-sourceparametername"></a>
The source parameter name of the `ParameterTextAreaControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-parametertextareacontrol-title"></a>
The title of the `ParameterTextAreaControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
