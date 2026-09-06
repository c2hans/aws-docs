---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule MetricsBackupConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration"></a>

Configuration for backing up centralized metrics data to a secondary region.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration-syntax.json"></a>

```
{
  "[Region](#cfn-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration-syntax.yaml"></a>

```
  [Region](#cfn-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration-region): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration-properties"></a>

`Region`  <a name="cfn-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration-region"></a>
Metrics specific backup destination region within the primary destination account to which metrics data should be centralized.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
