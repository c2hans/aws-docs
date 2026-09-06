---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetControlInfoIconLabelOptions
<a name="aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions"></a>

A control to display info icons for filters and parameters.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-syntax.json"></a>

```
{
  "[InfoIconText](#cfn-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-infoicontext)" : {{String}},
  "[Visibility](#cfn-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-syntax.yaml"></a>

```
  [InfoIconText](#cfn-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-infoicontext): {{String}}
  [Visibility](#cfn-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-properties"></a>

`InfoIconText`  <a name="cfn-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-infoicontext"></a>
 The text content of info icon.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-dashboard-sheetcontrolinfoiconlabeloptions-visibility"></a>
The visibility configuration of info icon label options.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
