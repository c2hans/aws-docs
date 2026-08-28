---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ekscontainervolumemount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksContainerVolumeMount
<a name="aws-properties-batch-jobdefinition-ekscontainervolumemount"></a>

The volume mounts for a container for an Amazon EKS job. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation*.

## Syntax
<a name="aws-properties-batch-jobdefinition-ekscontainervolumemount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ekscontainervolumemount-syntax.json"></a>

```
{
  "[MountPath](#cfn-batch-jobdefinition-ekscontainervolumemount-mountpath)" : {{String}},
  "[Name](#cfn-batch-jobdefinition-ekscontainervolumemount-name)" : {{String}},
  "[ReadOnly](#cfn-batch-jobdefinition-ekscontainervolumemount-readonly)" : {{Boolean}},
  "[SubPath](#cfn-batch-jobdefinition-ekscontainervolumemount-subpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ekscontainervolumemount-syntax.yaml"></a>

```
  [MountPath](#cfn-batch-jobdefinition-ekscontainervolumemount-mountpath): {{String}}
  [Name](#cfn-batch-jobdefinition-ekscontainervolumemount-name): {{String}}
  [ReadOnly](#cfn-batch-jobdefinition-ekscontainervolumemount-readonly): {{Boolean}}
  [SubPath](#cfn-batch-jobdefinition-ekscontainervolumemount-subpath): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ekscontainervolumemount-properties"></a>

`MountPath`  <a name="cfn-batch-jobdefinition-ekscontainervolumemount-mountpath"></a>
The path on the container where the volume is mounted.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-batch-jobdefinition-ekscontainervolumemount-name"></a>
The name the volume mount. This must match the name of one of the volumes in the pod.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadOnly`  <a name="cfn-batch-jobdefinition-ekscontainervolumemount-readonly"></a>
If this value is `true`, the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubPath`  <a name="cfn-batch-jobdefinition-ekscontainervolumemount-subpath"></a>
A sub-path inside the referenced volume instead of its root.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
