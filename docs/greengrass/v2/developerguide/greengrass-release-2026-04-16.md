---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-04-16.html
---

# Release: AWS IoT Greengrass Core v2.17.0 software update on April 16, 2026
<a name="greengrass-release-2026-04-16"></a>

This release provides version 2.17.0 of the Greengrass nucleus component, version 2.5.0 of the Greengrass nucleus lite component, and updates to AWS-provided components.

**Release date:** April 16, 2026

**Topics**
+ [Public component updates](#greengrass-2026-04-16-components)

## Public component updates
<a name="greengrass-2026-04-16-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | Version 2.17.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-04-16.html) |
| [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) | Version 2.5.0 of the [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-04-16.html) |
| [Stream manager](stream-manager-component.md) | Version 2.3.0 of the [stream manager](stream-manager-component.md) is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-04-16.html) |
| [Greengrass CLI](greengrass-cli-component.md) | <a name="changelog-cli-2.17.0"></a>Version 2.17.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.<br />Updates the component version for the Greengrass nucleus v2.17.0 release. |
| [Secure tunneling](secure-tunneling-component.md) | Version 2.0.0 of the [secure tunneling](secure-tunneling-component.md) component is available.[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-04-16.html) |
