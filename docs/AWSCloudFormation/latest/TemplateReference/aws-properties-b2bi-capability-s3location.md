---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-capability-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Capability S3Location
<a name="aws-properties-b2bi-capability-s3location"></a>

Specifies the details for the Amazon S3 file location that is being used with AWS B2B Data Interchange. File locations in Amazon S3 are identified using a combination of the bucket and key.

## Syntax
<a name="aws-properties-b2bi-capability-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-capability-s3location-syntax.json"></a>

```
{
  "[BucketName](#cfn-b2bi-capability-s3location-bucketname)" : {{String}},
  "[Key](#cfn-b2bi-capability-s3location-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-capability-s3location-syntax.yaml"></a>

```
  [BucketName](#cfn-b2bi-capability-s3location-bucketname): {{String}}
  [Key](#cfn-b2bi-capability-s3location-key): {{String}}
```

## Properties
<a name="aws-properties-b2bi-capability-s3location-properties"></a>

`BucketName`  <a name="cfn-b2bi-capability-s3location-bucketname"></a>
Specifies the name of the Amazon S3 bucket.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-b2bi-capability-s3location-key"></a>
Specifies the Amazon S3 key for the file location.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
