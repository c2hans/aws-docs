---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-signer-signingjob-s3signedobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::SigningJob S3SignedObject
<a name="aws-properties-signer-signingjob-s3signedobject"></a>

The Amazon S3 bucket name and key where Signer saved your signed code image.

## Syntax
<a name="aws-properties-signer-signingjob-s3signedobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-signer-signingjob-s3signedobject-syntax.json"></a>

```
{
  "[BucketName](#cfn-signer-signingjob-s3signedobject-bucketname)" : {{String}},
  "[Key](#cfn-signer-signingjob-s3signedobject-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-signer-signingjob-s3signedobject-syntax.yaml"></a>

```
  [BucketName](#cfn-signer-signingjob-s3signedobject-bucketname): {{String}}
  [Key](#cfn-signer-signingjob-s3signedobject-key): {{String}}
```

## Properties
<a name="aws-properties-signer-signingjob-s3signedobject-properties"></a>

`BucketName`  <a name="cfn-signer-signingjob-s3signedobject-bucketname"></a>
Name of the S3 bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-signer-signingjob-s3signedobject-key"></a>
Key name that uniquely identifies a signed code image in your bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
