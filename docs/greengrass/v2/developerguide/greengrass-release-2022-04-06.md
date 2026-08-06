---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2022-04-06.html
---

# Release: AWS IoT Greengrass Core v2.5.5 software update on April 6, 2022
<a name="greengrass-release-2022-04-06"></a>

This release provides version 2.5.5 of the Greengrass nucleus component.

**Release date:** April 6, 2022

**Topics**
+ [Public component updates](#greengrass-2022-04-06-components)

## Public component updates
<a name="greengrass-2022-04-06-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.5.5 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.5.5"></a>**New features**<br />   Adds the `GG_ROOT_CA_PATH` environment variable for components, so you can access the root certificate authority (CA) certificate in custom components.   <br />**Bug fixes and improvements**<br />   Adds support for Windows devices that use a display language other than English.   Updates how the Greengrass nucleus parses Boolean [installer arguments](configure-installer.md), so you can specify a Boolean argument without a Boolean value to specify a `true` value. For example, you can now specify `--provision` instead of `--provision true` to install with automatic resource provisioning.   Fixes an issue where the core device didn't report its status to the AWS IoT Greengrass cloud service after provisioning in certain scenarios.   Additional minor fixes and improvements.    |
