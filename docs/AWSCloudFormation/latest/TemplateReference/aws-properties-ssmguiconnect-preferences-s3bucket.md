---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmguiconnect-preferences-s3bucket.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMGuiConnect::Preferences S3Bucket
<a name="aws-properties-ssmguiconnect-preferences-s3bucket"></a>

The S3 bucket where RDP connection recordings are stored.

## Syntax
<a name="aws-properties-ssmguiconnect-preferences-s3bucket-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmguiconnect-preferences-s3bucket-syntax.json"></a>

```
{
  "[BucketName](#cfn-ssmguiconnect-preferences-s3bucket-bucketname)" : {{String}},
  "[BucketOwner](#cfn-ssmguiconnect-preferences-s3bucket-bucketowner)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmguiconnect-preferences-s3bucket-syntax.yaml"></a>

```
  [BucketName](#cfn-ssmguiconnect-preferences-s3bucket-bucketname): {{String}}
  [BucketOwner](#cfn-ssmguiconnect-preferences-s3bucket-bucketowner): {{String}}
```

## Properties
<a name="aws-properties-ssmguiconnect-preferences-s3bucket-properties"></a>

`BucketName`  <a name="cfn-ssmguiconnect-preferences-s3bucket-bucketname"></a>
The name of the S3 bucket where RDP connection recordings are stored.
*Required*: Yes
*Type*: String
*Pattern*: `(?=^.{3,63}$)(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketOwner`  <a name="cfn-ssmguiconnect-preferences-s3bucket-bucketowner"></a>
The AWS account number that owns the S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
