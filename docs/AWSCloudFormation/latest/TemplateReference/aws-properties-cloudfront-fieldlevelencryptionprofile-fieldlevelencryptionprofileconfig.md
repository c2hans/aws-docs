---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::FieldLevelEncryptionProfile FieldLevelEncryptionProfileConfig
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig"></a>

A complex data type of profiles for the field-level encryption.

## Syntax
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-syntax.json"></a>

```
{
  "[CallerReference](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-callerreference)" : {{String}},
  "[Comment](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-comment)" : {{String}},
  "[EncryptionEntities](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-encryptionentities)" : {{[ EncryptionEntity, ... ]}},
  "[Name](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-syntax.yaml"></a>

```
  [CallerReference](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-callerreference): {{String}}
  [Comment](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-comment): {{String}}
  [EncryptionEntities](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-encryptionentities): {{
    - EncryptionEntity}}
  [Name](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-name): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-properties"></a>

`CallerReference`  <a name="cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-callerreference"></a>
A unique number that ensures that the request can't be replayed.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Comment`  <a name="cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-comment"></a>
An optional comment for the field-level encryption profile. The comment cannot be longer than 128 characters.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionEntities`  <a name="cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-encryptionentities"></a>
A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.
*Required*: Yes
*Type*: Array of [EncryptionEntity](aws-properties-cloudfront-fieldlevelencryptionprofile-encryptionentity.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig-name"></a>
Profile name for the field-level encryption profile.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
