---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sheetcontrollayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SheetControlLayoutConfiguration
<a name="aws-properties-quicksight-analysis-sheetcontrollayoutconfiguration"></a>

The configuration that determines the elements and canvas size options of sheet control.

## Syntax
<a name="aws-properties-quicksight-analysis-sheetcontrollayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sheetcontrollayoutconfiguration-syntax.json"></a>

```
{
  "[GridLayout](#cfn-quicksight-analysis-sheetcontrollayoutconfiguration-gridlayout)" : {{GridLayoutConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sheetcontrollayoutconfiguration-syntax.yaml"></a>

```
  [GridLayout](#cfn-quicksight-analysis-sheetcontrollayoutconfiguration-gridlayout): {{
    GridLayoutConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sheetcontrollayoutconfiguration-properties"></a>

`GridLayout`  <a name="cfn-quicksight-analysis-sheetcontrollayoutconfiguration-gridlayout"></a>
The configuration that determines the elements and canvas size options of sheet control.
*Required*: No
*Type*: [GridLayoutConfiguration](aws-properties-quicksight-analysis-gridlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
