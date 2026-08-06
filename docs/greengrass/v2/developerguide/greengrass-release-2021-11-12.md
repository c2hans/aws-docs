---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2021-11-12.html
---

# Release: AWS IoT Greengrass Core v2.5.0 software update on November 12, 2021
<a name="greengrass-release-2021-11-12"></a>

This release provides version 2.5.0 of the Greengrass nucleus component, new AWS-provided components, and updates to AWS-provided components.

**Release date:** November 12, 2021

**Release highlights**
+ **Windows device support**—You can now run the AWS IoT Greengrass Core software on devices running Windows operating systems. For more information, see [Greengrass feature compatibility](operating-system-feature-support-matrix.md).
+ **New thing group removal behavior**—You can now remove a core device from a thing group to remove that thing group's components in the next deployment to that device.
**Important**
<a name="greengrass-nucleus-v2.5.0-thing-group-removal-permission-requirement"></a>As a result of this change, a core device's AWS IoT policy must have the `greengrass:ListThingGroupsForCoreDevice` permission. If you used the [AWS IoT Greengrass Core software installer to provision resources](quick-installation.md), the default AWS IoT policy allows `greengrass:*`, which includes this permission. For more information, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).
+ **Hardware security support**—You can now configure the AWS IoT Greengrass Core software to use a hardware security module (HSM), so you can securely store the device's private key and certificate. For more information, see [Hardware security integration](hardware-security.md).
+ **HTTPS proxy support**—You can now configure the AWS IoT Greengrass Core software to connect through HTTPS proxies. For more information, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy).

**Topics**
+ [Platform support updates](#greengrass-2021-11-12-platforms)
+ [Public component updates](#greengrass-2021-11-12-components)

## Platform support updates
<a name="greengrass-2021-11-12-platforms"></a>

| **Platform** | **Details** |
| --- | --- |
| Windows | AWS IoT Greengrass now supports running the AWS IoT Greengrass Core software on the following versions of Windows:+  Windows 10 <br />+  Windows Server 2019 <br />For more information, see [Greengrass feature compatibility](operating-system-feature-support-matrix.md). |

## Public component updates
<a name="greengrass-2021-11-12-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.5.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.5.0"></a>**New features**<br />   Adds support for core devices that run Windows.   Change the behavior of thing group removal. With this version, you can remove a core device from a thing group to uninstall that thing group's components in the next deployment. <br /><a name="greengrass-nucleus-v2.5.0-thing-group-removal-permission-requirement"></a>As a result of this change, a core device's AWS IoT policy must have the `greengrass:ListThingGroupsForCoreDevice` permission. If you used the [AWS IoT Greengrass Core software installer to provision resources](quick-installation.md), the default AWS IoT policy allows `greengrass:*`, which includes this permission. For more information, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).   Adds support for HTTPS proxy configurations. For more information, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy).   Adds the new `windowsUser` configuration parameter. You can use this parameter to specify the default user to use to run components on a Windows core device. For more information, see [Configure the user that runs components](configure-greengrass-core-v2.md#configure-component-user).   Adds the new `httpClient` configuration options that you can use to customize HTTP request timeouts to improve performance on slow networks. For more information, see the [httpClient](greengrass-nucleus-component.md#greengrass-nucleus-component-configuration-http-client) configuration parameter.   <br />**Bug fixes and improvements**<br />   Fixes the bootstrap lifecycle option to restart the core device from a component.   Adds support for hyphens in recipe variables.   Fixes IPC authorization for on-demand Lambda function components.   Improves log messages and changes non-critical logs from `INFO` to `DEBUG` level, so logs are more useful.   Removes the `iot:DescribeCertificate` permission from the default [token exchange role](device-service-role.md) that the Greengrass nucleus creates when you [install the AWS IoT Greengrass Core software with automatic provisioning](quick-installation.md). This permission isn't used by the Greengrass nucleus.   Fixes an issue so that the automatic provisioning script doesn't require the `iam:GetPolicy` permission if `iam:CreatePolicy` is available for the same policy.   Additional minor fixes and improvements.    |
| Greengrass CLI | Version 2.5.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.<a name="changelog-greengrass-cli-2.5.0"></a>**New features**<br />   Adds support for core devices that run Windows.   Adds the new `AuthorizedWindowsGroups` configuration parameter that you can specify to authorize system groups to use the Greengrass CLI on Windows devices.   Adds the `windowsUser` parameter for local deployments. You can use this parameter specify the user to use to run components on a Windows core device.    |
| CloudWatch metrics | Version 3.0.0 of the [CloudWatch metrics](cloudwatch-metrics-component.md) component is available.<br /><a name="changelog-cloudwatch-metrics-3.0.0-major-version-changes"></a>This version of the CloudWatch metrics component expects different configuration parameters than version 2.x. If you use a non-default configuration for version 2.x, and you want to upgrade from v2.x to v3.x, you must update the component's configuration. For more information, see [CloudWatch metrics component configuration](cloudwatch-metrics-component.md#cloudwatch-metrics-component-configuration).<a name="changelog-cloudwatch-metrics-3.0.0"></a>**New features**<br />   Adds support for core devices that run Windows.   Changes the component type from Lambda component to generic component. This component now no longer depends on the legacy subscription router component to create subscriptions.    Adds new `InputTopic` configuration parameter to specify the topic to which the component subscribes to receive messages.   Adds new `OutputTopic` configuration parameter to specify the topic to which the component publishes status responses.   Adds new `PubSubToIoTCore` configuration parameter to specify whether to publish and subscribe to AWS IoT Core MQTT topics.   Adds the new `UseInstaller` configuration parameter that lets you optionally disable the installation script that installs component dependencies.   <br />**Bug fixes and improvements**<br /> Adds support for duplicate timestamps in input data.  |
| Lambda manager | Version 2.2.0 of the [Lambda manager](lambda-manager-component.md) component is available.<a name="changelog-lambda-manager-2.2.0"></a>**Bug fixes and improvements**<br />   Fixes an issue where Lambda functions couldn't write logs after a restart.   Fixes an issue where the legacy subscription router sends duplicate messages when there are wildcards in the topic.   Fixes an issue where non-pinned Lambda functions couldn't use the Greengrass interprocess communication (IPC) library in the AWS IoT Device SDK.    |
