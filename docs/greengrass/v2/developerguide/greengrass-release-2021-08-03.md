---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2021-08-03.html
---

# Release: AWS IoT Greengrass Core v2.4.0 software update on August 3, 2021
<a name="greengrass-release-2021-08-03"></a>

This release provides version 2.4.0 of the Greengrass nucleus component, new AWS-provided components, and updates to AWS-provided components.

**Release date:** August 3, 2021

**Release highlights**
+ **System resource limits**—The Greengrass nucleus component now supports system resource limits. You can configure the maximum amount of CPU and RAM usage that each component's processes can use on the core device. For more information, see [Configure system resource limits for components](configure-greengrass-core-v2.md#configure-component-system-resource-limits).
+ **Pause/resume components**—The Greengrass nucleus now supports pausing and resuming components. You can use the interprocess communication (IPC) library to develop custom components that pause and resume other components' processes. For more information, see [PauseComponent](ipc-component-lifecycle.md#ipc-operation-pausecomponent) and [ResumeComponent](ipc-component-lifecycle.md#ipc-operation-resumecomponent).
+ **Install with AWS IoT fleet provisioning**—Use the new AWS IoT fleet provisioning plugin to install the AWS IoT Greengrass Core software on devices that connect to AWS IoT to provision required AWS resources. Devices use a claim certificate to provision. You can embed the claim certificate on devices during manufacturing, so each device can provision as soon as it comes online. For more information, see [Install AWS IoT Greengrass Core software with AWS IoT fleet provisioning](fleet-provisioning.md).
+ **Install with custom provisioning**—Develop a custom provisioning plugin to provision required AWS resources when you install the AWS IoT Greengrass Core software on devices. You can create a Java application that runs during installation to set up Greengrass core devices for your custom use case. For more information, see [Install AWS IoT Greengrass Core software with custom resource provisioning](custom-provisioning.md).

**Topics**
+ [Public component updates](#greengrass-2021-08-03-components)

## Public component updates
<a name="greengrass-2021-08-03-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.4.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.4.0"></a>**New features**<br />   Adds support for system resource limits. You can configure the maximum amount of CPU and RAM usage that each component's processes can use on the core device. For more information, see [Configure system resource limits for components](configure-greengrass-core-v2.md#configure-component-system-resource-limits).   Adds IPC operations to pause and resume components. For more information, see [PauseComponent](ipc-component-lifecycle.md#ipc-operation-pausecomponent) and [ResumeComponent](ipc-component-lifecycle.md#ipc-operation-resumecomponent).   Adds support for provisioning plugins. You can specify a JAR file to run during installation to provision required AWS resources for a Greengrass core device. The Greengrass nucleus includes an interface that you can implement to develop custom provisioning plugins. For more information, see [Install AWS IoT Greengrass Core software with custom resource provisioning](custom-provisioning.md).   Adds the optional `thing-name-policy` argument to the AWS IoT Greengrass Core software installer. You can use this option to specify an existing or custom AWS IoT policy when you [install the AWS IoT Greengrass Core software with automatic resource provisioning](quick-installation.md).   <br />**Bug fixes and improvements**<br />   Updates logging configuration on startup. This fixes an issue where the logging configuration wasn't applied on startup.   Updates the nucleus loader symlink to point to the component store in the Greengrass root folder during installation. This update enables you to delete the JAR file and other nucleus artifacts that you download when you install the AWS IoT Greengrass Core software.   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.    |
| Greengrass CLI | Version 2.4.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.<a name="changelog-greengrass-cli-2.4.0"></a>**New features**<br />   Adds support for system resource limits. When you create a local deployment, you can configure the maximum amount of CPU and RAM usage that each component's processes can use on the core device. For more information, see [Configure system resource limits for components](configure-greengrass-core-v2.md#configure-component-system-resource-limits) and the [deployment create command](gg-cli-deployment.md#deployment-create).    |
| AWS IoT fleet provisioning by claim | The AWS IoT fleet provisioning by claim plugin is now available. For more information, see [Install AWS IoT Greengrass Core software with AWS IoT fleet provisioning](fleet-provisioning.md).**New features**<br />   Adds support to install the AWS IoT Greengrass Core software with AWS IoT fleet provisioning. During installation, devices connect to AWS IoT to provision required AWS resources and download device certificates to use for regular operations.    |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
