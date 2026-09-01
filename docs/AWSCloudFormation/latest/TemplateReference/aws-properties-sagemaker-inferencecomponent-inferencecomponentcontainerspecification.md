---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentContainerSpecification
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification"></a>

Defines a container that provides the runtime environment for a model that you deploy with an inference component.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-syntax.json"></a>

```
{
  "[ArtifactUrl](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-artifacturl)" : {{String}},
  "[ContainerMetricsConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-containermetricsconfig)" : {{ContainerMetricsConfig}},
  "[DeployedImage](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-deployedimage)" : {{DeployedImage}},
  "[Environment](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-environment)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Image](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-image)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-syntax.yaml"></a>

```
  [ArtifactUrl](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-artifacturl): {{String}}
  [ContainerMetricsConfig](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-containermetricsconfig): {{
    ContainerMetricsConfig}}
  [DeployedImage](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-deployedimage): {{
    DeployedImage}}
  [Environment](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-environment): {{
    {{Key}}: {{Value}}}}
  [Image](#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-image): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-properties"></a>

`ArtifactUrl`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-artifacturl"></a>
The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerMetricsConfig`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-containermetricsconfig"></a>
The configuration for container metrics scraping. Specifies the metrics endpoint path and publishing frequency for the inference component's container. If not specified when `EnableDetailedObservability` is `True`, the default path `/metrics` on port `8080` is used. For first-party and Deep Learning Containers (DLC), the endpoint path is determined automatically and this configuration is optional.
*Required*: No
*Type*: [ContainerMetricsConfig](aws-properties-sagemaker-inferencecomponent-containermetricsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeployedImage`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-deployedimage"></a>
The deployed container image for the inference component.
*Required*: No
*Type*: [DeployedImage](aws-properties-sagemaker-inferencecomponent-deployedimage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-environment"></a>
The environment variables to set in the Docker container. Each key and value in the Environment string-to-string map can have length of up to 1024. We support up to 16 entries in the map.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]{1,1024}$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-image"></a>
The Amazon Elastic Container Registry (Amazon ECR) path where the Docker image for the model is stored.
*Required*: No
*Type*: String
*Pattern*: `[\S]+`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
