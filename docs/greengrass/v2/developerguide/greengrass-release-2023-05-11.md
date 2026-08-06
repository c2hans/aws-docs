---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-05-11.html
---

# Release: AWS IoT Greengrass Core v2.10.1 software update on May 11, 2023
<a name="greengrass-release-2023-05-11"></a>

This release provides version 2.10.1 of the Greengrass nucleus component.

**Release date:** May 11, 2023

**Topics**
+ [Public component updates](#greengrass-2023-05-11-components)

## Public component updates
<a name="greengrass-2023-05-11-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.10.1 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.10.1"></a>**Bug fixes and improvements**<br />   Fixes an issue that could cause a crash at startup on certain ARMv8 processors, including the Jetson Nano.   Greengrass no longer closes a component's standard in, this reverts the behavior to the pre-2.10.0 behavior    |
| Stream manager | Version 2.1.6 of the new [stream manager](stream-manager-component.md) is available.<a name="changelog-stream-manager-2.1.6"></a>**Bug fixes and improvements**<br /> Fixes an issue that could cause a crash at startup on certain ARMv8 processors, including the Jetson Nano.  |
