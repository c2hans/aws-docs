---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-parameterdropdowncontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ParameterDropDownControl
<a name="aws-properties-quicksight-template-parameterdropdowncontrol"></a>

A control to display a dropdown list with buttons that are used to select a single value.

## Syntax
<a name="aws-properties-quicksight-template-parameterdropdowncontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-parameterdropdowncontrol-syntax.json"></a>

```
{
  "[CascadingControlConfiguration](#cfn-quicksight-template-parameterdropdowncontrol-cascadingcontrolconfiguration)" : {{CascadingControlConfiguration}},
  "[CommitMode](#cfn-quicksight-template-parameterdropdowncontrol-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-template-parameterdropdowncontrol-displayoptions)" : {{DropDownControlDisplayOptions}},
  "[ParameterControlId](#cfn-quicksight-template-parameterdropdowncontrol-parametercontrolid)" : {{String}},
  "[SelectableValues](#cfn-quicksight-template-parameterdropdowncontrol-selectablevalues)" : {{ParameterSelectableValues}},
  "[SourceParameterName](#cfn-quicksight-template-parameterdropdowncontrol-sourceparametername)" : {{String}},
  "[Title](#cfn-quicksight-template-parameterdropdowncontrol-title)" : {{String}},
  "[Type](#cfn-quicksight-template-parameterdropdowncontrol-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-parameterdropdowncontrol-syntax.yaml"></a>

```
  [CascadingControlConfiguration](#cfn-quicksight-template-parameterdropdowncontrol-cascadingcontrolconfiguration): {{
    CascadingControlConfiguration}}
  [CommitMode](#cfn-quicksight-template-parameterdropdowncontrol-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-template-parameterdropdowncontrol-displayoptions): {{
    DropDownControlDisplayOptions}}
  [ParameterControlId](#cfn-quicksight-template-parameterdropdowncontrol-parametercontrolid): {{String}}
  [SelectableValues](#cfn-quicksight-template-parameterdropdowncontrol-selectablevalues): {{
    ParameterSelectableValues}}
  [SourceParameterName](#cfn-quicksight-template-parameterdropdowncontrol-sourceparametername): {{String}}
  [Title](#cfn-quicksight-template-parameterdropdowncontrol-title): {{String}}
  [Type](#cfn-quicksight-template-parameterdropdowncontrol-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-parameterdropdowncontrol-properties"></a>

`CascadingControlConfiguration`  <a name="cfn-quicksight-template-parameterdropdowncontrol-cascadingcontrolconfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
*Required*: No
*Type*: [CascadingControlConfiguration](aws-properties-quicksight-template-cascadingcontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CommitMode`  <a name="cfn-quicksight-template-parameterdropdowncontrol-commitmode"></a>
The visibility configuration of the Apply button on a `ParameterDropDownControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-template-parameterdropdowncontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [DropDownControlDisplayOptions](aws-properties-quicksight-template-dropdowncontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterControlId`  <a name="cfn-quicksight-template-parameterdropdowncontrol-parametercontrolid"></a>
The ID of the `ParameterDropDownControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectableValues`  <a name="cfn-quicksight-template-parameterdropdowncontrol-selectablevalues"></a>
A list of selectable values that are used in a control.
*Required*: No
*Type*: [ParameterSelectableValues](aws-properties-quicksight-template-parameterselectablevalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceParameterName`  <a name="cfn-quicksight-template-parameterdropdowncontrol-sourceparametername"></a>
The source parameter name of the `ParameterDropDownControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-parameterdropdowncontrol-title"></a>
The title of the `ParameterDropDownControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-template-parameterdropdowncontrol-type"></a>
The type parameter name of the `ParameterDropDownControl`.
*Required*: No
*Type*: String
*Allowed values*: `MULTI_SELECT | SINGLE_SELECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
