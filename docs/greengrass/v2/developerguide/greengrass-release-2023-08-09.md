---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-08-09.html
---

# Release: AWS IoT Greengrass Core v2.11.2 software update on August 9, 2023
<a name="greengrass-release-2023-08-09"></a>

This release provides version 2.11.2 of the Greengrass nucleus component.

**Release date:** August 9, 2023

**Topics**
+ [Public component updates](#greengrass-2023-08-09-components)

## Public component updates
<a name="greengrass-2023-08-09-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.11.2 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.11.2"></a>**Bug fixes and improvements**<br />   Fixes an issue in the nucleus MQTT 5 client where it may appear offline when a large number (> 50) of subscriptions are in use.   Adds a retry for the docker dial TCP failure.    |
