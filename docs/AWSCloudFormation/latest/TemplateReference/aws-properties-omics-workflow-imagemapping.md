---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-workflow-imagemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Workflow ImageMapping
<a name="aws-properties-omics-workflow-imagemapping"></a>

Specifies image mappings that workflow tasks can use. For example, you can replace all the task references of a public image to use an equivalent image in your private ECR repository. You can use image mappings with upstream registries that don't support pull through cache. You need to manually synchronize the upstream registry with your private repository.

## Syntax
<a name="aws-properties-omics-workflow-imagemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-workflow-imagemapping-syntax.json"></a>

```
{
  "[DestinationImage](#cfn-omics-workflow-imagemapping-destinationimage)" : {{String}},
  "[SourceImage](#cfn-omics-workflow-imagemapping-sourceimage)" : {{String}}
}
```

### YAML
<a name="aws-properties-omics-workflow-imagemapping-syntax.yaml"></a>

```
  [DestinationImage](#cfn-omics-workflow-imagemapping-destinationimage): {{String}}
  [SourceImage](#cfn-omics-workflow-imagemapping-sourceimage): {{String}}
```

## Properties
<a name="aws-properties-omics-workflow-imagemapping-properties"></a>

`DestinationImage`  <a name="cfn-omics-workflow-imagemapping-destinationimage"></a>
Specifies the URI of the corresponding image in the private ECR registry.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceImage`  <a name="cfn-omics-workflow-imagemapping-sourceimage"></a>
Specifies the URI of the source image in the upstream registry.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
