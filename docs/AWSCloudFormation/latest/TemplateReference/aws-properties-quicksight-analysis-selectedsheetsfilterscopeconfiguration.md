---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-selectedsheetsfilterscopeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SelectedSheetsFilterScopeConfiguration
<a name="aws-properties-quicksight-analysis-selectedsheetsfilterscopeconfiguration"></a>

The configuration for applying a filter to specific sheets or visuals. You can apply this filter to multiple visuals that are on one sheet or to all visuals on a sheet.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-selectedsheetsfilterscopeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-selectedsheetsfilterscopeconfiguration-syntax.json"></a>

```
{
  "[SheetVisualScopingConfigurations](#cfn-quicksight-analysis-selectedsheetsfilterscopeconfiguration-sheetvisualscopingconfigurations)" : {{[ SheetVisualScopingConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-selectedsheetsfilterscopeconfiguration-syntax.yaml"></a>

```
  [SheetVisualScopingConfigurations](#cfn-quicksight-analysis-selectedsheetsfilterscopeconfiguration-sheetvisualscopingconfigurations): {{
    - SheetVisualScopingConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-selectedsheetsfilterscopeconfiguration-properties"></a>

`SheetVisualScopingConfigurations`  <a name="cfn-quicksight-analysis-selectedsheetsfilterscopeconfiguration-sheetvisualscopingconfigurations"></a>
The sheet ID and visual IDs of the sheet and visuals that the filter is applied to.
*Required*: No
*Type*: Array of [SheetVisualScopingConfiguration](aws-properties-quicksight-analysis-sheetvisualscopingconfiguration.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
