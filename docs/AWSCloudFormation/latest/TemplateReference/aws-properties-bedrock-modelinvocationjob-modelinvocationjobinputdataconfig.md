---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelInvocationJob ModelInvocationJobInputDataConfig
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig"></a>

Details about the location of the input to the batch inference job.

## Syntax
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig-syntax.json"></a>

```
{
  "[S3InputDataConfig](#cfn-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig-s3inputdataconfig)" : {{ModelInvocationJobS3InputDataConfig}}
}
```

### YAML
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig-syntax.yaml"></a>

```
  [S3InputDataConfig](#cfn-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig-s3inputdataconfig): {{
    ModelInvocationJobS3InputDataConfig}}
```

## Properties
<a name="aws-properties-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig-properties"></a>

`S3InputDataConfig`  <a name="cfn-bedrock-modelinvocationjob-modelinvocationjobinputdataconfig-s3inputdataconfig"></a>
Contains the configuration of the S3 location of the input data.
*Required*: Yes
*Type*: [ModelInvocationJobS3InputDataConfig](aws-properties-bedrock-modelinvocationjob-modelinvocationjobs3inputdataconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
