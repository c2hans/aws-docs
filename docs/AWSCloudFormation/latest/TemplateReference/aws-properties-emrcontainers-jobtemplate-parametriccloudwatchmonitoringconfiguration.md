---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobTemplate ParametricCloudWatchMonitoringConfiguration
<a name="aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration"></a>

 A configuration for CloudWatch monitoring. You can configure your jobs to send log information to CloudWatch Logs. This data type allows job template parameters to be specified within.

## Syntax
<a name="aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-loggroupname)" : {{String}},
  "[LogStreamNamePrefix](#cfn-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-logstreamnameprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-syntax.yaml"></a>

```
  [LogGroupName](#cfn-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-loggroupname): {{String}}
  [LogStreamNamePrefix](#cfn-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-logstreamnameprefix): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-properties"></a>

`LogGroupName`  <a name="cfn-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-loggroupname"></a>
 The name of the log group for log publishing.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9\$\{\}]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogStreamNamePrefix`  <a name="cfn-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-logstreamnameprefix"></a>
 The specified name prefix for log streams.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
