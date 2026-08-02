---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-parentdataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet ParentDataSet
<a name="aws-properties-quicksight-dataset-parentdataset"></a>

References a parent dataset that serves as a data source, including its columns and metadata.

## Syntax
<a name="aws-properties-quicksight-dataset-parentdataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-parentdataset-syntax.json"></a>

```
{
  "[DataSetArn](#cfn-quicksight-dataset-parentdataset-datasetarn)" : {{String}},
  "[InputColumns](#cfn-quicksight-dataset-parentdataset-inputcolumns)" : {{[ InputColumn, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-parentdataset-syntax.yaml"></a>

```
  [DataSetArn](#cfn-quicksight-dataset-parentdataset-datasetarn): {{String}}
  [InputColumns](#cfn-quicksight-dataset-parentdataset-inputcolumns): {{
    - InputColumn}}
```

## Properties
<a name="aws-properties-quicksight-dataset-parentdataset-properties"></a>

`DataSetArn`  <a name="cfn-quicksight-dataset-parentdataset-datasetarn"></a>
The Amazon Resource Name (ARN) of the parent dataset.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputColumns`  <a name="cfn-quicksight-dataset-parentdataset-inputcolumns"></a>
The list of input columns available from the parent dataset.
*Required*: Yes
*Type*: Array of [InputColumn](aws-properties-quicksight-dataset-inputcolumn.md)
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
