---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application MonitoringConfiguration
<a name="aws-properties-emrserverless-application-monitoringconfiguration"></a>

The configuration setting for monitoring logs.

## Syntax
<a name="aws-properties-emrserverless-application-monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-monitoringconfiguration-syntax.json"></a>

```
{
  "[CloudWatchLoggingConfiguration](#cfn-emrserverless-application-monitoringconfiguration-cloudwatchloggingconfiguration)" : {{CloudWatchLoggingConfiguration}},
  "[ManagedPersistenceMonitoringConfiguration](#cfn-emrserverless-application-monitoringconfiguration-managedpersistencemonitoringconfiguration)" : {{ManagedPersistenceMonitoringConfiguration}},
  "[PrometheusMonitoringConfiguration](#cfn-emrserverless-application-monitoringconfiguration-prometheusmonitoringconfiguration)" : {{PrometheusMonitoringConfiguration}},
  "[S3MonitoringConfiguration](#cfn-emrserverless-application-monitoringconfiguration-s3monitoringconfiguration)" : {{S3MonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-monitoringconfiguration-syntax.yaml"></a>

```
  [CloudWatchLoggingConfiguration](#cfn-emrserverless-application-monitoringconfiguration-cloudwatchloggingconfiguration): {{
    CloudWatchLoggingConfiguration}}
  [ManagedPersistenceMonitoringConfiguration](#cfn-emrserverless-application-monitoringconfiguration-managedpersistencemonitoringconfiguration): {{
    ManagedPersistenceMonitoringConfiguration}}
  [PrometheusMonitoringConfiguration](#cfn-emrserverless-application-monitoringconfiguration-prometheusmonitoringconfiguration): {{
    PrometheusMonitoringConfiguration}}
  [S3MonitoringConfiguration](#cfn-emrserverless-application-monitoringconfiguration-s3monitoringconfiguration): {{
    S3MonitoringConfiguration}}
```

## Properties
<a name="aws-properties-emrserverless-application-monitoringconfiguration-properties"></a>

`CloudWatchLoggingConfiguration`  <a name="cfn-emrserverless-application-monitoringconfiguration-cloudwatchloggingconfiguration"></a>
The Amazon CloudWatch configuration for monitoring logs. You can configure your jobs to send log information to CloudWatch.
*Required*: No
*Type*: [CloudWatchLoggingConfiguration](aws-properties-emrserverless-application-cloudwatchloggingconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ManagedPersistenceMonitoringConfiguration`  <a name="cfn-emrserverless-application-monitoringconfiguration-managedpersistencemonitoringconfiguration"></a>
The managed log persistence configuration for a job run.
*Required*: No
*Type*: [ManagedPersistenceMonitoringConfiguration](aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PrometheusMonitoringConfiguration`  <a name="cfn-emrserverless-application-monitoringconfiguration-prometheusmonitoringconfiguration"></a>
The monitoring configuration object you can configure to send metrics to Amazon Managed Service for Prometheus for a job run.
*Required*: No
*Type*: [PrometheusMonitoringConfiguration](aws-properties-emrserverless-application-prometheusmonitoringconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`S3MonitoringConfiguration`  <a name="cfn-emrserverless-application-monitoringconfiguration-s3monitoringconfiguration"></a>
The Amazon S3 configuration for monitoring log publishing.
*Required*: No
*Type*: [S3MonitoringConfiguration](aws-properties-emrserverless-application-s3monitoringconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
