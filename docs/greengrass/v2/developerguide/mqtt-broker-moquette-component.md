---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-moquette-component.html
---

# MQTT 3.1.1 broker (Moquette)
<a name="mqtt-broker-moquette-component"></a>

The Moquette MQTT broker component (`aws.greengrass.clientdevices.mqtt.Moquette`) handles MQTT messages between client devices and a Greengrass core device. This component provides a modified version of the [Moquette MQTT broker](https://github.com/moquette-io/moquette). Deploy this MQTT broker to run a lightweight MQTT broker. For more information about how to choose an MQTT broker, see [Choose an MQTT broker](choose-local-mqtt-broker.md).

This broker implements the MQTT 3.1.1 protocol. It includes support for QoS 0, QoS 1, QoS 2 retained messages, last will messages, and persistent sessions.

**Note**  <a name="client-device-component-context"></a>
Client devices are local IoT devices that connect to a Greengrass core device to send MQTT messages and data to process. For more information, see [Interact with local IoT devices](interact-with-local-iot-devices.md).

**Topics**
+ [Versions](#mqtt-broker-moquette-component-versions)
+ [Type](#mqtt-broker-moquette-component-type)
+ [Operating system](#mqtt-broker-moquette-component-os-support)
+ [Requirements](#mqtt-broker-moquette-component-requirements)
+ [Dependencies](#mqtt-broker-moquette-component-dependencies)
+ [Configuration](#mqtt-broker-moquette-component-configuration)
+ [Local log file](#mqtt-broker-moquette-component-log-file)
+ [Changelog](#mqtt-broker-moquette-component-changelog)

## Versions
<a name="mqtt-broker-moquette-component-versions"></a>

This component has the following versions:
+ 2.3.x
+ 2.2.x
+ 2.1.x
+ 2.0.x

## Type
<a name="mqtt-broker-moquette-component-type"></a>

<a name="public-component-type-plugin-para1"></a>This component is a plugin component (`aws.greengrass.plugin`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs this component in the same Java Virtual Machine (JVM) as the nucleus. The nucleus restarts when you change this component's version on the core device.

<a name="public-component-type-plugin-para2"></a>This component uses the same log file as the Greengrass nucleus. For more information, see [Monitor AWS IoT Greengrass logs](monitor-logs.md).

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="mqtt-broker-moquette-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Requirements
<a name="mqtt-broker-moquette-component-requirements"></a>

This component has the following requirements:
+ The core device must be able to accept connections on the port where the MQTT broker operates. This component runs the MQTT broker on port 8883 by default. You can specify a different port when you configure this component.

  <a name="mqtt-broker-configuration-mqtt-bridge-requirement"></a>If you specify a different port, and you use the [MQTT bridge component](mqtt-bridge-component.md) to relay MQTT messages to other brokers, you must use MQTT bridge v2.1.0 or later. Configure it to use the port where the MQTT broker operates.

  <a name="mqtt-broker-configuration-ip-detector-requirement"></a>If you specify a different port, and you use the [IP detector component](ip-detector-component.md) to manage MQTT broker endpoints, you must use IP detector v2.1.0 or later. Configure it to report the port where the MQTT broker operates.
+ The Moquette MQTT broker component is supported to run in a VPC.

## Dependencies
<a name="mqtt-broker-moquette-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#mqtt-broker-moquette-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com//greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 2.3.7 ]

The following table lists the dependencies for version 2.3.7 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.6.0 | Hard |

------
#### [ 2.3.2 – 2.3.6 ]

The following table lists the dependencies for versions 2.3.2 through 2.3.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.5.0 | Hard |

------
#### [ 2.3.0 and 2.3.1 ]

The following table lists the dependencies for versions 2.3.0 and 2.3.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.4.0 | Hard |

------
#### [ 2.2.0 ]

The following table lists the dependencies for version 2.2.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.3.0 | Hard |

------
#### [ 2.1.0 ]

The following table lists the dependencies for version 2.1.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.0.0 <2.2.0 | Hard |

------
#### [ 2.0.0 - 2.0.2 ]

The following table lists the dependencies for versions 2.0.0 through 2.0.2 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.0.0 <2.1.0 | Hard |

------

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="mqtt-broker-moquette-component-configuration"></a>

This component provides the following configuration parameters that you can customize when you deploy the component.

`moquette`
(Optional) The [Moquette MQTT broker](https://github.com/moquette-io/moquette) configuration to use. You can configure a subset of Moqeutte configuration options in this component. For more information, see the inline comments in the [Moquette configuration file](https://github.com/moquette-io/moquette/blob/main/distribution/src/main/resources/moquette.conf).
This object contains the following information:
`ssl_port`
(Optional) The port where the MQTT broker operates.
<a name="mqtt-broker-configuration-mqtt-bridge-requirement"></a>If you specify a different port, and you use the [MQTT bridge component](mqtt-bridge-component.md) to relay MQTT messages to other brokers, you must use MQTT bridge v2.1.0 or later. Configure it to use the port where the MQTT broker operates.
<a name="mqtt-broker-configuration-ip-detector-requirement"></a>If you specify a different port, and you use the [IP detector component](ip-detector-component.md) to manage MQTT broker endpoints, you must use IP detector v2.1.0 or later. Configure it to report the port where the MQTT broker operates.
Default: `8883`
`host`
(Optional) The interface where the MQTT broker binds. For example, you might change this parameter so that the MQTT broker binds only to a specific local network.
Default: `0.0.0.0` (binds to all network interfaces)

startupTimeoutSeconds
(Optional) The maximum of time in seconds for the component to start. The component's state changes to `BROKEN` if it exceeds this timeout.
Default: `120`

**Example: Configuration merge update**
The following example configuration specifies to operate the MQTT broker on port 443.

```
{
  "moquette": {
    "ssl_port": "443"
  }
}
```

## Local log file
<a name="mqtt-broker-moquette-component-log-file"></a>

This component uses the same log file as the [Greengrass nucleus](greengrass-nucleus-component.md) component.

------
#### [ Linux ]

```
{{/greengrass/v2}}/logs/greengrass.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\logs\greengrass.log
```

------

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

  ```
  sudo tail -f {{/greengrass/v2}}/logs/greengrass.log
  ```

------
#### [ Windows (PowerShell) ]

  ```
  Get-Content {{C:\greengrass\v2}}\logs\greengrass.log -Tail 10 -Wait
  ```

------

## Changelog
<a name="mqtt-broker-moquette-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.3.7 | Version updated for [client device auth](client-device-auth-component.md) version 2.5.0 release. |
| 2.3.6 |  **Bug fixes and improvements**<br />   General bug fixes and improvements.     |
| 2.3.5 |  **Bug fixes and improvements**<br />   Updated Moquette to version 0.17.     |
| 2.3.4 |  **Bug fixes and improvements**<br />   Fixes an issue where clients may experience invalid session errors when sending or receiving messages, due to duplicate client IDs. This issue caused the client's session to close.     |
| 2.3.3 |  <a name="changelog-mqtt-broker-moquette-2.3.3"></a>**New features**<br /> Adds a new `startupTimeoutSeconds` configuration option.   |
| 2.3.2 | Version updated for [client device auth](client-device-auth-component.md) version 2.4.0 release. |
| 2.3.1 |  **Bug fixes and improvements**<br />   Fixes a race condition where clients may be disconnected after attempting to reconnect, due to an invalid session.     |
| 2.3.0 | Adds support for certificate chains. |
| 2.2.0 | Version updated for [client device auth](client-device-auth-component.md) version 2.2.0 release. |
| 2.1.0 |  **Bug fixes and improvements**<br />   Updates this component to use [Moquette](https://github.com/moquette-io/moquette) version 0.16, which improves performance and includes several other improvements.   Fixes an issue where the local MQTT server certificate rotates more often than intended in certain scenarios. <br />To apply this fix, you must also use v2.1.0 or later of the [client device auth component](client-device-auth-component.md).     |
| 2.0.2 |  **Bug fixes and improvements**<br />   Increases the maximum MQTT message size from 8,092 bytes to 128 kilobytes. The effective MQTT message payload limit is slightly less, because the message size limit includes message headers.   Adds support for integer values in the `ssl_port` parameter.     |
| 2.0.1 | Version updated for Greengrass nucleus version 2.4.0 release. |
| 2.0.0 | Initial version. |
