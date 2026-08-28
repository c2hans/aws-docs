---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard Sheet
<a name="aws-properties-quicksight-dashboard-sheet"></a>

A *sheet*, which is an object that contains a set of visuals that are viewed together on one page in Quick Sight. Every analysis and dashboard contains at least one sheet. Each sheet contains at least one visualization widget, for example a chart, pivot table, or narrative insight. Sheets can be associated with other components, such as controls, filters, and so on.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheet-syntax.json"></a>

```
{
  "[Name](#cfn-quicksight-dashboard-sheet-name)" : {{String}},
  "[SheetId](#cfn-quicksight-dashboard-sheet-sheetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheet-syntax.yaml"></a>

```
  [Name](#cfn-quicksight-dashboard-sheet-name): {{String}}
  [SheetId](#cfn-quicksight-dashboard-sheet-sheetid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheet-properties"></a>

`Name`  <a name="cfn-quicksight-dashboard-sheet-name"></a>
The name of a sheet. This name is displayed on the sheet's tab in the Quick Sight console.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetId`  <a name="cfn-quicksight-dashboard-sheet-sheetid"></a>
The unique identifier associated with a sheet.
*Required*: No
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
