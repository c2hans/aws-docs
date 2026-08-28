---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-defaultfilterlistcontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DefaultFilterListControlOptions
<a name="aws-properties-quicksight-dashboard-defaultfilterlistcontroloptions"></a>

The default options that correspond to the `List` filter control type.

## Syntax
<a name="aws-properties-quicksight-dashboard-defaultfilterlistcontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-defaultfilterlistcontroloptions-syntax.json"></a>

```
{
  "[DisplayOptions](#cfn-quicksight-dashboard-defaultfilterlistcontroloptions-displayoptions)" : {{ListControlDisplayOptions}},
  "[SelectableValues](#cfn-quicksight-dashboard-defaultfilterlistcontroloptions-selectablevalues)" : {{FilterSelectableValues}},
  "[Type](#cfn-quicksight-dashboard-defaultfilterlistcontroloptions-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-defaultfilterlistcontroloptions-syntax.yaml"></a>

```
  [DisplayOptions](#cfn-quicksight-dashboard-defaultfilterlistcontroloptions-displayoptions): {{
    ListControlDisplayOptions}}
  [SelectableValues](#cfn-quicksight-dashboard-defaultfilterlistcontroloptions-selectablevalues): {{
    FilterSelectableValues}}
  [Type](#cfn-quicksight-dashboard-defaultfilterlistcontroloptions-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-defaultfilterlistcontroloptions-properties"></a>

`DisplayOptions`  <a name="cfn-quicksight-dashboard-defaultfilterlistcontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [ListControlDisplayOptions](aws-properties-quicksight-dashboard-listcontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectableValues`  <a name="cfn-quicksight-dashboard-defaultfilterlistcontroloptions-selectablevalues"></a>
A list of selectable values that are used in a control.
*Required*: No
*Type*: [FilterSelectableValues](aws-properties-quicksight-dashboard-filterselectablevalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dashboard-defaultfilterlistcontroloptions-type"></a>
The type of the `DefaultFilterListControlOptions`. Choose one of the following options:
+ `MULTI_SELECT`: The user can select multiple entries from the list.
+ `SINGLE_SELECT`: The user can select a single entry from the list.
*Required*: No
*Type*: String
*Allowed values*: `MULTI_SELECT | SINGLE_SELECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
