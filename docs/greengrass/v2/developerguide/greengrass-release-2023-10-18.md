---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-10-18.html
---

# Release: AWS IoT Greengrass Core v2.11.3 software update on October 18, 2023
<a name="greengrass-release-2023-10-18"></a>

This release provides version 2.11.3 of the Greengrass nucleus component.

**Release date:** October 18, 2023

**Topics**
+ [Public component updates](#greengrass-2023-10-18-components)

## Public component updates
<a name="greengrass-2023-10-18-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.11.3 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.11.3"></a>**Bug fixes and improvements**<br />   Fixes an issue in the nucleus where it may improperly start a component when its dependencies fail.   <br />**New features**<br />   Adds configurable s3 endpoint type.    |
| Lambda manager | Version 2.3.1 of the [Lambda manager](lambda-manager-component.md) component is available.<a name="changelog-lambda-manager-2.3.1"></a>**Bug fixes and improvements**<br />   Adjusts log levels for certain errors.    |
| Local deubg console | Version 2.4.0 of the [Lambda manager](local-debug-console-component.md) component is available.<a name="changelog-local-debug-console-2.4.0"></a>**New features**<br />   Adds stream manager debugging console.    |
| Log manager | Version 2.3.6 of the [log manager](log-manager-component.md) component is available.<a name="changelog-log-manager-2.3.6"></a>**Bug fixes and improvements**<br />   Adjusts log levels for certain errors.    |
| Shadow manager | Version 2.3.4 of the [Shadow manager](shadow-manager-component.md) component is available.<a name="changelog-shadow-manager-2.3.4"></a>**Bug fixes and improvements**<br />   Adds support for null and empty shadow state documents.    |
