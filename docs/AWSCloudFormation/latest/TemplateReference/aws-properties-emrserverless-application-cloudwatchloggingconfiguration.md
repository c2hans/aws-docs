---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-cloudwatchloggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application CloudWatchLoggingConfiguration
<a name="aws-properties-emrserverless-application-cloudwatchloggingconfiguration"></a>

The Amazon CloudWatch configuration for monitoring logs. You can configure your jobs to send log information to CloudWatch.

## Syntax
<a name="aws-properties-emrserverless-application-cloudwatchloggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-cloudwatchloggingconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-emrserverless-application-cloudwatchloggingconfiguration-enabled)" : {{Boolean}},
  "[EncryptionKeyArn](#cfn-emrserverless-application-cloudwatchloggingconfiguration-encryptionkeyarn)" : {{String}},
  "[LogGroupName](#cfn-emrserverless-application-cloudwatchloggingconfiguration-loggroupname)" : {{String}},
  "[LogStreamNamePrefix](#cfn-emrserverless-application-cloudwatchloggingconfiguration-logstreamnameprefix)" : {{String}},
  "[LogTypeMap](#cfn-emrserverless-application-cloudwatchloggingconfiguration-logtypemap)" : {{[ LogTypeMapKeyValuePair, ... ]}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-cloudwatchloggingconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-emrserverless-application-cloudwatchloggingconfiguration-enabled): {{Boolean}}
  [EncryptionKeyArn](#cfn-emrserverless-application-cloudwatchloggingconfiguration-encryptionkeyarn): {{String}}
  [LogGroupName](#cfn-emrserverless-application-cloudwatchloggingconfiguration-loggroupname): {{String}}
  [LogStreamNamePrefix](#cfn-emrserverless-application-cloudwatchloggingconfiguration-logstreamnameprefix): {{String}}
  [LogTypeMap](#cfn-emrserverless-application-cloudwatchloggingconfiguration-logtypemap): {{
    - LogTypeMapKeyValuePair}}
```

## Properties
<a name="aws-properties-emrserverless-application-cloudwatchloggingconfiguration-properties"></a>

`Enabled`  <a name="cfn-emrserverless-application-cloudwatchloggingconfiguration-enabled"></a>
Enables CloudWatch logging.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EncryptionKeyArn`  <a name="cfn-emrserverless-application-cloudwatchloggingconfiguration-encryptionkeyarn"></a>
The AWS Key Management Service (KMS) key ARN to encrypt the logs that you store in CloudWatch Logs.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):kms:[a-zA-Z0-9\-]*:(\d{12})?:key\/[a-zA-Z0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LogGroupName`  <a name="cfn-emrserverless-application-cloudwatchloggingconfiguration-loggroupname"></a>
The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LogStreamNamePrefix`  <a name="cfn-emrserverless-application-cloudwatchloggingconfiguration-logstreamnameprefix"></a>
Prefix for the CloudWatch log stream name.
*Required*: No
*Type*: String
*Pattern*: `^[^:*]*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LogTypeMap`  <a name="cfn-emrserverless-application-cloudwatchloggingconfiguration-logtypemap"></a>
Property description not available.
*Required*: No
*Type*: Array of [LogTypeMapKeyValuePair](aws-properties-emrserverless-application-logtypemapkeyvaluepair.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
