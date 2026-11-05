---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-cloudwatchlogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster CloudWatchLogConfiguration
<a name="aws-properties-emr-cluster-cloudwatchlogconfiguration"></a>

Holds CloudWatch log configuration settings and metadata that specify settings like log files to monitor and where to send them.

## Syntax
<a name="aws-properties-emr-cluster-cloudwatchlogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-cloudwatchlogconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-emr-cluster-cloudwatchlogconfiguration-enabled)" : {{Boolean}},
  "[EncryptionKeyArn](#cfn-emr-cluster-cloudwatchlogconfiguration-encryptionkeyarn)" : {{String}},
  "[LogGroupName](#cfn-emr-cluster-cloudwatchlogconfiguration-loggroupname)" : {{String}},
  "[LogStreamNamePrefix](#cfn-emr-cluster-cloudwatchlogconfiguration-logstreamnameprefix)" : {{String}},
  "[LogTypes](#cfn-emr-cluster-cloudwatchlogconfiguration-logtypes)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-emr-cluster-cloudwatchlogconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-emr-cluster-cloudwatchlogconfiguration-enabled): {{Boolean}}
  [EncryptionKeyArn](#cfn-emr-cluster-cloudwatchlogconfiguration-encryptionkeyarn): {{String}}
  [LogGroupName](#cfn-emr-cluster-cloudwatchlogconfiguration-loggroupname): {{String}}
  [LogStreamNamePrefix](#cfn-emr-cluster-cloudwatchlogconfiguration-logstreamnameprefix): {{String}}
  [LogTypes](#cfn-emr-cluster-cloudwatchlogconfiguration-logtypes): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-emr-cluster-cloudwatchlogconfiguration-properties"></a>

`Enabled`  <a name="cfn-emr-cluster-cloudwatchlogconfiguration-enabled"></a>
Specifies if CloudWatch logging is enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionKeyArn`  <a name="cfn-emr-cluster-cloudwatchlogconfiguration-encryptionkeyarn"></a>
The ARN of the encryption key used to encrypt the logs.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogGroupName`  <a name="cfn-emr-cluster-cloudwatchlogconfiguration-loggroupname"></a>
The name of the CloudWatch log group where logs are published.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogStreamNamePrefix`  <a name="cfn-emr-cluster-cloudwatchlogconfiguration-logstreamnameprefix"></a>
The prefix of the log stream name.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogTypes`  <a name="cfn-emr-cluster-cloudwatchlogconfiguration-logtypes"></a>
A map of log types to file names for publishing logs to the standard output or standard error streams for CloudWatch. Valid log types include STEP\_LOGS, SPARK\_DRIVER, and SPARK\_EXECUTOR. Valid file names for each type include STDOUT and STDERR.
*Required*: No
*Type*: Object of Array
*Pattern*: `.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
