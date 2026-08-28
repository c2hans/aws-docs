---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-deployedimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent DeployedImage
<a name="aws-properties-sagemaker-inferencecomponent-deployedimage"></a>

Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this [ProductionVariant](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html).

If you used the `registry/repository[:tag]` form to specify the image path of the primary container when you created the model hosted in this `ProductionVariant`, the path resolves to a path of the form `registry/repository[@digest]`. A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see [Pulling an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide*.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-deployedimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-deployedimage-syntax.json"></a>

```
{
  "[ResolutionTime](#cfn-sagemaker-inferencecomponent-deployedimage-resolutiontime)" : {{String}},
  "[ResolvedImage](#cfn-sagemaker-inferencecomponent-deployedimage-resolvedimage)" : {{String}},
  "[SpecifiedImage](#cfn-sagemaker-inferencecomponent-deployedimage-specifiedimage)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-deployedimage-syntax.yaml"></a>

```
  [ResolutionTime](#cfn-sagemaker-inferencecomponent-deployedimage-resolutiontime): {{String}}
  [ResolvedImage](#cfn-sagemaker-inferencecomponent-deployedimage-resolvedimage): {{String}}
  [SpecifiedImage](#cfn-sagemaker-inferencecomponent-deployedimage-specifiedimage): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-deployedimage-properties"></a>

`ResolutionTime`  <a name="cfn-sagemaker-inferencecomponent-deployedimage-resolutiontime"></a>
The date and time when the image path for the model resolved to the `ResolvedImage`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolvedImage`  <a name="cfn-sagemaker-inferencecomponent-deployedimage-resolvedimage"></a>
The specific digest path of the image hosted in this `ProductionVariant`.
*Required*: No
*Type*: String
*Pattern*: `[\S]+`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpecifiedImage`  <a name="cfn-sagemaker-inferencecomponent-deployedimage-specifiedimage"></a>
The image path you specified when you created the model.
*Required*: No
*Type*: String
*Pattern*: `[\S]+`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
