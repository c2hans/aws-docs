---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pluginvisualitemslimitconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PluginVisualItemsLimitConfiguration
<a name="aws-properties-quicksight-analysis-pluginvisualitemslimitconfiguration"></a>

A query limits configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-pluginvisualitemslimitconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pluginvisualitemslimitconfiguration-syntax.json"></a>

```
{
  "[ItemsLimit](#cfn-quicksight-analysis-pluginvisualitemslimitconfiguration-itemslimit)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pluginvisualitemslimitconfiguration-syntax.yaml"></a>

```
  [ItemsLimit](#cfn-quicksight-analysis-pluginvisualitemslimitconfiguration-itemslimit): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pluginvisualitemslimitconfiguration-properties"></a>

`ItemsLimit`  <a name="cfn-quicksight-analysis-pluginvisualitemslimitconfiguration-itemslimit"></a>
Determines how many values are be fetched at once.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
