---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-inferencespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm InferenceSpecification
<a name="aws-properties-sagemaker-algorithm-inferencespecification"></a>

Defines how to perform inference generation after a training job is run.

## Syntax
<a name="aws-properties-sagemaker-algorithm-inferencespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-inferencespecification-syntax.json"></a>

```
{
  "[Containers](#cfn-sagemaker-algorithm-inferencespecification-containers)" : {{[ ModelPackageContainerDefinition, ... ]}},
  "[SupportedContentTypes](#cfn-sagemaker-algorithm-inferencespecification-supportedcontenttypes)" : {{[ String, ... ]}},
  "[SupportedRealtimeInferenceInstanceTypes](#cfn-sagemaker-algorithm-inferencespecification-supportedrealtimeinferenceinstancetypes)" : {{[ String, ... ]}},
  "[SupportedResponseMIMETypes](#cfn-sagemaker-algorithm-inferencespecification-supportedresponsemimetypes)" : {{[ String, ... ]}},
  "[SupportedTransformInstanceTypes](#cfn-sagemaker-algorithm-inferencespecification-supportedtransforminstancetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-inferencespecification-syntax.yaml"></a>

```
  [Containers](#cfn-sagemaker-algorithm-inferencespecification-containers): {{
    - ModelPackageContainerDefinition}}
  [SupportedContentTypes](#cfn-sagemaker-algorithm-inferencespecification-supportedcontenttypes): {{
    - String}}
  [SupportedRealtimeInferenceInstanceTypes](#cfn-sagemaker-algorithm-inferencespecification-supportedrealtimeinferenceinstancetypes): {{
    - String}}
  [SupportedResponseMIMETypes](#cfn-sagemaker-algorithm-inferencespecification-supportedresponsemimetypes): {{
    - String}}
  [SupportedTransformInstanceTypes](#cfn-sagemaker-algorithm-inferencespecification-supportedtransforminstancetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-inferencespecification-properties"></a>

`Containers`  <a name="cfn-sagemaker-algorithm-inferencespecification-containers"></a>
The Amazon ECR registry path of the Docker image that contains the inference code.
*Required*: Yes
*Type*: Array of [ModelPackageContainerDefinition](aws-properties-sagemaker-algorithm-modelpackagecontainerdefinition.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportedContentTypes`  <a name="cfn-sagemaker-algorithm-inferencespecification-supportedcontenttypes"></a>
The supported MIME types for the input data.
*Required*: No
*Type*: Array of String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportedRealtimeInferenceInstanceTypes`  <a name="cfn-sagemaker-algorithm-inferencespecification-supportedrealtimeinferenceinstancetypes"></a>
A list of the instance types that are used to generate inferences in real-time.
This parameter is required for unversioned models, and optional for versioned models.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportedResponseMIMETypes`  <a name="cfn-sagemaker-algorithm-inferencespecification-supportedresponsemimetypes"></a>
The supported MIME types for the output data.
*Required*: No
*Type*: Array of String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportedTransformInstanceTypes`  <a name="cfn-sagemaker-algorithm-inferencespecification-supportedtransforminstancetypes"></a>
A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.
This parameter is required for unversioned models, and optional for versioned models.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
