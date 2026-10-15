---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::FieldLevelEncryptionConfig QueryArgProfile
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofile"></a>

Query argument-profile mapping for field-level encryption.

## Syntax
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofile-syntax.json"></a>

```
{
  "[ProfileId](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofile-profileid)" : {{String}},
  "[QueryArg](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofile-queryarg)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofile-syntax.yaml"></a>

```
  [ProfileId](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofile-profileid): {{String}}
  [QueryArg](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofile-queryarg): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofile-properties"></a>

`ProfileId`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-queryargprofile-profileid"></a>
ID of profile to use for field-level encryption query argument-profile mapping
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryArg`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-queryargprofile-queryarg"></a>
Query argument for field-level encryption query argument-profile mapping.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
