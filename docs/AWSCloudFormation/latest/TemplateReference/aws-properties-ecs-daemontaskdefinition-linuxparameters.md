---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-linuxparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition LinuxParameters
<a name="aws-properties-ecs-daemontaskdefinition-linuxparameters"></a>

The Linux-specific options that are applied to the container, such as Linux [KernelCapabilities](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_KernelCapabilities.html).

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-linuxparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-linuxparameters-syntax.json"></a>

```
{
  "[Capabilities](#cfn-ecs-daemontaskdefinition-linuxparameters-capabilities)" : {{KernelCapabilities}},
  "[Devices](#cfn-ecs-daemontaskdefinition-linuxparameters-devices)" : {{[ Device, ... ]}},
  "[InitProcessEnabled](#cfn-ecs-daemontaskdefinition-linuxparameters-initprocessenabled)" : {{Boolean}},
  "[Tmpfs](#cfn-ecs-daemontaskdefinition-linuxparameters-tmpfs)" : {{[ Tmpfs, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-linuxparameters-syntax.yaml"></a>

```
  [Capabilities](#cfn-ecs-daemontaskdefinition-linuxparameters-capabilities): {{
    KernelCapabilities}}
  [Devices](#cfn-ecs-daemontaskdefinition-linuxparameters-devices): {{
    - Device}}
  [InitProcessEnabled](#cfn-ecs-daemontaskdefinition-linuxparameters-initprocessenabled): {{Boolean}}
  [Tmpfs](#cfn-ecs-daemontaskdefinition-linuxparameters-tmpfs): {{
    - Tmpfs}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-linuxparameters-properties"></a>

`Capabilities`  <a name="cfn-ecs-daemontaskdefinition-linuxparameters-capabilities"></a>
The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
For tasks that use the Fargate launch type, `capabilities` is supported for all platform versions but the `add` parameter is only supported if using platform version 1.4.0 or later.
*Required*: No
*Type*: [KernelCapabilities](aws-properties-ecs-daemontaskdefinition-kernelcapabilities.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Devices`  <a name="cfn-ecs-daemontaskdefinition-linuxparameters-devices"></a>
Any host devices to expose to the container. This parameter maps to `Devices` in the docker container create command and the `--device` option to docker run.
If you're using tasks that use the Fargate launch type, the `devices` parameter isn't supported.
*Required*: No
*Type*: Array of [Device](aws-properties-ecs-daemontaskdefinition-device.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InitProcessEnabled`  <a name="cfn-ecs-daemontaskdefinition-linuxparameters-initprocessenabled"></a>
Run an `init` process inside the container that forwards signals and reaps processes. This parameter maps to the `--init` option to docker run. This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version --format '{{.Server.APIVersion}}'`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tmpfs`  <a name="cfn-ecs-daemontaskdefinition-linuxparameters-tmpfs"></a>
The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the `--tmpfs` option to docker run.
*Required*: No
*Type*: [Array](aws-properties-ecs-daemontaskdefinition-tmpfs.md) of [Tmpfs](aws-properties-ecs-daemontaskdefinition-tmpfs.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
