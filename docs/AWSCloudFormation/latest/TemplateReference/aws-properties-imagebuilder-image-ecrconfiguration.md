---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-ecrconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image EcrConfiguration
<a name="aws-properties-imagebuilder-image-ecrconfiguration"></a>

Settings that Image Builder uses to configure the ECR repository and the output container images that Amazon Inspector scans.

## Syntax
<a name="aws-properties-imagebuilder-image-ecrconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-ecrconfiguration-syntax.json"></a>

```
{
  "[ContainerTags](#cfn-imagebuilder-image-ecrconfiguration-containertags)" : {{[ String, ... ]}},
  "[RepositoryName](#cfn-imagebuilder-image-ecrconfiguration-repositoryname)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-ecrconfiguration-syntax.yaml"></a>

```
  [ContainerTags](#cfn-imagebuilder-image-ecrconfiguration-containertags): {{
    - String}}
  [RepositoryName](#cfn-imagebuilder-image-ecrconfiguration-repositoryname): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-image-ecrconfiguration-properties"></a>

`ContainerTags`  <a name="cfn-imagebuilder-image-ecrconfiguration-containertags"></a>
Tags for Image Builder to apply to the output container image that Amazon Inspector scans. Tags can help you identify and manage your scanned images.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RepositoryName`  <a name="cfn-imagebuilder-image-ecrconfiguration-repositoryname"></a>
The name of the container repository where Image Builder pushes the container image for the vulnerability scan. Provide the repository name only (a namespace path is allowed, but not the registry hostname); the repository must already exist in your account. If you don't specify a repository name, Image Builder creates the default repository `image-builder-image-scanning-repository` in your account.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
