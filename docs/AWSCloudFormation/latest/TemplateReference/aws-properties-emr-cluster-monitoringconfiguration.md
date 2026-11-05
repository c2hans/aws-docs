---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster MonitoringConfiguration
<a name="aws-properties-emr-cluster-monitoringconfiguration"></a>

Contains CloudWatch log configuration and S3 logging configuration metadata and settings.

## Syntax
<a name="aws-properties-emr-cluster-monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-monitoringconfiguration-syntax.json"></a>

```
{
  "[CloudWatchLogConfiguration](#cfn-emr-cluster-monitoringconfiguration-cloudwatchlogconfiguration)" : {{CloudWatchLogConfiguration}}
}
```

### YAML
<a name="aws-properties-emr-cluster-monitoringconfiguration-syntax.yaml"></a>

```
  [CloudWatchLogConfiguration](#cfn-emr-cluster-monitoringconfiguration-cloudwatchlogconfiguration): {{
    CloudWatchLogConfiguration}}
```

## Properties
<a name="aws-properties-emr-cluster-monitoringconfiguration-properties"></a>

`CloudWatchLogConfiguration`  <a name="cfn-emr-cluster-monitoringconfiguration-cloudwatchlogconfiguration"></a>
CloudWatch log configuration settings and metadata that specify settings like log files to monitor and where to send them.
*Required*: No
*Type*: [CloudWatchLogConfiguration](aws-properties-emr-cluster-cloudwatchlogconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
