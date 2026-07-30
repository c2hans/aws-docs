---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelInvocationJob ModelInvocationJobS3InputDataConfig
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig"></a>

Contains the configuration of the S3 location of the input data.

## Syntax
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-syntax.json"></a>

```
{
  "[S3BucketOwner](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-s3bucketowner)" : {{String}},
  "[S3Uri](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-syntax.yaml"></a>

```
  [S3BucketOwner](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-s3bucketowner): {{String}}
  [S3Uri](#cfn-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-s3uri): {{String}}
```

## Properties
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-properties"></a>

`S3BucketOwner`  <a name="cfn-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-s3bucketowner"></a>
The ID of the AWS account that owns the S3 bucket containing the input data.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Uri`  <a name="cfn-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig-s3uri"></a>
The S3 location of the input data.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][-.a-z0-9]{1,61}[a-z0-9](?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
