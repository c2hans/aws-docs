---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-filterscopeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FilterScopeConfiguration
<a name="aws-properties-quicksight-template-filterscopeconfiguration"></a>

The scope configuration for a `FilterGroup`.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-template-filterscopeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-filterscopeconfiguration-syntax.json"></a>

```
{
  "[AllSheets](#cfn-quicksight-template-filterscopeconfiguration-allsheets)" : {{Json}},
  "[SelectedSheets](#cfn-quicksight-template-filterscopeconfiguration-selectedsheets)" : {{SelectedSheetsFilterScopeConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-filterscopeconfiguration-syntax.yaml"></a>

```
  [AllSheets](#cfn-quicksight-template-filterscopeconfiguration-allsheets): {{Json}}
  [SelectedSheets](#cfn-quicksight-template-filterscopeconfiguration-selectedsheets): {{
    SelectedSheetsFilterScopeConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-filterscopeconfiguration-properties"></a>

`AllSheets`  <a name="cfn-quicksight-template-filterscopeconfiguration-allsheets"></a>
The configuration that applies a filter to all sheets. When you choose `AllSheets` as the value for a `FilterScopeConfiguration`, this filter is applied to all visuals of all sheets in an Analysis, Dashboard, or Template. The `AllSheetsFilterScopeConfiguration` is chosen.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedSheets`  <a name="cfn-quicksight-template-filterscopeconfiguration-selectedsheets"></a>
The configuration for applying a filter to specific sheets.
*Required*: No
*Type*: [SelectedSheetsFilterScopeConfiguration](aws-properties-quicksight-template-selectedsheetsfilterscopeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
