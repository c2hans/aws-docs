---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule DestinationMetricsConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration"></a>

Configuration for centralization destination metrics, including backup settings.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration-syntax.json"></a>

```
{
  "[BackupConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration-backupconfiguration)" : {{MetricsBackupConfiguration}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration-syntax.yaml"></a>

```
  [BackupConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration-backupconfiguration): {{
    MetricsBackupConfiguration}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration-properties"></a>

`BackupConfiguration`  <a name="cfn-observabilityadmin-organizationcentralizationrule-destinationmetricsconfiguration-backupconfiguration"></a>
Configuration defining the backup region for the metrics backup destination.
*Required*: No
*Type*: [MetricsBackupConfiguration](aws-properties-observabilityadmin-organizationcentralizationrule-metricsbackupconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
