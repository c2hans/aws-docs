---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcardexportjob-modelcardexportartifacts.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCardExportJob ModelCardExportArtifacts
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportartifacts"></a>

The artifacts of the model card export job.

## Syntax
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportartifacts-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportartifacts-syntax.json"></a>

```
{
  "[S3ExportArtifacts](#cfn-sagemaker-modelcardexportjob-modelcardexportartifacts-s3exportartifacts)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportartifacts-syntax.yaml"></a>

```
  [S3ExportArtifacts](#cfn-sagemaker-modelcardexportjob-modelcardexportartifacts-s3exportartifacts): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcardexportjob-modelcardexportartifacts-properties"></a>

`S3ExportArtifacts`  <a name="cfn-sagemaker-modelcardexportjob-modelcardexportartifacts-s3exportartifacts"></a>
The Amazon S3 URI of the exported model artifacts.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
