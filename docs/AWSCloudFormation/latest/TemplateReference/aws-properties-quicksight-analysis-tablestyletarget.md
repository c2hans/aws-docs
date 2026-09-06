---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-tablestyletarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TableStyleTarget
<a name="aws-properties-quicksight-analysis-tablestyletarget"></a>

The table style target.

## Syntax
<a name="aws-properties-quicksight-analysis-tablestyletarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-tablestyletarget-syntax.json"></a>

```
{
  "[CellType](#cfn-quicksight-analysis-tablestyletarget-celltype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-tablestyletarget-syntax.yaml"></a>

```
  [CellType](#cfn-quicksight-analysis-tablestyletarget-celltype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-tablestyletarget-properties"></a>

`CellType`  <a name="cfn-quicksight-analysis-tablestyletarget-celltype"></a>
The cell type of the table style target.
*Required*: Yes
*Type*: String
*Allowed values*: `TOTAL | METRIC_HEADER | VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
