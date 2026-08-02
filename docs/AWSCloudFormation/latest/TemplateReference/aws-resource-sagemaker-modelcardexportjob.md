---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-modelcardexportjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCardExportJob
<a name="aws-resource-sagemaker-modelcardexportjob"></a>

Creates an Amazon SageMaker Model Card export job.

## Syntax
<a name="aws-resource-sagemaker-modelcardexportjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-modelcardexportjob-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::ModelCardExportJob",
  "Properties" : {
      "[ModelCardExportJobName](#cfn-sagemaker-modelcardexportjob-modelcardexportjobname)" : {{String}},
      "[ModelCardName](#cfn-sagemaker-modelcardexportjob-modelcardname)" : {{String}},
      "[ModelCardVersion](#cfn-sagemaker-modelcardexportjob-modelcardversion)" : {{Integer}},
      "[OutputConfig](#cfn-sagemaker-modelcardexportjob-outputconfig)" : {{ModelCardExportOutputConfig}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-modelcardexportjob-syntax.yaml"></a>

```
Type: AWS::SageMaker::ModelCardExportJob
Properties:
  [ModelCardExportJobName](#cfn-sagemaker-modelcardexportjob-modelcardexportjobname): {{String}}
  [ModelCardName](#cfn-sagemaker-modelcardexportjob-modelcardname): {{String}}
  [ModelCardVersion](#cfn-sagemaker-modelcardexportjob-modelcardversion): {{Integer}}
  [OutputConfig](#cfn-sagemaker-modelcardexportjob-outputconfig): {{
    ModelCardExportOutputConfig}}
```

## Properties
<a name="aws-resource-sagemaker-modelcardexportjob-properties"></a>

`ModelCardExportJobName`  <a name="cfn-sagemaker-modelcardexportjob-modelcardexportjobname"></a>
The name of the model card export job.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelCardName`  <a name="cfn-sagemaker-modelcardexportjob-modelcardname"></a>
The name of the model card that the export job exports.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model-card/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelCardVersion`  <a name="cfn-sagemaker-modelcardexportjob-modelcardversion"></a>
The version of the model card that the export job exports.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputConfig`  <a name="cfn-sagemaker-modelcardexportjob-outputconfig"></a>
Contains information about the output location for the compiled model and the target device that the model runs on. `TargetDevice` and `TargetPlatform` are mutually exclusive, so you need to choose one between the two to specify your target device or platform. If you cannot find your device you want to use from the `TargetDevice` list, use `TargetPlatform` to describe the platform of your edge device and `CompilerOptions` if there are specific settings that are required or recommended to use for particular TargetPlatform.
*Required*: Yes
*Type*: [ModelCardExportOutputConfig](aws-properties-sagemaker-modelcardexportjob-modelcardexportoutputconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-modelcardexportjob-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-modelcardexportjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-modelcardexportjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-modelcardexportjob-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the model card export job was created.

`LastModifiedAt`  <a name="LastModifiedAt-fn::getatt"></a>
The date and time that the model card export job was last modified..

`ModelCardExportJobArn`  <a name="ModelCardExportJobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the model card export job.

`Status`  <a name="Status-fn::getatt"></a>
The completion status of the model card export job.
