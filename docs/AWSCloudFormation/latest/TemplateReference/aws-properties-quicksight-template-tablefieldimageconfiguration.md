---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablefieldimageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableFieldImageConfiguration
<a name="aws-properties-quicksight-template-tablefieldimageconfiguration"></a>

The image configuration of a table field URL.

## Syntax
<a name="aws-properties-quicksight-template-tablefieldimageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablefieldimageconfiguration-syntax.json"></a>

```
{
  "[SizingOptions](#cfn-quicksight-template-tablefieldimageconfiguration-sizingoptions)" : {{TableCellImageSizingConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablefieldimageconfiguration-syntax.yaml"></a>

```
  [SizingOptions](#cfn-quicksight-template-tablefieldimageconfiguration-sizingoptions): {{
    TableCellImageSizingConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-tablefieldimageconfiguration-properties"></a>

`SizingOptions`  <a name="cfn-quicksight-template-tablefieldimageconfiguration-sizingoptions"></a>
The sizing options for the table image configuration.
*Required*: No
*Type*: [TableCellImageSizingConfiguration](aws-properties-quicksight-template-tablecellimagesizingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
