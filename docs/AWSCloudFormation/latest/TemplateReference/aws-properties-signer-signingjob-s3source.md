---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-signer-signingjob-s3source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::SigningJob S3Source
<a name="aws-properties-signer-signingjob-s3source"></a>

Information about the Amazon S3 bucket where you saved your unsigned code.

## Syntax
<a name="aws-properties-signer-signingjob-s3source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-signer-signingjob-s3source-syntax.json"></a>

```
{
  "[BucketName](#cfn-signer-signingjob-s3source-bucketname)" : {{String}},
  "[Key](#cfn-signer-signingjob-s3source-key)" : {{String}},
  "[Version](#cfn-signer-signingjob-s3source-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-signer-signingjob-s3source-syntax.yaml"></a>

```
  [BucketName](#cfn-signer-signingjob-s3source-bucketname): {{String}}
  [Key](#cfn-signer-signingjob-s3source-key): {{String}}
  [Version](#cfn-signer-signingjob-s3source-version): {{String}}
```

## Properties
<a name="aws-properties-signer-signingjob-s3source-properties"></a>

`BucketName`  <a name="cfn-signer-signingjob-s3source-bucketname"></a>
Name of the S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-signer-signingjob-s3source-key"></a>
Key name of the bucket object that contains your unsigned code.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-signer-signingjob-s3source-version"></a>
Version of your source image in your version enabled S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
