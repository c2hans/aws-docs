---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-device.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition Device
<a name="aws-properties-ecs-taskdefinition-device"></a>

The `Device` property specifies an object representing a container instance host device.

## Syntax
<a name="aws-properties-ecs-taskdefinition-device-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-device-syntax.json"></a>

```
{
  "[ContainerPath](#cfn-ecs-taskdefinition-device-containerpath)" : {{String}},
  "[HostPath](#cfn-ecs-taskdefinition-device-hostpath)" : {{String}},
  "[Permissions](#cfn-ecs-taskdefinition-device-permissions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-device-syntax.yaml"></a>

```
  [ContainerPath](#cfn-ecs-taskdefinition-device-containerpath): {{String}}
  [HostPath](#cfn-ecs-taskdefinition-device-hostpath): {{String}}
  [Permissions](#cfn-ecs-taskdefinition-device-permissions): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-device-properties"></a>

`ContainerPath`  <a name="cfn-ecs-taskdefinition-device-containerpath"></a>
The path inside the container at which to expose the host device.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostPath`  <a name="cfn-ecs-taskdefinition-device-hostpath"></a>
The path for the device on the host container instance.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Permissions`  <a name="cfn-ecs-taskdefinition-device-permissions"></a>
The explicit permissions to provide to the container for the device. By default, the container has permissions for `read`, `write`, and `mknod` for the device.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
