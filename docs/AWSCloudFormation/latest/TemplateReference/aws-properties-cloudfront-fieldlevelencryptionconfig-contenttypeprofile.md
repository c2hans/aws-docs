---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::FieldLevelEncryptionConfig ContentTypeProfile
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofile"></a>

A field-level encryption content type profile.

## Syntax
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-syntax.json"></a>

```
{
  "[ContentType](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-contenttype)" : {{String}},
  "[Format](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-format)" : {{String}},
  "[ProfileId](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-profileid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-syntax.yaml"></a>

```
  [ContentType](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-contenttype): {{String}}
  [Format](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-format): {{String}}
  [ProfileId](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-profileid): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-properties"></a>

`ContentType`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-contenttype"></a>
The content type for a field-level encryption content type-profile mapping.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-format"></a>
The format for a field-level encryption content type-profile mapping.
*Required*: Yes
*Type*: String
*Allowed values*: `URLEncoded`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileId`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofile-profileid"></a>
The profile ID for a field-level encryption content type-profile mapping.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
