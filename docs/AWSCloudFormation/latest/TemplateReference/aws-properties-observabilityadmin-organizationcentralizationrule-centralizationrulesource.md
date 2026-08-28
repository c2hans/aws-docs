---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule CentralizationRuleSource
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource"></a>

Configuration specifying the source of telemetry data to be centralized.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource-syntax.json"></a>

```
{
  "[Regions](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-regions)" : {{[ String, ... ]}},
  "[Scope](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-scope)" : {{String}},
  "[SourceLogsConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-sourcelogsconfiguration)" : {{SourceLogsConfiguration}},
  "[SourceMetricsConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-sourcemetricsconfiguration)" : {{SourceMetricsConfiguration}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource-syntax.yaml"></a>

```
  [Regions](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-regions): {{
    - String}}
  [Scope](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-scope): {{String}}
  [SourceLogsConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-sourcelogsconfiguration): {{
    SourceLogsConfiguration}}
  [SourceMetricsConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-sourcemetricsconfiguration): {{
    SourceMetricsConfiguration}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource-properties"></a>

`Regions`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-regions"></a>
The list of source regions from which telemetry data should be centralized.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-scope"></a>
The organizational scope from which telemetry data should be centralized, specified using organization id, accounts or organizational unit ids.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLogsConfiguration`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-sourcelogsconfiguration"></a>
Log specific configuration for centralization source log groups.
*Required*: No
*Type*: [SourceLogsConfiguration](aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceMetricsConfiguration`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-sourcemetricsconfiguration"></a>
Metric specific configuration for centralization source metrics.
*Required*: No
*Type*: [SourceMetricsConfiguration](aws-properties-observabilityadmin-organizationcentralizationrule-sourcemetricsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
