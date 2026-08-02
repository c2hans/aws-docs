---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iot-greengrass-golden-images/methods.html
---

# Golden image methods
<a name="methods"></a>

At a high level, you can choose between two methods for creating a golden image that includes the Greengrass directory tree:
+ Take a snapshot of the entire Greengrass directory tree on the golden device.
+ Take only a partial snapshot of the Greengrass directory tree on the golden device.

The following table summarizes the key differences between these methods.

|
|
|  | **Full Greengrass snapshot** | **Partial Greengrass snapshot** |
| --- |--- |--- |
| **Greengrass directories included** | All Greengrass directories (optionally excluding empty directories or those with only ephemeral data, as explained in the [previous section](anatomy.md#greengrass-directory)). | `alts`, `packages`, and `plugins` directories only. |
| **Advantage** | Production devices are in a fully working state immediately. | Supports simple and robust configuration of each production device. |
| **Disadvantage** | Requires more complicated configuration of each production device.  | Production devices must receive a cloud deployment to enter a fully working state. |

## Full Greengrass snapshot
<a name="full-snapshot"></a>

By including a full snapshot of the Greengrass directory tree in your golden image, you retain the history and context of the deployments and component configuration that were applied to your golden device. This means that the devices produced from this image also have this history and context. Consequently, your production devices can boot up and run all application components, and each device can be in a fully working state immediately.

The complication with this method is that the history and context can make it more difficult to personalize each production device with unique configuration. These configuration steps are detailed in the [next section](procedure.md).

**Limitations of the fully working state:**

Although your application components will run, they need to gracefully deal with the following limitations:
+ Your device will not synchronize any secrets to disk until it contacts the cloud.
+ Your device will not have valid AWS Identity and Access Management (IAM) credentials through [token exchange](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html) until it contacts the cloud.
+ If your device uses [fleet provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html) or [just-in-time provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/jit-provisioning.html), it will not connect to AWS IoT Core until provisioning is complete.

## Partial Greengrass snapshot
<a name="partial-snapshot"></a>

When you use the partial Greengrass snapshot method, the golden image includes only the `alts`, `packages`, and `plugins` directories. The `config` directory is excluded, so the history and context of deployments and configuration are omitted.

The chief advantage of this method is that the unique configuration steps required for each production device are simple and robust. These configuration steps are detailed in the [next section](procedure.md).

The chief disadvantage is that your application components will not be in a running state until your production devices receive a cloud deployment. This might not meet all your requirements. However, because the component artifacts are present on disk, they will not be re-downloaded when your devices receive the cloud deployment, if the cloud deployment still matches the artifacts on disk. Consequently, the cloud deployment is relatively quick and will not incur large data charges on a cellular network.
