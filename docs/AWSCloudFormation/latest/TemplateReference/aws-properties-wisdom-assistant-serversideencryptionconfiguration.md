---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::Assistant ServerSideEncryptionConfiguration
<a name="aws-properties-wisdom-assistant-serversideencryptionconfiguration"></a>

The configuration information for the customer managed key used for encryption.

## Syntax
<a name="aws-properties-wisdom-assistant-serversideencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-assistant-serversideencryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-assistant-serversideencryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-wisdom-assistant-serversideencryptionconfiguration-properties"></a>

`KmsKeyId`  <a name="cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid"></a>
The customer managed key used for encryption. The customer managed key must have a policy that allows `kms:CreateGrant` and `kms:DescribeKey` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow `kms:Decrypt`, `kms:GenerateDataKey*`, and `kms:DescribeKey` permissions to the `connect.amazonaws.com` service principal. For more information about setting up a customer managed key for Wisdom, see [Enable Connect Customer Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html). For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
