---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2022-11-15.html
---

# Release: AWS IoT Greengrass Core v2.9.0 software update on November 15, 2022
<a name="greengrass-release-2022-11-15"></a>

This release provides version 2.9.0 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** November 15, 2022

**Release highlights**
+ **Offline authentication** – AWS IoT Greengrass now supports offline authentication. You can configure your AWS IoT Greengrass core device so that client devices can connect to a core device, even when the core device isn't connected to the cloud. For more information, see [Offline authentication](https://docs.aws.amazon.com/greengrass/v2/developerguide/offline-authentication.html).
+ **Subdeployments** – You can now create subdeployments. You can use a subdeployment to resolve unsuccessful deployments. Each subdeployment can test a different configuration of an unsuccessful deployment on a smaller subset of devices. For more information, see [Create subdeployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-subdeployments.html).

**Topics**
+ [Public component updates](#greengrass-2022-11-15-components)

## Public component updates
<a name="greengrass-2022-11-15-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.9.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.9.0"></a>**New features**<br />   Adds the ability to create subdeployments that retry deployments with a smaller subset of devices. This feature creates a more efficient way to test and resolve unsuccessful deployments.   <br />**Bug fixes and improvements**<br />   Improves support for systems that don't have `useradd`, `groupadd`, and `usermod`.   Additional minor fixes and improvements.    |
| Client device auth | Version 2.3.0 of the [client device auth component](client-device-auth-component.md) is available.<a name="changelog-client-device-auth-2.3.0"></a>**New features**<br />   Adds support for offline authentication of client devices. With this feature, client devices can continue to connect to the core device when the core device isn't connected to the Internet.   Adds support for customer-provided certificate authorities (CA). Your core device uses a customer-provided CA as the root certificate to generate MQTT broker certificates.    |
| MQTT 5 broker (EMQX) | Version 1.2.0 of the [MQTT 5 broker (EMQX)](mqtt-broker-emqx-component.md) component is available.<a name="changelog-emqx-1.2.0"></a>**New features**<br /> Adds support for certificate chains.  |
| Moquette MQTT broker | Version 2.3.0 of the new [Moquette MQTT broker component](mqtt-broker-moquette-component.md) is available.<a name="changelog-moquette-2.3.0"></a>**New features**<br /> Adds support for certificate chains.  |
| Secret manager | Version 2.1.4 of the new [secret manager](secret-manager-component.md) is available.<a name="changelog-secret-manager-2.3.0"></a>**Bug fixes and improvements**<br /> Fixes an issue where cached secrets were being removed when secret manager is deployed and Greengrass nucleus restarts.  |
| Stream manager | Version 2.1.2 of the new [stream manager](stream-manager-component.md) is available.<a name="changelog-stream-manager-2.1.2"></a>**Bug fixes and improvements**<br /> Fixes an issue on Windows OS that use a non-English language.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
