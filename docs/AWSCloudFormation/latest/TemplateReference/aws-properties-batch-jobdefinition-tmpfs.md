---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-tmpfs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition Tmpfs
<a name="aws-properties-batch-jobdefinition-tmpfs"></a>

The container path, mount options, and size of the `tmpfs` mount.

**Note**
This object isn't applicable to jobs that are running on Fargate resources.

## Syntax
<a name="aws-properties-batch-jobdefinition-tmpfs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-tmpfs-syntax.json"></a>

```
{
  "[ContainerPath](#cfn-batch-jobdefinition-tmpfs-containerpath)" : {{String}},
  "[MountOptions](#cfn-batch-jobdefinition-tmpfs-mountoptions)" : {{[ String, ... ]}},
  "[Size](#cfn-batch-jobdefinition-tmpfs-size)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-tmpfs-syntax.yaml"></a>

```
  [ContainerPath](#cfn-batch-jobdefinition-tmpfs-containerpath): {{String}}
  [MountOptions](#cfn-batch-jobdefinition-tmpfs-mountoptions): {{
    - String}}
  [Size](#cfn-batch-jobdefinition-tmpfs-size): {{Integer}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-tmpfs-properties"></a>

`ContainerPath`  <a name="cfn-batch-jobdefinition-tmpfs-containerpath"></a>
The absolute file path in the container where the `tmpfs` volume is mounted.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountOptions`  <a name="cfn-batch-jobdefinition-tmpfs-mountoptions"></a>
The list of `tmpfs` volume mount options.
Valid values: "`defaults`" \| "`ro`" \| "`rw`" \| "`suid`" \| "`nosuid`" \| "`dev`" \| "`nodev`" \| "`exec`" \| "`noexec`" \| "`sync`" \| "`async`" \| "`dirsync`" \| "`remount`" \| "`mand`" \| "`nomand`" \| "`atime`" \| "`noatime`" \| "`diratime`" \| "`nodiratime`" \| "`bind`" \| "`rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime`" \| "`norelatime`" \| "`strictatime`" \| "`nostrictatime`" \| "`mode`" \| "`uid`" \| "`gid`" \| "`nr_inodes`" \| "`nr_blocks`" \| "`mpol`"
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Size`  <a name="cfn-batch-jobdefinition-tmpfs-size"></a>
The size (in MiB) of the `tmpfs` volume.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
