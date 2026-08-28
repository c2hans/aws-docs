---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-device.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition Device
<a name="aws-properties-batch-jobdefinition-device"></a>

An object that represents a container instance host device.

**Note**
This object isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

## Syntax
<a name="aws-properties-batch-jobdefinition-device-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-device-syntax.json"></a>

```
{
  "[ContainerPath](#cfn-batch-jobdefinition-device-containerpath)" : {{String}},
  "[HostPath](#cfn-batch-jobdefinition-device-hostpath)" : {{String}},
  "[Permissions](#cfn-batch-jobdefinition-device-permissions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-device-syntax.yaml"></a>

```
  [ContainerPath](#cfn-batch-jobdefinition-device-containerpath): {{String}}
  [HostPath](#cfn-batch-jobdefinition-device-hostpath): {{String}}
  [Permissions](#cfn-batch-jobdefinition-device-permissions): {{
    - String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-device-properties"></a>

`ContainerPath`  <a name="cfn-batch-jobdefinition-device-containerpath"></a>
The path inside the container that's used to expose the host device. By default, the `hostPath` value is used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostPath`  <a name="cfn-batch-jobdefinition-device-hostpath"></a>
The path for the device on the host container instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-batch-jobdefinition-device-permissions"></a>
The explicit permissions to provide to the container for the device. By default, the container has permissions for `read`, `write`, and `mknod` for the device.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
