---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-jobrun-monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun MonitoringConfiguration
<a name="aws-properties-emrserverless-jobrun-monitoringconfiguration"></a>

The configuration setting for monitoring.

## Syntax
<a name="aws-properties-emrserverless-jobrun-monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-jobrun-monitoringconfiguration-syntax.json"></a>

```
{
  "[ManagedPersistenceMonitoringConfiguration](#cfn-emrserverless-jobrun-monitoringconfiguration-managedpersistencemonitoringconfiguration)" : {{ManagedPersistenceMonitoringConfiguration}},
  "[S3MonitoringConfiguration](#cfn-emrserverless-jobrun-monitoringconfiguration-s3monitoringconfiguration)" : {{S3MonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-emrserverless-jobrun-monitoringconfiguration-syntax.yaml"></a>

```
  [ManagedPersistenceMonitoringConfiguration](#cfn-emrserverless-jobrun-monitoringconfiguration-managedpersistencemonitoringconfiguration): {{
    ManagedPersistenceMonitoringConfiguration}}
  [S3MonitoringConfiguration](#cfn-emrserverless-jobrun-monitoringconfiguration-s3monitoringconfiguration): {{
    S3MonitoringConfiguration}}
```

## Properties
<a name="aws-properties-emrserverless-jobrun-monitoringconfiguration-properties"></a>

`ManagedPersistenceMonitoringConfiguration`  <a name="cfn-emrserverless-jobrun-monitoringconfiguration-managedpersistencemonitoringconfiguration"></a>
The managed log persistence configuration for a job run.
*Required*: No
*Type*: [ManagedPersistenceMonitoringConfiguration](aws-properties-emrserverless-jobrun-managedpersistencemonitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3MonitoringConfiguration`  <a name="cfn-emrserverless-jobrun-monitoringconfiguration-s3monitoringconfiguration"></a>
The Amazon S3 configuration for monitoring log publishing.
*Required*: No
*Type*: [S3MonitoringConfiguration](aws-properties-emrserverless-jobrun-s3monitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
