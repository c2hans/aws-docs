---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelInvocationJob ModelInvocationJobS3OutputDataConfig
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig"></a>

Contains the configuration of the S3 location of the output data.

## Syntax
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-syntax.json"></a>

```
{
  "[S3BucketOwner](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3bucketowner)" : {{String}},
  "[S3EncryptionKeyId](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3encryptionkeyid)" : {{String}},
  "[S3Uri](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-syntax.yaml"></a>

```
  [S3BucketOwner](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3bucketowner): {{String}}
  [S3EncryptionKeyId](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3encryptionkeyid): {{String}}
  [S3Uri](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3uri): {{String}}
```

## Properties
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-properties"></a>

`S3BucketOwner`  <a name="cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3bucketowner"></a>
The ID of the AWS account that owns the S3 bucket containing the output data.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3EncryptionKeyId`  <a name="cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3encryptionkeyid"></a>
The unique identifier of the key that encrypts the S3 location of the output data.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Uri`  <a name="cfn-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig-s3uri"></a>
The S3 location of the output data.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][-.a-z0-9]{1,61}[a-z0-9](?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
