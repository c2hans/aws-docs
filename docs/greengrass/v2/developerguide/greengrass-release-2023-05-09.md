---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-05-09.html
---

# Release: AWS IoT Greengrass Core v2.10.0 software update on May 9, 2023
<a name="greengrass-release-2023-05-09"></a>

This release provides version 2.10.0 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** May 9, 2023

**Release highlights**
+ **MQTT5 support** – AWS IoT Greengrass now supports sending and receiving messages from AWS IoT Core using MQTT5. For more information, see [Publish AWS IoT Core MQTT messages](https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-iot-core-mqtt.html#ipc-operation-publishtoiotcore).

**Topics**
+ [Public component updates](#greengrass-2023-05-09-components)

## Public component updates
<a name="greengrass-2023-05-09-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.10.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.10.0"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-05-09.html) |
| Shadow manager | Version 2.3.2 of the new [shadow manager](shadow-manager-component.md) is available.<a name="changelog-stream-manager-2.3.2"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-05-09.html) |
