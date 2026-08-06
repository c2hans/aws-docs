---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2026-07-08.html
---

# Release: AWS IoT Greengrass Core v2.18.0 software update on July 8, 2026
<a name="greengrass-release-2026-07-08"></a>

This release provides version 2.18.0 of the Greengrass nucleus component and updates to AWS-provided components.

**Release date:** July 8, 2026

**Topics**
+ [Public component updates](#greengrass-2026-07-08-components)

## Public component updates
<a name="greengrass-2026-07-08-components"></a>

The following table lists components provided by AWS that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | Version 2.18.0 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.**New features**<br />   Adds support for switching a core device's AWS IoT connectivity to a different AWS account or region through a nucleus configuration deployment. The nucleus validates connectivity to the new endpoints before it applies the change, and reports the terminal deployment status to the source account.   Adds support for Windows Server 2025.   <br />**Bug fixes and improvements**<br />   Fixes a startup timing issue on systemd devices by starting the AWS IoT Greengrass Core software only after the system clock synchronizes.   Fixes an issue where a component might encounter stale subscriptions after it closes a local IPC stream during an in-progress subscribe request.   General bug fixes and improvements.    |
| [Stream manager](stream-manager-component.md) | Version 2.3.1 of the [stream manager](stream-manager-component.md) is available.**Bug fixes and improvements**<br />   Improves the throughput of stream manager exports to Kinesis Data Streams destinations, especially for small record sizes.   Adds shard-aware pacing that distributes records across the shards of the target data stream to keep requests within the per-shard limits of Kinesis Data Streams. To use shard-aware pacing, grant the `kinesis:ListShards` permission in the [Greengrass token exchange role](device-service-role.md).   Adds the `STREAM_MANAGER_EXPORTER_KINESIS_INTER_CALL_DELAY_MS` configuration parameter, which sets a fallback delay between export requests when stream manager cannot determine the shard layout of the target data stream. The default is 1000 milliseconds. To turn off the fallback delay, set this parameter to `0`.    |
| [Shadow manager](shadow-manager-component.md) | Version 2.3.15 of the [shadow manager](shadow-manager-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where the shadow manager could stop working after a power outage corrupted its local database.   Validates the integrity of the local database on startup and recreates the database when it detects corruption.    |
| [MQTT bridge](mqtt-bridge-component.md) | Version 2.3.3 of the [MQTT bridge](mqtt-bridge-component.md) is available.**Bug fixes and improvements**<br />   Fixes an issue where high concurrent device load could cause the MQTT bridge to stop relaying messages after a dropped PUBACK.    |
| [Secret manager](secret-manager-component.md) | Version 2.2.9 of the [secret manager](secret-manager-component.md) is available.**Bug fixes and improvements**<br />   General bug fixes and improvements.    |
| [Greengrass CLI](greengrass-cli-component.md) | <a name="changelog-cli-2.18.0"></a>Version 2.18.0 of the [Greengrass CLI](greengrass-cli-component.md) is available.<br />Updates the component version for the Greengrass nucleus version 2.18.0 release. |
| [Secure tunneling](secure-tunneling-component.md) | Version 2.0.1 of the [secure tunneling](secure-tunneling-component.md) component is available.**Bug fixes and improvements**<br />   Updates the bundled local proxy binary to version 3.3.0.   Fixes concurrency and object-lifetime bugs that could affect tunnel data integrity.   Requires TLS 1.2 or later and no longer allows SSLv2, SSLv3, TLS 1.0, or TLS 1.1.    |
