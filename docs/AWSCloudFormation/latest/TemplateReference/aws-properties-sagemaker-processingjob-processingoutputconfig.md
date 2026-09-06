---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-processingoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob ProcessingOutputConfig
<a name="aws-properties-sagemaker-processingjob-processingoutputconfig"></a>

Configuration for uploading output from the processing container.

## Syntax
<a name="aws-properties-sagemaker-processingjob-processingoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-processingoutputconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-sagemaker-processingjob-processingoutputconfig-kmskeyid)" : {{String}},
  "[Outputs](#cfn-sagemaker-processingjob-processingoutputconfig-outputs)" : {{[ ProcessingOutputsObject, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-processingoutputconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-sagemaker-processingjob-processingoutputconfig-kmskeyid): {{String}}
  [Outputs](#cfn-sagemaker-processingjob-processingoutputconfig-outputs): {{
    - ProcessingOutputsObject}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-processingoutputconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-processingjob-processingoutputconfig-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the processing job output. `KmsKeyId` can be an ID of a KMS key, ARN of a KMS key, or alias of a KMS key. The `KmsKeyId` is applied to all outputs.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:/_-]*`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Outputs`  <a name="cfn-sagemaker-processingjob-processingoutputconfig-outputs"></a>
An array of outputs configuring the data to upload from the processing container.
*Required*: Yes
*Type*: Array of [ProcessingOutputsObject](aws-properties-sagemaker-processingjob-processingoutputsobject.md)
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
