---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/client-device-components.html
---

# AWS-provided client device components
<a name="client-device-components"></a>

AWS IoT Greengrass provides the following public components that you can deploy to core devices. These components enable client devices to connect and communicate with a core device.

**Note**  <a name="component-nucleus-dependency-update-note"></a>
Several AWS-provided components depend on specific minor versions of the Greengrass nucleus. Because of this dependency, you need to update these components when you update the Greengrass nucleus to a new minor version. For information about the specific versions of the nucleus that each component depends on, see the corresponding component topic. For more information about updating the nucleus, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

<a name="component-table-type-description"></a>When a component has a component type of both generic and Lambda, the current version of the component is the generic type and a previous version of the component is the Lambda type.

| Component | Description | [Component type](develop-greengrass-components.md#component-types) | Supported OS | [Open source](open-source.md) |
| --- | --- | --- | --- | --- |
| <a name="client-device-auth-component-table-row"></a>[Client device auth](client-device-auth-component.md) | Enables local IoT devices, called client devices, to connect to the core device. | Plugin | Linux, Windows | [Yes](https://github.com/aws-greengrass/aws-greengrass-client-device-auth) |
| <a name="ip-detector-component-table-row"></a>[IP detector](ip-detector-component.md) | Reports MQTT broker connectivity information to AWS IoT Greengrass, so client devices can discover how to connect. | Plugin | Linux, Windows | [Yes](https://github.com/aws-greengrass/aws-greengrass-ip-detector) |
| <a name="mqtt-bridge-component-table-row"></a>[MQTT bridge](mqtt-bridge-component.md) | Relays MQTT messages between client devices, local AWS IoT Greengrass publish/subscribe, and AWS IoT Core. | Plugin | Linux, Windows | [Yes](https://github.com/aws-greengrass/aws-greengrass-mqtt-bridge) |
| <a name="mqtt-broker-moquette-component-table-row"></a>[MQTT 3.1.1 broker (Moquette)](mqtt-broker-moquette-component.md) | Runs an MQTT 3.1.1 broker that handles messages between client devices and the core device. | Plugin | Linux, Windows | [Yes](https://github.com/aws-greengrass/aws-greengrass-moquette-mqtt) |
| <a name="mqtt-broker-emqx-component-table-row"></a>[MQTT 5 broker (EMQX)](mqtt-broker-emqx-component.md) | Runs an MQTT 5 broker that handles messages between client devices and the core device. | Generic | Linux, Windows | No |
| <a name="shadow-manager-component-table-row"></a>[Shadow manager](shadow-manager-component.md) | Enables interaction with shadows on the core device. It manages shadow document storage and also the synchronization of local shadow states with the AWS IoT Device Shadow service. | Plugin | Linux, Windows | [Yes](https://github.com/aws-greengrass/aws-greengrass-shadow-manager) |
