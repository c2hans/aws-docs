---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-12-16.html
---

# Release: AWS IoT Greengrass Core v2.14.0 software update on December 16, 2024
<a name="greengrass-release-2024-12-16"></a>

This release provides version 2.14.0 of the Greengrass nucleus component, and new AWS IoT Greengrass nucleus lite updates. The AWS IoT Greengrass nucleus lite is a new runtime, available for AWS IoT Greengrass version 2. It provides a reduced memory footprint alternative. This is a good option for resource-constrained devices. It implements a subset of the nucleus functionality with increased featured compatibility planned for future releases. The source code is available now on [Github](https://github.com/aws-greengrass/aws-greengrass-lite). With the nucleus lite runtime you can:
+ Deploy components to Greengrass core devices. Use the same recipe format, though some advanced features may not be available yet.
+ Applications deployed as Greengrass components can use the device SDKs to access the supported Greengrass IPC APIs, such as: AWS IoT Core MQTT access, local pub/sub, and Greengrass configuration access. See the compatibility chart for the list of [supported IPC APIs](https://docs.aws.amazon.com/greengrass/v2/developerguide/choosing-your-runtime.html).
+ Some AWS managed components have been updated for nucleus lite support. See the [AWS-provided components](https://docs.aws.amazon.com/greengrass/v2/developerguide/public-components.html) for a list of existing compatible components.

**New features:**
+ Uses less memory and disk space (less than 5MB of RAM and less than 5MB of storage).
+ Components integrate with the host system’s service manager (systemd for currently supported Linux platforms).

**Things to watch out for:**
+ AWS IoT Greengrass nucleus lite recipes are case-sensitive. Ensure the correct (keys) casing is used as in the [https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html)recipe reference.
+ The nucleus lite runtime supports **thing group** deployments, and does not yet support the (single) **Core device** deployment target type. To deploy to a single Greengrass device, use a thing group with only that one device in it.
+ The nucleus lite runtime uses bounded memory resources; functionality which scales according to usage on the classic runtime may fail due to exceeding resources available on lite. This includes a current limitation on max of 50 MQTT subscriptions at a time, and maximum limits on recipe file sizes and deployments. Some of these limits are configurable at compile time if compiling the lite runtime yourself.
+ The nucleus lite runtime does not ship with Java. To use components requiring Java, the system will need Java already installed, or a component may be used to install Java.
+ We recommend compiling the nucleus lite runtime from source and using your own build tailored for your system. For Yocto systems, a layer is available to integrate the nucleus lite runtime into your system image.
+ Currently the nucleus lite assumes a Linux system using *systemd*, or a container image using *systemd*.
+ While you can manage Docker containers with recipe scripts, Greengrass managed container artifacts are not yet available.
+ The nucleus lite runtime does not yet have support for keys stored in a PKCS11 module. If your use case requires keys stored on a secure element, the classic runtime can support this use case currently. To prevent leaks of your device credentials, ensure production devices are using full disk encryption.

Alongside the introduction of nucleus lite, we are also releasing nucleus v2.14.0. This update brings significant enhancements to the existing Greengrass nucleus.

**Key features and improvements:**
+ New dual-stack endpoint support enables IPv6 network communication.
+ Enhanced resilience against nucleus restart failures and directory corruption.
+ Fixed memory leaks in IPC PubSub subscription closures.

**Release date:** December 16, 2024

## Public component updates
<a name="greengrass-2024-12-16-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus lite | Version 2.0.0 of the [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) is available.<a name="changelog-nucleus-2.0.0"></a>**New features**<br />   Uses less memory and disk space (less than 5MB of RAM and less than 5MB of storage).   Components integrate with the host system’s service manager (systemd for currently supported Linux platforms).    |
| Greengrass nucleus | Version 2.14.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**New features**<br />   New dual-stack endpoint support enables IPv6 network communication.  Enhanced resilience against nucleus restart failures and directory corruption.  <br />**Bug fixes and improvements**<br />   Fixed memory leaks in IPC PubSub subscription closures.   Fixes run lifecycle of the component where it enters into ERRORED state due to startup timeout when skipif condition is true.   Fixes an issue where the core device fails to connect to AWS IoT Core when the TLS policy is set to TLS13\_1\_3\_2022\_10.     |
| Greengrass CLI | Version 2.14.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**Bug fixes and improvements**<br />   Validate deployment target parameter in the cli command.     |
| Stream manager | Version 2.14.0 of the [Stream manager](stream-manager-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**New features**<br />   Adds a new configuration key for startup timeout. Default value is 120 seconds.   Add recipe supports for Greengrass nucleus lite.    |
| MQTT 5 broker (EMQX) | Version 2.0.2 of the [MQTT 5 broker (EMQX)](mqtt-broker-emqx-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**Bug fixes and improvements**<br />   Fixes an issue where EMQX starts up before the Client device auth component is ready.     |
| Lambda runtimes component | Version 2.0.9 of the [Lambda runtimes component](lambda-runtimes-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**Bug fixes and improvements**<br />   Fixes an syntax warning with Python 3.12    |
| Lambda manager component | Version 2.3.5 of the [Lambda manager component](lambda-manager-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**Bug fixes and improvements**<br />   Improves performance by using epoll instead of nio when available    |
| Secret manager component | Version 2.2.2 of the [Secret manager component](cloudwatch-metrics-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**Bug fixes and improvements**<br />   Fixes an issue where secret manager doesn’t download the secrets configured with partial arns.    |
| Secure tunneling component | Version 1.1.0 of the [Secure tunneling component](secure-tunneling-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**New features**<br />   Add recipe supports for Greengrass nucleus lite    |
| CloudWatch metrics component | Version 1.1.0 of the [CloudWatch metrics component](cloudwatch-metrics-component.md) is available.<a name="changelog-nucleus-2.14.0"></a>**New features**<br />   Add recipe supports for Greengrass nucleus lite    |
