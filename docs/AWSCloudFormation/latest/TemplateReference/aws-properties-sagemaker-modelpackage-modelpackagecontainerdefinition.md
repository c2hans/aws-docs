---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage ModelPackageContainerDefinition
<a name="aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition"></a>

Describes the Docker container for the model package.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition-syntax.json"></a>

```
{
  "[ContainerHostname](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-containerhostname)" : {{String}},
  "[Environment](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-environment)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Framework](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-framework)" : {{String}},
  "[FrameworkVersion](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-frameworkversion)" : {{String}},
  "[Image](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-image)" : {{String}},
  "[ImageDigest](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-imagedigest)" : {{String}},
  "[ModelDataSource](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modeldatasource)" : {{ModelDataSource}},
  "[ModelDataUrl](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modeldataurl)" : {{String}},
  "[ModelInput](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modelinput)" : {{ModelInput}},
  "[NearestModelName](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-nearestmodelname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition-syntax.yaml"></a>

```
  [ContainerHostname](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-containerhostname): {{String}}
  [Environment](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-environment): {{
    {{Key}}: {{Value}}}}
  [Framework](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-framework): {{String}}
  [FrameworkVersion](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-frameworkversion): {{String}}
  [Image](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-image): {{String}}
  [ImageDigest](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-imagedigest): {{String}}
  [ModelDataSource](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modeldatasource): {{
    ModelDataSource}}
  [ModelDataUrl](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modeldataurl): {{String}}
  [ModelInput](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modelinput): {{
    ModelInput}}
  [NearestModelName](#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-nearestmodelname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition-properties"></a>

`ContainerHostname`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-containerhostname"></a>
The DNS host name for the Docker container.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-environment"></a>
The environment variables to set in the Docker container. Each key and value in the `Environment` string to string map can have length of up to 1024. We support up to 16 entries in the map.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_][a-zA-Z0-9_]*`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Framework`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-framework"></a>
The machine learning framework of the model package container image.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FrameworkVersion`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-frameworkversion"></a>
The framework version of the Model Package Container Image.
*Required*: No
*Type*: String
*Pattern*: `[0-9]\.[A-Za-z0-9.]+`
*Minimum*: `3`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-image"></a>
The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.
If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
*Required*: Yes
*Type*: String
*Pattern*: `[\S]{1,255}`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageDigest`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-imagedigest"></a>
An MD5 hash of the training algorithm that identifies the Docker image used for training.
*Required*: No
*Type*: String
*Pattern*: `^[Ss][Hh][Aa]256:[0-9a-fA-F]{64}$`
*Maximum*: `72`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelDataSource`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modeldatasource"></a>
Specifies the location of ML model data to deploy during endpoint creation.
*Required*: No
*Type*: [ModelDataSource](aws-properties-sagemaker-modelpackage-modeldatasource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelDataUrl`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modeldataurl"></a>
The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).
The model artifacts must be in an S3 bucket that is in the same region as the model package.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelInput`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modelinput"></a>
A structure with Model Input details.
*Required*: No
*Type*: [ModelInput](aws-properties-sagemaker-modelpackage-modelinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NearestModelName`  <a name="cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-nearestmodelname"></a>
The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling `ListModelMetadata`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
