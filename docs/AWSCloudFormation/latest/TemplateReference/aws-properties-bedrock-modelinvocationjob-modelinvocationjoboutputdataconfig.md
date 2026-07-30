---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelInvocationJob ModelInvocationJobOutputDataConfig
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig"></a>

Contains the configuration of the S3 location of the output data.

## Syntax
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig-syntax.json"></a>

```
{
  "[S3OutputDataConfig](#cfn-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig-s3outputdataconfig)" : {{ModelInvocationJobS3OutputDataConfig}}
}
```

### YAML
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig-syntax.yaml"></a>

```
  [S3OutputDataConfig](#cfn-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig-s3outputdataconfig): {{
    ModelInvocationJobS3OutputDataConfig}}
```

## Properties
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig-properties"></a>

`S3OutputDataConfig`  <a name="cfn-bedrock-modelinvocationjob-modelinvocationjoboutputdataconfig-s3outputdataconfig"></a>
Contains the configuration of the S3 location of the output data.
*Required*: Yes
*Type*: [ModelInvocationJobS3OutputDataConfig](aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3outputdataconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
