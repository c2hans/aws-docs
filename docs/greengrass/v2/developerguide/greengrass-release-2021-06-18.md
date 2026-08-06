---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2021-06-18.html
---

# Release: AWS IoT Greengrass Core v2.2.0 software update on June 18, 2021
<a name="greengrass-release-2021-06-18"></a>

This release provides version 2.2.0 of the Greengrass nucleus component, new AWS-provided components, and updates to AWS-provided components.

**Release date:** June 18, 2021

**Release highlights**
+ **Client device support**—The new AWS-provided client device components enable you to connect client devices to your core devices using cloud discovery. You can sync client devices with AWS IoT Core and interact with client devices in Greengrass components. For more information, see [Interact with local IoT devices](interact-with-local-iot-devices.md).
+ **Local shadow service**—The new shadow manager component enables the local shadow service on your core devices. You can use this shadow service to interact with local shadows while offline using the Greengrass interprocess communication (IPC) libraries in the AWS IoT Device SDK. You can also use the shadow manager component to synchronize local shadow states with AWS IoT Core. For more information, see [Interact with device shadows](interact-with-shadows.md).

**Topics**
+ [Public component updates](#greengrass-2021-06-18-components)

## Public component updates
<a name="greengrass-2021-06-18-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.2.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.2.0"></a>**New features**<br />   Adds IPC operations for local shadow management.   <br />**Bug fixes and improvements**<br />   Reduces the size of the JAR file.   Reduces memory usage.   Fixes issues where the log configuration wasn't updated in certain cases.   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.    |
| Shadow manager | Version 2.0.0 of the new [shadow manager component](shadow-manager-component.md) is available.**New features**<br />   Adds support for classic and named shadows.   Adds support for local shadow management using IPC.   Adds support for shadow synchronization with AWS IoT Core.    |
| Client device auth | Version 2.0.0 of the new [client device auth component](client-device-auth-component.md) is available.**New features**<br />   Adds support for Greengrass client devices, which are local IoT devices that connect to a core device over MQTT.   Adds support for authentication and authorization of client devices and their MQTT actions.    |
| Moquette MQTT broker | Version 2.0.0 of the new [Moquette MQTT broker component](mqtt-broker-moquette-component.md) is available.**New features**<br />   Adds support for a local Moquette MQTT broker that handles communication with client devices.    |
| MQTT bridge | Version 2.0.0 of the new [MQTT bridge component](mqtt-bridge-component.md) is available.**New features**<br />   Adds support to relay messages between the local MQTT broker, the local Greengrass publish/subscribe broker, and the AWS IoT Core MQTT broker.    |
| IP detector | Version 2.0.0 of the new [IP detector component](ip-detector-component.md) is available.**New features**<br />   Adds support to report a core device's local MQTT broker endpoints to the AWS IoT Greengrass cloud service for client devices to connect.    |
| Log manager | Version 2.1.1 of the [log manager component](log-manager-component.md) is available.<a name="changelog-log-manager-2.1.1"></a>**Bug fixes and improvements**<br />   Fixes an issue where the system log configuration wasn't updated in certain cases.    |
| DLR object detection | Version 2.1.2 of the [DLR object detection](dlr-object-detection-component.md) is available.<a name="changelog-dlr-object-detection-2.1.2"></a>**Bug fixes and improvements**<br />   Fixes an image scaling issue that resulted in inaccurate bounding boxes in the sample DLR object detection inference results.    |
| TensorFlow Lite object detection | Version 2.1.1 of the [TensorFlow Lite object detection](tensorflow-lite-object-detection-component.md) is available.<a name="changelog-tensorflow-lite-object-detection-2.1.1"></a>**Bug fixes and improvements**<br />   Fixes an image scaling issue that resulted in inaccurate bounding boxes in the sample TensorFlow Lite object detection inference results.    |
