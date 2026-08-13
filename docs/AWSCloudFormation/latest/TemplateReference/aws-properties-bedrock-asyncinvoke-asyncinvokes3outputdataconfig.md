---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-asyncinvoke-asyncinvokes3outputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AsyncInvoke AsyncInvokeS3OutputDataConfig
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokes3outputdataconfig"></a>

Asynchronous invocation output data settings.

## Syntax
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokes3outputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokes3outputdataconfig-syntax.json"></a>

```
{
  "[S3Uri](#cfn-bedrock-asyncinvoke-asyncinvokes3outputdataconfig-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokes3outputdataconfig-syntax.yaml"></a>

```
  [S3Uri](#cfn-bedrock-asyncinvoke-asyncinvokes3outputdataconfig-s3uri): {{String}}
```

## Properties
<a name="aws-properties-bedrock-asyncinvoke-asyncinvokes3outputdataconfig-properties"></a>

`S3Uri`  <a name="cfn-bedrock-asyncinvoke-asyncinvokes3outputdataconfig-s3uri"></a>
An object URI starting with `s3://`.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
