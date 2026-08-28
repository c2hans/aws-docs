---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-listcontroldisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ListControlDisplayOptions
<a name="aws-properties-quicksight-analysis-listcontroldisplayoptions"></a>

The display options of a control.

## Syntax
<a name="aws-properties-quicksight-analysis-listcontroldisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-listcontroldisplayoptions-syntax.json"></a>

```
{
  "[InfoIconLabelOptions](#cfn-quicksight-analysis-listcontroldisplayoptions-infoiconlabeloptions)" : {{SheetControlInfoIconLabelOptions}},
  "[SearchOptions](#cfn-quicksight-analysis-listcontroldisplayoptions-searchoptions)" : {{ListControlSearchOptions}},
  "[SelectAllOptions](#cfn-quicksight-analysis-listcontroldisplayoptions-selectalloptions)" : {{ListControlSelectAllOptions}},
  "[TitleOptions](#cfn-quicksight-analysis-listcontroldisplayoptions-titleoptions)" : {{LabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-listcontroldisplayoptions-syntax.yaml"></a>

```
  [InfoIconLabelOptions](#cfn-quicksight-analysis-listcontroldisplayoptions-infoiconlabeloptions): {{
    SheetControlInfoIconLabelOptions}}
  [SearchOptions](#cfn-quicksight-analysis-listcontroldisplayoptions-searchoptions): {{
    ListControlSearchOptions}}
  [SelectAllOptions](#cfn-quicksight-analysis-listcontroldisplayoptions-selectalloptions): {{
    ListControlSelectAllOptions}}
  [TitleOptions](#cfn-quicksight-analysis-listcontroldisplayoptions-titleoptions): {{
    LabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-listcontroldisplayoptions-properties"></a>

`InfoIconLabelOptions`  <a name="cfn-quicksight-analysis-listcontroldisplayoptions-infoiconlabeloptions"></a>
The configuration of info icon label options.
*Required*: No
*Type*: [SheetControlInfoIconLabelOptions](aws-properties-quicksight-analysis-sheetcontrolinfoiconlabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SearchOptions`  <a name="cfn-quicksight-analysis-listcontroldisplayoptions-searchoptions"></a>
The configuration of the search options in a list control.
*Required*: No
*Type*: [ListControlSearchOptions](aws-properties-quicksight-analysis-listcontrolsearchoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectAllOptions`  <a name="cfn-quicksight-analysis-listcontroldisplayoptions-selectalloptions"></a>
The configuration of the `Select all` options in a list control.
*Required*: No
*Type*: [ListControlSelectAllOptions](aws-properties-quicksight-analysis-listcontrolselectalloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleOptions`  <a name="cfn-quicksight-analysis-listcontroldisplayoptions-titleoptions"></a>
The options to configure the title visibility, name, and font size.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-analysis-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
