---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcardexportjob-modelcardexportoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCardExportJob ModelCardExportOutputConfig
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportoutputconfig"></a>

Configure the export output details for an Amazon SageMaker Model Card.

## Syntax
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportoutputconfig-syntax.json"></a>

```
{
  "[S3OutputPath](#cfn-sagemaker-modelcardexportjob-modelcardexportoutputconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportoutputconfig-syntax.yaml"></a>

```
  [S3OutputPath](#cfn-sagemaker-modelcardexportjob-modelcardexportoutputconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportoutputconfig-properties"></a>

`S3OutputPath`  <a name="cfn-sagemaker-modelcardexportjob-modelcardexportoutputconfig-s3outputpath"></a>
The Amazon S3 output path to export your model card PDF.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
