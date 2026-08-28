---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow SecretsManagerEncryptionKeyConfiguration
<a name="aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration"></a>

The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

## Syntax
<a name="aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-syntax.json"></a>

```
{
  "[RoleArn](#cfn-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-rolearn)" : {{String}},
  "[SecretArn](#cfn-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-syntax.yaml"></a>

```
  [RoleArn](#cfn-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-rolearn): {{String}}
  [SecretArn](#cfn-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-properties"></a>

`RoleArn`  <a name="cfn-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-rolearn"></a>
The ARN of the IAM role assumed by MediaConnect to access the AWS Secrets Manager secret.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-secretarn"></a>
The ARN of the AWS Secrets Manager secret used for transit encryption.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
