---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-defaultfiltercontrolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DefaultFilterControlConfiguration
<a name="aws-properties-quicksight-dashboard-defaultfiltercontrolconfiguration"></a>

The default configuration for all dependent controls of the filter.

## Syntax
<a name="aws-properties-quicksight-dashboard-defaultfiltercontrolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-defaultfiltercontrolconfiguration-syntax.json"></a>

```
{
  "[ControlOptions](#cfn-quicksight-dashboard-defaultfiltercontrolconfiguration-controloptions)" : {{DefaultFilterControlOptions}},
  "[Title](#cfn-quicksight-dashboard-defaultfiltercontrolconfiguration-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-defaultfiltercontrolconfiguration-syntax.yaml"></a>

```
  [ControlOptions](#cfn-quicksight-dashboard-defaultfiltercontrolconfiguration-controloptions): {{
    DefaultFilterControlOptions}}
  [Title](#cfn-quicksight-dashboard-defaultfiltercontrolconfiguration-title): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-defaultfiltercontrolconfiguration-properties"></a>

`ControlOptions`  <a name="cfn-quicksight-dashboard-defaultfiltercontrolconfiguration-controloptions"></a>
The control option for the `DefaultFilterControlConfiguration`.
*Required*: Yes
*Type*: [DefaultFilterControlOptions](aws-properties-quicksight-dashboard-defaultfiltercontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-dashboard-defaultfiltercontrolconfiguration-title"></a>
The title of the `DefaultFilterControlConfiguration`. This title is shared by all controls that are tied to this filter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
