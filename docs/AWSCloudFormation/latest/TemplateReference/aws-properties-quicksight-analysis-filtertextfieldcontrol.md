---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-filtertextfieldcontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FilterTextFieldControl
<a name="aws-properties-quicksight-analysis-filtertextfieldcontrol"></a>

A control to display a text box that is used to enter a single entry.

## Syntax
<a name="aws-properties-quicksight-analysis-filtertextfieldcontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-filtertextfieldcontrol-syntax.json"></a>

```
{
  "[DisplayOptions](#cfn-quicksight-analysis-filtertextfieldcontrol-displayoptions)" : {{TextFieldControlDisplayOptions}},
  "[FilterControlId](#cfn-quicksight-analysis-filtertextfieldcontrol-filtercontrolid)" : {{String}},
  "[SourceFilterId](#cfn-quicksight-analysis-filtertextfieldcontrol-sourcefilterid)" : {{String}},
  "[Title](#cfn-quicksight-analysis-filtertextfieldcontrol-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-filtertextfieldcontrol-syntax.yaml"></a>

```
  [DisplayOptions](#cfn-quicksight-analysis-filtertextfieldcontrol-displayoptions): {{
    TextFieldControlDisplayOptions}}
  [FilterControlId](#cfn-quicksight-analysis-filtertextfieldcontrol-filtercontrolid): {{String}}
  [SourceFilterId](#cfn-quicksight-analysis-filtertextfieldcontrol-sourcefilterid): {{String}}
  [Title](#cfn-quicksight-analysis-filtertextfieldcontrol-title): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-filtertextfieldcontrol-properties"></a>

`DisplayOptions`  <a name="cfn-quicksight-analysis-filtertextfieldcontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [TextFieldControlDisplayOptions](aws-properties-quicksight-analysis-textfieldcontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControlId`  <a name="cfn-quicksight-analysis-filtertextfieldcontrol-filtercontrolid"></a>
The ID of the `FilterTextFieldControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFilterId`  <a name="cfn-quicksight-analysis-filtertextfieldcontrol-sourcefilterid"></a>
The source filter ID of the `FilterTextFieldControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-filtertextfieldcontrol-title"></a>
The title of the `FilterTextFieldControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
