---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-cloudwatchmonitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun CloudWatchMonitoringConfiguration
<a name="aws-properties-emrcontainers-jobrun-cloudwatchmonitoringconfiguration"></a>

A configuration for CloudWatch monitoring. You can configure your jobs to send log information to CloudWatch Logs.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-loggroupname)" : {{String}},
  "[LogStreamNamePrefix](#cfn-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-logstreamnameprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-syntax.yaml"></a>

```
  [LogGroupName](#cfn-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-loggroupname): {{String}}
  [LogStreamNamePrefix](#cfn-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-logstreamnameprefix): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-properties"></a>

`LogGroupName`  <a name="cfn-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-loggroupname"></a>
The name of the log group for log publishing.
*Required*: Yes
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogStreamNamePrefix`  <a name="cfn-emrcontainers-jobrun-cloudwatchmonitoringconfiguration-logstreamnameprefix"></a>
The specified name prefix for log streams.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
