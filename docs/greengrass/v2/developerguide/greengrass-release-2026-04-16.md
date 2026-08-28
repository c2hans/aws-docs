---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-04-16.html
---

# Release: AWS IoT Greengrass Core v2.17.0 software update on April 16, 2026
<a name="greengrass-release-2026-04-16"></a>

This release provides version 2.17.0 of the Greengrass nucleus component, version 2.5.0 of the Greengrass nucleus lite component, and updates to AWS-provided components.

**Release date:** April 16, 2026

**Topics**
+ [Public component updates](#greengrass-2026-04-16-components)

## Public component updates
<a name="greengrass-2026-04-16-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | Version 2.17.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**New features**<br />   Installs all Amazon Root CA certificates during auto-provisioning.   Adds an uninstall lifecycle that runs when a deployment removes a component.   Allows installing Greengrass Core software as a regular Linux user.    |
| [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) | Version 2.5.0 of the [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) is available.**New features**<br />   Adds PKCS\#11 support via OpenSSL Providers.   Adds support for using TPM with fleet provisioning.    |
| [Stream manager](stream-manager-component.md) | Version 2.3.0 of the [stream manager](stream-manager-component.md) is available.**Bug fixes and improvements**<br />   Updates to the AWS SDK for Java v2 for improved performance and compatibility.   Changes proxy precedence behavior to align with standard AWS SDK proxy configuration.    |
| [Greengrass CLI](greengrass-cli-component.md) | <a name="changelog-cli-2.17.0"></a>Version 2.17.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.<br />Updates the component version for the Greengrass nucleus v2.17.0 release. |
| [Secure tunneling](secure-tunneling-component.md) | Version 2.0.0 of the [secure tunneling](secure-tunneling-component.md) component is available.**New features**<br />   Replaces the Java wrapper with a C wrapper.   Replaces AWS IoT Device Client with [AWS IoT Securetunneling Localproxy](https://github.com/aws-samples/aws-iot-securetunneling-localproxy).   Reduces the binary size from approximately 36 MB to approximately 4 MB.   Reduces the memory footprint from approximately 100 MB to approximately 2 MB.    |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
