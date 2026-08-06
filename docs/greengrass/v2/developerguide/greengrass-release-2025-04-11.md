---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-04-11.html
---

# Release: AWS IoT Greengrass Core v2.14.3 software update on April 11, 2025
<a name="greengrass-release-2025-04-11"></a>

This release provides version 2.14.3 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** April 11, 2025

**Topics**
+ [Public component updates](#greengrass-2025-04-11-components)

## Public component updates
<a name="greengrass-2025-04-11-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.14.3 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**Bug fixes and improvements**<br />   Allows the token exchange service to restart on port configuration changes.   Fixes an issue where fleet status service doesn't send component status change messages for unpinned lambdas if they aren't triggered.   Fixes an issue where components aren't gracefully shutdown when a new component version is deployed.   Fixes an issue where built-in plugins’ injection hooks are executed twice resulting in extra lifecycle events and duplicate logging.   Improves component lifecycle logging on Windows devices.    |
| Greengrass CLI | Version 2.14.3 of the [Greengrass CLI](greengrass-cli-component.md) is available.**Bug fixes and improvements**<br />   Version updated for Greengrass nucleus version 2.14.3 release.    |
| Secret manager | Version 2.2.4 of the [secret manager](secret-manager-component.md) is available.**Bug fixes and improvements**<br />   Reduces the frequency of writes to the local secret store. Secret manager now writes to the local store only when secrets are updated.    |
| EMQX MQTT broker | Version 2.0.3 of the [EMQX MQTT broker](mqtt-broker-emqx-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where EMQX doesn't start on Windows if the path contains spaces.    |
