---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationlibrary-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationLibrary EncryptionConfiguration
<a name="aws-properties-bedrock-dataautomationlibrary-encryptionconfiguration"></a>

Encryption settings for an invocation.

## Syntax
<a name="aws-properties-bedrock-dataautomationlibrary-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationlibrary-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsEncryptionContext](#cfn-bedrock-dataautomationlibrary-encryptionconfiguration-kmsencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
  "[KmsKeyId](#cfn-bedrock-dataautomationlibrary-encryptionconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationlibrary-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsEncryptionContext](#cfn-bedrock-dataautomationlibrary-encryptionconfiguration-kmsencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [KmsKeyId](#cfn-bedrock-dataautomationlibrary-encryptionconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationlibrary-encryptionconfiguration-properties"></a>

`KmsEncryptionContext`  <a name="cfn-bedrock-dataautomationlibrary-encryptionconfiguration-kmsencryptioncontext"></a>
Name-value pairs to include as an encryption context.
*Required*: No
*Type*: Object of String
*Pattern*: `^.*\S.*$`
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-bedrock-dataautomationlibrary-encryptionconfiguration-kmskeyid"></a>
A KMS key ID to use for encryption.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
