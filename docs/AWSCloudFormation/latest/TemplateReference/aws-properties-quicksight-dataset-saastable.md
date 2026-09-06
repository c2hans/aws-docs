---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-saastable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet SaaSTable
<a name="aws-properties-quicksight-dataset-saastable"></a>

A table from a Software-as-a-Service (SaaS) data source, including connection details and column definitions.

## Syntax
<a name="aws-properties-quicksight-dataset-saastable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-saastable-syntax.json"></a>

```
{
  "[DataSourceArn](#cfn-quicksight-dataset-saastable-datasourcearn)" : {{String}},
  "[InputColumns](#cfn-quicksight-dataset-saastable-inputcolumns)" : {{[ InputColumn, ... ]}},
  "[TablePath](#cfn-quicksight-dataset-saastable-tablepath)" : {{[ TablePathElement, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-saastable-syntax.yaml"></a>

```
  [DataSourceArn](#cfn-quicksight-dataset-saastable-datasourcearn): {{String}}
  [InputColumns](#cfn-quicksight-dataset-saastable-inputcolumns): {{
    - InputColumn}}
  [TablePath](#cfn-quicksight-dataset-saastable-tablepath): {{
    - TablePathElement}}
```

## Properties
<a name="aws-properties-quicksight-dataset-saastable-properties"></a>

`DataSourceArn`  <a name="cfn-quicksight-dataset-saastable-datasourcearn"></a>
The Amazon Resource Name (ARN) of the SaaS data source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputColumns`  <a name="cfn-quicksight-dataset-saastable-inputcolumns"></a>
The list of input columns available from the SaaS table.
*Required*: Yes
*Type*: Array of [InputColumn](aws-properties-quicksight-dataset-inputcolumn.md)
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TablePath`  <a name="cfn-quicksight-dataset-saastable-tablepath"></a>
The hierarchical path to the table within the SaaS data source.
*Required*: Yes
*Type*: Array of [TablePathElement](aws-properties-quicksight-dataset-tablepathelement.md)
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
