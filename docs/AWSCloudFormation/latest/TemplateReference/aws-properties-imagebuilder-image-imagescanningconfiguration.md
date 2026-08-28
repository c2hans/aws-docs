---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-imagescanningconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image ImageScanningConfiguration
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration"></a>

Contains settings for Image Builder image resource and container image scans.

## Syntax
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration-syntax.json"></a>

```
{
  "[EcrConfiguration](#cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration)" : {{EcrConfiguration}},
  "[ImageScanningEnabled](#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration-syntax.yaml"></a>

```
  [EcrConfiguration](#cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration): {{
    EcrConfiguration}}
  [ImageScanningEnabled](#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-imagebuilder-image-imagescanningconfiguration-properties"></a>

`EcrConfiguration`  <a name="cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration"></a>
Contains Amazon ECR settings for vulnerability scans.
*Required*: No
*Type*: [EcrConfiguration](aws-properties-imagebuilder-image-ecrconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageScanningEnabled`  <a name="cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled"></a>
A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
