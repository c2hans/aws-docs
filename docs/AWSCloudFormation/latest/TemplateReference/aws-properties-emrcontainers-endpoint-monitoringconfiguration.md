---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::Endpoint MonitoringConfiguration
<a name="aws-properties-emrcontainers-endpoint-monitoringconfiguration"></a>

Configuration setting for monitoring.

## Syntax
<a name="aws-properties-emrcontainers-endpoint-monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-endpoint-monitoringconfiguration-syntax.json"></a>

```
{
  "[CloudWatchMonitoringConfiguration](#cfn-emrcontainers-endpoint-monitoringconfiguration-cloudwatchmonitoringconfiguration)" : {{CloudWatchMonitoringConfiguration}},
  "[ContainerLogRotationConfiguration](#cfn-emrcontainers-endpoint-monitoringconfiguration-containerlogrotationconfiguration)" : {{ContainerLogRotationConfiguration}},
  "[PersistentAppUI](#cfn-emrcontainers-endpoint-monitoringconfiguration-persistentappui)" : {{String}},
  "[S3MonitoringConfiguration](#cfn-emrcontainers-endpoint-monitoringconfiguration-s3monitoringconfiguration)" : {{S3MonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-endpoint-monitoringconfiguration-syntax.yaml"></a>

```
  [CloudWatchMonitoringConfiguration](#cfn-emrcontainers-endpoint-monitoringconfiguration-cloudwatchmonitoringconfiguration): {{
    CloudWatchMonitoringConfiguration}}
  [ContainerLogRotationConfiguration](#cfn-emrcontainers-endpoint-monitoringconfiguration-containerlogrotationconfiguration): {{
    ContainerLogRotationConfiguration}}
  [PersistentAppUI](#cfn-emrcontainers-endpoint-monitoringconfiguration-persistentappui): {{String}}
  [S3MonitoringConfiguration](#cfn-emrcontainers-endpoint-monitoringconfiguration-s3monitoringconfiguration): {{
    S3MonitoringConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-endpoint-monitoringconfiguration-properties"></a>

`CloudWatchMonitoringConfiguration`  <a name="cfn-emrcontainers-endpoint-monitoringconfiguration-cloudwatchmonitoringconfiguration"></a>
Monitoring configurations for CloudWatch.
*Required*: No
*Type*: [CloudWatchMonitoringConfiguration](aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerLogRotationConfiguration`  <a name="cfn-emrcontainers-endpoint-monitoringconfiguration-containerlogrotationconfiguration"></a>
Enable or disable container log rotation.
*Required*: No
*Type*: [ContainerLogRotationConfiguration](aws-properties-emrcontainers-endpoint-containerlogrotationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PersistentAppUI`  <a name="cfn-emrcontainers-endpoint-monitoringconfiguration-persistentappui"></a>
Monitoring configurations for the persistent application UI.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3MonitoringConfiguration`  <a name="cfn-emrcontainers-endpoint-monitoringconfiguration-s3monitoringconfiguration"></a>
Amazon S3 configuration for monitoring log publishing.
*Required*: No
*Type*: [S3MonitoringConfiguration](aws-properties-emrcontainers-endpoint-s3monitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
