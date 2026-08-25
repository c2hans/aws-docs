---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun MonitoringConfiguration
<a name="aws-properties-emrcontainers-jobrun-monitoringconfiguration"></a>

Configuration setting for monitoring.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-monitoringconfiguration-syntax.json"></a>

```
{
  "[CloudWatchMonitoringConfiguration](#cfn-emrcontainers-jobrun-monitoringconfiguration-cloudwatchmonitoringconfiguration)" : {{CloudWatchMonitoringConfiguration}},
  "[ContainerLogRotationConfiguration](#cfn-emrcontainers-jobrun-monitoringconfiguration-containerlogrotationconfiguration)" : {{ContainerLogRotationConfiguration}},
  "[ManagedLogs](#cfn-emrcontainers-jobrun-monitoringconfiguration-managedlogs)" : {{ManagedLogs}},
  "[PersistentAppUI](#cfn-emrcontainers-jobrun-monitoringconfiguration-persistentappui)" : {{String}},
  "[S3MonitoringConfiguration](#cfn-emrcontainers-jobrun-monitoringconfiguration-s3monitoringconfiguration)" : {{S3MonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-monitoringconfiguration-syntax.yaml"></a>

```
  [CloudWatchMonitoringConfiguration](#cfn-emrcontainers-jobrun-monitoringconfiguration-cloudwatchmonitoringconfiguration): {{
    CloudWatchMonitoringConfiguration}}
  [ContainerLogRotationConfiguration](#cfn-emrcontainers-jobrun-monitoringconfiguration-containerlogrotationconfiguration): {{
    ContainerLogRotationConfiguration}}
  [ManagedLogs](#cfn-emrcontainers-jobrun-monitoringconfiguration-managedlogs): {{
    ManagedLogs}}
  [PersistentAppUI](#cfn-emrcontainers-jobrun-monitoringconfiguration-persistentappui): {{String}}
  [S3MonitoringConfiguration](#cfn-emrcontainers-jobrun-monitoringconfiguration-s3monitoringconfiguration): {{
    S3MonitoringConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-monitoringconfiguration-properties"></a>

`CloudWatchMonitoringConfiguration`  <a name="cfn-emrcontainers-jobrun-monitoringconfiguration-cloudwatchmonitoringconfiguration"></a>
Monitoring configurations for CloudWatch.
*Required*: No
*Type*: [CloudWatchMonitoringConfiguration](aws-properties-emrcontainers-jobrun-cloudwatchmonitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerLogRotationConfiguration`  <a name="cfn-emrcontainers-jobrun-monitoringconfiguration-containerlogrotationconfiguration"></a>
Enable or disable container log rotation.
*Required*: No
*Type*: [ContainerLogRotationConfiguration](aws-properties-emrcontainers-jobrun-containerlogrotationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManagedLogs`  <a name="cfn-emrcontainers-jobrun-monitoringconfiguration-managedlogs"></a>
The entity that controls configuration for managed logs.
*Required*: No
*Type*: [ManagedLogs](aws-properties-emrcontainers-jobrun-managedlogs.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PersistentAppUI`  <a name="cfn-emrcontainers-jobrun-monitoringconfiguration-persistentappui"></a>
Monitoring configurations for the persistent application UI.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3MonitoringConfiguration`  <a name="cfn-emrcontainers-jobrun-monitoringconfiguration-s3monitoringconfiguration"></a>
Amazon S3 configuration for monitoring log publishing.
*Required*: No
*Type*: [S3MonitoringConfiguration](aws-properties-emrcontainers-jobrun-s3monitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
