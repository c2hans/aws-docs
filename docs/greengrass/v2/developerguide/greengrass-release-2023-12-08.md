---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-12-08.html
---

# Release: AWS IoT Greengrass Core v2.12.1 software update on December 8, 2023
<a name="greengrass-release-2023-12-08"></a>

This release provides version 2.12.1 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** December 8, 2023

**Topics**
+ [Public component updates](#greengrass-2023-12-08-components)

## Public component updates
<a name="greengrass-2023-12-08-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.12.1 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where the nucleus may duplicate MQTT subscriptions to deployment topics leading to additional logging and MQTT publishes.    |
| Client device auth | Version 2.4.5 of the [ client device auth component](client-device-auth-component.md) is available.**New features**<br /> Adds support for wildcard prefixes for selecting thing names with the `selectionRule` parameter. <br />**Bug fixes and improvements**<br /> Fixes an issue where certificates aren't updated with new connectivity information in certain cases.  |
| Disk spooler | Version 1.0.2 of the [ disk spooler component](disk-spooler-component.md) is available.**Bug fixes and improvements**<br /> Fixes an issue where the MQTT message format field isn't persisted in certain cases.  |
| MQTT bridge | Version 2.3.1 of the [ disk spooler component](mqtt-bridge-component.md) is available.**Bug fixes and improvements**<br /> Fixes an issue where the local MQTT client gets into a disconnect loop.  |
| Stream manager | Version 2.1.12 of the [ stream manager component](stream-manager-component.md) is available.**Bug fixes and improvements**<br /> Updates the order that credentials are used so that Greengrass credentials are preferred for AWS service requests.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
