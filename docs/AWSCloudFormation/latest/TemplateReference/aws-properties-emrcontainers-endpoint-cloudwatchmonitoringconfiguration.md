---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::Endpoint CloudWatchMonitoringConfiguration
<a name="aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration"></a>

A configuration for CloudWatch monitoring. You can configure your jobs to send log information to CloudWatch Logs.

## Syntax
<a name="aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-loggroupname)" : {{String}},
  "[LogStreamNamePrefix](#cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-logstreamnameprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-syntax.yaml"></a>

```
  [LogGroupName](#cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-loggroupname): {{String}}
  [LogStreamNamePrefix](#cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-logstreamnameprefix): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-properties"></a>

`LogGroupName`  <a name="cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-loggroupname"></a>
The name of the log group for log publishing.
*Required*: Yes
*Type*: String
*Pattern*: `[\.\-_/#A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogStreamNamePrefix`  <a name="cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-logstreamnameprefix"></a>
The specified name prefix for log streams.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
