---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry EncryptionConfiguration
<a name="aws-properties-agentregistry-registry-encryptionconfiguration"></a>

The server-side encryption configuration for a registry. It specifies a customer managed AWS Key Management Service (AWS KMS) key that encrypts the registry's content.

You can't change the encryption configuration after you create the registry. Changing it replaces the registry.

## Syntax
<a name="aws-properties-agentregistry-registry-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-agentregistry-registry-encryptionconfiguration-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-agentregistry-registry-encryptionconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registry-encryptionconfiguration-properties"></a>

`KmsKeyArn`  <a name="cfn-agentregistry-registry-encryptionconfiguration-kmskeyarn"></a>
Specify the Amazon Resource Name (ARN) of the customer managed KMS key that encrypts the registry's content. You must use a symmetric encryption key in the same AWS account and Region as the registry. You can't use a multi-Region key.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
