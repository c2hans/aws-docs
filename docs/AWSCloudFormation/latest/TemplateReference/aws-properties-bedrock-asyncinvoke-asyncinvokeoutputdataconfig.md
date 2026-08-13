---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-asyncinvoke-asyncinvokeoutputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AsyncInvoke AsyncInvokeOutputDataConfig
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokeoutputdataconfig"></a>

Asynchronous invocation output data settings.

## Syntax
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokeoutputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokeoutputdataconfig-syntax.json"></a>

```
{
  "[S3OutputDataConfig](#cfn-bedrock-asyncinvoke-asyncinvokeoutputdataconfig-s3outputdataconfig)" : {{AsyncInvokeS3OutputDataConfig}}
}
```

### YAML
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokeoutputdataconfig-syntax.yaml"></a>

```
  [S3OutputDataConfig](#cfn-bedrock-asyncinvoke-asyncinvokeoutputdataconfig-s3outputdataconfig): {{
    AsyncInvokeS3OutputDataConfig}}
```

## Properties
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokeoutputdataconfig-properties"></a>

`S3OutputDataConfig`  <a name="cfn-bedrock-asyncinvoke-asyncinvokeoutputdataconfig-s3outputdataconfig"></a>
A storage location for the output data in an S3 bucket
*Required*: Yes
*Type*: [AsyncInvokeS3OutputDataConfig](aws-properties-bedrock-asyncinvoke-asyncinvokes3outputdataconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
