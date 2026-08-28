---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-insightconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis InsightConfiguration
<a name="aws-properties-quicksight-analysis-insightconfiguration"></a>

The configuration of an insight visual.

## Syntax
<a name="aws-properties-quicksight-analysis-insightconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-insightconfiguration-syntax.json"></a>

```
{
  "[Computations](#cfn-quicksight-analysis-insightconfiguration-computations)" : {{[ Computation, ... ]}},
  "[CustomNarrative](#cfn-quicksight-analysis-insightconfiguration-customnarrative)" : {{CustomNarrativeOptions}},
  "[Interactions](#cfn-quicksight-analysis-insightconfiguration-interactions)" : {{VisualInteractionOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-insightconfiguration-syntax.yaml"></a>

```
  [Computations](#cfn-quicksight-analysis-insightconfiguration-computations): {{
    - Computation}}
  [CustomNarrative](#cfn-quicksight-analysis-insightconfiguration-customnarrative): {{
    CustomNarrativeOptions}}
  [Interactions](#cfn-quicksight-analysis-insightconfiguration-interactions): {{
    VisualInteractionOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-insightconfiguration-properties"></a>

`Computations`  <a name="cfn-quicksight-analysis-insightconfiguration-computations"></a>
The computations configurations of the insight visual
*Required*: No
*Type*: Array of [Computation](aws-properties-quicksight-analysis-computation.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomNarrative`  <a name="cfn-quicksight-analysis-insightconfiguration-customnarrative"></a>
The custom narrative of the insight visual.
*Required*: No
*Type*: [CustomNarrativeOptions](aws-properties-quicksight-analysis-customnarrativeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-analysis-insightconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-analysis-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
