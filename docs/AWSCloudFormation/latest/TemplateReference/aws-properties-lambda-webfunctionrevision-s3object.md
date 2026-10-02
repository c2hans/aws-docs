---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-s3object.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionRevision S3Object
<a name="aws-properties-lambda-webfunctionrevision-s3object"></a>

<a name="aws-properties-lambda-webfunctionrevision-s3object-description"></a>The `S3Object` property type specifies Property description not available. for an [AWS::Lambda::WebFunctionRevision](aws-resource-lambda-webfunctionrevision.md).

## Syntax
<a name="aws-properties-lambda-webfunctionrevision-s3object-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionrevision-s3object-syntax.json"></a>

```
{
  "[Bucket](#cfn-lambda-webfunctionrevision-s3object-bucket)" : {{String}},
  "[Key](#cfn-lambda-webfunctionrevision-s3object-key)" : {{String}},
  "[VersionId](#cfn-lambda-webfunctionrevision-s3object-versionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionrevision-s3object-syntax.yaml"></a>

```
  [Bucket](#cfn-lambda-webfunctionrevision-s3object-bucket): {{String}}
  [Key](#cfn-lambda-webfunctionrevision-s3object-key): {{String}}
  [VersionId](#cfn-lambda-webfunctionrevision-s3object-versionid): {{String}}
```

## Properties
<a name="aws-properties-lambda-webfunctionrevision-s3object-properties"></a>

`Bucket`  <a name="cfn-lambda-webfunctionrevision-s3object-bucket"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-z0-9][a-z0-9\.\-]{1,61}[a-z0-9])$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Key`  <a name="cfn-lambda-webfunctionrevision-s3object-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VersionId`  <a name="cfn-lambda-webfunctionrevision-s3object-versionid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
