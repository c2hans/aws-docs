---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput FlowTransitEncryptionKeyConfiguration
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration"></a>

Configuration settings for flow transit encryption keys.

## Syntax
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-syntax.json"></a>

```
{
  "[Automatic](#cfn-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-automatic)" : {{Json}},
  "[SecretsManager](#cfn-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-secretsmanager)" : {{SecretsManagerEncryptionKeyConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-syntax.yaml"></a>

```
  [Automatic](#cfn-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-automatic): {{Json}}
  [SecretsManager](#cfn-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-secretsmanager): {{
    SecretsManagerEncryptionKeyConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-properties"></a>

`Automatic`  <a name="cfn-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-automatic"></a>
Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManager`  <a name="cfn-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-secretsmanager"></a>
The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.
*Required*: No
*Type*: [SecretsManagerEncryptionKeyConfiguration](aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
