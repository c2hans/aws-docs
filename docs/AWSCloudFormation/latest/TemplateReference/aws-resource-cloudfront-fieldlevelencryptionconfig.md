---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-fieldlevelencryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::FieldLevelEncryptionConfig
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig"></a>

A complex data type that includes the profile configurations specified for field-level encryption.

## Syntax
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::FieldLevelEncryptionConfig",
  "Properties" : {
      "[CallerReference](#cfn-cloudfront-fieldlevelencryptionconfig-callerreference)" : {{String}},
      "[Comment](#cfn-cloudfront-fieldlevelencryptionconfig-comment)" : {{String}},
      "[ContentTypeProfileConfig](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig)" : {{ContentTypeProfileConfig}},
      "[QueryArgProfileConfig](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig)" : {{QueryArgProfileConfig}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig-syntax.yaml"></a>

```
Type: AWS::CloudFront::FieldLevelEncryptionConfig
Properties:
  [CallerReference](#cfn-cloudfront-fieldlevelencryptionconfig-callerreference): {{String}}
  [Comment](#cfn-cloudfront-fieldlevelencryptionconfig-comment): {{String}}
  [ContentTypeProfileConfig](#cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig): {{
    ContentTypeProfileConfig}}
  [QueryArgProfileConfig](#cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig): {{
    QueryArgProfileConfig}}
```

## Properties
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig-properties"></a>

`CallerReference`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-callerreference"></a>
A unique number that ensures the request can't be replayed.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Comment`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-comment"></a>
An optional comment about the configuration. The comment cannot be longer than 128 characters.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentTypeProfileConfig`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig"></a>
A complex data type that specifies when to forward content if a content type isn't recognized and profiles to use as by default in a request if a query argument doesn't specify a profile to use.
*Required*: Yes
*Type*: [ContentTypeProfileConfig](aws-properties-cloudfront-fieldlevelencryptionconfig-contenttypeprofileconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryArgProfileConfig`  <a name="cfn-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig"></a>
A complex data type that specifies when to forward content if a profile isn't found and the profile that can be provided as a query argument in a request.
*Required*: Yes
*Type*: [QueryArgProfileConfig](aws-properties-cloudfront-fieldlevelencryptionconfig-queryargprofileconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudfront-fieldlevelencryptionconfig-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Property description not available.
