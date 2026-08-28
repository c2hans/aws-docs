---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2022-12-22.html
---

# Release: AWS IoT Greengrass Core v2.9.2 software update on December 22, 2022
<a name="greengrass-release-2022-12-22"></a>

This release provides version 2.9.2 of the Greengrass nucleus component.

**Release date:** December 22, 2022

**Topics**
+ [Public component updates](#greengrass-2022-12-22-components)

## Public component updates
<a name="greengrass-2022-12-22-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.9.2 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.9.2"></a>**Bug fixes and improvements**<br />   Fixes an issue where configuring `interpolateComponentConfiguration` doesn't apply to an ongoing deployment.   Uses OSHI to list all child processes.    |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
