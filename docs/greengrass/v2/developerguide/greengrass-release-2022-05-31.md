---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2022-05-31.html
---

# Release: AWS IoT Greengrass Core v2.5.6 software update on May 31, 2022
<a name="greengrass-release-2022-05-31"></a>

This release provides version 2.5.6 of the Greengrass nucleus component and version 2.2.4 of the log manager component.

**Release date:** May 31, 2022

**Topics**
+ [Public component updates](#greengrass-2022-05-31-components)

## Public component updates
<a name="greengrass-2022-05-31-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.5.6 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.5.6"></a>**New features**<br />   Adds support for hardware security modules that use ECC keys. You can use a hardware security module (HSM) to securely store the device's private key and certificate. For more information, see [Hardware security integration](hardware-security.md).   <br />**Bug fixes and improvements**<br />   Fixes an issue where the deployment never completes when you deploy a component with a broken install script in certain scenarios.   Improves performance during startup.   Additional minor fixes and improvements.    |
| Log manager | Version 2.2.4 of the [log manager](log-manager-component.md) component is available.<a name="changelog-log-manager-2.2.4"></a>**Bug fixes and improvements**<br />   Improves stability when handling invalid configurations.   Additional minor fixes and improvements.    |
