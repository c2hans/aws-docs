---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration TargetContainerRepository
<a name="aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository"></a>

The container repository where the output container image is stored.

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository-syntax.json"></a>

```
{
  "[RepositoryName](#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-repositoryname)" : {{String}},
  "[Service](#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-service)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository-syntax.yaml"></a>

```
  [RepositoryName](#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-repositoryname): {{String}}
  [Service](#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-service): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository-properties"></a>

`RepositoryName`  <a name="cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-repositoryname"></a>
The name of the container repository where the output container image is stored. This name is prefixed by the repository location. For example, `<repository location url>/repository_name`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Service`  <a name="cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-service"></a>
Specifies the service in which this image was registered.
*Required*: No
*Type*: String
*Allowed values*: `ECR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
