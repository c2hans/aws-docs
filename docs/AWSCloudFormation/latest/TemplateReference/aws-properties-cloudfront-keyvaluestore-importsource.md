---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-keyvaluestore-importsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::KeyValueStore ImportSource
<a name="aws-properties-cloudfront-keyvaluestore-importsource"></a>

The import source for the key value store.

## Syntax
<a name="aws-properties-cloudfront-keyvaluestore-importsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-keyvaluestore-importsource-syntax.json"></a>

```
{
  "[SourceArn](#cfn-cloudfront-keyvaluestore-importsource-sourcearn)" : {{String}},
  "[SourceType](#cfn-cloudfront-keyvaluestore-importsource-sourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-keyvaluestore-importsource-syntax.yaml"></a>

```
  [SourceArn](#cfn-cloudfront-keyvaluestore-importsource-sourcearn): {{String}}
  [SourceType](#cfn-cloudfront-keyvaluestore-importsource-sourcetype): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-keyvaluestore-importsource-properties"></a>

`SourceArn`  <a name="cfn-cloudfront-keyvaluestore-importsource-sourcearn"></a>
The Amazon Resource Name (ARN) of the import source for the key value store.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceType`  <a name="cfn-cloudfront-keyvaluestore-importsource-sourcetype"></a>
The source type of the import source for the key value store.
*Required*: Yes
*Type*: String
*Allowed values*: `S3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
