---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-sheetbackgroundstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme SheetBackgroundStyle
<a name="aws-properties-quicksight-theme-sheetbackgroundstyle"></a>

The background configuration for sheets.

## Syntax
<a name="aws-properties-quicksight-theme-sheetbackgroundstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-sheetbackgroundstyle-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-theme-sheetbackgroundstyle-color)" : {{String}},
  "[Gradient](#cfn-quicksight-theme-sheetbackgroundstyle-gradient)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-sheetbackgroundstyle-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-theme-sheetbackgroundstyle-color): {{String}}
  [Gradient](#cfn-quicksight-theme-sheetbackgroundstyle-gradient): {{String}}
```

## Properties
<a name="aws-properties-quicksight-theme-sheetbackgroundstyle-properties"></a>

`Color`  <a name="cfn-quicksight-theme-sheetbackgroundstyle-color"></a>
The solid color background option for sheets.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gradient`  <a name="cfn-quicksight-theme-sheetbackgroundstyle-gradient"></a>
The gradient background option for sheets.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
