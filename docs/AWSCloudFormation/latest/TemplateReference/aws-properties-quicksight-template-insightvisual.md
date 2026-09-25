---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-insightvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template InsightVisual
<a name="aws-properties-quicksight-template-insightvisual"></a>

An insight visual.

For more information, see [Working with insights](https://docs.aws.amazon.com/quicksight/latest/user/computational-insights.html) in the *Amazon Quick Suite User Guide*.

## Syntax
<a name="aws-properties-quicksight-template-insightvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-insightvisual-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-template-insightvisual-actions)" : {{[ VisualCustomAction, ... ]}},
  "[DataSetIdentifier](#cfn-quicksight-template-insightvisual-datasetidentifier)" : {{String}},
  "[InsightConfiguration](#cfn-quicksight-template-insightvisual-insightconfiguration)" : {{InsightConfiguration}},
  "[Subtitle](#cfn-quicksight-template-insightvisual-subtitle)" : {{VisualSubtitleLabelOptions}},
  "[Title](#cfn-quicksight-template-insightvisual-title)" : {{VisualTitleLabelOptions}},
  "[TopicIdentifier](#cfn-quicksight-template-insightvisual-topicidentifier)" : {{String}},
  "[VisualContentAltText](#cfn-quicksight-template-insightvisual-visualcontentalttext)" : {{String}},
  "[VisualId](#cfn-quicksight-template-insightvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-insightvisual-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-template-insightvisual-actions): {{
    - VisualCustomAction}}
  [DataSetIdentifier](#cfn-quicksight-template-insightvisual-datasetidentifier): {{String}}
  [InsightConfiguration](#cfn-quicksight-template-insightvisual-insightconfiguration): {{
    InsightConfiguration}}
  [Subtitle](#cfn-quicksight-template-insightvisual-subtitle): {{
    VisualSubtitleLabelOptions}}
  [Title](#cfn-quicksight-template-insightvisual-title): {{
    VisualTitleLabelOptions}}
  [TopicIdentifier](#cfn-quicksight-template-insightvisual-topicidentifier): {{String}}
  [VisualContentAltText](#cfn-quicksight-template-insightvisual-visualcontentalttext): {{String}}
  [VisualId](#cfn-quicksight-template-insightvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-insightvisual-properties"></a>

`Actions`  <a name="cfn-quicksight-template-insightvisual-actions"></a>
The list of custom actions that are configured for a visual.
*Required*: No
*Type*: Array of [VisualCustomAction](aws-properties-quicksight-template-visualcustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifier`  <a name="cfn-quicksight-template-insightvisual-datasetidentifier"></a>
The dataset that is used in the insight visual.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InsightConfiguration`  <a name="cfn-quicksight-template-insightvisual-insightconfiguration"></a>
The configuration of an insight visual.
*Required*: No
*Type*: [InsightConfiguration](aws-properties-quicksight-template-insightconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-quicksight-template-insightvisual-subtitle"></a>
The subtitle that is displayed on the visual.
*Required*: No
*Type*: [VisualSubtitleLabelOptions](aws-properties-quicksight-template-visualsubtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-insightvisual-title"></a>
The title that is displayed on the visual.
*Required*: No
*Type*: [VisualTitleLabelOptions](aws-properties-quicksight-template-visualtitlelabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicIdentifier`  <a name="cfn-quicksight-template-insightvisual-topicidentifier"></a>
The topic that is used in the insight visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualContentAltText`  <a name="cfn-quicksight-template-insightvisual-visualcontentalttext"></a>
The alt text for the visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-template-insightvisual-visualid"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
