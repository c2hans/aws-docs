---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-insightconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard InsightConfiguration
<a name="aws-properties-quicksight-dashboard-insightconfiguration"></a>

The configuration of an insight visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-insightconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-insightconfiguration-syntax.json"></a>

```
{
  "[Computations](#cfn-quicksight-dashboard-insightconfiguration-computations)" : {{[ Computation, ... ]}},
  "[CustomNarrative](#cfn-quicksight-dashboard-insightconfiguration-customnarrative)" : {{CustomNarrativeOptions}},
  "[Interactions](#cfn-quicksight-dashboard-insightconfiguration-interactions)" : {{VisualInteractionOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-insightconfiguration-syntax.yaml"></a>

```
  [Computations](#cfn-quicksight-dashboard-insightconfiguration-computations): {{
    - Computation}}
  [CustomNarrative](#cfn-quicksight-dashboard-insightconfiguration-customnarrative): {{
    CustomNarrativeOptions}}
  [Interactions](#cfn-quicksight-dashboard-insightconfiguration-interactions): {{
    VisualInteractionOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-insightconfiguration-properties"></a>

`Computations`  <a name="cfn-quicksight-dashboard-insightconfiguration-computations"></a>
The computations configurations of the insight visual
*Required*: No
*Type*: Array of [Computation](aws-properties-quicksight-dashboard-computation.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomNarrative`  <a name="cfn-quicksight-dashboard-insightconfiguration-customnarrative"></a>
The custom narrative of the insight visual.
*Required*: No
*Type*: [CustomNarrativeOptions](aws-properties-quicksight-dashboard-customnarrativeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-dashboard-insightconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-dashboard-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
