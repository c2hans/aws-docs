---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sheetvisualscopingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SheetVisualScopingConfiguration
<a name="aws-properties-quicksight-template-sheetvisualscopingconfiguration"></a>

The filter that is applied to the options.

## Syntax
<a name="aws-properties-quicksight-template-sheetvisualscopingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sheetvisualscopingconfiguration-syntax.json"></a>

```
{
  "[Scope](#cfn-quicksight-template-sheetvisualscopingconfiguration-scope)" : {{String}},
  "[SheetId](#cfn-quicksight-template-sheetvisualscopingconfiguration-sheetid)" : {{String}},
  "[VisualIds](#cfn-quicksight-template-sheetvisualscopingconfiguration-visualids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sheetvisualscopingconfiguration-syntax.yaml"></a>

```
  [Scope](#cfn-quicksight-template-sheetvisualscopingconfiguration-scope): {{String}}
  [SheetId](#cfn-quicksight-template-sheetvisualscopingconfiguration-sheetid): {{String}}
  [VisualIds](#cfn-quicksight-template-sheetvisualscopingconfiguration-visualids): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-template-sheetvisualscopingconfiguration-properties"></a>

`Scope`  <a name="cfn-quicksight-template-sheetvisualscopingconfiguration-scope"></a>
The scope of the applied entities. Choose one of the following options:
+  `ALL_VISUALS`
+  `SELECTED_VISUALS`
*Required*: Yes
*Type*: String
*Allowed values*: `ALL_VISUALS | SELECTED_VISUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetId`  <a name="cfn-quicksight-template-sheetvisualscopingconfiguration-sheetid"></a>
The selected sheet that the filter is applied to.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualIds`  <a name="cfn-quicksight-template-sheetvisualscopingconfiguration-visualids"></a>
The selected visuals that the filter is applied to.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `512 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
