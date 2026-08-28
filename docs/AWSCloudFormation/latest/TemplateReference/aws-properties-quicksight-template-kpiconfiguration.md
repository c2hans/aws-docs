---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-kpiconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template KPIConfiguration
<a name="aws-properties-quicksight-template-kpiconfiguration"></a>

The configuration of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-template-kpiconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-kpiconfiguration-syntax.json"></a>

```
{
  "[FieldWells](#cfn-quicksight-template-kpiconfiguration-fieldwells)" : {{KPIFieldWells}},
  "[Interactions](#cfn-quicksight-template-kpiconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[KPIOptions](#cfn-quicksight-template-kpiconfiguration-kpioptions)" : {{KPIOptions}},
  "[SortConfiguration](#cfn-quicksight-template-kpiconfiguration-sortconfiguration)" : {{KPISortConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-kpiconfiguration-syntax.yaml"></a>

```
  [FieldWells](#cfn-quicksight-template-kpiconfiguration-fieldwells): {{
    KPIFieldWells}}
  [Interactions](#cfn-quicksight-template-kpiconfiguration-interactions): {{
    VisualInteractionOptions}}
  [KPIOptions](#cfn-quicksight-template-kpiconfiguration-kpioptions): {{
    KPIOptions}}
  [SortConfiguration](#cfn-quicksight-template-kpiconfiguration-sortconfiguration): {{
    KPISortConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-kpiconfiguration-properties"></a>

`FieldWells`  <a name="cfn-quicksight-template-kpiconfiguration-fieldwells"></a>
The field well configuration of a KPI visual.
*Required*: No
*Type*: [KPIFieldWells](aws-properties-quicksight-template-kpifieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-template-kpiconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-template-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KPIOptions`  <a name="cfn-quicksight-template-kpiconfiguration-kpioptions"></a>
The options that determine the presentation of a KPI visual.
*Required*: No
*Type*: [KPIOptions](aws-properties-quicksight-template-kpioptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-template-kpiconfiguration-sortconfiguration"></a>
The sort configuration of a KPI visual.
*Required*: No
*Type*: [KPISortConfiguration](aws-properties-quicksight-template-kpisortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
