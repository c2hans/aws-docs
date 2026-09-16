---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel EncryptionConfiguration
<a name="aws-properties-kinesis-channel-encryptionconfiguration"></a>

<a name="aws-properties-kinesis-channel-encryptionconfiguration-description"></a>The `EncryptionConfiguration` property type specifies Property description not available. for an [AWS::Kinesis::Channel](aws-resource-kinesis-channel.md).

## Syntax
<a name="aws-properties-kinesis-channel-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-encryptionconfiguration-syntax.json"></a>

```
{
  "[EncryptionType](#cfn-kinesis-channel-encryptionconfiguration-encryptiontype)" : {{String}},
  "[KeyId](#cfn-kinesis-channel-encryptionconfiguration-keyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-encryptionconfiguration-syntax.yaml"></a>

```
  [EncryptionType](#cfn-kinesis-channel-encryptionconfiguration-encryptiontype): {{String}}
  [KeyId](#cfn-kinesis-channel-encryptionconfiguration-keyid): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-encryptionconfiguration-properties"></a>

`EncryptionType`  <a name="cfn-kinesis-channel-encryptionconfiguration-encryptiontype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `KMS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KeyId`  <a name="cfn-kinesis-channel-encryptionconfiguration-keyid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
