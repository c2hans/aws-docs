---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-fieldlevelencryptionprofile-encryptionentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::FieldLevelEncryptionProfile EncryptionEntity
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-encryptionentity"></a>

Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.

## Syntax
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-encryptionentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-encryptionentity-syntax.json"></a>

```
{
  "[FieldPatterns](#cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-fieldpatterns)" : {{[ String, ... ]}},
  "[ProviderId](#cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-providerid)" : {{String}},
  "[PublicKeyId](#cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-publickeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-encryptionentity-syntax.yaml"></a>

```
  [FieldPatterns](#cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-fieldpatterns): {{
    - String}}
  [ProviderId](#cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-providerid): {{String}}
  [PublicKeyId](#cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-publickeyid): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-encryptionentity-properties"></a>

`FieldPatterns`  <a name="cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-fieldpatterns"></a>
Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (\*). You can't overlap field patterns. For example, you can't have both ABC\* and AB\*. Note that field patterns are case-sensitive.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderId`  <a name="cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-providerid"></a>
The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicKeyId`  <a name="cfn-cloudfront-fieldlevelencryptionprofile-encryptionentity-publickeyid"></a>
The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
