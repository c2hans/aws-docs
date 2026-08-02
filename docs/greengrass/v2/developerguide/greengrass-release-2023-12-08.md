---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-12-08.html
---

# Release: AWS IoT Greengrass Core v2.12.1 software update on December 8, 2023
<a name="greengrass-release-2023-12-08"></a>

This release provides version 2.12.1 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** December 8, 2023

**Topics**
+ [Public component updates](#greengrass-2023-12-08-components)

## Public component updates
<a name="greengrass-2023-12-08-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.12.1 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-12-08.html) |
| Client device auth | Version 2.4.5 of the [ client device auth component](client-device-auth-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-12-08.html) |
| Disk spooler | Version 1.0.2 of the [ disk spooler component](disk-spooler-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-12-08.html) |
| MQTT bridge | Version 2.3.1 of the [ disk spooler component](mqtt-bridge-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-12-08.html) |
| Stream manager | Version 2.1.12 of the [ stream manager component](stream-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-12-08.html) |
