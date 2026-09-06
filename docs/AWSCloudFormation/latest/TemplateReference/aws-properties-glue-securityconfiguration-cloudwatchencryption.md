---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-securityconfiguration-cloudwatchencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::SecurityConfiguration CloudWatchEncryption
<a name="aws-properties-glue-securityconfiguration-cloudwatchencryption"></a>

Specifies how Amazon CloudWatch data should be encrypted.

## Syntax
<a name="aws-properties-glue-securityconfiguration-cloudwatchencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-securityconfiguration-cloudwatchencryption-syntax.json"></a>

```
{
  "[CloudWatchEncryptionMode](#cfn-glue-securityconfiguration-cloudwatchencryption-cloudwatchencryptionmode)" : {{String}},
  "[KmsKeyArn](#cfn-glue-securityconfiguration-cloudwatchencryption-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-securityconfiguration-cloudwatchencryption-syntax.yaml"></a>

```
  [CloudWatchEncryptionMode](#cfn-glue-securityconfiguration-cloudwatchencryption-cloudwatchencryptionmode): {{String}}
  [KmsKeyArn](#cfn-glue-securityconfiguration-cloudwatchencryption-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-glue-securityconfiguration-cloudwatchencryption-properties"></a>

`CloudWatchEncryptionMode`  <a name="cfn-glue-securityconfiguration-cloudwatchencryption-cloudwatchencryptionmode"></a>
The encryption mode to use for CloudWatch data.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | SSE-KMS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-glue-securityconfiguration-cloudwatchencryption-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
*Required*: No
*Type*: String
*Pattern*: `^$|arn:aws[a-z0-9-]*:kms:.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
