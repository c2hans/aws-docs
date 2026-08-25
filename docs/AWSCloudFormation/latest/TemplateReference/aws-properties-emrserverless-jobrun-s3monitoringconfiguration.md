---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-jobrun-s3monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun S3MonitoringConfiguration
<a name="aws-properties-emrserverless-jobrun-s3monitoringconfiguration"></a>

The Amazon S3 configuration for monitoring log publishing. You can configure your jobs to send log information to Amazon S3.

## Syntax
<a name="aws-properties-emrserverless-jobrun-s3monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-jobrun-s3monitoringconfiguration-syntax.json"></a>

```
{
  "[LogUri](#cfn-emrserverless-jobrun-s3monitoringconfiguration-loguri)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-jobrun-s3monitoringconfiguration-syntax.yaml"></a>

```
  [LogUri](#cfn-emrserverless-jobrun-s3monitoringconfiguration-loguri): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-jobrun-s3monitoringconfiguration-properties"></a>

`LogUri`  <a name="cfn-emrserverless-jobrun-s3monitoringconfiguration-loguri"></a>
The Amazon S3 destination URI for log publishing.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
