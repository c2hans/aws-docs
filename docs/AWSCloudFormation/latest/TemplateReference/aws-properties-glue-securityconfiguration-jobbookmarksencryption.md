---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::SecurityConfiguration JobBookmarksEncryption
<a name="aws-properties-glue-securityconfiguration-jobbookmarksencryption"></a>

Specifies how job bookmark data should be encrypted.

## Syntax
<a name="aws-properties-glue-securityconfiguration-jobbookmarksencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-securityconfiguration-jobbookmarksencryption-syntax.json"></a>

```
{
  "[JobBookmarksEncryptionMode](#cfn-glue-securityconfiguration-jobbookmarksencryption-jobbookmarksencryptionmode)" : {{String}},
  "[KmsKeyArn](#cfn-glue-securityconfiguration-jobbookmarksencryption-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-securityconfiguration-jobbookmarksencryption-syntax.yaml"></a>

```
  [JobBookmarksEncryptionMode](#cfn-glue-securityconfiguration-jobbookmarksencryption-jobbookmarksencryptionmode): {{String}}
  [KmsKeyArn](#cfn-glue-securityconfiguration-jobbookmarksencryption-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-glue-securityconfiguration-jobbookmarksencryption-properties"></a>

`JobBookmarksEncryptionMode`  <a name="cfn-glue-securityconfiguration-jobbookmarksencryption-jobbookmarksencryptionmode"></a>
The encryption mode to use for job bookmarks data.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | CSE-KMS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-glue-securityconfiguration-jobbookmarksencryption-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
*Required*: No
*Type*: String
*Pattern*: `^$|arn:aws[a-z0-9-]*:kms:.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
