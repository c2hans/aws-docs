---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheetvisualscopingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetVisualScopingConfiguration
<a name="aws-properties-quicksight-dashboard-sheetvisualscopingconfiguration"></a>

The filter that is applied to the options.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheetvisualscopingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheetvisualscopingconfiguration-syntax.json"></a>

```
{
  "[Scope](#cfn-quicksight-dashboard-sheetvisualscopingconfiguration-scope)" : {{String}},
  "[SheetId](#cfn-quicksight-dashboard-sheetvisualscopingconfiguration-sheetid)" : {{String}},
  "[VisualIds](#cfn-quicksight-dashboard-sheetvisualscopingconfiguration-visualids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheetvisualscopingconfiguration-syntax.yaml"></a>

```
  [Scope](#cfn-quicksight-dashboard-sheetvisualscopingconfiguration-scope): {{String}}
  [SheetId](#cfn-quicksight-dashboard-sheetvisualscopingconfiguration-sheetid): {{String}}
  [VisualIds](#cfn-quicksight-dashboard-sheetvisualscopingconfiguration-visualids): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheetvisualscopingconfiguration-properties"></a>

`Scope`  <a name="cfn-quicksight-dashboard-sheetvisualscopingconfiguration-scope"></a>
The scope of the applied entities. Choose one of the following options:
+  `ALL_VISUALS`
+  `SELECTED_VISUALS`
*Required*: Yes
*Type*: String
*Allowed values*: `ALL_VISUALS | SELECTED_VISUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetId`  <a name="cfn-quicksight-dashboard-sheetvisualscopingconfiguration-sheetid"></a>
The selected sheet that the filter is applied to.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualIds`  <a name="cfn-quicksight-dashboard-sheetvisualscopingconfiguration-visualids"></a>
The selected visuals that the filter is applied to.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `512 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
