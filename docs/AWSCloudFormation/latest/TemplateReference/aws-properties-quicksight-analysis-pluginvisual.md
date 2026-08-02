---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pluginvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PluginVisual
<a name="aws-properties-quicksight-analysis-pluginvisual"></a>

A flexible visualization type that allows engineers to create new custom charts in Quick Sight.

## Syntax
<a name="aws-properties-quicksight-analysis-pluginvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pluginvisual-syntax.json"></a>

```
{
  "[ChartConfiguration](#cfn-quicksight-analysis-pluginvisual-chartconfiguration)" : {{PluginVisualConfiguration}},
  "[PluginArn](#cfn-quicksight-analysis-pluginvisual-pluginarn)" : {{String}},
  "[Subtitle](#cfn-quicksight-analysis-pluginvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-analysis-pluginvisual-title)" : {{VisualTitleLabelOptions}},
  "[VisualContentAltText](#cfn-quicksight-analysis-pluginvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-analysis-pluginvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pluginvisual-syntax.yaml"></a>

```
  [ChartConfiguration](#cfn-quicksight-analysis-pluginvisual-chartconfiguration): {{
    PluginVisualConfiguration}}
  [PluginArn](#cfn-quicksight-analysis-pluginvisual-pluginarn): {{String}}
  [Subtitle](#cfn-quicksight-analysis-pluginvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-analysis-pluginvisual-title): {{
    VisualTitleLabelOptions}}
  [VisualContentAltText](#cfn-quicksight-analysis-pluginvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-analysis-pluginvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pluginvisual-properties"></a>

`ChartConfiguration`  <a name="cfn-quicksight-analysis-pluginvisual-chartconfiguration"></a>
 A description of the plugin field wells and their persisted properties.
*Required*: No
*Type*: [PluginVisualConfiguration](aws-properties-quicksight-analysis-pluginvisualconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PluginArn`  <a name="cfn-quicksight-analysis-pluginvisual-pluginarn"></a>
The Amazon Resource Name (ARN) that reflects the plugin and version.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-analysis-pluginvisual-subtitle"></a>
Property description not available.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-analysis-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-pluginvisual-title"></a>
Property description not available.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-analysis-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-analysis-pluginvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-analysis-pluginvisual-visualid"></a>
The ID of the visual that you want to use.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
