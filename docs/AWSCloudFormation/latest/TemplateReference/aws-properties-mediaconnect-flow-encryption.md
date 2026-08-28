---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-encryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow Encryption
<a name="aws-properties-mediaconnect-flow-encryption"></a>

 Encryption information.

## Syntax
<a name="aws-properties-mediaconnect-flow-encryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-encryption-syntax.json"></a>

```
{
  "[Algorithm](#cfn-mediaconnect-flow-encryption-algorithm)" : {{String}},
  "[ConstantInitializationVector](#cfn-mediaconnect-flow-encryption-constantinitializationvector)" : {{String}},
  "[DeviceId](#cfn-mediaconnect-flow-encryption-deviceid)" : {{String}},
  "[KeyType](#cfn-mediaconnect-flow-encryption-keytype)" : {{String}},
  "[Region](#cfn-mediaconnect-flow-encryption-region)" : {{String}},
  "[ResourceId](#cfn-mediaconnect-flow-encryption-resourceid)" : {{String}},
  "[RoleArn](#cfn-mediaconnect-flow-encryption-rolearn)" : {{String}},
  "[SecretArn](#cfn-mediaconnect-flow-encryption-secretarn)" : {{String}},
  "[Url](#cfn-mediaconnect-flow-encryption-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-encryption-syntax.yaml"></a>

```
  [Algorithm](#cfn-mediaconnect-flow-encryption-algorithm): {{String}}
  [ConstantInitializationVector](#cfn-mediaconnect-flow-encryption-constantinitializationvector): {{String}}
  [DeviceId](#cfn-mediaconnect-flow-encryption-deviceid): {{String}}
  [KeyType](#cfn-mediaconnect-flow-encryption-keytype): {{String}}
  [Region](#cfn-mediaconnect-flow-encryption-region): {{String}}
  [ResourceId](#cfn-mediaconnect-flow-encryption-resourceid): {{String}}
  [RoleArn](#cfn-mediaconnect-flow-encryption-rolearn): {{String}}
  [SecretArn](#cfn-mediaconnect-flow-encryption-secretarn): {{String}}
  [Url](#cfn-mediaconnect-flow-encryption-url): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-encryption-properties"></a>

`Algorithm`  <a name="cfn-mediaconnect-flow-encryption-algorithm"></a>
The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
*Required*: No
*Type*: String
*Allowed values*: `aes128 | aes192 | aes256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConstantInitializationVector`  <a name="cfn-mediaconnect-flow-encryption-constantinitializationvector"></a>
 A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceId`  <a name="cfn-mediaconnect-flow-encryption-deviceid"></a>
 The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyType`  <a name="cfn-mediaconnect-flow-encryption-keytype"></a>
The type of key that is used for the encryption. If you don't specify a `keyType` value, the service uses the default setting (`static-key`). Valid key types are: `static-key`, `speke`, and `srt-password`.
*Required*: No
*Type*: String
*Allowed values*: `speke | static-key | srt-password`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-mediaconnect-flow-encryption-region"></a>
 The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceId`  <a name="cfn-mediaconnect-flow-encryption-resourceid"></a>
 An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-mediaconnect-flow-encryption-rolearn"></a>
 The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-mediaconnect-flow-encryption-secretarn"></a>
 The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediaconnect-flow-encryption-url"></a>
 The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
