---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2025-11-06-2.15.1.html
---

# Release: AWS IoT Greengrass Core v2.15.1 software update on November 6, 2025
<a name="greengrass-release-2025-11-06-2.15.1"></a>

This release provides version 2.15.1 of the Greengrass nucleus component and version 2.15.1 of the Greengrass CLI component.

**Release date:** November 6, 2025

**Topics**
+ [Public component updates](#greengrass-2025-11-06-2.15.1-components)

## Public component updates
<a name="greengrass-2025-11-06-2.15.1-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md)<br />Version 2.15.1 | <a name="changelog-nucleus-2.15.1"></a> **Bug fixes and improvements**<br />   Fixes an issue where Nucleus failed to clean up component processes after the 30-second shutdown timeout during bootstrap deployments.     |
| [Greengrass CLI](greengrass-cli-component.md)<br />Version 2.15.1 | <a name="changelog-cli-2.15.1"></a>Version updated for the Greengrass Nucleus v2.15.1 release. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
