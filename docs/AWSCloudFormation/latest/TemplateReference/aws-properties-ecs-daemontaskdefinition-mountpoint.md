---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-mountpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition MountPoint
<a name="aws-properties-ecs-daemontaskdefinition-mountpoint"></a>

The details for a volume mount point that's used in a container definition.

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-mountpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-mountpoint-syntax.json"></a>

```
{
  "[ContainerPath](#cfn-ecs-daemontaskdefinition-mountpoint-containerpath)" : {{String}},
  "[ReadOnly](#cfn-ecs-daemontaskdefinition-mountpoint-readonly)" : {{Boolean}},
  "[SourceVolume](#cfn-ecs-daemontaskdefinition-mountpoint-sourcevolume)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-mountpoint-syntax.yaml"></a>

```
  [ContainerPath](#cfn-ecs-daemontaskdefinition-mountpoint-containerpath): {{String}}
  [ReadOnly](#cfn-ecs-daemontaskdefinition-mountpoint-readonly): {{Boolean}}
  [SourceVolume](#cfn-ecs-daemontaskdefinition-mountpoint-sourcevolume): {{String}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-mountpoint-properties"></a>

`ContainerPath`  <a name="cfn-ecs-daemontaskdefinition-mountpoint-containerpath"></a>
The path on the container to mount the host volume at.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReadOnly`  <a name="cfn-ecs-daemontaskdefinition-mountpoint-readonly"></a>
If this value is `true`, the container has read-only access to the volume. If this value is `false`, then the container can write to the volume. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceVolume`  <a name="cfn-ecs-daemontaskdefinition-mountpoint-sourcevolume"></a>
The name of the volume to mount. Must be a volume name referenced in the `name` parameter of task definition `volume`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
