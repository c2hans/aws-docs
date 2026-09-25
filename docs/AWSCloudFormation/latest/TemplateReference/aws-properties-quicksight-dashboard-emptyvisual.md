---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-emptyvisual.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard EmptyVisual
<a name="aws-properties-quicksight-dashboard-emptyvisual"></a>

An empty visual.

Empty visuals are used in layouts but have not been configured to show any data. A new visual created in the Quick Sight console is considered an `EmptyVisual` until a visual type is selected.

## Syntax
<a name="aws-properties-quicksight-dashboard-emptyvisual-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-emptyvisual-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-dashboard-emptyvisual-actions)" : {{[ VisualCustomAction, ... ]}},
  "[DataSetIdentifier](#cfn-quicksight-dashboard-emptyvisual-datasetidentifier)" : {{String}},
  "[TopicIdentifier](#cfn-quicksight-dashboard-emptyvisual-topicidentifier)" : {{String}},
  "[VisualId](#cfn-quicksight-dashboard-emptyvisual-visualid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-emptyvisual-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-dashboard-emptyvisual-actions): {{
    - VisualCustomAction}}
  [DataSetIdentifier](#cfn-quicksight-dashboard-emptyvisual-datasetidentifier): {{String}}
  [TopicIdentifier](#cfn-quicksight-dashboard-emptyvisual-topicidentifier): {{String}}
  [VisualId](#cfn-quicksight-dashboard-emptyvisual-visualid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-emptyvisual-properties"></a>

`Actions`  <a name="cfn-quicksight-dashboard-emptyvisual-actions"></a>
The list of custom actions that are configured for a visual.
*Required*: No
*Type*: Array of [VisualCustomAction](aws-properties-quicksight-dashboard-visualcustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifier`  <a name="cfn-quicksight-dashboard-emptyvisual-datasetidentifier"></a>
The data set that is used in the empty visual. Every visual requires a dataset or a topic to render.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicIdentifier`  <a name="cfn-quicksight-dashboard-emptyvisual-topicidentifier"></a>
The topic that is used in the empty visual. Every visual requires a dataset or a topic to render.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualId`  <a name="cfn-quicksight-dashboard-emptyvisual-visualid"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
