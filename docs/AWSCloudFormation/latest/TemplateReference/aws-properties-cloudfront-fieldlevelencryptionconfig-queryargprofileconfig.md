---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::FieldLevelEncryptionConfig QueryArgProfileConfig
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig"></a>

Configuration for query argument-profile mapping for field-level encryption.

## Syntax
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-syntax.json"></a>

```
{
  "[ForwardWhenQueryArgProfileIsUnknown](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-forwardwhenqueryargprofileisunknown)" : {{Boolean}},
  "[QueryArgProfiles](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-queryargprofiles)" : {{[ QueryArgProfile, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-syntax.yaml"></a>

```
  [ForwardWhenQueryArgProfileIsUnknown](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-forwardwhenqueryargprofileisunknown): {{Boolean}}
  [QueryArgProfiles](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-queryargprofiles): {{
    - QueryArgProfile}}
```

## Properties
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-properties"></a>

`ForwardWhenQueryArgProfileIsUnknown`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-forwardwhenqueryargprofileisunknown"></a>
Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryArgProfiles`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig-queryargprofiles"></a>
Profiles specified for query argument-profile mapping for field-level encryption.
*Required*: Yes
*Type*: Array of [QueryArgProfile](aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
