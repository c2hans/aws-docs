---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-globaltableborderoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GlobalTableBorderOptions
<a name="aws-properties-quicksight-template-globaltableborderoptions"></a>

Determines the border options for a table visual.

## Syntax
<a name="aws-properties-quicksight-template-globaltableborderoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-globaltableborderoptions-syntax.json"></a>

```
{
  "[SideSpecificBorder](#cfn-quicksight-template-globaltableborderoptions-sidespecificborder)" : {{TableSideBorderOptions}},
  "[UniformBorder](#cfn-quicksight-template-globaltableborderoptions-uniformborder)" : {{TableBorderOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-globaltableborderoptions-syntax.yaml"></a>

```
  [SideSpecificBorder](#cfn-quicksight-template-globaltableborderoptions-sidespecificborder): {{
    TableSideBorderOptions}}
  [UniformBorder](#cfn-quicksight-template-globaltableborderoptions-uniformborder): {{
    TableBorderOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-globaltableborderoptions-properties"></a>

`SideSpecificBorder`  <a name="cfn-quicksight-template-globaltableborderoptions-sidespecificborder"></a>
Determines the options for side specific border.
*Required*: No
*Type*: [TableSideBorderOptions](aws-properties-quicksight-template-tablesideborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UniformBorder`  <a name="cfn-quicksight-template-globaltableborderoptions-uniformborder"></a>
Determines the options for uniform border.
*Required*: No
*Type*: [TableBorderOptions](aws-properties-quicksight-template-tableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
