---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-reportconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan ReportConfiguration
<a name="aws-properties-arcregionswitch-plan-reportconfiguration"></a>

Configuration for automatic report generation for plan executions. When configured, Region switch automatically generates a report after each plan execution that includes execution events, plan configuration, and CloudWatch alarm states.

## Syntax
<a name="aws-properties-arcregionswitch-plan-reportconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-reportconfiguration-syntax.json"></a>

```
{
  "[ReportOutput](#cfn-arcregionswitch-plan-reportconfiguration-reportoutput)" : {{[ ReportOutputConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-reportconfiguration-syntax.yaml"></a>

```
  [ReportOutput](#cfn-arcregionswitch-plan-reportconfiguration-reportoutput): {{
    - ReportOutputConfiguration}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-reportconfiguration-properties"></a>

`ReportOutput`  <a name="cfn-arcregionswitch-plan-reportconfiguration-reportoutput"></a>
The output configuration for the report.
*Required*: No
*Type*: Array of [ReportOutputConfiguration](aws-properties-arcregionswitch-plan-reportoutputconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
