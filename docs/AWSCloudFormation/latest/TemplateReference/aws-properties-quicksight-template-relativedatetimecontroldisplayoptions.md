---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-relativedatetimecontroldisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template RelativeDateTimeControlDisplayOptions
<a name="aws-properties-quicksight-template-relativedatetimecontroldisplayoptions"></a>

The display options of a control.

## Syntax
<a name="aws-properties-quicksight-template-relativedatetimecontroldisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-relativedatetimecontroldisplayoptions-syntax.json"></a>

```
{
  "[DateTimeFormat](#cfn-quicksight-template-relativedatetimecontroldisplayoptions-datetimeformat)" : {{String}},
  "[InfoIconLabelOptions](#cfn-quicksight-template-relativedatetimecontroldisplayoptions-infoiconlabeloptions)" : {{SheetControlInfoIconLabelOptions}},
  "[TitleOptions](#cfn-quicksight-template-relativedatetimecontroldisplayoptions-titleoptions)" : {{LabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-relativedatetimecontroldisplayoptions-syntax.yaml"></a>

```
  [DateTimeFormat](#cfn-quicksight-template-relativedatetimecontroldisplayoptions-datetimeformat): {{String}}
  [InfoIconLabelOptions](#cfn-quicksight-template-relativedatetimecontroldisplayoptions-infoiconlabeloptions): {{
    SheetControlInfoIconLabelOptions}}
  [TitleOptions](#cfn-quicksight-template-relativedatetimecontroldisplayoptions-titleoptions): {{
    LabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-relativedatetimecontroldisplayoptions-properties"></a>

`DateTimeFormat`  <a name="cfn-quicksight-template-relativedatetimecontroldisplayoptions-datetimeformat"></a>
Customize how dates are formatted in controls.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfoIconLabelOptions`  <a name="cfn-quicksight-template-relativedatetimecontroldisplayoptions-infoiconlabeloptions"></a>
The configuration of info icon label options.
*Required*: No
*Type*: [SheetControlInfoIconLabelOptions](aws-properties-quicksight-template-sheetcontrolinfoiconlabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleOptions`  <a name="cfn-quicksight-template-relativedatetimecontroldisplayoptions-titleoptions"></a>
The options to configure the title visibility, name, and font size.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-template-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
