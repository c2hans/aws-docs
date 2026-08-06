---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/secure-tunneling-component.html
---

# Secure tunneling
<a name="secure-tunneling-component"></a>

With the `aws.greengrass.SecureTunneling` component, you can establish secure bidirectional communication with a Greengrass core device located behind restricted firewalls.

For example, imagine you have a Greengrass core device behind a firewall that prohibits all incoming connections. Secure tunneling uses MQTT to transfer an access token to the device and then uses WebSockets to make an SSH connection to the device through the firewall. With this AWS IoT managed tunnel, you can open the SSH connection needed for your device. For more information about using AWS IoT secure tunneling to connect to remote devices, see [AWS IoT secure tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html) in the *AWS IoT Developer Guide*.

This component subscribes to the AWS IoT Core MQTT message broker on the `$aws/things/{{greengrass-core-device}}/tunnels/notify` topic to receive secure tunneling notifications.

**Topics**
+ [Versions](#secure-tunneling-component-versions)
+ [Type](#secure-tunneling-component-type)
+ [Operating system](#secure-tunneling-component-os-support)
+ [Requirements](#secure-tunneling-component-requirements)
+ [Dependencies](#secure-tunneling-component-dependencies)
+ [Configuration](#secure-tunneling-component-configuration)
+ [Local log file](#secure-tunneling-component-log-file)
+ [Licenses](#secure-tunneling-component-licenses)
+ [Usage](#secure-tunneling-component-usage)
+ [See also](#secure-tunneling-component-see-also)
+ [Changelog](#secure-tunneling-component-changelog)

## Versions
<a name="secure-tunneling-component-versions"></a>

This component has the following versions:
+ 2.0.x
+ 1.1.x
+ 1.0.x

## Type
<a name="secure-tunneling-component-type"></a>

<a name="public-component-type-generic"></a>This <a name="public-component-type-generic-phrase"></a>component is a generic component (`aws.greengrass.generic`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs the component's lifecycle scripts.

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="secure-tunneling-component-os-support"></a>

This component can be installed on Linux core devices only.

Architectures:
+ Armv71
+ Armv8 (AArch64)
+ x86\_64

## Requirements
<a name="secure-tunneling-component-requirements"></a>

This component has the following requirements:

------
#### [ 2.0.x ]
+ Minimum of 4 MB disk space available for the secure tunneling component. This requirement does not include the Greengrass core software or other components running on the same device.
+ Minimum of 3 MB RAM available for the secure tunneling component. This requirement does not include the Greengrass core software or other components running on the same device.
+ GNU C Library (glibc) version 2.35 or greater. Versions of the operating system and libraries past their long-term support end of life date are not supported. You should use an operating system and libraries with long-term support.
+ The following runtime libraries installed on the Greengrass core device:
  + `libstdc++` version 3.4.29 or greater
  + `libgcc_s` version 3.0 or greater
  + OpenSSL version 3.0.0 or greater
+ Open outbound traffic on port 443 on the Greengrass core device.
+ Turn on support for the communication service that you want to use to communicate with the Greengrass core device. For example, to open an SSH connection to the device, you must turn on SSH on that device.

------
#### [ 1.0.x - 1.1.x ]
+ Minimum of 32 MB disk space available for the secure tunneling component. This requirement does not include the Greengrass core software or other components running on the same device.
+ Minimum of 16 MB RAM available for the secure tunneling component. This requirement does not include the Greengrass core software or other components running on the same device. For more information, see [Control memory allocation with JVM options](configure-greengrass-core-v2.md#jvm-tuning).
+ GNU C Library (glibc) version 2.25 or greater with a Linux kernel of 3.2 or greater are required for the secure tunneling component version 1.0.12 and greater. Versions of the operating system and libraries past their long-term support end of life date are not supported. You should use an operating system and libraries with long-term support.
+ Both the operating system and the Java runtime must be installed as 64 bit.
+ [Python](https://www.python.org/) 3.5 or later installed on the Greengrass core device and added to the PATH environment variable.
+ `libcrypto.so.1.1` installed on the Greengrass core device and added to the PATH environment variable.
+ Open outbound traffic on port 443 on the Greengrass core device.
+ Turn on support for the communication service that you want to use to communicate with the Greengrass core device. For example, to open an SSH connection to the device, you must turn on SSH on that device.

------

### Endpoints and ports
<a name="secure-tunneling-component-endpoints"></a>

This component must be able to perform outbound requests to the following endpoints and ports, in addition to endpoints and ports required for basic operation. For more information, see [Allow device traffic through a proxy or firewall](allow-device-traffic.md).

| Endpoint | Port | Required | Description |
| --- | --- | --- | --- |
| `data.tunneling.iot.{{region}}.amazonaws.com` | 443 | Yes | Establish secure tunnels. |

## Dependencies
<a name="secure-tunneling-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#secure-tunneling-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com//greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 2.0.0 ]

Version 2.0.0 of this component supports both Greengrass nucleus and Greengrass nucleus lite. The following table lists the dependencies for version 2.0.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) OR [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) |  >=2.0.0 <3.0.0  | Soft |

------
#### [ 1.0.19 – 1.1.3 ]

The following table lists the dependencies for versions 1.0.19 through 1.1.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <3.0.0  | Soft |

------
#### [ 1.0.18 ]

The following table lists the dependencies for version 1.0.18 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.13.0  | Soft |

------
#### [ 1.0.16 – 1.0.17 ]

The following table lists the dependencies for versions 1.0.16 to 1.0.17 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.12.0  | Soft |

------
#### [ 1.0.14 – 1.0.15 ]

The following table lists the dependencies for versions 1.0.14 to 1.0.15 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.11.0  | Soft |

------
#### [ 1.0.11 – 1.0.13 ]

The following table lists the dependencies for versions 1.0.11 – 1.0.13 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.10.0  | Soft |

------
#### [ 1.0.10 ]

The following table lists the dependencies for version 1.0.10 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.9.0  | Soft |

------
#### [ 1.0.9 ]

The following table lists the dependencies for version 1.0.9 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.8.0  | Soft |

------
#### [ 1.0.8 ]

The following table lists the dependencies for version 1.0.8 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.7.0  | Soft |

------
#### [ 1.0.5 - 1.0.7 ]

The following table lists the dependencies for versions 1.0.5 through 1.0.7 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.6.0  | Soft |

------
#### [ 1.0.4 ]

The following table lists the dependencies for version 1.0.4 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.5.0  | Soft |

------
#### [ 1.0.3 ]

The following table lists the dependencies for version 1.0.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.4.0  | Soft |

------
#### [ 1.0.2 ]

The following table lists the dependencies for version 1.0.2 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.3.0  | Soft |

------
#### [ 1.0.1 ]

The following table lists the dependencies for version 1.0.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.2.0  | Soft |

------
#### [ 1.0.0 ]

The following table lists the dependencies for version 1.0.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.3 <2.1.0  | Soft |

------

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="secure-tunneling-component-configuration"></a>

This component provides the following configuration parameters that you can customize when you deploy the component.

------
#### [ 2.0.x ]

`maxConcurrentTunnels`
(Optional) Maximum number of concurrent tunnels allowed.
The value cannot be more than 20.
Default: `20`

`tunnelTimeoutSeconds`
(Optional) Tunnel timeout duration in seconds.
Default: `43200` (12 hours)

`accessControl`
(Optional) The object that contains the [authorization policy](interprocess-communication.md#ipc-authorization-policies) that allows the component to subscribe to the secure tunneling notifications topic.
Do not modify this configuration parameter if your deployment targets a thing group. If your deployment targets an individual core device, and you want to restrict its subscription to the device's topic, specify the core device's thing name. In the `resources` value in the device's authorization policy, replace the MQTT topic wildcard with the device's thing name.

```
{
  "aws.greengrass.ipc.mqttproxy": {
    "aws.greengrass.SecureTunneling:mqttproxy:1": {
      "policyDescription": "Access to tunnel notification pubsub topic",
      "operations": [
        "aws.greengrass#SubscribeToIoTCore"
      ],
      "resources": [
        "$aws/things/+/tunnels/notify"
      ]
    }
  }
}
```

**Example: Configuration merge update**
The following example configuration specifies the maximum concurrent tunnels and timeout settings.

```
{
  "maxConcurrentTunnels": 20,
  "tunnelTimeoutSeconds": 43200,
  "accessControl": {
    "aws.greengrass.ipc.mqttproxy": {
      "aws.greengrass.SecureTunneling:mqttproxy:1": {
        "policyDescription": "Access to tunnel notification pubsub topic",
        "operations": [
          "aws.greengrass#SubscribeToIoTCore"
        ],
        "resources": [
          "$aws/things/MyGreengrassCore/tunnels/notify"
        ]
      }
    }
  }
}
```

------
#### [ 1.0.x - 1.1.x ]

`OS_DIST_INFO`
(Optional) The operating system of your core device. By default, the component attempts to identify automatically the operating system running on your core device. If the component fails to start with the default value, use this value to specify the operating system. For a list of supported operating systems for this component, see [Device requirements](greengrass-nucleus-component.md#greengrass-v2-requirements).
This value can be one of the following: `auto`, `ubuntu`, `amzn2`, `raspberrypi`.
Default: `auto`

`accessControl`
(Optional) The object that contains the [authorization policy](interprocess-communication.md#ipc-authorization-policies) that allows the component to subscribe to the secure tunneling notifications topic.
Do not modify this configuration parameter if your deployment targets a thing group. If your deployment targets an individual core device, and you want to restrict its subscription to the device's topic, specify the core device's thing name. In the `resources` value in the device's authorization policy, replace the MQTT topic wildcard with the device's thing name.

```
{
  "aws.greengrass.ipc.mqttproxy": {
    "aws.iot.SecureTunneling:mqttproxy:1": {
      "policyDescription": "Access to tunnel notification pubsub topic",
      "operations": [
        "aws.greengrass#SubscribeToIoTCore"
      ],
      "resources": [
        "$aws/things/+/tunnels/notify"
      ]
    }
  }
}
```

**Example: Configuration merge update**
The following example configuration specifies to allow this component to open secure tunnels on a core device named **MyGreengrassCore** that runs Ubuntu.

```
{
  "OS_DIST_INFO": "ubuntu",
  "accessControl": {
    "aws.greengrass.ipc.mqttproxy": {
      "aws.iot.SecureTunneling:mqttproxy:1": {
        "policyDescription": "Access to tunnel notification pubsub topic",
        "operations": [
          "aws.greengrass#SubscribeToIoTCore"
        ],
        "resources": [
          "$aws/things/MyGreengrassCore/tunnels/notify"
        ]
      }
    }
  }
}
```

------

## Local log file
<a name="secure-tunneling-component-log-file"></a>

------
#### [ Greengrass nucleus ]

This component uses the following log file.

```
{{/greengrass/v2}}/logs/aws.greengrass.SecureTunneling.log
```

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace `{{/greengrass/v2}}` with the path to the AWS IoT Greengrass root folder.

  ```
  sudo tail -f {{/greengrass/v2}}/logs/aws.greengrass.SecureTunneling.log
  ```

------
#### [ Greengrass nucleus lite ]

Run the following command on the core device to view this component's logs.

```
journalctl -xeau ggl.aws.greengrass.SecureTunneling.service
```

Run the following command on the core device to view this component's logs in real time.

```
journalctl -fau ggl.aws.greengrass.SecureTunneling.service
```

------

## Licenses
<a name="secure-tunneling-component-licenses"></a>

This component includes the following third-party software/licensing:

------
#### [ 2.0.x ]
+ [AWS IoT Secure Tunneling Local Proxy](https://github.com/aws-samples/aws-iot-securetunneling-localproxy)/Apache License 2.0
+ [AWS Greengrass Component SDK](https://github.com/aws-greengrass/aws-greengrass-component-sdk)/Apache License 2.0
+ [Boost C\+\+ Libraries](https://www.boost.org/)/Boost Software License 1.0
+ [Protocol Buffers](https://github.com/protocolbuffers/protobuf)/BSD 3-Clause License

------
#### [ 1.0.x - 1.1.x ]
+ [AWS IoT Device Client](https://github.com/awslabs/aws-iot-device-client)/Apache License 2.0
+ [AWS IoT Device SDK for Java](https://github.com/aws/aws-greengrass-core-sdk-java/)/Apache License 2.0
+ [gson](https://github.com/google/gson)/Apache License 2.0
+ [log4j](https://logging.apache.org/log4j/2.x/)/Apache License 2.0
+ [slf4j](http://www.slf4j.org/)/Apache License 2.0

------

## Usage
<a name="secure-tunneling-component-usage"></a>

To use the secure tunneling component on your device, do the following:

1. Deploy the secure tunneling component to your device.

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot). From the left menu, choose **Remote actions**, and then choose **Secure tunnels**.

1. Create a tunnel to your Greengrass device.

1. Download the source access token.

1. Use the local proxy with the source access token to connect to your destination. For more information, see [How to use the local proxy](https://docs.aws.amazon.com/iot/latest/developerguide/how-use-local-proxy.html) in the *AWS IoT Developer Guide*.

## See also
<a name="secure-tunneling-component-see-also"></a>
+ [AWS IoT secure tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html) in the *AWS IoT Developer Guide*
+ [How to use the local proxy](https://docs.aws.amazon.com/iot/latest/developerguide/how-use-local-proxy.html) in the *AWS IoT Developer Guide*

## Changelog
<a name="secure-tunneling-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.0.1 |  **Bug fixes and improvements**<br />   Updates the bundled local proxy binary to version 3.3.0.   Fixes concurrency and object-lifetime bugs that could affect tunnel data integrity.   Requires TLS 1.2 or later and no longer allows SSLv2, SSLv3, TLS 1.0, or TLS 1.1.     |
| 2.0.0 |  **New features**<br />   Replaces the Java wrapper with a C wrapper.   Replaces AWS IoT Device Client with [AWS IoT Securetunneling Localproxy](https://github.com/aws-samples/aws-iot-securetunneling-localproxy).   Reduces the binary size from approximately 36 MB to approximately 4 MB.   Reduces the memory footprint from approximately 100 MB to approximately 2 MB.     |
| 1.1.3 |  **Bug fixes and improvements**<br />   Upgrades the underlying [AWS IoT Device Client](https://github.com/awslabs/aws-iot-device-client) invoked by the component from version 1.10.0 to version 1.10.1.   Fixes the GNU C Library (glibc) compatibility issues in secure tunneling component version 1.1.2.     |
| 1.1.2 |   This version is no longer available. The improvements in this version are available in later versions of this component.  **Bug fixes and improvements**<br />   Upgrades the underlying [AWS IoT Device Client](https://github.com/awslabs/aws-iot-device-client) invoked by the component from version 1.9.0 to version 1.10.0.   Fixes the payload transfer issue which prevents users from forwarding large files from Greengrass V2 core devices to the source device through the secure tunnel.     |
| 1.1.1 |  **Bug fixes and improvements**<br />   Adds a configuration to support Greengrass nucleus lite.     |
| 1.1.0 |  **New features**<br />   Adds recipe supports for Greengrass nucleus lite.     |
| 1.0.19 |  **Bug fixes and improvements**<br />   Upgrades the underlying [AWS IoT Device Client](https://github.com/awslabs/aws-iot-device-client) invoked by the component from version 1.8.0 to version 1.9.0.   Increases the concurrent tunnel limit to 20 tunnels on a component level.   Increases the default AWS IoT Greengrass Core IPC timeout from 3 seconds to 10 seconds.     If you are using the secure tunneling local proxy as the tunnel source client, do not update your component to this version until you have also upgraded the local proxy to version 3.1.1 or later.   |
| 1.0.18 | Version updated for Greengrass nucleus version 2.12.0 release. |
| 1.0.17 |  **Bug fixes and improvements**<br />   Fixes the thread cleanup issue which was blocking users from creating tunnels. This component will now cleanup a thread either once it receives the CloseTunnel signal or if the tunnel is expired after 12 hours.     |
| 1.0.16 | Version updated for Greengrass nucleus version 2.11.0 release. |
| 1.0.15 |  **Bug fixes and improvements**<br />   Fixes a startup issue for users that do not have a home directory on the device. The secure tunneling component now starts without creating a directory for shadow documents.     |
| 1.0.14 | Version updated for Greengrass nucleus version 2.10.0 release. |
| 1.0.13 |  **Bug fixes and improvements**<br />   Fixes an issue where an orphan client process prevents more than one tunnel from targeting the device.     |
| 1.0.12 |  **Bug fixes and improvements**<br />   Adds support for x86\_64 (AMD64) and ARMv8 (Aarch64) when running on Raspberry Pi OS.     |
| 1.0.11 | Version updated for Greengrass nucleus version 2.9.0 release. |
| 1.0.10 | Version updated for Greengrass nucleus version 2.8.0 release. |
| 1.0.9 | Version updated for Greengrass nucleus version 2.7.0 release. |
| 1.0.8 | Version updated for Greengrass nucleus version 2.6.0 release. |
| 1.0.7 |  **Bug fixes and improvements**<br />   Fixes an issue where the component disconnects when you transfer large files over SCP.     |
| 1.0.6 | This version contains bug fixes. |
| 1.0.5 | Version updated for Greengrass nucleus version 2.5.0 release. |
| 1.0.4 | Version updated for Greengrass nucleus version 2.4.0 release. |
| 1.0.3 | Version updated for Greengrass nucleus version 2.3.0 release. |
| 1.0.2 | Version updated for Greengrass nucleus version 2.2.0 release. |
| 1.0.1 | Version updated for Greengrass nucleus version 2.1.0 release. |
| 1.0.0 | Initial version. |
