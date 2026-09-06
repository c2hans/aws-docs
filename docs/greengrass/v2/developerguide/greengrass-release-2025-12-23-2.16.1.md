---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-12-23-2.16.1.html
---

# Release: AWS IoT Greengrass Core v2.16.1 software update on December 23, 2025
<a name="greengrass-release-2025-12-23-2.16.1"></a>

This release provides version 2.16.1 of the Greengrass nucleus component and version 2.16.1 of the Greengrass CLI component.

**Release date:** December 23, 2025

## Public component updates
<a name="greengrass-2025-12-23-2.16.1-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | Version 2.16.1 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**Bug fixes and improvements**<br />   Adds configuration for credential retry intervals after Token Exchange Service failures.    |
| [Greengrass CLI](greengrass-cli-component.md) | <a name="changelog-cli-2.16.1"></a>Version 2.16.1 of the [Greengrass CLI](greengrass-cli-component.md) is available.<br />Version updated for the Greengrass Nucleus v2.16.1 release. |
