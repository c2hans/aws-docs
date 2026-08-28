---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-tmpfs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition Tmpfs
<a name="aws-properties-ecs-daemontaskdefinition-tmpfs"></a>

The container path, mount options, and size of the tmpfs mount.

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-tmpfs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-tmpfs-syntax.json"></a>

```
{
  "[ContainerPath](#cfn-ecs-daemontaskdefinition-tmpfs-containerpath)" : {{String}},
  "[MountOptions](#cfn-ecs-daemontaskdefinition-tmpfs-mountoptions)" : {{[ String, ... ]}},
  "[Size](#cfn-ecs-daemontaskdefinition-tmpfs-size)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-tmpfs-syntax.yaml"></a>

```
  [ContainerPath](#cfn-ecs-daemontaskdefinition-tmpfs-containerpath): {{String}}
  [MountOptions](#cfn-ecs-daemontaskdefinition-tmpfs-mountoptions): {{
    - String}}
  [Size](#cfn-ecs-daemontaskdefinition-tmpfs-size): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-tmpfs-properties"></a>

`ContainerPath`  <a name="cfn-ecs-daemontaskdefinition-tmpfs-containerpath"></a>
The absolute file path where the tmpfs volume is to be mounted.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MountOptions`  <a name="cfn-ecs-daemontaskdefinition-tmpfs-mountoptions"></a>
The list of tmpfs volume mount options.
Valid values: `"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"`
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Size`  <a name="cfn-ecs-daemontaskdefinition-tmpfs-size"></a>
The maximum size (in MiB) of the tmpfs volume.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
