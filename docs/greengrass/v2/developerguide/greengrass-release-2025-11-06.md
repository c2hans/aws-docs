---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-11-06.html
---

# Release: AWS IoT Greengrass Core v2.16.0 software update on November 6, 2025
<a name="greengrass-release-2025-11-06"></a>

This release provides version 2.16.0 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** November 6, 2025

**Topics**
+ [Public component updates](#greengrass-2025-11-06-components)

## Public component updates
<a name="greengrass-2025-11-06-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.16.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**New features**<br />   Nucleus now supports cgroups V2.   <br />**Bug fixes and improvements**<br />   Fixes an issue where Nucleus would not clean up stale deployments when a deployment was cancelled.    |
| Greengrass nucleus lite | Version 2.3.0 of the [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) is available.**New features**<br />   Support for [ using TPM 2.0](gg-lite-with-tpm-tutorial.md) for IoT Core MQTT authorization.    The sample apt packages now support more operating systems: Ubuntu 22.04, Ubuntu 24.04, Debian 12, and Debian 13.   RestartComponent IPC is now supported.   <br />**Bug fixes and improvements**<br />   Local deployments no longer need internet access.   GetConfiguration has been updated to match the Greengrass Nucleus runtime behavior. (**Breaking Change**)   General bug fixes and improvements.    |
| Shadow manager | Version 2.3.12 of the [shadow manager](shadow-manager-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where deployments were blocked when more than 1024 device shadows were configured.    |
| Log manager | Version 2.3.11 of the [log manager](log-manager-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where Log Manager runtime configuration grew indefinitely with stale information of uploaded log files.    |
| System log forwarder | Version 2.1.0 of the [system log forwarder](system-log-forwarder-component.md) is available.**Bug fixes and improvements**<br />   Updates the component recipe to properly support Greengrass nucleus.   Improved logging output when there are no logs to upload.   General bug fixes and improvements.    |
