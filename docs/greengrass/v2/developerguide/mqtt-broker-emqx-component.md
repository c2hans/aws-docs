---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html
---

# MQTT 5 broker (EMQX)
<a name="mqtt-broker-emqx-component"></a>

The EMQX MQTT broker component (`aws.greengrass.clientdevices.mqtt.EMQX`) handles MQTT messages between client devices and a Greengrass core device. This component provides a modified version of the [EMQX MQTT 5.0 broker](https://www.emqx.com/en/mqtt/mqtt5). Deploy this MQTT broker to use MQTT 5 features in communication between client devices and a core device. For more information about how to choose an MQTT broker, see [Choose an MQTT broker](choose-local-mqtt-broker.md).

This broker implements the MQTT 5.0 protocol. It includes support for session and message expiration intervals, user properties, shared subscriptions, topic aliases, and more. MQTT 5 is backwards compatible with MQTT 3.1.1, so if you run the [Moquette MQTT 3.1.1 broker](mqtt-broker-moquette-component.md), you can replace it with the EMQX MQTT 5 broker, and client devices can continue to connect and operate as usual.

<a name="note-local-mqtt-broker-mqtt-5-features"></a>

**Note**  <a name="client-device-component-context"></a>
Client devices are local IoT devices that connect to a Greengrass core device to send MQTT messages and data to process. For more information, see [Interact with local IoT devices](interact-with-local-iot-devices.md).

**Topics**
+ [Versions](#mqtt-broker-emqx-component-versions)
+ [Type](#mqtt-broker-emqx-component-type)
+ [Operating system](#mqtt-broker-emqx-component-os-support)
+ [Requirements](#mqtt-broker-emqx-component-requirements)
+ [Dependencies](#mqtt-broker-emqx-component-dependencies)
+ [Configuration](#mqtt-broker-emqx-component-configuration)
+ [Local log file](#mqtt-broker-emqx-component-log-file)
+ [Licenses](#mqtt-broker-emqx-component-licenses)
+ [Changelog](#mqtt-broker-emqx-component-changelog)

## Versions
<a name="mqtt-broker-emqx-component-versions"></a>

This component has the following versions:
+ 2.0.x
+ 1.2.x
+ 1.1.x
+ 1.0.x

## Type
<a name="mqtt-broker-emqx-component-type"></a>

<a name="public-component-type-generic"></a>This <a name="public-component-type-generic-phrase"></a>component is a generic component (`aws.greengrass.generic`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs the component's lifecycle scripts.

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="mqtt-broker-emqx-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Requirements
<a name="mqtt-broker-emqx-component-requirements"></a>

This component has the following requirements:
+ The core device must be able to accept connections on the port where the MQTT broker operates. This component runs the MQTT broker on port 8883 by default. You can specify a different port when you configure this component.

  <a name="mqtt-broker-configuration-mqtt-bridge-requirement"></a>If you specify a different port, and you use the [MQTT bridge component](mqtt-bridge-component.md) to relay MQTT messages to other brokers, you must use MQTT bridge v2.1.0 or later. Configure it to use the port where the MQTT broker operates.

  <a name="mqtt-broker-configuration-ip-detector-requirement"></a>If you specify a different port, and you use the [IP detector component](ip-detector-component.md) to manage MQTT broker endpoints, you must use IP detector v2.1.0 or later. Configure it to report the port where the MQTT broker operates.
+ On Linux core devices, Docker installed and configured on the core device:
  + <a name="docker-engine-requirement"></a>[Docker Engine](https://docs.docker.com/engine/) 1.9.1 or later installed on the Greengrass core device. Versions up to and including 29.6.0, such as 20.10, 24.0, 25.0, and 27.5, work with the AWS IoT Greengrass Core software. You must install Docker directly on the core device before you deploy components that run Docker containers.
  + <a name="docker-daemon-requirement"></a>The Docker daemon started and running on the core device before you deploy this component.
  + The system user that runs this component must have root or administrator permissions. Alternatively, you can run this component as a system user in the `docker` group and configure this component's `requiresPrivileges` option to `false` to run the EQMX MQTT broker without privileges.
+ The EMQX MQTT broker component is supported to run in a VPC.
+ The EMQX MQTT broker component is not supported on the `armv7` platform.

## Dependencies
<a name="mqtt-broker-emqx-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#mqtt-broker-emqx-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com//greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 2.0.2 – 2.0.3 ]

The following table lists the dependencies for versions 2.0.2 and 2.0.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.6.0 | Soft |

------
#### [ 2.0.1 ]

The following table lists the dependencies for version 2.0.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.6.0 | Hard |

------
#### [ 2.0.0 ]

The following table lists the dependencies for version 2.0.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.5.0 | Hard |

------
#### [ 1.2.2 – 1.2.3 ]

The following table lists the dependencies for versions 1.2.2 to 1.2.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.5.0 | Hard |

------
#### [ 1.2.0 and 1.2.1 ]

The following table lists the dependencies for versions 1.2.0 and 1.2.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.4.0 | Hard |

------
#### [ 1.0.0 and 1.1.0 ]

The following table lists the dependencies for versions 1.0.0 and 1.1.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Client device auth](client-device-auth-component.md) | >=2.2.0 <2.3.0 | Hard |

------

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="mqtt-broker-emqx-component-configuration"></a>

------
#### [ 2.0.0 - 2.0.3 ]

This component provides the following configuration parameters that you can customize when you deploy the component.

**Important**
If you use version 2 of the MQTT 5 broker (EMQX) component, you must update your configuration file. Version 1 configuration files do not work with version 2.

emqxConfig
 (Optional) The [EMQX MQTT broker](https://www.emqx.io/docs/en/v5.1/configuration/configuration.html) configuration to use. You can set EMQX configuration options in this component.
When you use the EMQX broker, Greengrass uses a default configuration. This configuration is used unless you modify it using this field.
Modifying the following configuration settings causes the EMQX broker component to restart. Other configuration changes apply without restarting the component.
+ `emqxConfig/cluster`
+ `emqxConfig/node`
+ `emqxConfig/rpc`
`aws.greengrass.clientdevices.mqtt.EMQX` allows you to configure security-sensitive options. These include TLS settings, authentication, and authorization providers. We recommended the default configuration that uses mutual TLS authentication and the Greengrass client device auth provider.

**Example: Default configuration**
The following example shows the defaults set for the MQTT 5 (EMQX) broker. You can override these settings using the `emqxConfig` configuration setting.

```
{
  "authorization": {
    "no_match": "deny",
    "sources": []
  },
  "node": {
    "cookie": "{{<placeholder>}}"
  },
  "listeners": {
     "ssl": {
       "default": {
         "ssl_options": {
           "keyfile": "{work:path}\\data\\key.pem",
           "certfile": "{work:path}\\data\\cert.pem",
           "cacertfile": null,
           "verify": "verify_peer",
           "versions": ["tlsv1.3", "tlsv1.2"],
           "fail_if_no_peer_cert": true
         }
       }
     },
     "tcp": {
       "default": {
         "enabled": false
       }
     },
     "ws": {
       "default": {
         "enabled": false
       }
     },
     "wss": {
       "default": {
         "enabled": false
       }
     }
  },
  "plugins": {
    "states": [{"name_vsn": "gg-1.0.0", "enable": true}],
    "install_dir": "plugins"
  }
}
```

authMode
(Optional) Sets the authorization provider for the broker. Can be one of the following values:
+ `enabled` – (Default) Use the Greengrass authentication and authorization provider.
+ `bypass_on_failure` – Use the Greengrass authentication provider, then use any remaining authentication providers in the EMQX provider chain if Greengrass denies either authentication or authorization.
+ `bypass` – The Greengrass provider is disabled. Authentication and authorization is handled by the EMQX provider chain.

`requiresPrivilege`
(Optional) On Linux core devices, you can specify to run the EMQX MQTT broker without root or administrator privileges. If you set this option to `false`, the system user that runs this component must be a member of the `docker` group.
Default: `true`

`startupTimeoutSeconds`
(Optional) The maximum of time in seconds for the EMQX MQTT broker to start. The component's state changes to `BROKEN` if it exceeds this timeout.
Default: `90`

`ipcTimeoutSeconds`
(Optional) The maximum of time in seconds for the component to wait for the Greengrass nucleus to respond to interprocess communication (IPC) requests. Increase this number if this component reports timeout errors when it checks if a client device is authorized.
Default: `5`

`crtLogLevel`
(Optional) The log level for the AWS Common Runtime (CRT) library.
Defaults to the EMQX MQTT broker log level (`log.level` in `emqx`).

`restartIdentifier`
(Optional) Configure this option to restart the EMQX MQTT broker. When this configuration value changes, this component restarts the MQTT broker. You can use this option to force client devices to disconnect.

`dockerOptions`
(Optional) Configure this option only on Linux operating systems to add parameters to the Docker command line. For example, to map additional ports, use the `-p` Docker parameter:

```
"-p 1883:1883"
```

**Example: Updating a v1.x configuration file to v2.x**
The following example shows the changes necessary to update a v1.x configuration file to version 2.x.
The version 1.x configuration file:

```
{
    "emqx": {
        "listener.ssl.external": "443",
        "listener.ssl.external.max_connections": "1024000",
        "listener.ssl.external.max_conn_rate": "500",
        "listener.ssl.external.rate_limit": "50KB,5s",
        "listener.ssl.external.handshake_timeout": "15s",
        "log.level": "warning"
    },
    "mergeConfigurationFiles": {
        "etc/plugins/aws_greengrass_emqx_auth.conf": "auth_mode=enabled\n use_greengrass_managed_certificates=true\n"
    }
}
```
The equivalent configuration file for v2:

```
{
    "emqxConfig": {
        "listeners": {
            "ssl": {
                "default": {
                   "bind": "8883",
                   "max_connections": "1024000",
                   "max_conn_rate": "500",
                   "ssl_options": {
                        "handshake_timeout": "15s"
                   }
                }
            }
        },
        "log": {
            "console": {
              "enable": true,
              "level": "warning"
            }
        }
    },
    "authMode": "enabled"
}
```
There is no equivalent to the `listener.ssl.external.rate_limit` configuration entry. The `use_greengrass_managed_certificates` configuration option has been removed.

**Example: Set a new port for the broker**
The following example changes the port where the MQTT broker operates from the default 8883 to port 1234. If you are using Linux, include the `dockerOptions` field.

```
{
  "emqxConfig": {
    "listeners": {
      "ssl": {
        "default": {
          "bind": 1234
        }
      }
    }
  },
  "dockerOptions": "-p 1234:1234"
}
```

**Example: Adjust the MQTT broker's log level**
The following example changes the MQTT broker's log level to `debug`. You can choose from the following log levels:
+ `debug`
+ `info`
+ `notice`
+ `warning`
+ `error`
+ `critical`
+ `alert`
+ `emergency`
The default log level is `warning`.

```
{
  "emqxConfig": {
    "log": {
      "console": {
         "level": "debug"
      }
    }
  }
}
```

**Example: Enable the EMQX dashboard**
The following example enables the EMQX dashboard so that you can monitor and manage your broker. If you are using Linux, include the `dockerOptions` field.

```
{
  "emqxConfig": {
    "dashboard": {
      "listeners": {
        "http": {
          "bind": 18083
        }
      }
    }
  },
  "dockerOptions": "-p 18083:18083"
}
```

------
#### [ 1.0.0 - 1.2.2 ]

This component provides the following configuration parameters that you can customize when you deploy the component.

`emqx`
(Optional) The [EMQX MQTT broker](https://www.emqx.io/docs/en/v4.4/configuration/configuration.html) configuration to use. You can configure a subset of EMQX configuration options in this component.
This object contains the following information:
`listener.ssl.external`
(Optional) The port where the MQTT broker operates.
<a name="mqtt-broker-configuration-mqtt-bridge-requirement"></a>If you specify a different port, and you use the [MQTT bridge component](mqtt-bridge-component.md) to relay MQTT messages to other brokers, you must use MQTT bridge v2.1.0 or later. Configure it to use the port where the MQTT broker operates.
<a name="mqtt-broker-configuration-ip-detector-requirement"></a>If you specify a different port, and you use the [IP detector component](ip-detector-component.md) to manage MQTT broker endpoints, you must use IP detector v2.1.0 or later. Configure it to report the port where the MQTT broker operates.
Default: `8883`
`listener.ssl.external.max_connections`
(Optional) The maximum number of concurrent connections that the MQTT broker supports.
Default: `1024000`
`listener.ssl.external.max_conn_rate`
(Optional) The maximum number of new connections per second the MQTT broker can receive.
Default: `500`
`listener.ssl.external.rate_limit`
(Optional) The bandwidth limit for all connections to the MQTT broker. Specify the bandwidth and duration for that bandwidth separated by a comma (`,`) in the following format: `bandwidth,duration`. For example, you can specify `50KB,5s` to limit the MQTT broker to 50 kilobytes (KB) of data every 5 seconds.
`listener.ssl.external.handshake_timeout`
(Optional) The amount of time that the MQTT broker waits to finish authenticating a new connection.
Default: `15s`
`mqtt.max_packet_size`
(Optional) The maximum size of an MQTT message.
Default: `268435455` (256 MB minus 1)
`log.level`
(Optional) The log level for the MQTT broker. Choose from the following options:
+ `debug`
+ `info`
+ `notice`
+ `warning`
+ `error`
+ `critical`
+ `alert`
+ `emergency`
The default log level is `warning`.

`requiresPrivilege`
(Optional) On Linux core devices, you can specify to run the EMQX MQTT broker without root or administrator privileges. If you set this option to `false`, the system user that runs this component must be a member of the `docker` group.
Default: `true`

`startupTimeoutSeconds`
(Optional) The maximum of time in seconds for the EMQX MQTT broker to start. The component's state changes to `BROKEN` if it exceeds this timeout.
Default: `90`

`ipcTimeoutSeconds`
(Optional) The maximum of time in seconds for the component to wait for the Greengrass nucleus to respond to interprocess communication (IPC) requests. Increase this number if this component reports timeout errors when it checks if a client device is authorized.
Default: `5`

`crtLogLevel`
(Optional) The log level for the AWS Common Runtime (CRT) library.
Defaults to the EMQX MQTT broker log level (`log.level` in `emqx`).

`restartIdentifier`
(Optional) Configure this option to restart the EMQX MQTT broker. When this configuration value changes, this component restarts the MQTT broker. You can use this option to force client devices to disconnect.

`dockerOptions`
(Optional) Configure this option only on Linux operating systems to add parameters to the Docker command line. For example, to map additional ports, use the `-p` Docker parameter:

```
"-p 1883:1883"
```

`mergeConfigurationFiles`
(Optional) Configure this option to add to or override the defaults in the specified EMQX configuration files. For information about the configuration files and their formats, see [Configuration](https://www.emqx.io/docs/en/v4.4/configuration/configuration.html) in the *EMQX 4.0 Documentation*. The values that you specify are appended to the configuration file.
The following example updates the `etc/emqx.conf` file.

```
"mergeConfigurationFiles": {
    "etc/emqx.conf": "broker.sys_interval=30s\nbroker.sys_heartbeat=10s"
},
```
In addition to the configuration files supported by EMQX, Greengrass supports a file that configures the Greengrass auth plugin for EMQX called `etc/plugins/aws_greengrass_emqx_auth.conf`. There are two supported options, `auth_mode` and `use_greengrass_managed_certificates`. To use another auth provider, set the `auth_mode` option to one of the following:
+ `enabled` – (Default) Use the Greengrass authentication and authorization provider.
+ `bypass_on_failure` – Use the Greengrass authentication provider, then use any remaining authentication providers in the EMQX provider chain if Greengrass denies either authentication or authorization.
+ `bypass` – The Greengrass provider is disabled. Authentication and authorization is then handled by the EMQX provider chain.
If the `use_greengrass_managed_certificates` is `true`, this option indicates that Greengrass manages the broker TLS certificates. If `false`, it indicates that you provide the certificates through another source.
The following example updates the defaults in the `etc/plugins/aws_greengrass_emqx_auth.conf` configuration file.

```
"mergeConfigurationFiles": {
    "etc/plugins/aws_greengrass_emqx_auth.conf": "auth_mode=enabled\n use_greengrass_managed_certificates=true\n"
  },
```
`aws.greengrass.clientdevices.mqtt.EMQX` allows you to configure security-sensitive options. These include TLS settings, authentication, and authorization providers. The recommended configuration is the default configuration that uses mutual TLS authentication and the Greengrass Client Device Auth provider.

`replaceConfigurationFiles`
(Optional) Configure this option to replace the specified EMQX configuration files. The values that you specify replace the entire existing configuration file. You can't specify the `etc/emqx.conf` file in this section. You must use `mergeConfigurationFile` to modify `etc/emqx.conf`.

**Example: Configuration merge update**
The following example configuration specifies to operate the MQTT broker on port 443.

```
{
  "emqx": {
    "listener.ssl.external": "443",
    "listener.ssl.external.max_connections": "1024000",
    "listener.ssl.external.max_conn_rate": "500",
    "listener.ssl.external.rate_limit": "50KB,5s",
    "listener.ssl.external.handshake_timeout": "15s",
    "log.level": "warning"
  },
  "requiresPrivilege": "true",
  "startupTimeoutSeconds": "90",
  "ipcTimeoutSeconds": "5"
}
```

------

## Local log file
<a name="mqtt-broker-emqx-component-log-file"></a>

This component uses the following log file.

------
#### [ Linux ]

```
{{/greengrass/v2}}/logs/aws.greengrass.clientdevices.mqtt.EMQX.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\logs\aws.greengrass.clientdevices.mqtt.EMQX.log
```

------

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

  ```
  sudo tail -f {{/greengrass/v2}}/logs/aws.greengrass.clientdevices.mqtt.EMQX.log
  ```

------
#### [ Windows (PowerShell) ]

  ```
  Get-Content {{C:\greengrass\v2}}\logs\aws.greengrass.clientdevices.mqtt.EMQX.log -Tail 10 -Wait
  ```

------

## Licenses
<a name="mqtt-broker-emqx-component-licenses"></a>

On Windows operating systems, this software includes code distributed under the [Microsoft Software License Terms - Microsoft Visual Studio Community 2022](https://visualstudio.microsoft.com/license-terms/vs2022-ga-community). By downloading this software, you agree to that code's license terms.

<a name="component-core-software-license"></a>This component is released under the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

## Changelog
<a name="mqtt-broker-emqx-component-changelog"></a>

The following table describes the changes in each version of the component.

------
#### [ v2.x ]

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.0.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html)  |
| 2.0.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html)  |
| 2.0.1 | Version updated for [client device auth](client-device-auth-component.md) version 2.5.0 release. |
| 2.0.0 | This version of the MQTT 5 broker (EMQX) expects different configuration parameters than version 1.x. If you use a non-default configuration for version 1.x, you must update the component's configuration for 2.x. For more information, see [Configuration](#mqtt-broker-emqx-component-configuration).[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html) |

------
#### [ v1.x ]

|  **Version**  |  **Changes**  |
| --- | --- |
| 1.2.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html)  |
| 1.2.2 | Version updated for [client device auth](client-device-auth-component.md) version 2.4.0 release. |
| 1.2.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html)  |
| 1.2.0 | Adds support for certificate chains. |
| 1.1.0 | <a name="changelog-emqx-1.1.0"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html) |
| 1.0.1 | Fixes an issue during the TLS handshake which results in some MQTT clients failing to connect. |
| 1.0.0 | Initial version. |

------
