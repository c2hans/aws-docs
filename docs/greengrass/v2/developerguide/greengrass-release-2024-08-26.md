---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-08-26.html
---

# Release: AWS IoT Greengrass Core v2.13.0 software update on August 26, 2024
<a name="greengrass-release-2024-08-26"></a>

This release provides version 2.13.0 of the Greengrass nucleus component.

**Release date:** August 26, 2024

## Public component updates
<a name="greengrass-2024-08-26-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.13.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.13.0"></a>**New features**<br />   Support FIPS endpoint in Nucleus. For more information, see [FIPS endpoints](FIPS.md).   <br />**Bug fixes and improvements**<br />   Cancel deployment improvements - deployments can now be cancelled while new configuration is being merged and while waiting for services to start.    |
| Stream manager | Version 2.1.13 of the [Stream manager component](stream-manager-component.md) is available.<a name="changelog-nucleus-2.13.0"></a>**Bug fixes and improvements**<br />   Support FIPS endpoint in AWS IoT SiteWise    |
| Secret manager | Version 2.2.0 of the [Secret manager component](secret-manager-component.md) is available.<a name="changelog-nucleus-2.13.0"></a>**New features**<br />   Adds support for periodic refresh of configured secrets through a new component configuration key.   Adds support for a new request parameter in the **GetSecretValue** IPC request to refresh the secrets per request    |
| IP detector | Version 2.2.0 of the [IP detector component](ip-detector-component.md) is available.<a name="changelog-nucleus-2.13.0"></a>**New features**<br />   Adds support for IPv6. You can now use IPv6 for local messaging.    |
| Client device auth | Version 2.5.1 of the [Client device auth](client-device-auth-component.md) is available.<a name="changelog-nucleus-2.13.0"></a>**Bug fixes and improvements**<br />   General bugs and fixes.   Supports FIPS endpoint.    |
| Local debug console | Version 2.4.3 of the [Local debug console](local-debug-console-component.md) is available.<a name="changelog-nucleus-2.13.0"></a>**Bug fixes and improvements**<br />   Fixes an issue that incorrectly displayed STREAM\_MANAGER\_EXPORTER\_MAX\_BANDWIDTH in Mpbs instead of bytes/sec.    |
