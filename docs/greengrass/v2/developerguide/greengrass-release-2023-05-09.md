---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2023-05-09.html
---

# Release: AWS IoT Greengrass Core v2.10.0 software update on May 9, 2023
<a name="greengrass-release-2023-05-09"></a>

This release provides version 2.10.0 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** May 9, 2023

**Release highlights**
+ **MQTT5 support** – AWS IoT Greengrass now supports sending and receiving messages from AWS IoT Core using MQTT5. For more information, see [Publish AWS IoT Core MQTT messages](https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-iot-core-mqtt.html#ipc-operation-publishtoiotcore).

**Topics**
+ [Public component updates](#greengrass-2023-05-09-components)

## Public component updates
<a name="greengrass-2023-05-09-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.10.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.10.0"></a>**New features**<br />   Adds `interpolateComponentConfiguration` support for the empty regular expression. Greengrass now interpolates from the root config object.   Adds support for MQTT5.   Adds a mechanism for loading plugin components quickly without scanning.   Enables Greengrass to save disk space by deleting unused Docker images.   <br />**Bug fixes and improvements**<br />   Fixes an issue where rollback leaves certain configuration values in place from a deployment.   Fixes an issue where the Greengrass nucleus validates for an AWS domain sequence in custom non-AWS credentials and data endpoints.   Updates multi-group dependency resolution to re-resolve all group dependencies via AWS Cloud negotiation, instead of locking to the active version. This update also removes the deployment error code `INSTALLED_COMPONENT_NOT_FOUND`.   Updates the Greengrass nucleus to skip downloading Docker images when they already exist locally.   Updates the Greengrass nucleus to restart a component install step before timeout expires.   Additional minor fixes and improvements.    |
| Shadow manager | Version 2.3.2 of the new [shadow manager](shadow-manager-component.md) is available.<a name="changelog-stream-manager-2.3.2"></a>**Bug fixes and improvements**<br /> Fixes an issue where shadow manager enters the `BROKEN` state when the local shadow database is corrupted.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
