---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-mountpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition MountPoint
<a name="aws-properties-batch-jobdefinition-mountpoint"></a>

Details for a Docker volume mount point that's used in a job's container properties. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the *Docker Remote API* and the `--volume` option to docker run.

## Syntax
<a name="aws-properties-batch-jobdefinition-mountpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-mountpoint-syntax.json"></a>

```
{
  "[ContainerPath](#cfn-batch-jobdefinition-mountpoint-containerpath)" : {{String}},
  "[ReadOnly](#cfn-batch-jobdefinition-mountpoint-readonly)" : {{Boolean}},
  "[SourceVolume](#cfn-batch-jobdefinition-mountpoint-sourcevolume)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-mountpoint-syntax.yaml"></a>

```
  [ContainerPath](#cfn-batch-jobdefinition-mountpoint-containerpath): {{String}}
  [ReadOnly](#cfn-batch-jobdefinition-mountpoint-readonly): {{Boolean}}
  [SourceVolume](#cfn-batch-jobdefinition-mountpoint-sourcevolume): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-mountpoint-properties"></a>

`ContainerPath`  <a name="cfn-batch-jobdefinition-mountpoint-containerpath"></a>
The path on the container where the host volume is mounted.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadOnly`  <a name="cfn-batch-jobdefinition-mountpoint-readonly"></a>
If this value is `true`, the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceVolume`  <a name="cfn-batch-jobdefinition-mountpoint-sourcevolume"></a>
The name of the volume to mount.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
