---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-originendpoint-cmafencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::OriginEndpoint CmafEncryption
<a name="aws-properties-mediapackage-originendpoint-cmafencryption"></a>

Holds encryption information so that access to the content can be controlled by a DRM solution.

## Syntax
<a name="aws-properties-mediapackage-originendpoint-cmafencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-originendpoint-cmafencryption-syntax.json"></a>

```
{
  "[ConstantInitializationVector](#cfn-mediapackage-originendpoint-cmafencryption-constantinitializationvector)" : {{String}},
  "[EncryptionMethod](#cfn-mediapackage-originendpoint-cmafencryption-encryptionmethod)" : {{String}},
  "[KeyRotationIntervalSeconds](#cfn-mediapackage-originendpoint-cmafencryption-keyrotationintervalseconds)" : {{Integer}},
  "[SpekeKeyProvider](#cfn-mediapackage-originendpoint-cmafencryption-spekekeyprovider)" : {{SpekeKeyProvider}}
}
```

### YAML
<a name="aws-properties-mediapackage-originendpoint-cmafencryption-syntax.yaml"></a>

```
  [ConstantInitializationVector](#cfn-mediapackage-originendpoint-cmafencryption-constantinitializationvector): {{String}}
  [EncryptionMethod](#cfn-mediapackage-originendpoint-cmafencryption-encryptionmethod): {{String}}
  [KeyRotationIntervalSeconds](#cfn-mediapackage-originendpoint-cmafencryption-keyrotationintervalseconds): {{Integer}}
  [SpekeKeyProvider](#cfn-mediapackage-originendpoint-cmafencryption-spekekeyprovider): {{
    SpekeKeyProvider}}
```

## Properties
<a name="aws-properties-mediapackage-originendpoint-cmafencryption-properties"></a>

`ConstantInitializationVector`  <a name="cfn-mediapackage-originendpoint-cmafencryption-constantinitializationvector"></a>
An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you don't specify a value, then AWS Elemental MediaPackage creates the constant initialization vector (IV).
*Required*: No
*Type*: String
*Pattern*: `\A[0-9a-fA-F]+\Z`
*Minimum*: `32`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionMethod`  <a name="cfn-mediapackage-originendpoint-cmafencryption-encryptionmethod"></a>
The encryption method to use.
*Required*: No
*Type*: String
*Allowed values*: `SAMPLE_AES | AES_CTR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyRotationIntervalSeconds`  <a name="cfn-mediapackage-originendpoint-cmafencryption-keyrotationintervalseconds"></a>
Number of seconds before AWS Elemental MediaPackage rotates to a new key. By default, rotation is set to 60 seconds. Set to `0` to disable key rotation.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpekeKeyProvider`  <a name="cfn-mediapackage-originendpoint-cmafencryption-spekekeyprovider"></a>
Parameters for the SPEKE key provider.
*Required*: Yes
*Type*: [SpekeKeyProvider](aws-properties-mediapackage-originendpoint-spekekeyprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
