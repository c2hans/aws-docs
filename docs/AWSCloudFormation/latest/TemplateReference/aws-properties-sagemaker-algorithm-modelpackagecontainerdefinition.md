---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-modelpackagecontainerdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm ModelPackageContainerDefinition
<a name="aws-properties-sagemaker-algorithm-modelpackagecontainerdefinition"></a>

Describes the Docker container for the model package.

## Syntax
<a name="aws-properties-sagemaker-algorithm-modelpackagecontainerdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-modelpackagecontainerdefinition-syntax.json"></a>

```
{
  "[ContainerHostname](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-containerhostname)" : {{String}},
  "[Environment](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-environment)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Framework](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-framework)" : {{String}},
  "[FrameworkVersion](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-frameworkversion)" : {{String}},
  "[Image](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-image)" : {{String}},
  "[ImageDigest](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-imagedigest)" : {{String}},
  "[IsCheckpoint](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-ischeckpoint)" : {{Boolean}},
  "[ModelInput](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-modelinput)" : {{ModelInput}},
  "[NearestModelName](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-nearestmodelname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-modelpackagecontainerdefinition-syntax.yaml"></a>

```
  [ContainerHostname](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-containerhostname): {{String}}
  [Environment](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-environment): {{
    {{Key}}: {{Value}}}}
  [Framework](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-framework): {{String}}
  [FrameworkVersion](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-frameworkversion): {{String}}
  [Image](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-image): {{String}}
  [ImageDigest](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-imagedigest): {{String}}
  [IsCheckpoint](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-ischeckpoint): {{Boolean}}
  [ModelInput](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-modelinput): {{
    ModelInput}}
  [NearestModelName](#cfn-sagemaker-algorithm-modelpackagecontainerdefinition-nearestmodelname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-modelpackagecontainerdefinition-properties"></a>

`ContainerHostname`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-containerhostname"></a>
The DNS host name for the Docker container.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-environment"></a>
The environment variables to set in the Docker container. Each key and value in the `Environment` string to string map can have length of up to 1024. We support up to 16 entries in the map.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\S]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Framework`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-framework"></a>
The machine learning framework of the model package container image.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FrameworkVersion`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-frameworkversion"></a>
The framework version of the Model Package Container Image.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]\.[A-Za-z0-9.-]+$`
*Minimum*: `3`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Image`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-image"></a>
The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.
If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
*Required*: Yes
*Type*: String
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageDigest`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-imagedigest"></a>
An MD5 hash of the training algorithm that identifies the Docker image used for training.
*Required*: No
*Type*: String
*Pattern*: `^[Ss][Hh][Aa]256:[0-9a-fA-F]{64}$`
*Maximum*: `72`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsCheckpoint`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-ischeckpoint"></a>
 Specifies whether the model data is a training checkpoint.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelInput`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-modelinput"></a>
A structure with Model Input details.
*Required*: No
*Type*: [ModelInput](aws-properties-sagemaker-algorithm-modelinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NearestModelName`  <a name="cfn-sagemaker-algorithm-modelpackagecontainerdefinition-nearestmodelname"></a>
The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling `ListModelMetadata`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
