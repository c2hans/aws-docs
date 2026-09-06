---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-encryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint Encryption
<a name="aws-properties-mediapackagev2-originendpoint-encryption"></a>

The parameters for encrypting content.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-encryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-encryption-syntax.json"></a>

```
{
  "[CmafExcludeSegmentDrmMetadata](#cfn-mediapackagev2-originendpoint-encryption-cmafexcludesegmentdrmmetadata)" : {{Boolean}},
  "[ConstantInitializationVector](#cfn-mediapackagev2-originendpoint-encryption-constantinitializationvector)" : {{String}},
  "[EncryptionMethod](#cfn-mediapackagev2-originendpoint-encryption-encryptionmethod)" : {{EncryptionMethod}},
  "[KeyRotationIntervalSeconds](#cfn-mediapackagev2-originendpoint-encryption-keyrotationintervalseconds)" : {{Integer}},
  "[SpekeKeyProvider](#cfn-mediapackagev2-originendpoint-encryption-spekekeyprovider)" : {{SpekeKeyProvider}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-encryption-syntax.yaml"></a>

```
  [CmafExcludeSegmentDrmMetadata](#cfn-mediapackagev2-originendpoint-encryption-cmafexcludesegmentdrmmetadata): {{Boolean}}
  [ConstantInitializationVector](#cfn-mediapackagev2-originendpoint-encryption-constantinitializationvector): {{String}}
  [EncryptionMethod](#cfn-mediapackagev2-originendpoint-encryption-encryptionmethod): {{
    EncryptionMethod}}
  [KeyRotationIntervalSeconds](#cfn-mediapackagev2-originendpoint-encryption-keyrotationintervalseconds): {{Integer}}
  [SpekeKeyProvider](#cfn-mediapackagev2-originendpoint-encryption-spekekeyprovider): {{
    SpekeKeyProvider}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-encryption-properties"></a>

`CmafExcludeSegmentDrmMetadata`  <a name="cfn-mediapackagev2-originendpoint-encryption-cmafexcludesegmentdrmmetadata"></a>
Excludes SEIG and SGPD boxes from segment metadata in CMAF containers.
When set to `true`, MediaPackage omits these DRM metadata boxes from CMAF segments, which can improve compatibility with certain devices and players that don't support these boxes.
Important considerations:
+ This setting only affects CMAF container formats
+ Key rotation can still be handled through media playlist signaling
+ PSSH and TENC boxes remain unaffected
+ Default behavior is preserved when this setting is disabled
Valid values: `true` \| `false`
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConstantInitializationVector`  <a name="cfn-mediapackagev2-originendpoint-encryption-constantinitializationvector"></a>
A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting content. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV).
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-fA-F]+$`
*Minimum*: `32`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionMethod`  <a name="cfn-mediapackagev2-originendpoint-encryption-encryptionmethod"></a>
The encryption method to use.
*Required*: Yes
*Type*: [EncryptionMethod](aws-properties-mediapackagev2-originendpoint-encryptionmethod.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyRotationIntervalSeconds`  <a name="cfn-mediapackagev2-originendpoint-encryption-keyrotationintervalseconds"></a>
The interval, in seconds, to rotate encryption keys for the origin endpoint.
*Required*: No
*Type*: Integer
*Minimum*: `300`
*Maximum*: `31536000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpekeKeyProvider`  <a name="cfn-mediapackagev2-originendpoint-encryption-spekekeyprovider"></a>
The SPEKE key provider to use for encryption.
*Required*: Yes
*Type*: [SpekeKeyProvider](aws-properties-mediapackagev2-originendpoint-spekekeyprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
