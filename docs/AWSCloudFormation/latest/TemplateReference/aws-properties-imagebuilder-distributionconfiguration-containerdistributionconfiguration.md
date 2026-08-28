---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration ContainerDistributionConfiguration
<a name="aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration"></a>

Container distribution settings for encryption, licensing, and sharing in a specific Region.

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration-syntax.json"></a>

```
{
  "[ContainerTags](#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-containertags)" : {{[ String, ... ]}},
  "[Description](#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-description)" : {{String}},
  "[TargetRepository](#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-targetrepository)" : {{TargetContainerRepository}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration-syntax.yaml"></a>

```
  [ContainerTags](#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-containertags): {{
    - String}}
  [Description](#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-description): {{String}}
  [TargetRepository](#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-targetrepository): {{
    TargetContainerRepository}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration-properties"></a>

`ContainerTags`  <a name="cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-containertags"></a>
Tags that are attached to the container distribution configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-description"></a>
The description of the container distribution configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRepository`  <a name="cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-targetrepository"></a>
The destination repository for the container distribution configuration.
*Required*: No
*Type*: [TargetContainerRepository](aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
