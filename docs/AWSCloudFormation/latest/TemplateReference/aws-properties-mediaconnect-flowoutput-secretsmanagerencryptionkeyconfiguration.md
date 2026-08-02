---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput SecretsManagerEncryptionKeyConfiguration
<a name="aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration"></a>

The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

## Syntax
<a name="aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-syntax.json"></a>

```
{
  "[RoleArn](#cfn-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-rolearn)" : {{String}},
  "[SecretArn](#cfn-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-syntax.yaml"></a>

```
  [RoleArn](#cfn-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-rolearn): {{String}}
  [SecretArn](#cfn-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-properties"></a>

`RoleArn`  <a name="cfn-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-rolearn"></a>
The ARN of the IAM role assumed by MediaConnect to access the AWS Secrets Manager secret.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-secretarn"></a>
The ARN of the AWS Secrets Manager secret used for transit encryption.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
