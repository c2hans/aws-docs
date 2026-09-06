---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-defaultfilterdropdowncontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DefaultFilterDropDownControlOptions
<a name="aws-properties-quicksight-analysis-defaultfilterdropdowncontroloptions"></a>

The default options that correspond to the `Dropdown` filter control type.

## Syntax
<a name="aws-properties-quicksight-analysis-defaultfilterdropdowncontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-defaultfilterdropdowncontroloptions-syntax.json"></a>

```
{
  "[CommitMode](#cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-displayoptions)" : {{DropDownControlDisplayOptions}},
  "[SelectableValues](#cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-selectablevalues)" : {{FilterSelectableValues}},
  "[Type](#cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-defaultfilterdropdowncontroloptions-syntax.yaml"></a>

```
  [CommitMode](#cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-displayoptions): {{
    DropDownControlDisplayOptions}}
  [SelectableValues](#cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-selectablevalues): {{
    FilterSelectableValues}}
  [Type](#cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-defaultfilterdropdowncontroloptions-properties"></a>

`CommitMode`  <a name="cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-commitmode"></a>
The visibility configuration of the Apply button on a `FilterDropDownControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [DropDownControlDisplayOptions](aws-properties-quicksight-analysis-dropdowncontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectableValues`  <a name="cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-selectablevalues"></a>
A list of selectable values that are used in a control.
*Required*: No
*Type*: [FilterSelectableValues](aws-properties-quicksight-analysis-filterselectablevalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-analysis-defaultfilterdropdowncontroloptions-type"></a>
The type of the `FilterDropDownControl`. Choose one of the following options:
+ `MULTI_SELECT`: The user can select multiple entries from a dropdown menu.
+ `SINGLE_SELECT`: The user can select a single entry from a dropdown menu.
*Required*: No
*Type*: String
*Allowed values*: `MULTI_SELECT | SINGLE_SELECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
