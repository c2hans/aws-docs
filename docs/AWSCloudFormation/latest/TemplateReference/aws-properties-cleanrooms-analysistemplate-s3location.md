---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate S3Location
<a name="aws-properties-cleanrooms-analysistemplate-s3location"></a>

The S3 location.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-cleanrooms-analysistemplate-s3location-bucket)" : {{String}},
  "[Key](#cfn-cleanrooms-analysistemplate-s3location-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-cleanrooms-analysistemplate-s3location-bucket): {{String}}
  [Key](#cfn-cleanrooms-analysistemplate-s3location-key): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-s3location-properties"></a>

`Bucket`  <a name="cfn-cleanrooms-analysistemplate-s3location-bucket"></a>
 The bucket name.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Key`  <a name="cfn-cleanrooms-analysistemplate-s3location-key"></a>
 The object key.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9!_.*'()-/]+`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
