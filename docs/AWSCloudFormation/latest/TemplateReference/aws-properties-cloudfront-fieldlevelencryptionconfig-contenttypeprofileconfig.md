---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::FieldLevelEncryptionConfig ContentTypeProfileConfig
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig"></a>

The configuration for a field-level encryption content type-profile mapping.

## Syntax
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-syntax.json"></a>

```
{
  "[ContentTypeProfiles](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-contenttypeprofiles)" : {{[ ContentTypeProfile, ... ]}},
  "[ForwardWhenContentTypeIsUnknown](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-forwardwhencontenttypeisunknown)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-syntax.yaml"></a>

```
  [ContentTypeProfiles](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-contenttypeprofiles): {{
    - ContentTypeProfile}}
  [ForwardWhenContentTypeIsUnknown](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-forwardwhencontenttypeisunknown): {{Boolean}}
```

## Properties
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-properties"></a>

`ContentTypeProfiles`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-contenttypeprofiles"></a>
The configuration for a field-level encryption content type-profile.
*Required*: Yes
*Type*: Array of [ContentTypeProfile](aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofile.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForwardWhenContentTypeIsUnknown`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig-forwardwhencontenttypeisunknown"></a>
The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
