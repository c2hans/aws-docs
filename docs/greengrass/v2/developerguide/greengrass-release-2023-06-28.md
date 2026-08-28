---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-06-28.html
---

# Release: AWS IoT Greengrass Core v2.11.0 software update on June 28, 2023
<a name="greengrass-release-2023-06-28"></a>

This release provides version 2.11.0 of the Greengrass nucleus component.

**Release date:** June 28, 2023

**Release highlights**
+ **Persistent disk spooler** – AWS IoT Greengrass now provides a persistent spooler implementation for messages spooled from Greengrass core devices to AWS IoT Core. This component will store these outbound messages on disk. For more information, see [Disk spooler](disk-spooler-component.md).
+ **Local deployment improvements** – You can now cancel local deployments, set deployment failing handling polices, and get detailed deployment status.
+ **Logging speed improvements** – Log upload speeds for the log manager component have been improved.

**Topics**
+ [Public component updates](#greengrass-2023-06-28-components)

## Public component updates
<a name="greengrass-2023-06-28-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.11.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.11.0"></a>**New features**<br />   Enables you to cancel a local deployment.   Enables you to configure a failure handling policy for a local deployment.   Adds support for a disk spooler plugin.    |
| Greengrass CLI | Version 2.11.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.<a name="changelog-cli-2.11.0"></a>**New features**<br />   Enables you to cancel a local deployment.   Enables you to configure a failure handling policy for a local deployment.   Improves detailed deployment status reporting.    |
| Disk spooler | Version 1.0.0 of the [disk spooler](disk-spooler-component.md) component is available.+  The disk spooler component provides persistent storage of messages sent from Greengrass core devices to AWS IoT Core.  |
| Log manager | Version 2.3.5 of the [log manager](log-manager-component.md) component is available.<a name="changelog-log-manager-2.3.5"></a>**Improvements**<br /> Improves log upload speed.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
