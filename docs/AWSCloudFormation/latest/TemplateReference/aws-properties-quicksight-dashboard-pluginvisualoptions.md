---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-pluginvisualoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard PluginVisualOptions
<a name="aws-properties-quicksight-dashboard-pluginvisualoptions"></a>

The options and persisted properties for the plugin visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-pluginvisualoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-pluginvisualoptions-syntax.json"></a>

```
{
  "[VisualProperties](#cfn-quicksight-dashboard-pluginvisualoptions-visualproperties)" : {{[ PluginVisualProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-pluginvisualoptions-syntax.yaml"></a>

```
  [VisualProperties](#cfn-quicksight-dashboard-pluginvisualoptions-visualproperties): {{
    - PluginVisualProperty}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-pluginvisualoptions-properties"></a>

`VisualProperties`  <a name="cfn-quicksight-dashboard-pluginvisualoptions-visualproperties"></a>
The persisted properties and their values.
*Required*: No
*Type*: Array of [PluginVisualProperty](aws-properties-quicksight-dashboard-pluginvisualproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
