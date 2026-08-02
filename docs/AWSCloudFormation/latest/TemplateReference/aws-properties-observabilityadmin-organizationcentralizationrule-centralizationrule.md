---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule CentralizationRule
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule"></a>

Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule-syntax.json"></a>

```
{
  "[Destination](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-destination)" : {{CentralizationRuleDestination}},
  "[Source](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-source)" : {{CentralizationRuleSource}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule-syntax.yaml"></a>

```
  [Destination](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-destination): {{
    CentralizationRuleDestination}}
  [Source](#cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-source): {{
    CentralizationRuleSource}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule-properties"></a>

`Destination`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-destination"></a>
Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.
*Required*: Yes
*Type*: [CentralizationRuleDestination](aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-source"></a>
Configuration determining the source of the telemetry data to be centralized.
*Required*: Yes
*Type*: [CentralizationRuleSource](aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
