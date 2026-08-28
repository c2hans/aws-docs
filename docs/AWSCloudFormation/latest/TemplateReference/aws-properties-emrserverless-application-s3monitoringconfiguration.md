---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-s3monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application S3MonitoringConfiguration
<a name="aws-properties-emrserverless-application-s3monitoringconfiguration"></a>

The Amazon S3 configuration for monitoring log publishing. You can configure your jobs to send log information to Amazon S3.

## Syntax
<a name="aws-properties-emrserverless-application-s3monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-s3monitoringconfiguration-syntax.json"></a>

```
{
  "[EncryptionKeyArn](#cfn-emrserverless-application-s3monitoringconfiguration-encryptionkeyarn)" : {{String}},
  "[LogUri](#cfn-emrserverless-application-s3monitoringconfiguration-loguri)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-s3monitoringconfiguration-syntax.yaml"></a>

```
  [EncryptionKeyArn](#cfn-emrserverless-application-s3monitoringconfiguration-encryptionkeyarn): {{String}}
  [LogUri](#cfn-emrserverless-application-s3monitoringconfiguration-loguri): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-application-s3monitoringconfiguration-properties"></a>

`EncryptionKeyArn`  <a name="cfn-emrserverless-application-s3monitoringconfiguration-encryptionkeyarn"></a>
The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):kms:[a-zA-Z0-9\-]*:(\d{12})?:key\/[a-zA-Z0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LogUri`  <a name="cfn-emrserverless-application-s3monitoringconfiguration-loguri"></a>
The Amazon S3 destination URI for log publishing.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `10280`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
