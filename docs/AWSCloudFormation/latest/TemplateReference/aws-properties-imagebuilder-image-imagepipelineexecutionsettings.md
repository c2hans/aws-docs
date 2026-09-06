---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-imagepipelineexecutionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image ImagePipelineExecutionSettings
<a name="aws-properties-imagebuilder-image-imagepipelineexecutionsettings"></a>

Contains settings for creating an image by running an existing image pipeline.

## Syntax
<a name="aws-properties-imagebuilder-image-imagepipelineexecutionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-imagepipelineexecutionsettings-syntax.json"></a>

```
{
  "[DeploymentId](#cfn-imagebuilder-image-imagepipelineexecutionsettings-deploymentid)" : {{String}},
  "[OnUpdate](#cfn-imagebuilder-image-imagepipelineexecutionsettings-onupdate)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-imagepipelineexecutionsettings-syntax.yaml"></a>

```
  [DeploymentId](#cfn-imagebuilder-image-imagepipelineexecutionsettings-deploymentid): {{String}}
  [OnUpdate](#cfn-imagebuilder-image-imagepipelineexecutionsettings-onupdate): {{Boolean}}
```

## Properties
<a name="aws-properties-imagebuilder-image-imagepipelineexecutionsettings-properties"></a>

`DeploymentId`  <a name="cfn-imagebuilder-image-imagepipelineexecutionsettings-deploymentid"></a>
The deployment ID of the image pipeline that creates this image. The deployment ID changes each time the pipeline configuration changes. To set this value, use the `Fn::GetAtt` intrinsic function to retrieve the `DeploymentId` attribute of your `AWS::ImageBuilder::ImagePipeline` resource.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`OnUpdate`  <a name="cfn-imagebuilder-image-imagepipelineexecutionsettings-onupdate"></a>
Specifies whether the pipeline runs again when the referenced image pipeline is updated. If you set this to `true`, a change to the pipeline's deployment ID triggers a new pipeline execution and builds a new image. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
