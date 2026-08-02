---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-kpiconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard KPIConfiguration
<a name="aws-properties-quicksight-dashboard-kpiconfiguration"></a>

The configuration of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-kpiconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-kpiconfiguration-syntax.json"></a>

```
{
  "[FieldWells](#cfn-quicksight-dashboard-kpiconfiguration-fieldwells)" : {{KPIFieldWells}},
  "[Interactions](#cfn-quicksight-dashboard-kpiconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[KPIOptions](#cfn-quicksight-dashboard-kpiconfiguration-kpioptions)" : {{KPIOptions}},
  "[SortConfiguration](#cfn-quicksight-dashboard-kpiconfiguration-sortconfiguration)" : {{KPISortConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-kpiconfiguration-syntax.yaml"></a>

```
  [FieldWells](#cfn-quicksight-dashboard-kpiconfiguration-fieldwells): {{
    KPIFieldWells}}
  [Interactions](#cfn-quicksight-dashboard-kpiconfiguration-interactions): {{
    VisualInteractionOptions}}
  [KPIOptions](#cfn-quicksight-dashboard-kpiconfiguration-kpioptions): {{
    KPIOptions}}
  [SortConfiguration](#cfn-quicksight-dashboard-kpiconfiguration-sortconfiguration): {{
    KPISortConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-kpiconfiguration-properties"></a>

`FieldWells`  <a name="cfn-quicksight-dashboard-kpiconfiguration-fieldwells"></a>
The field well configuration of a KPI visual.
*Required*: No
*Type*: [KPIFieldWells](aws-properties-quicksight-dashboard-kpifieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-dashboard-kpiconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-dashboard-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KPIOptions`  <a name="cfn-quicksight-dashboard-kpiconfiguration-kpioptions"></a>
The options that determine the presentation of a KPI visual.
*Required*: No
*Type*: [KPIOptions](aws-properties-quicksight-dashboard-kpioptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-dashboard-kpiconfiguration-sortconfiguration"></a>
The sort configuration of a KPI visual.
*Required*: No
*Type*: [KPISortConfiguration](aws-properties-quicksight-dashboard-kpisortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
