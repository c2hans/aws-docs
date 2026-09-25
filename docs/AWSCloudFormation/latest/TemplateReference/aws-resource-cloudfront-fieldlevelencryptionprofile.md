---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-fieldlevelencryptionprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::FieldLevelEncryptionProfile
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile"></a>

A complex data type for field-level encryption profiles.

## Syntax
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::FieldLevelEncryptionProfile",
  "Properties" : {
      "[FieldLevelEncryptionProfileConfig](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig)" : {{FieldLevelEncryptionProfileConfig}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile-syntax.yaml"></a>

```
Type: AWS::CloudFront::FieldLevelEncryptionProfile
Properties:
  [FieldLevelEncryptionProfileConfig](#cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig): {{
    FieldLevelEncryptionProfileConfig}}
```

## Properties
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile-properties"></a>

`FieldLevelEncryptionProfileConfig`  <a name="cfn-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig"></a>
A complex data type that includes the profile name and the encryption entities for the field-level encryption profile.
*Required*: Yes
*Type*: [FieldLevelEncryptionProfileConfig](aws-properties-cloudfront-fieldlevelencryptionprofile-fieldlevelencryptionprofileconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudfront-fieldlevelencryptionprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The ID for a field-level encryption profile configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The last time the field-level encryption profile was updated.
