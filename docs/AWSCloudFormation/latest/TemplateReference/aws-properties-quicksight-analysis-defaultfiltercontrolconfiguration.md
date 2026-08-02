---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DefaultFilterControlConfiguration
<a name="aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration"></a>

The default configuration for all dependent controls of the filter.

## Syntax
<a name="aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration-syntax.json"></a>

```
{
  "[ControlOptions](#cfn-quicksight-analysis-defaultfiltercontrolconfiguration-controloptions)" : {{DefaultFilterControlOptions}},
  "[Title](#cfn-quicksight-analysis-defaultfiltercontrolconfiguration-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration-syntax.yaml"></a>

```
  [ControlOptions](#cfn-quicksight-analysis-defaultfiltercontrolconfiguration-controloptions): {{
    DefaultFilterControlOptions}}
  [Title](#cfn-quicksight-analysis-defaultfiltercontrolconfiguration-title): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration-properties"></a>

`ControlOptions`  <a name="cfn-quicksight-analysis-defaultfiltercontrolconfiguration-controloptions"></a>
The control option for the `DefaultFilterControlConfiguration`.
*Required*: Yes
*Type*: [DefaultFilterControlOptions](aws-properties-quicksight-analysis-defaultfiltercontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-defaultfiltercontrolconfiguration-title"></a>
The title of the `DefaultFilterControlConfiguration`. This title is shared by all controls that are tied to this filter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
