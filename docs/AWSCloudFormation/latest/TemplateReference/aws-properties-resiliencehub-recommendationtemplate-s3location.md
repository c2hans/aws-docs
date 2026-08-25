---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehub-recommendationtemplate-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::RecommendationTemplate S3Location
<a name="aws-properties-resiliencehub-recommendationtemplate-s3location"></a>

The location of the Amazon S3 bucket.

## Syntax
<a name="aws-properties-resiliencehub-recommendationtemplate-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehub-recommendationtemplate-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-resiliencehub-recommendationtemplate-s3location-bucket)" : {{String}},
  "[Prefix](#cfn-resiliencehub-recommendationtemplate-s3location-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehub-recommendationtemplate-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-resiliencehub-recommendationtemplate-s3location-bucket): {{String}}
  [Prefix](#cfn-resiliencehub-recommendationtemplate-s3location-prefix): {{String}}
```

## Properties
<a name="aws-properties-resiliencehub-recommendationtemplate-s3location-properties"></a>

`Bucket`  <a name="cfn-resiliencehub-recommendationtemplate-s3location-bucket"></a>
The name of the Amazon S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-resiliencehub-recommendationtemplate-s3location-prefix"></a>
The prefix for the Amazon S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
