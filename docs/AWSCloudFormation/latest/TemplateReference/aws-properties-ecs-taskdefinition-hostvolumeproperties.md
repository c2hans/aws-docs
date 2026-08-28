---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-hostvolumeproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition HostVolumeProperties
<a name="aws-properties-ecs-taskdefinition-hostvolumeproperties"></a>

The `HostVolumeProperties` property specifies details on a container instance bind mount host volume.

## Syntax
<a name="aws-properties-ecs-taskdefinition-hostvolumeproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-hostvolumeproperties-syntax.json"></a>

```
{
  "[SourcePath](#cfn-ecs-taskdefinition-hostvolumeproperties-sourcepath)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-hostvolumeproperties-syntax.yaml"></a>

```
  [SourcePath](#cfn-ecs-taskdefinition-hostvolumeproperties-sourcepath): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-hostvolumeproperties-properties"></a>

`SourcePath`  <a name="cfn-ecs-taskdefinition-hostvolumeproperties-sourcepath"></a>
When the `host` parameter is used, specify a `sourcePath` to declare the path on the host container instance that's presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the `host` parameter contains a `sourcePath` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the `sourcePath` value doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
If you're using the Fargate launch type, the `sourcePath` parameter is not supported.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
