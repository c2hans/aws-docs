---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-incrementalrefresh.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet IncrementalRefresh
<a name="aws-properties-quicksight-dataset-incrementalrefresh"></a>

The incremental refresh configuration for a dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-incrementalrefresh-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-incrementalrefresh-syntax.json"></a>

```
{
  "[LookbackWindow](#cfn-quicksight-dataset-incrementalrefresh-lookbackwindow)" : {{LookbackWindow}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-incrementalrefresh-syntax.yaml"></a>

```
  [LookbackWindow](#cfn-quicksight-dataset-incrementalrefresh-lookbackwindow): {{
    LookbackWindow}}
```

## Properties
<a name="aws-properties-quicksight-dataset-incrementalrefresh-properties"></a>

`LookbackWindow`  <a name="cfn-quicksight-dataset-incrementalrefresh-lookbackwindow"></a>
The lookback window setup for an incremental refresh configuration.
*Required*: Yes
*Type*: [LookbackWindow](aws-properties-quicksight-dataset-lookbackwindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
