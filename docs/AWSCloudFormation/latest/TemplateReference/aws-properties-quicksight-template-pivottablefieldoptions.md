---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pivottablefieldoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PivotTableFieldOptions
<a name="aws-properties-quicksight-template-pivottablefieldoptions"></a>

The field options for a pivot table visual.

## Syntax
<a name="aws-properties-quicksight-template-pivottablefieldoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pivottablefieldoptions-syntax.json"></a>

```
{
  "[CollapseStateOptions](#cfn-quicksight-template-pivottablefieldoptions-collapsestateoptions)" : {{[ PivotTableFieldCollapseStateOption, ... ]}},
  "[DataPathOptions](#cfn-quicksight-template-pivottablefieldoptions-datapathoptions)" : {{[ PivotTableDataPathOption, ... ]}},
  "[SelectedFieldOptions](#cfn-quicksight-template-pivottablefieldoptions-selectedfieldoptions)" : {{[ PivotTableFieldOption, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pivottablefieldoptions-syntax.yaml"></a>

```
  [CollapseStateOptions](#cfn-quicksight-template-pivottablefieldoptions-collapsestateoptions): {{
    - PivotTableFieldCollapseStateOption}}
  [DataPathOptions](#cfn-quicksight-template-pivottablefieldoptions-datapathoptions): {{
    - PivotTableDataPathOption}}
  [SelectedFieldOptions](#cfn-quicksight-template-pivottablefieldoptions-selectedfieldoptions): {{
    - PivotTableFieldOption}}
```

## Properties
<a name="aws-properties-quicksight-template-pivottablefieldoptions-properties"></a>

`CollapseStateOptions`  <a name="cfn-quicksight-template-pivottablefieldoptions-collapsestateoptions"></a>
The collapse state options for the pivot table field options.
*Required*: No
*Type*: Array of [PivotTableFieldCollapseStateOption](aws-properties-quicksight-template-pivottablefieldcollapsestateoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataPathOptions`  <a name="cfn-quicksight-template-pivottablefieldoptions-datapathoptions"></a>
The data path options for the pivot table field options.
*Required*: No
*Type*: Array of [PivotTableDataPathOption](aws-properties-quicksight-template-pivottabledatapathoption.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedFieldOptions`  <a name="cfn-quicksight-template-pivottablefieldoptions-selectedfieldoptions"></a>
The selected field options for the pivot table field options.
*Required*: No
*Type*: Array of [PivotTableFieldOption](aws-properties-quicksight-template-pivottablefieldoption.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
