---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-lookbackwindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet LookbackWindow
<a name="aws-properties-quicksight-dataset-lookbackwindow"></a>

The lookback window setup of an incremental refresh configuration.

## Syntax
<a name="aws-properties-quicksight-dataset-lookbackwindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-lookbackwindow-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-lookbackwindow-columnname)" : {{String}},
  "[Size](#cfn-quicksight-dataset-lookbackwindow-size)" : {{Number}},
  "[SizeUnit](#cfn-quicksight-dataset-lookbackwindow-sizeunit)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-lookbackwindow-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-lookbackwindow-columnname): {{String}}
  [Size](#cfn-quicksight-dataset-lookbackwindow-size): {{Number}}
  [SizeUnit](#cfn-quicksight-dataset-lookbackwindow-sizeunit): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-lookbackwindow-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-lookbackwindow-columnname"></a>
The name of the lookback window column.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Size`  <a name="cfn-quicksight-dataset-lookbackwindow-size"></a>
The lookback window column size.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeUnit`  <a name="cfn-quicksight-dataset-lookbackwindow-sizeunit"></a>
The size unit that is used for the lookback window column. Valid values for this structure are `HOUR`, `DAY`, and `WEEK`.
*Required*: Yes
*Type*: String
*Allowed values*: `HOUR | DAY | WEEK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
