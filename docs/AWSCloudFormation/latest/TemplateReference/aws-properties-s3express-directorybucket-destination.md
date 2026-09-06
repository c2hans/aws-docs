---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket Destination
<a name="aws-properties-s3express-directorybucket-destination"></a>

Specifies information about where to publish analysis or configuration results for an Amazon S3 bucket and S3 Replication Time Control (S3 RTC).

## Syntax
<a name="aws-properties-s3express-directorybucket-destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-destination-syntax.json"></a>

```
{
  "[BucketAccountId](#cfn-s3express-directorybucket-destination-bucketaccountid)" : {{String}},
  "[BucketArn](#cfn-s3express-directorybucket-destination-bucketarn)" : {{String}},
  "[Format](#cfn-s3express-directorybucket-destination-format)" : {{String}},
  "[Prefix](#cfn-s3express-directorybucket-destination-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-destination-syntax.yaml"></a>

```
  [BucketAccountId](#cfn-s3express-directorybucket-destination-bucketaccountid): {{String}}
  [BucketArn](#cfn-s3express-directorybucket-destination-bucketarn): {{String}}
  [Format](#cfn-s3express-directorybucket-destination-format): {{String}}
  [Prefix](#cfn-s3express-directorybucket-destination-prefix): {{String}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-destination-properties"></a>

`BucketAccountId`  <a name="cfn-s3express-directorybucket-destination-bucketaccountid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketArn`  <a name="cfn-s3express-directorybucket-destination-bucketarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-s3express-directorybucket-destination-format"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `CSV | ORC | Parquet`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-s3express-directorybucket-destination-prefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
