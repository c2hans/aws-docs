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
| Greengrass nucleus | Version 2.16.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-11-06.html) |
| Greengrass nucleus lite | Version 2.3.0 of the [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-11-06.html) |
| Shadow manager | Version 2.3.12 of the [shadow manager](shadow-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-11-06.html) |
| Log manager | Version 2.3.11 of the [log manager](log-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-11-06.html) |
| System log forwarder | Version 2.1.0 of the [system log forwarder](system-log-forwarder-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-11-06.html) |
