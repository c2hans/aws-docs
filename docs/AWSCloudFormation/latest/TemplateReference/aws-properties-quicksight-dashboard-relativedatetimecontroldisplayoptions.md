---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-relativedatetimecontroldisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard RelativeDateTimeControlDisplayOptions
<a name="aws-properties-quicksight-dashboard-relativedatetimecontroldisplayoptions"></a>

The display options of a control.

## Syntax
<a name="aws-properties-quicksight-dashboard-relativedatetimecontroldisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-relativedatetimecontroldisplayoptions-syntax.json"></a>

```
{
  "[DateTimeFormat](#cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-datetimeformat)" : {{String}},
  "[InfoIconLabelOptions](#cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-infoiconlabeloptions)" : {{SheetControlInfoIconLabelOptions}},
  "[TitleOptions](#cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-titleoptions)" : {{LabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-relativedatetimecontroldisplayoptions-syntax.yaml"></a>

```
  [DateTimeFormat](#cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-datetimeformat): {{String}}
  [InfoIconLabelOptions](#cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-infoiconlabeloptions): {{
    SheetControlInfoIconLabelOptions}}
  [TitleOptions](#cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-titleoptions): {{
    LabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-relativedatetimecontroldisplayoptions-properties"></a>

`DateTimeFormat`  <a name="cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-datetimeformat"></a>
Customize how dates are formatted in controls.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfoIconLabelOptions`  <a name="cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-infoiconlabeloptions"></a>
The configuration of info icon label options.
*Required*: No
*Type*: [SheetControlInfoIconLabelOptions](aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleOptions`  <a name="cfn-quicksight-dashboard-relativedatetimecontroldisplayoptions-titleoptions"></a>
The options to configure the title visibility, name, and font size.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-dashboard-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
