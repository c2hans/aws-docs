---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automloutputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLOutputDataConfig
<a name="aws-properties-sagemaker-automljob-automloutputdataconfig"></a>

The output data configuration.

## Syntax
<a name="aws-properties-sagemaker-automljob-automloutputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automloutputdataconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-sagemaker-automljob-automloutputdataconfig-kmskeyid)" : {{String}},
  "[S3OutputPath](#cfn-sagemaker-automljob-automloutputdataconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automloutputdataconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-sagemaker-automljob-automloutputdataconfig-kmskeyid): {{String}}
  [S3OutputPath](#cfn-sagemaker-automljob-automloutputdataconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automloutputdataconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-automljob-automloutputdataconfig-kmskeyid"></a>
The AWS Key Management Service encryption key ID.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/_-]*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3OutputPath`  <a name="cfn-sagemaker-automljob-automloutputdataconfig-s3outputpath"></a>
The Amazon S3 output path. Must be 512 characters or less.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
