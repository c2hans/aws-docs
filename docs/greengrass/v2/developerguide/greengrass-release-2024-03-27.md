---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-03-27.html
---

# Release: AWS IoT Greengrass Core v2.12.3 software update on March 27, 2024
<a name="greengrass-release-2024-03-27"></a>

This release provides version 2.12.3 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** March 27, 2024

**Topics**
+ [Public component updates](#greengrass-2024-03-27-components)

## Public component updates
<a name="greengrass-2024-03-27-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.12.3 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-03-27.html) |
| Shadow manager | Version 2.3.7 of the [shadow manager component](shadow-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-03-27.html) |
| Fleet provisioning | Version 1.2.1 of the [AWS IoT fleet provisioning plugin](fleet-provisioning-changelog.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-03-27.html) |
| IP detector | Version 2.1.9 of the [disk spooler component](ip-detector-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-03-27.html) |
| Moquette MQTT 3.1.1 broker component | Version 2.3.6 of the [Moquette MQTT 3.1.1 broker component](mqtt-broker-moquette-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-03-27.html) |
| Lambda manager | Version 2.3.3 of the [Lambda manager component](lambda-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-03-27.html) |
| Local debug console | Version 2.4.2 of the [local debug console component](local-debug-console-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-03-27.html) |
