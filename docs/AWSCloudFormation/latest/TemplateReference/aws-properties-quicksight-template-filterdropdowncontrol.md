---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-filterdropdowncontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FilterDropDownControl
<a name="aws-properties-quicksight-template-filterdropdowncontrol"></a>

A control to display a dropdown list with buttons that are used to select a single value.

## Syntax
<a name="aws-properties-quicksight-template-filterdropdowncontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-filterdropdowncontrol-syntax.json"></a>

```
{
  "[CascadingControlConfiguration](#cfn-quicksight-template-filterdropdowncontrol-cascadingcontrolconfiguration)" : {{CascadingControlConfiguration}},
  "[CommitMode](#cfn-quicksight-template-filterdropdowncontrol-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-template-filterdropdowncontrol-displayoptions)" : {{DropDownControlDisplayOptions}},
  "[FilterControlId](#cfn-quicksight-template-filterdropdowncontrol-filtercontrolid)" : {{String}},
  "[SelectableValues](#cfn-quicksight-template-filterdropdowncontrol-selectablevalues)" : {{FilterSelectableValues}},
  "[SourceFilterId](#cfn-quicksight-template-filterdropdowncontrol-sourcefilterid)" : {{String}},
  "[Title](#cfn-quicksight-template-filterdropdowncontrol-title)" : {{String}},
  "[Type](#cfn-quicksight-template-filterdropdowncontrol-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-filterdropdowncontrol-syntax.yaml"></a>

```
  [CascadingControlConfiguration](#cfn-quicksight-template-filterdropdowncontrol-cascadingcontrolconfiguration): {{
    CascadingControlConfiguration}}
  [CommitMode](#cfn-quicksight-template-filterdropdowncontrol-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-template-filterdropdowncontrol-displayoptions): {{
    DropDownControlDisplayOptions}}
  [FilterControlId](#cfn-quicksight-template-filterdropdowncontrol-filtercontrolid): {{String}}
  [SelectableValues](#cfn-quicksight-template-filterdropdowncontrol-selectablevalues): {{
    FilterSelectableValues}}
  [SourceFilterId](#cfn-quicksight-template-filterdropdowncontrol-sourcefilterid): {{String}}
  [Title](#cfn-quicksight-template-filterdropdowncontrol-title): {{String}}
  [Type](#cfn-quicksight-template-filterdropdowncontrol-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-filterdropdowncontrol-properties"></a>

`CascadingControlConfiguration`  <a name="cfn-quicksight-template-filterdropdowncontrol-cascadingcontrolconfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
*Required*: No
*Type*: [CascadingControlConfiguration](aws-properties-quicksight-template-cascadingcontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CommitMode`  <a name="cfn-quicksight-template-filterdropdowncontrol-commitmode"></a>
The visibility configuration of the Apply button on a `FilterDropDownControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-template-filterdropdowncontrol-displayoptions"></a>
The display options of the `FilterDropDownControl`.
*Required*: No
*Type*: [DropDownControlDisplayOptions](aws-properties-quicksight-template-dropdowncontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControlId`  <a name="cfn-quicksight-template-filterdropdowncontrol-filtercontrolid"></a>
The ID of the `FilterDropDownControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectableValues`  <a name="cfn-quicksight-template-filterdropdowncontrol-selectablevalues"></a>
A list of selectable values that are used in a control.
*Required*: No
*Type*: [FilterSelectableValues](aws-properties-quicksight-template-filterselectablevalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFilterId`  <a name="cfn-quicksight-template-filterdropdowncontrol-sourcefilterid"></a>
The source filter ID of the `FilterDropDownControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-filterdropdowncontrol-title"></a>
The title of the `FilterDropDownControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-template-filterdropdowncontrol-type"></a>
The type of the `FilterDropDownControl`. Choose one of the following options:
+ `MULTI_SELECT`: The user can select multiple entries from a dropdown menu.
+ `SINGLE_SELECT`: The user can select a single entry from a dropdown menu.
*Required*: No
*Type*: String
*Allowed values*: `MULTI_SELECT | SINGLE_SELECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
