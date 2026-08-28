---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-filterlistcontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FilterListControl
<a name="aws-properties-quicksight-analysis-filterlistcontrol"></a>

A control to display a list of buttons or boxes. This is used to select either a single value or multiple values.

## Syntax
<a name="aws-properties-quicksight-analysis-filterlistcontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-filterlistcontrol-syntax.json"></a>

```
{
  "[CascadingControlConfiguration](#cfn-quicksight-analysis-filterlistcontrol-cascadingcontrolconfiguration)" : {{CascadingControlConfiguration}},
  "[DisplayOptions](#cfn-quicksight-analysis-filterlistcontrol-displayoptions)" : {{ListControlDisplayOptions}},
  "[FilterControlId](#cfn-quicksight-analysis-filterlistcontrol-filtercontrolid)" : {{String}},
  "[SelectableValues](#cfn-quicksight-analysis-filterlistcontrol-selectablevalues)" : {{FilterSelectableValues}},
  "[SourceFilterId](#cfn-quicksight-analysis-filterlistcontrol-sourcefilterid)" : {{String}},
  "[Title](#cfn-quicksight-analysis-filterlistcontrol-title)" : {{String}},
  "[Type](#cfn-quicksight-analysis-filterlistcontrol-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-filterlistcontrol-syntax.yaml"></a>

```
  [CascadingControlConfiguration](#cfn-quicksight-analysis-filterlistcontrol-cascadingcontrolconfiguration): {{
    CascadingControlConfiguration}}
  [DisplayOptions](#cfn-quicksight-analysis-filterlistcontrol-displayoptions): {{
    ListControlDisplayOptions}}
  [FilterControlId](#cfn-quicksight-analysis-filterlistcontrol-filtercontrolid): {{String}}
  [SelectableValues](#cfn-quicksight-analysis-filterlistcontrol-selectablevalues): {{
    FilterSelectableValues}}
  [SourceFilterId](#cfn-quicksight-analysis-filterlistcontrol-sourcefilterid): {{String}}
  [Title](#cfn-quicksight-analysis-filterlistcontrol-title): {{String}}
  [Type](#cfn-quicksight-analysis-filterlistcontrol-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-filterlistcontrol-properties"></a>

`CascadingControlConfiguration`  <a name="cfn-quicksight-analysis-filterlistcontrol-cascadingcontrolconfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
*Required*: No
*Type*: [CascadingControlConfiguration](aws-properties-quicksight-analysis-cascadingcontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-analysis-filterlistcontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [ListControlDisplayOptions](aws-properties-quicksight-analysis-listcontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControlId`  <a name="cfn-quicksight-analysis-filterlistcontrol-filtercontrolid"></a>
The ID of the `FilterListControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectableValues`  <a name="cfn-quicksight-analysis-filterlistcontrol-selectablevalues"></a>
A list of selectable values that are used in a control.
*Required*: No
*Type*: [FilterSelectableValues](aws-properties-quicksight-analysis-filterselectablevalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFilterId`  <a name="cfn-quicksight-analysis-filterlistcontrol-sourcefilterid"></a>
The source filter ID of the `FilterListControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-filterlistcontrol-title"></a>
The title of the `FilterListControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-analysis-filterlistcontrol-type"></a>
The type of the `FilterListControl`. Choose one of the following options:
+ `MULTI_SELECT`: The user can select multiple entries from the list.
+ `SINGLE_SELECT`: The user can select a single entry from the list.
*Required*: No
*Type*: String
*Allowed values*: `MULTI_SELECT | SINGLE_SELECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
