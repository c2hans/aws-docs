---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-sourcetable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet SourceTable
<a name="aws-properties-quicksight-dataset-sourcetable"></a>

A source table that provides initial data from either a physical table or parent dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-sourcetable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-sourcetable-syntax.json"></a>

```
{
  "[DataSet](#cfn-quicksight-dataset-sourcetable-dataset)" : {{ParentDataSet}},
  "[PhysicalTableId](#cfn-quicksight-dataset-sourcetable-physicaltableid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-sourcetable-syntax.yaml"></a>

```
  [DataSet](#cfn-quicksight-dataset-sourcetable-dataset): {{
    ParentDataSet}}
  [PhysicalTableId](#cfn-quicksight-dataset-sourcetable-physicaltableid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-sourcetable-properties"></a>

`DataSet`  <a name="cfn-quicksight-dataset-sourcetable-dataset"></a>
A parent dataset that serves as the data source instead of a physical table.
*Required*: No
*Type*: [ParentDataSet](aws-properties-quicksight-dataset-parentdataset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhysicalTableId`  <a name="cfn-quicksight-dataset-sourcetable-physicaltableid"></a>
The identifier of the physical table that serves as the data source.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-zA-Z-]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
