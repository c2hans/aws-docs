---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-workflowversion-imagemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::WorkflowVersion ImageMapping
<a name="aws-properties-omics-workflowversion-imagemapping"></a>

Specifies image mappings that workflow tasks can use. For example, you can replace all the task references of a public image to use an equivalent image in your private ECR repository. You can use image mappings with upstream registries that don't support pull through cache. You need to manually synchronize the upstream registry with your private repository.

## Syntax
<a name="aws-properties-omics-workflowversion-imagemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-workflowversion-imagemapping-syntax.json"></a>

```
{
  "[DestinationImage](#cfn-omics-workflowversion-imagemapping-destinationimage)" : {{String}},
  "[SourceImage](#cfn-omics-workflowversion-imagemapping-sourceimage)" : {{String}}
}
```

### YAML
<a name="aws-properties-omics-workflowversion-imagemapping-syntax.yaml"></a>

```
  [DestinationImage](#cfn-omics-workflowversion-imagemapping-destinationimage): {{String}}
  [SourceImage](#cfn-omics-workflowversion-imagemapping-sourceimage): {{String}}
```

## Properties
<a name="aws-properties-omics-workflowversion-imagemapping-properties"></a>

`DestinationImage`  <a name="cfn-omics-workflowversion-imagemapping-destinationimage"></a>
Specifies the URI of the corresponding image in the private ECR registry.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceImage`  <a name="cfn-omics-workflowversion-imagemapping-sourceimage"></a>
Specifies the URI of the source image in the upstream registry.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
