---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-rollingdateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard RollingDateConfiguration
<a name="aws-properties-quicksight-dashboard-rollingdateconfiguration"></a>

The rolling date configuration of a date time filter.

## Syntax
<a name="aws-properties-quicksight-dashboard-rollingdateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-rollingdateconfiguration-syntax.json"></a>

```
{
  "[DataSetIdentifier](#cfn-quicksight-dashboard-rollingdateconfiguration-datasetidentifier)" : {{String}},
  "[Expression](#cfn-quicksight-dashboard-rollingdateconfiguration-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-rollingdateconfiguration-syntax.yaml"></a>

```
  [DataSetIdentifier](#cfn-quicksight-dashboard-rollingdateconfiguration-datasetidentifier): {{String}}
  [Expression](#cfn-quicksight-dashboard-rollingdateconfiguration-expression): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-rollingdateconfiguration-properties"></a>

`DataSetIdentifier`  <a name="cfn-quicksight-dashboard-rollingdateconfiguration-datasetidentifier"></a>
The data set that is used in the rolling date configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-quicksight-dashboard-rollingdateconfiguration-expression"></a>
The expression of the rolling date configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
