---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-07-03.html
---

# Release: AWS IoT Greengrass Core v2.15.0 software update on July 3, 2025
<a name="greengrass-release-2025-07-03"></a>

This release provides version 2.15.0 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** July 3, 2025

**Topics**
+ [Public component updates](#greengrass-2025-07-03-components)

## Public component updates
<a name="greengrass-2025-07-03-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.15.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**New features**<br />   Adds telemetry feature to include host system information like CPU and OS details. For more information, see [telemetry metrics](telemetry.md#telemetry-metrics).   Adds `deploymentConfigurationTimeSource` configuration. For more information, see [Greengrass nucleus configuration](greengrass-nucleus-component.md#greengrass-nucleus-component-configuration).   **Bug fixes and improvements**<br />   Nucleus now prioritizes the use of local versions and artifacts by default, improving deployment consistency and reducing external dependencies. Users can override this behavior by specifying alternative preferences in the deployment document.   Adds a new warning log when a provided Windows user doesn't match the character set normally accepted by Windows.    |
| Greengrass CLI | Version 2.15.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.**Bug fixes and improvements**<br />   Adds a fix so that when the auth configuration changes, the component won't reinstall but will still restart.   General bug fixes and improvements.    |
| Greengrass nucleus lite | Version 2.2.0 of the [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) is available.**New features**<br />   Adds support for container image artifact URIs.   <br />**Bug fixes and improvements**<br />   General bug fixes and improvements.    |
| Log manager | Version 2.3.10 of the [log manager](log-manager-component.md) is available.**New features**<br />   Adds a new configuration key (`updateToTlogIntervalSec`) to control the frequency at which log-upload event details are persisted to the local transaction log (`config.tlog`).   <br />**Bug fixes and improvements**<br />   Improves log manager to refresh cloudwatch client for socket connection error.    |
| Secret manager | Version 2.2.6 of the [secret manager](secret-manager-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where secret manager fails to get a secret due to a slow or unresponsive Trusted Platform Module.    |
