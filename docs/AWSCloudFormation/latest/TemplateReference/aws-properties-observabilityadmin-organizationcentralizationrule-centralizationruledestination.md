---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule CentralizationRuleDestination
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination"></a>

Configuration specifying the primary destination for centralized telemetry data.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination-syntax.json"></a>

```
{
  "[Account](#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-account)" : {{String}},
  "[DestinationLogsConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-destinationlogsconfiguration)" : {{DestinationLogsConfiguration}},
  "[DestinationMetricsConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-destinationmetricsconfiguration)" : {{DestinationMetricsConfiguration}},
  "[Region](#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination-syntax.yaml"></a>

```
  [Account](#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-account): {{String}}
  [DestinationLogsConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-destinationlogsconfiguration): {{
    DestinationLogsConfiguration}}
  [DestinationMetricsConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-destinationmetricsconfiguration): {{
    DestinationMetricsConfiguration}}
  [Region](#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-region): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination-properties"></a>

`Account`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-account"></a>
The destination account (within the organization) to which the telemetry data should be centralized.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationLogsConfiguration`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-destinationlogsconfiguration"></a>
Log specific configuration for centralization destination log groups.
*Required*: No
*Type*: [DestinationLogsConfiguration](aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationMetricsConfiguration`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-destinationmetricsconfiguration"></a>
Metric specific configuration for centralization destination metrics.
*Required*: No
*Type*: [DestinationMetricsConfiguration](aws-properties-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-region"></a>
The primary destination region to which telemetry data should be centralized.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
