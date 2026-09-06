---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-02-15.html
---

# Release: AWS IoT Greengrass Core v2.12.2 software update on February 15, 2024
<a name="greengrass-release-2024-02-15"></a>

This release provides version 2.12.2 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** February 15, 2024

**Topics**
+ [Public component updates](#greengrass-2024-02-15-components)

## Public component updates
<a name="greengrass-2024-02-15-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.12.2 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where old logs weren't cleaned up properly.   General bug fixes and improvements.    |
| Shadow manager | Version 2.3.6 of the [shadow manager component](shadow-manager-component.md) is available.**Bug fixes and improvements**<br /> Fixes an issue where shadow properties that are deleted through AWS Cloud updates while the device is offline continue to exist in the local shadow after regaining connectivity.  |
| Lambda launcher | Version 2.0.13 of the [lambda launcher component](lambda-launcher-component.md) is available.**Bug fixes and improvements**<br /> General bug fixes and improvements.  |
| Disk spooler | Version 1.0.3 of the [disk spooler component](disk-spooler-component.md) is available.**Bug fixes and improvements**<br /> Improves performance by reusing database connections.  |
