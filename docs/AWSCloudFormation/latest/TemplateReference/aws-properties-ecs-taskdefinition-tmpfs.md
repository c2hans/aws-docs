---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-tmpfs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition Tmpfs
<a name="aws-properties-ecs-taskdefinition-tmpfs"></a>

The container path, mount options, and size of the tmpfs mount.

## Syntax
<a name="aws-properties-ecs-taskdefinition-tmpfs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-tmpfs-syntax.json"></a>

```
{
  "[ContainerPath](#cfn-ecs-taskdefinition-tmpfs-containerpath)" : {{String}},
  "[MountOptions](#cfn-ecs-taskdefinition-tmpfs-mountoptions)" : {{[ String, ... ]}},
  "[Size](#cfn-ecs-taskdefinition-tmpfs-size)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-tmpfs-syntax.yaml"></a>

```
  [ContainerPath](#cfn-ecs-taskdefinition-tmpfs-containerpath): {{String}}
  [MountOptions](#cfn-ecs-taskdefinition-tmpfs-mountoptions): {{
    - String}}
  [Size](#cfn-ecs-taskdefinition-tmpfs-size): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-tmpfs-properties"></a>

`ContainerPath`  <a name="cfn-ecs-taskdefinition-tmpfs-containerpath"></a>
The absolute file path where the tmpfs volume is to be mounted.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MountOptions`  <a name="cfn-ecs-taskdefinition-tmpfs-mountoptions"></a>
The list of tmpfs volume mount options.
Valid values: `"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"`
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Size`  <a name="cfn-ecs-taskdefinition-tmpfs-size"></a>
The maximum size (in MiB) of the tmpfs volume.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
