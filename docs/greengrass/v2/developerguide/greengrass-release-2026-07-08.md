---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-07-08.html
---

# Release: AWS IoT Greengrass Core v2.18.0 software update on July 8, 2026
<a name="greengrass-release-2026-07-08"></a>

This release provides version 2.18.0 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** July 8, 2026

**Topics**
+ [Public component updates](#greengrass-2026-07-08-components)

## Public component updates
<a name="greengrass-2026-07-08-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | Version 2.18.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-07-08.html) |
| [Stream manager](stream-manager-component.md) | Version 2.3.1 of the [stream manager](stream-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-07-08.html) |
| [Shadow manager](shadow-manager-component.md) | Version 2.3.15 of the [shadow manager](shadow-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-07-08.html) |
| [MQTT bridge](mqtt-bridge-component.md) | Version 2.3.3 of the [MQTT bridge](mqtt-bridge-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-07-08.html) |
| [Secret manager](secret-manager-component.md) | Version 2.2.9 of the [secret manager](secret-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-07-08.html) |
| [Greengrass CLI](greengrass-cli-component.md) | <a name="changelog-cli-2.18.0"></a>Version 2.18.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.<br />Updates the component version for the Greengrass nucleus version 2.18.0 release. |
| [Secure tunneling](secure-tunneling-component.md) | Version 2.0.1 of the [secure tunneling](secure-tunneling-component.md) component is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-07-08.html) |
