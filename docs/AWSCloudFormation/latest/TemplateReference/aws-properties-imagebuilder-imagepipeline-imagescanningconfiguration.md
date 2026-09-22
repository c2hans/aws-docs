---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline ImageScanningConfiguration
<a name="aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration"></a>

Contains settings for Image Builder image resource and container image scans.

## Syntax
<a name="aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration-syntax.json"></a>

```
{
  "[EcrConfiguration](#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-ecrconfiguration)" : {{EcrConfiguration}},
  "[ImageScanningEnabled](#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-imagescanningenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration-syntax.yaml"></a>

```
  [EcrConfiguration](#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-ecrconfiguration): {{
    EcrConfiguration}}
  [ImageScanningEnabled](#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-imagescanningenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration-properties"></a>

`EcrConfiguration`  <a name="cfn-imagebuilder-imagepipeline-imagescanningconfiguration-ecrconfiguration"></a>
Contains Amazon ECR settings for vulnerability scans.
*Required*: No
*Type*: [EcrConfiguration](aws-properties-imagebuilder-imagepipeline-ecrconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageScanningEnabled`  <a name="cfn-imagebuilder-imagepipeline-imagescanningconfiguration-imagescanningenabled"></a>
Specifies whether Amazon Inspector scans for vulnerabilities when you create a new image, and whether Image Builder saves the findings. Amazon Inspector must be enabled in the account. Image tests must also be enabled. For AMI output, Amazon Inspector scans the test instance. For container output, Amazon Inspector scans the container image that Image Builder pushes to the Amazon ECR repository from your `ecrConfiguration` settings.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
