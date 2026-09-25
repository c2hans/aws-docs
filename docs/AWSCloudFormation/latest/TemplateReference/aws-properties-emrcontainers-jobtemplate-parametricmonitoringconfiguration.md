---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobTemplate ParametricMonitoringConfiguration
<a name="aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration"></a>

 Configuration setting for monitoring. This data type allows job template parameters to be specified within.

## Syntax
<a name="aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration-syntax.json"></a>

```
{
  "[CloudWatchMonitoringConfiguration](#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-cloudwatchmonitoringconfiguration)" : {{ParametricCloudWatchMonitoringConfiguration}},
  "[PersistentAppUI](#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-persistentappui)" : {{String}},
  "[S3MonitoringConfiguration](#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-s3monitoringconfiguration)" : {{ParametricS3MonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration-syntax.yaml"></a>

```
  [CloudWatchMonitoringConfiguration](#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-cloudwatchmonitoringconfiguration): {{
    ParametricCloudWatchMonitoringConfiguration}}
  [PersistentAppUI](#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-persistentappui): {{String}}
  [S3MonitoringConfiguration](#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-s3monitoringconfiguration): {{
    ParametricS3MonitoringConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration-properties"></a>

`CloudWatchMonitoringConfiguration`  <a name="cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-cloudwatchmonitoringconfiguration"></a>
 Monitoring configurations for CloudWatch.
*Required*: No
*Type*: [ParametricCloudWatchMonitoringConfiguration](aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PersistentAppUI`  <a name="cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-persistentappui"></a>
 Monitoring configurations for the persistent application UI.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9\$\{\}]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3MonitoringConfiguration`  <a name="cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-s3monitoringconfiguration"></a>
 Amazon S3 configuration for monitoring log publishing.
*Required*: No
*Type*: [ParametricS3MonitoringConfiguration](aws-properties-emrcontainers-jobtemplate-parametrics3monitoringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
