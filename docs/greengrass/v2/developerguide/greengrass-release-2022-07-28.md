---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2022-07-28.html
---

# Release: AWS IoT Greengrass Core v2.7.0 software update on July 28, 2022
<a name="greengrass-release-2022-07-28"></a>

This release provides version 2.7.0 of the Greengrass nucleus component, version 2.1.0 of the stream manager component, and version 2.2.5 of the Lambda manager component.

**Release date:** July 28, 2022

**Release highlights**
+ **Stream manager telemetry metrics** – Stream manager now automatically sends telemetry metrics to Amazon EventBridge, so you can create cloud applications that monitor and analyze the volume of data that your core devices upload. For more information, see [Gather system health telemetry data from AWS IoT Greengrass core devices](telemetry.md).
+ **Custom certificate authority (CA)** – Client certificates signed by a custom certificate CA, where the CA isn't registered with AWS IoT, are now supported. For more information, see [Use a device certificate signed by a private CA](configure-greengrass-core-v2.md#configure-nucleus-private-ca).

**Topics**
+ [Public component updates](#greengrass-2022-07-28-components)

## Public component updates
<a name="greengrass-2022-07-28-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.7.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.7.0"></a>**New features**<br />   Updates the Greengrass nucleus to send status updates to the AWS IoT Greengrass cloud when the core device applies a local deployment.   Adds support for client certificates signed by a custom certificate authority (CA), where the CA isn't registered with AWS IoT. To use this feature, you can set the new `greengrassDataPlaneEndpoint` configuration option to `iotdata`. For more information, see [Use a device certificate signed by a private CA](configure-greengrass-core-v2.md#configure-nucleus-private-ca).    <br />**Bug fixes and improvements**<br />   Fixes an issue where the Greengrass nucleus rolls back a deployment in certain scenarios when the nucleus is stopped or restarted. The nucleus now resumes the deployment after the nucleus restarts.   Updates the Greengrass installer to respect the `--start` argument when you specify to set up the software as a system service.   Updates the behavior of [SubscribeToComponentUpdates](ipc-component-lifecycle.md#ipc-operation-subscribetocomponentupdates) to set the deployment ID in events where the nucleus updated a component.   Additional minor fixes and improvements.    |
| Stream manager | Version 2.1.0 of the [stream manager](stream-manager-component.md) component is available.<a name="changelog-stream-manager-2.1.0"></a>**New features**<br />   Updates this component to automatically send telemetry metrics to Amazon EventBridge. For more information, see [Gather system health telemetry data from AWS IoT Greengrass core devices](telemetry.md). <br />This feature requires v2.7.0 or later of the [Greengrass nucleus component](greengrass-nucleus-component.md).   Version updated for Greengrass nucleus version 2.7.0 release.    |
| Lambda manager | Version 2.2.5 of the [Lambda manager](lambda-manager-component.md) component is available.<a name="changelog-lambda-manager-2.2.5"></a>**New features**<br />   Adds support for MQTT topic wildcards in event sources where you subscribe to local publish/subscribe messages. <br />This feature requires v2.6.0 or later of the [Greengrass nucleus component](greengrass-nucleus-component.md).   Version updated for Greengrass nucleus version 2.7.0 release.    |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
