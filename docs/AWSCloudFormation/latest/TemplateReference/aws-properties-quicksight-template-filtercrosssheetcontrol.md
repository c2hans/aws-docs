---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-filtercrosssheetcontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FilterCrossSheetControl
<a name="aws-properties-quicksight-template-filtercrosssheetcontrol"></a>

A control from a filter that is scoped across more than one sheet. This represents your filter control on a sheet

## Syntax
<a name="aws-properties-quicksight-template-filtercrosssheetcontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-filtercrosssheetcontrol-syntax.json"></a>

```
{
  "[CascadingControlConfiguration](#cfn-quicksight-template-filtercrosssheetcontrol-cascadingcontrolconfiguration)" : {{CascadingControlConfiguration}},
  "[FilterControlId](#cfn-quicksight-template-filtercrosssheetcontrol-filtercontrolid)" : {{String}},
  "[SourceFilterId](#cfn-quicksight-template-filtercrosssheetcontrol-sourcefilterid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-filtercrosssheetcontrol-syntax.yaml"></a>

```
  [CascadingControlConfiguration](#cfn-quicksight-template-filtercrosssheetcontrol-cascadingcontrolconfiguration): {{
    CascadingControlConfiguration}}
  [FilterControlId](#cfn-quicksight-template-filtercrosssheetcontrol-filtercontrolid): {{String}}
  [SourceFilterId](#cfn-quicksight-template-filtercrosssheetcontrol-sourcefilterid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-filtercrosssheetcontrol-properties"></a>

`CascadingControlConfiguration`  <a name="cfn-quicksight-template-filtercrosssheetcontrol-cascadingcontrolconfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
*Required*: No
*Type*: [CascadingControlConfiguration](aws-properties-quicksight-template-cascadingcontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControlId`  <a name="cfn-quicksight-template-filtercrosssheetcontrol-filtercontrolid"></a>
The ID of the `FilterCrossSheetControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFilterId`  <a name="cfn-quicksight-template-filtercrosssheetcontrol-sourcefilterid"></a>
The source filter ID of the `FilterCrossSheetControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
