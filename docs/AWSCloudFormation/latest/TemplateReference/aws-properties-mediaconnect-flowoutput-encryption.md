---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowoutput-encryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput Encryption
<a name="aws-properties-mediaconnect-flowoutput-encryption"></a>

 Encryption information.

## Syntax
<a name="aws-properties-mediaconnect-flowoutput-encryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowoutput-encryption-syntax.json"></a>

```
{
  "[Algorithm](#cfn-mediaconnect-flowoutput-encryption-algorithm)" : {{String}},
  "[KeyType](#cfn-mediaconnect-flowoutput-encryption-keytype)" : {{String}},
  "[RoleArn](#cfn-mediaconnect-flowoutput-encryption-rolearn)" : {{String}},
  "[SecretArn](#cfn-mediaconnect-flowoutput-encryption-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowoutput-encryption-syntax.yaml"></a>

```
  [Algorithm](#cfn-mediaconnect-flowoutput-encryption-algorithm): {{String}}
  [KeyType](#cfn-mediaconnect-flowoutput-encryption-keytype): {{String}}
  [RoleArn](#cfn-mediaconnect-flowoutput-encryption-rolearn): {{String}}
  [SecretArn](#cfn-mediaconnect-flowoutput-encryption-secretarn): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flowoutput-encryption-properties"></a>

`Algorithm`  <a name="cfn-mediaconnect-flowoutput-encryption-algorithm"></a>
The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
*Required*: No
*Type*: String
*Allowed values*: `aes128 | aes192 | aes256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyType`  <a name="cfn-mediaconnect-flowoutput-encryption-keytype"></a>
The type of key that is used for the encryption. If you don't specify a `keyType` value, the service uses the default setting (`static-key`). Valid key types are: `static-key`, `speke`, and `srt-password`.
*Required*: No
*Type*: String
*Allowed values*: `static-key | srt-password`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-mediaconnect-flowoutput-encryption-rolearn"></a>
 The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-mediaconnect-flowoutput-encryption-secretarn"></a>
 The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
