---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetrefreshproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetRefreshProperties
<a name="aws-properties-quicksight-dataset-datasetrefreshproperties"></a>

The refresh properties of a dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetrefreshproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetrefreshproperties-syntax.json"></a>

```
{
  "[FailureConfiguration](#cfn-quicksight-dataset-datasetrefreshproperties-failureconfiguration)" : {{RefreshFailureConfiguration}},
  "[RefreshConfiguration](#cfn-quicksight-dataset-datasetrefreshproperties-refreshconfiguration)" : {{RefreshConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetrefreshproperties-syntax.yaml"></a>

```
  [FailureConfiguration](#cfn-quicksight-dataset-datasetrefreshproperties-failureconfiguration): {{
    RefreshFailureConfiguration}}
  [RefreshConfiguration](#cfn-quicksight-dataset-datasetrefreshproperties-refreshconfiguration): {{
    RefreshConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetrefreshproperties-properties"></a>

`FailureConfiguration`  <a name="cfn-quicksight-dataset-datasetrefreshproperties-failureconfiguration"></a>
The failure configuration for a dataset.
*Required*: No
*Type*: [RefreshFailureConfiguration](aws-properties-quicksight-dataset-refreshfailureconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshConfiguration`  <a name="cfn-quicksight-dataset-datasetrefreshproperties-refreshconfiguration"></a>
The refresh configuration for a dataset.
*Required*: No
*Type*: [RefreshConfiguration](aws-properties-quicksight-dataset-refreshconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
