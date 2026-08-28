---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-tablestyletarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TableStyleTarget
<a name="aws-properties-quicksight-dashboard-tablestyletarget"></a>

The table style target.

## Syntax
<a name="aws-properties-quicksight-dashboard-tablestyletarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-tablestyletarget-syntax.json"></a>

```
{
  "[CellType](#cfn-quicksight-dashboard-tablestyletarget-celltype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-tablestyletarget-syntax.yaml"></a>

```
  [CellType](#cfn-quicksight-dashboard-tablestyletarget-celltype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-tablestyletarget-properties"></a>

`CellType`  <a name="cfn-quicksight-dashboard-tablestyletarget-celltype"></a>
The cell type of the table style target.
*Required*: Yes
*Type*: String
*Allowed values*: `TOTAL | METRIC_HEADER | VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
