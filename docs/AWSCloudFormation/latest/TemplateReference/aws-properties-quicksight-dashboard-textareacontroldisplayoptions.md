---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-textareacontroldisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TextAreaControlDisplayOptions
<a name="aws-properties-quicksight-dashboard-textareacontroldisplayoptions"></a>

The display options of a control.

## Syntax
<a name="aws-properties-quicksight-dashboard-textareacontroldisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-textareacontroldisplayoptions-syntax.json"></a>

```
{
  "[InfoIconLabelOptions](#cfn-quicksight-dashboard-textareacontroldisplayoptions-infoiconlabeloptions)" : {{SheetControlInfoIconLabelOptions}},
  "[PlaceholderOptions](#cfn-quicksight-dashboard-textareacontroldisplayoptions-placeholderoptions)" : {{TextControlPlaceholderOptions}},
  "[TitleOptions](#cfn-quicksight-dashboard-textareacontroldisplayoptions-titleoptions)" : {{LabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-textareacontroldisplayoptions-syntax.yaml"></a>

```
  [InfoIconLabelOptions](#cfn-quicksight-dashboard-textareacontroldisplayoptions-infoiconlabeloptions): {{
    SheetControlInfoIconLabelOptions}}
  [PlaceholderOptions](#cfn-quicksight-dashboard-textareacontroldisplayoptions-placeholderoptions): {{
    TextControlPlaceholderOptions}}
  [TitleOptions](#cfn-quicksight-dashboard-textareacontroldisplayoptions-titleoptions): {{
    LabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-textareacontroldisplayoptions-properties"></a>

`InfoIconLabelOptions`  <a name="cfn-quicksight-dashboard-textareacontroldisplayoptions-infoiconlabeloptions"></a>
The configuration of info icon label options.
*Required*: No
*Type*: [SheetControlInfoIconLabelOptions](aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlaceholderOptions`  <a name="cfn-quicksight-dashboard-textareacontroldisplayoptions-placeholderoptions"></a>
The configuration of the placeholder options in a text area control.
*Required*: No
*Type*: [TextControlPlaceholderOptions](aws-properties-quicksight-dashboard-textcontrolplaceholderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleOptions`  <a name="cfn-quicksight-dashboard-textareacontroldisplayoptions-titleoptions"></a>
The options to configure the title visibility, name, and font size.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-dashboard-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
