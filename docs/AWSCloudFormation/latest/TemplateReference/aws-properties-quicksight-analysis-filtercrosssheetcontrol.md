---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-filtercrosssheetcontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FilterCrossSheetControl
<a name="aws-properties-quicksight-analysis-filtercrosssheetcontrol"></a>

A control from a filter that is scoped across more than one sheet. This represents your filter control on a sheet

## Syntax
<a name="aws-properties-quicksight-analysis-filtercrosssheetcontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-filtercrosssheetcontrol-syntax.json"></a>

```
{
  "[CascadingControlConfiguration](#cfn-quicksight-analysis-filtercrosssheetcontrol-cascadingcontrolconfiguration)" : {{CascadingControlConfiguration}},
  "[FilterControlId](#cfn-quicksight-analysis-filtercrosssheetcontrol-filtercontrolid)" : {{String}},
  "[SourceFilterId](#cfn-quicksight-analysis-filtercrosssheetcontrol-sourcefilterid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-filtercrosssheetcontrol-syntax.yaml"></a>

```
  [CascadingControlConfiguration](#cfn-quicksight-analysis-filtercrosssheetcontrol-cascadingcontrolconfiguration): {{
    CascadingControlConfiguration}}
  [FilterControlId](#cfn-quicksight-analysis-filtercrosssheetcontrol-filtercontrolid): {{String}}
  [SourceFilterId](#cfn-quicksight-analysis-filtercrosssheetcontrol-sourcefilterid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-filtercrosssheetcontrol-properties"></a>

`CascadingControlConfiguration`  <a name="cfn-quicksight-analysis-filtercrosssheetcontrol-cascadingcontrolconfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
*Required*: No
*Type*: [CascadingControlConfiguration](aws-properties-quicksight-analysis-cascadingcontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControlId`  <a name="cfn-quicksight-analysis-filtercrosssheetcontrol-filtercontrolid"></a>
The ID of the `FilterCrossSheetControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFilterId`  <a name="cfn-quicksight-analysis-filtercrosssheetcontrol-sourcefilterid"></a>
The source filter ID of the `FilterCrossSheetControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
