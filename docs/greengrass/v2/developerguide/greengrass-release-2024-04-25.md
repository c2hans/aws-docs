---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2024-04-25.html
---

# Release: AWS IoT Greengrass Core v2.12.5 software update on April 25, 2024
<a name="greengrass-release-2024-04-25"></a>

This release provides version 2.12.5 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** April 25, 2024

**Topics**
+ [Public component updates](#greengrass-2024-04-25-components)

## Public component updates
<a name="greengrass-2024-04-25-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.12.5 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where deployment rollback occasionally gets stuck while rolling back a previously broken component with hard dependencies.   Fixes an issue where the nucleus doesn't publish status updates after fleet provisioning.   Adds retries for the `GetDeploymentConfiguration` API after getting 404 errors.    |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
