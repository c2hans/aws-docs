---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-05.html
---

# Release: AWS IoT Greengrass Core v2.10.2 software update on June 5, 2023
<a name="greengrass-release-2023-06-05"></a>

This release provides version 2.10.2 of the Greengrass nucleus component.

**Release date:** June 5, 2023

**Topics**
+ [Public component updates](#greengrass-2023-06-05-components)

## Public component updates
<a name="greengrass-2023-06-05-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.10.2 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.10.2"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-05.html) |
| Client device auth | Version 2.4.2 of the [client device auth](client-device-auth-component.md) component is available.<a name="changelog-client-device-auth-2.4.2"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-05.html) |
| Lambda manager | Version 2.2.9 of the [Lambda manager](lambda-manager-component.md) component is available.<a name="changelog-lambda-manager-2.2.9"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-05.html) |
| Log manager | Version 2.3.4 of the [log manager](log-manager-component.md) component is available.<a name="changelog-log-manager-2.3.4"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-05.html) |
| MQTT 3.1 broker (Moquette) | Version 2.3.3 of the [MQTT 3.1 broker (Moquette)](mqtt-broker-moquette-component.md) component is available.<a name="changelog-mqtt-broker-moquette-2.3.3"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-05.html) |
| MQTT bridge | Version 2.2.6 of the [MQTT bridge](mqtt-bridge-component.md) component is available.<a name="changelog-mqtt-bridge-2.2.6"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-05.html) |
| Stream manager | Version 2.1.7 of the [stream manager](stream-manager-component.md) component is available.<a name="changelog-stream-manager-2.1.7"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-05.html) |
