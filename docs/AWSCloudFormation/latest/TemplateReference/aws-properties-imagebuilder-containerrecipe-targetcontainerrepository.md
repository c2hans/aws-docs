---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ContainerRecipe TargetContainerRepository
<a name="aws-properties-imagebuilder-containerrecipe-targetcontainerrepository"></a>

The container repository where the output container image is stored.

## Syntax
<a name="aws-properties-imagebuilder-containerrecipe-targetcontainerrepository-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-containerrecipe-targetcontainerrepository-syntax.json"></a>

```
{
  "[RepositoryName](#cfn-imagebuilder-containerrecipe-targetcontainerrepository-repositoryname)" : {{String}},
  "[Service](#cfn-imagebuilder-containerrecipe-targetcontainerrepository-service)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-containerrecipe-targetcontainerrepository-syntax.yaml"></a>

```
  [RepositoryName](#cfn-imagebuilder-containerrecipe-targetcontainerrepository-repositoryname): {{String}}
  [Service](#cfn-imagebuilder-containerrecipe-targetcontainerrepository-service): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-containerrecipe-targetcontainerrepository-properties"></a>

`RepositoryName`  <a name="cfn-imagebuilder-containerrecipe-targetcontainerrepository-repositoryname"></a>
The name of the container repository where the output container image is stored. Provide the repository name only (a namespace path such as `team-a/my-repo` is allowed, but not the registry hostname).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Service`  <a name="cfn-imagebuilder-containerrecipe-targetcontainerrepository-service"></a>
Specifies the service in which this image was registered.
*Required*: No
*Type*: String
*Allowed values*: `ECR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
