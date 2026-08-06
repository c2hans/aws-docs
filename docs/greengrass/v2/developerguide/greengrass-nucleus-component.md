---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html
---

# Greengrass nucleus
<a name="greengrass-nucleus-component"></a>

The Greengrass nucleus component (`aws.greengrass.Nucleus`) is a mandatory component and the minimum requirement to run the AWS IoT Greengrass Core software on a device. You can configure this component to customize and update your AWS IoT Greengrass Core software remotely. Deploy this component to configure settings such as proxy, device role, and AWS IoT thing configuration on your core devices.

**Note**
As of Greengrass version 2.14.0, a memory footprint optimized version of the nucleus device runtime is available for constrained edge devices. See [Greengrass nucleus lite](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html) for more information on its configuration and use.

**Important**
When the version of the nucleus component changes, or when you change certain configuration parameters, the AWS IoT Greengrass Core software—which includes the nucleus and all other components on your device—restarts to apply the changes.
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

**Topics**
+ [Versions](#greengrass-nucleus-component-versions)
+ [Device requirements](#greengrass-v2-requirements)
+ [Supported platforms](#greengrass-v2-supported-platforms)
+ [Operating system](#greengrass-nucleus-component-os-support)
+ [Requirements](#greengrass-nucleus-component-requirements)
+ [Dependencies](#greengrass-nucleus-component-dependencies)
+ [Download and installation](#greengrass-nucleus-component-install)
+ [Configuration](#greengrass-nucleus-component-configuration)
+ [Local log file](#greengrass-nucleus-component-log-file)
+ [Changelog](#greengrass-nucleus-component-changelog)

## Versions
<a name="greengrass-nucleus-component-versions"></a>

This component has the following versions:
+ 2.18.x
+ 2.17.x
+ 2.16.x
+ 2.15.x
+ 2.14.x
+ 2.13.x
+ 2.12.x
+ 2.11.x
+ 2.10.x
+ 2.9.x
+ 2.8.x
+ 2.7.x
+ 2.6.x
+ 2.5.x
+ 2.4.x
+ 2.3.x
+ 2.2.x
+ 2.1.x
+ 2.0.x

## Device requirements
<a name="greengrass-v2-requirements"></a>

**Note**
You can use AWS IoT Device Tester for AWS IoT Greengrass to verify that your device can run the AWS IoT Greengrass Core software and communicate with the AWS Cloud. For more information, see [Using AWS IoT Device Tester for AWS IoT Greengrass V2](device-tester-for-greengrass-ug.md).

------
#### [ Linux ]
+ <a name="requirement-supported-region"></a>The use of an [AWS Region](https://en.wikipedia.org/wiki/Amazon_Web_Services#Availability_and_topology) that supports AWS IoT Greengrass V2. For the list of supported Regions, see [AWS IoT Greengrass V2 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html) in the *AWS General Reference*.
+ Minimum 256 MB disk space available for the AWS IoT Greengrass Core software. This requirement doesn't include components deployed to the core device.
+ Minimum 96 MB RAM allocated to the AWS IoT Greengrass Core software. This requirement doesn't include components that run on the core device. For more information, see [Control memory allocation with JVM options](configure-greengrass-core-v2.md#jvm-tuning).
+ Java Runtime Environment (JRE) version 8 or greater. Java must be available on the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) environment variable on the device. To use Java to develop custom components, you must install a Java Development Kit (JDK). We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required.
+ [GNU C Library](https://www.gnu.org/software/libc/) (glibc) version 2.25 or greater.
+ You can run the AWS IoT Greengrass Core software as a root user. Use `sudo`, for example. You can also run the AWS IoT Greengrass Core software as a non-root user. For more information, see [Set up AWS IoT Greengrass V2 core devices as non-root](setup-greengrass-non-root.md).
+ The root user that runs the AWS IoT Greengrass Core software, such as `root`, must have permission to run `sudo` with any user and any group. The `/etc/sudoers` file must give this user permission to run `sudo` as other groups. The permission for the user in `/etc/sudoers` should look like the following example.

  ```
  root    ALL=(ALL:ALL) ALL
  ```
+ The core device must be able to perform outbound requests to a set of endpoints and ports. For more information, see [Allow device traffic through a proxy or firewall](allow-device-traffic.md).
+ The `/tmp` directory must be mounted with `exec` permissions.
+ All of the following shell commands:
  + `ps -ax -o pid,ppid`
  + `sudo`
  + `sh`
  + `kill`
  + `cp`
  + `chmod`
  + `rm`
  + `ln`
  + `echo`
  + `exit`
  + `id`
  + `uname`
  + `grep`
+ Your device may also require the following optional shell commands:
  + (Optional) `systemctl`. This command is used to set up the AWS IoT Greengrass Core software as a system service.
  + (Optional) `useradd`, `groupadd`, and `usermod`. These command are used to set up the `ggc_user` system user and `ggc_group` system group.
  + (Optional) `mkfifo`. This command is used to run Lambda functions as components.
+ To configure system resource limits for component processes, your device must run Linux kernel version 2.6.24 or later.
+ To run Lambda functions, your device must meet additional requirements. For more information, see [Lambda function requirements](setting-up.md#greengrass-v2-lambda-requirements).

**Important**
On Ubuntu 25.10 and later, the default `sudo` implementation does not support the `-E` (preserve environment) flag. Without this flag, the system does not forward environment variables to components that run as a different system user. As a result, those components fail to start.
To resolve this issue, switch to the classic `sudo` implementation (`sudo.ws`). You must make this change because AWS IoT Greengrass uses the `-E` flag to pass environment variables to component processes.

```
sudo update-alternatives --set sudo /usr/bin/sudo.ws
```

------
#### [ Windows ]
+ <a name="requirement-supported-region"></a>The use of an [AWS Region](https://en.wikipedia.org/wiki/Amazon_Web_Services#Availability_and_topology) that supports AWS IoT Greengrass V2. For the list of supported Regions, see [AWS IoT Greengrass V2 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html) in the *AWS General Reference*.
+ Minimum 256 MB disk space available for the AWS IoT Greengrass Core software. This requirement doesn't include components deployed to the core device.
+ Minimum 160 MB RAM allocated to the AWS IoT Greengrass Core software. This requirement doesn't include components that run on the core device. For more information, see [Control memory allocation with JVM options](configure-greengrass-core-v2.md#jvm-tuning).
+ Java Runtime Environment (JRE) version 8 or greater. Java must be available on the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) system variable on the device. To use Java to develop custom components, you must install a Java Development Kit (JDK). We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required..
**Note**
To use version 2.5.0 of the [Greengrass nucleus](#greengrass-nucleus-component), you must use a 64-bit version of the Java Runtime Environment (JRE). Greengrass nucleus version 2.5.1 supports 32-bit and 64-bit JREs.
+ The user who installs the AWS IoT Greengrass Core software must be an administrator.
+ You must install the AWS IoT Greengrass Core software as a system service. Specify `--setup-system-service true` when you install the software.
+ Each user that runs component processes must exist in the LocalSystem account, and the user's name and password must be in the Credential Manager instance for the LocalSystem account. You can set up this user when you follow instructions to [install the AWS IoT Greengrass Core software](install-greengrass-core-v2.md).
+ The core device must be able to perform outbound requests to a set of endpoints and ports. For more information, see [Allow device traffic through a proxy or firewall](allow-device-traffic.md).

------

## Supported platforms
<a name="greengrass-v2-supported-platforms"></a>

AWS IoT Greengrass officially supports devices running the following platforms. Devices with platforms not included in this list might work, but AWS IoT Greengrass tests on only these specified platforms.

------
#### [ Linux ]

Architectures:
+ Armv7l
+ Armv8 (AArch64)
+ x86\_64

------
#### [ Windows ]

Architectures:
+ x86\_64

Versions:
+ Windows 10
+ Windows 11
+ Windows Server 2019
+ Windows Server 2022
+ Windows Server 2025

**Note**
Some AWS IoT Greengrass features aren't currently supported on Windows devices. For more information, see [Greengrass feature compatibility](operating-system-feature-support-matrix.md) and [Feature considerations](#greengrass-v2-windows-feature-considerations).

------

### Feature considerations
<a name="greengrass-v2-windows-feature-considerations"></a>

Some AWS IoT Greengrass features aren't currently supported on Windows devices. Review the feature differences to confirm if a Windows device satisfies your requirements. For more information, see [Greengrass feature compatibility](operating-system-feature-support-matrix.md).

To build a custom Linux-based operating system, you can use the BitBake recipe for AWS IoT Greengrass in the [`meta-aws` project](https://github.com/aws/meta-aws/tree/master/recipes-iot). The `meta-aws` project provides recipes that you can use to build AWS edge software capabilities in [embedded Linux](https://elinux.org/) systems that are built with [OpenEmbedded](https://www.openembedded.org/wiki/Main_Page) and Yocto Project build frameworks. The [Yocto Project](https://www.yoctoproject.org/) is an open source collaboration project that helps you build custom Linux-based systems for embedded applications regardless of hardware architecture. The BitBake recipe for AWS IoT Greengrass installs, configures, and automatically runs the AWS IoT Greengrass Core software on your device.

Linux platforms can also run AWS IoT Greengrass in a Docker container. For more information, see [Run AWS IoT Greengrass Core software in a Docker container](run-greengrass-docker.md).

## Operating system
<a name="greengrass-nucleus-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

For more information, see [Supported platforms](#greengrass-v2-supported-platforms).

## Requirements
<a name="greengrass-nucleus-component-requirements"></a>

Devices must meet certain requirements to install and run the Greengrass nucleus and the AWS IoT Greengrass Core software. For more information, see [Device requirements](#greengrass-v2-requirements).

The Greengrass nucleus component is supported to run in a VPC. To deploy this component in a VPC, the following is required.
+ The Greengrass nucleus component must have connectivity to AWS IoT data, AWS IoT Credentials, and Amazon S3.

## Dependencies
<a name="greengrass-nucleus-component-dependencies"></a>

The Greengrass nucleus does not include any component dependencies. However, several AWS-provided components include the nucleus as a dependency. For more information, see [AWS-provided components](public-components.md).

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Download and installation
<a name="greengrass-nucleus-component-install"></a>

You can download an installer that sets up the Greengrass nucleus component on your device. This installer sets up your device as a Greengrass core device. There are two types of installations that you can perform: a quick installation that creates required AWS resources for you, or a manual installation where you create the AWS resources yourself. For more information, see [Install the AWS IoT Greengrass Core software](install-greengrass-core-v2.md).

You can also follow a tutorial to install the Greengrass nucleus and explore Greengrass component development. For more information, see [Tutorial: Getting started with AWS IoT Greengrass V2](getting-started.md).

## Configuration
<a name="greengrass-nucleus-component-configuration"></a>

This component provides the following configuration parameters that you can customize when you deploy the component. Some parameters require that the AWS IoT Greengrass Core software restarts to take effect. For more information about why and how to configure this component, see [Configure the AWS IoT Greengrass Core software](configure-greengrass-core-v2.md).

`iotRoleAlias`
<a name="nucleus-component-configuration-iot-role-alias"></a>The AWS IoT role alias that points to a token exchange IAM role. The AWS IoT credentials provider assumes this role to allow the Greengrass core device to interact with AWS services. For more information, see [Authorize core devices to interact with AWS services](device-service-role.md).
When you run the AWS IoT Greengrass Core software with the `--provision true` option, the software provisions a role alias and sets its value in the nucleus component.

  `interpolateComponentConfiguration`
(Optional) You can enable the Greengrass nucleus to interpolate [component recipe variables](component-recipe-reference.md#recipe-variables) in component configurations and [merge configuration updates](update-component-configurations.md#merge-configuration-update-recipe-variables). We recommend that you set this option to `true` so that the core device can run Greengrass components that use recipe variables in their configurations.
This feature is available for v2.6.0 and later of this component.
Default: `false`

`networkProxy`
(Optional) The network proxy to use for all connections. For more information, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy).
<a name="nucleus-component-parameter-restart-para"></a>When you deploy a change to this configuration parameter, the AWS IoT Greengrass Core software restarts for the change to take effect.
This object contains the following information:
`noProxyAddresses`
(Optional) A comma-separated list of IP addresses or hostnames that are exempt from the proxy.
`proxy`
The proxy to which to connect. This object contains the following information:
`url`
The URL of the proxy server in the format `scheme://userinfo@host:port`.  <a name="nucleus-component-configuration-proxy-url-segments"></a>
+ `scheme` – The scheme, which must be `http` or `https`.
**Important**
<a name="https-proxy-greengrass-nucleus-requirement"></a>Greengrass core devices must run [Greengrass nucleus ](#greengrass-nucleus-component) v2.5.0 or later to use HTTPS proxies.
If you configure an HTTPS proxy, you must add the proxy server CA certificate to the core device's Amazon root CA certificate. For more information, see [Enable the core device to trust an HTTPS proxy](configure-greengrass-core-v2.md#https-proxy-certificate-trust).
+ `userinfo` – (Optional) The user name and password information. If you specify this information in the `url`, the Greengrass core device ignores the `username` and `password` fields.
+ `host` – The host name or IP address of the proxy server.
+ `port` – (Optional) The port number. If you don't specify the port, then the Greengrass core device uses the following default values:
  + `http` – 80
  + `https` – 443
`username`
(Optional) The user name that authenticates the proxy server.
`password`
(Optional) The password that authenticates the proxy server.

`mqtt`
(Optional) The MQTT configuration for the Greengrass core device. For more information, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy).
<a name="nucleus-component-parameter-restart-para"></a>When you deploy a change to this configuration parameter, the AWS IoT Greengrass Core software restarts for the change to take effect.
This object contains the following information:
`port`
(Optional) The port to use for MQTT connections.
Default: `8883`
`keepAliveTimeoutMs`
(Optional) The amount of time in milliseconds between each `PING` message that the client sends to keep the MQTT connection alive. This value must be greater than `pingTimeoutMs`.
Default: `60000` (60 seconds)
`pingTimeoutMs`
(Optional) The amount of time in milliseconds that the client waits to receive a `PINGACK` message from the server. If the wait exceeds the timeout, the core device closes and reopens the MQTT connection. This value must be less than `keepAliveTimeoutMs`.
Default: `30000` (30 seconds)
`operationTimeoutMs`
(Optional) The amount of time in milliseconds that the client waits for MQTT operations (such as `CONNECT` or `PUBLISH`) to complete. This option doesn't apply to MQTT `PING` or keep alive messages.
Default: `30000` (30 seconds)
`maxInFlightPublishes`
(Optional) The maximum number of unacknowledged MQTT QoS 1 messages that can be in flight at the same time.
This feature is available for v2.1.0 and later of this component.
Default: `5`
Valid range: Maximum value of 100
`maxMessageSizeInBytes`
(Optional) The maximum size of an MQTT message. If a message exceeds this size, the Greengrass nucleus rejects the message with an error.
This feature is available for v2.1.0 and later of this component.
Default: `131072` (128 KB)
Valid range: Maximum value of `2621440` (2.5 MB)
`maxPublishRetry`
(Optional) The maximum number of times to retry a message that fails to publish. You can specify `-1` to retry unlimited times.
This feature is available for v2.1.0 and later of this component.
Default: `100`
`standaloneMqttTimeoutMs`
(Optional) The time, in milliseconds, that the nucleus waits for standalone MQTT connections during IoT connectivity switch operations. This timeout covers the pre-flight connectivity check and the status report that the nucleus sends to the source account after a successful switch.
This feature requires v2.18.0 or later of this component.
Default: `60000` (60 seconds)
Valid range: Minimum value of 1
`spooler`
(Optional) The MQTT spooler configuration for the Greengrass core device. This object contains the following information:
`storageType`
The storage type for storing messages. If `storageType` is set to `Disk`, the `pluginName` can be configured. You can specify either `Memory` or `Disk`.
This feature is available for v2.11.0 and later of the [Greengrass nucleus component](#greengrass-nucleus-component).
If the MQTT spooler `storageType` is set to `Disk` and you want to downgrade Greengrass nucleus from version 2.11.x to an earlier version, you must change the configuration back to `Memory`. The only configuration for `storageType` that is supported in Greengrass nucleus versions 2.10.x and earlier is `Memory`. Not following this guidance can result in the spooler breaking. This would cause your Greengrass core device to not be able to send MQTT messages to the AWS Cloud.
Default: `Memory`
`pluginName`
(Optional) The plugin component name. This component will only be used if `storageType` is set to `Disk`. This option defaults to `aws.greengrass.DiskSpooler` and will use the Greengrass-provided [Disk spooler](disk-spooler-component.md).
This feature is available for v2.11.0 and later of the [Greengrass nucleus component](#greengrass-nucleus-component).
Default: `"aws.greengrass.DiskSpooler"`
`maxSizeInBytes`
(Optional) The maximum size of the cache where the core device stores unprocessed MQTT messages in memory. If the cache is full, new messages are rejected.
Default: `2621440` (2.5 MB)
`keepQos0WhenOffline`
(Optional) You can spool MQTT QoS 0 messages that the core device receives while its offline. If you set this option to `true`, the core device spools QoS 0 messages that it can't send while it's offline. If you set this option to `false`, the core device discards these messages. The core device always spools QoS 1 messages unless the spool is full.
Default: `false`
`version`
(Optional) The version of MQTT. You can specify either `mqtt3` or `mqtt5`.
This feature is available for v2.10.0 and later of the [Greengrass nucleus component](#greengrass-nucleus-component).
Default: `mqtt5`
`receiveMaximum`
(Optional) The maximum number of unacknowledged QoS1 packets the broker can send.
This feature is available for v2.10.0 and later of the [Greengrass nucleus component](#greengrass-nucleus-component).
Default: `100`
`sessionExpirySeconds`
(Optional) The amount of time in seconds you can request for a session to last from IoT Core. The default is the maximum time supported by AWS IoT Core.
This feature is available for v2.10.0 and later of the [Greengrass nucleus component](#greengrass-nucleus-component).
Default: `604800 (7 days)`
`minimumReconnectDelaySeconds`
(Optional) An option for reconnection behavior. The minimum amount of time in seconds for MQTT to reconnect.
This feature is available for v2.10.0 and later of the [Greengrass nucleus component](#greengrass-nucleus-component).
Default: `1`
`maximumReconnectDelaySeconds`
(Optional) An option for reconnection behavior. The maximum amount of time in seconds for MQTT to reconnect.
This feature is available for v2.10.0 and later of the [Greengrass nucleus component](#greengrass-nucleus-component).
Default: `120`
`minimumConnectedTimeBeforeRetryResetSeconds`
(Optional) An option for reconnection behavior. The amount of time in seconds a connection must be active before the retry delay is reset back to the minimum.
This feature is available for v2.10.0 and later of the [Greengrass nucleus component](#greengrass-nucleus-component).
Default: `30`

  `jvmOptions`
(Optional) The JVM options to use to run the AWS IoT Greengrass Core software. For information about recommended JVM options for running AWS IoT Greengrass Core software, see [Control memory allocation with JVM options](configure-greengrass-core-v2.md#jvm-tuning).
<a name="nucleus-component-parameter-restart-para"></a>When you deploy a change to this configuration parameter, the AWS IoT Greengrass Core software restarts for the change to take effect.

`iotDataEndpoint`
<a name="nucleus-component-configuration-iot-data-endpoint"></a>The AWS IoT data endpoint for your AWS account.
<a name="nucleus-component-set-iot-endpoints"></a>When you run the AWS IoT Greengrass Core software with the `--provision true` option, the software gets your data and credentials endpoints from AWS IoT and sets them in the nucleus component.

`iotCredEndpoint`
<a name="nucleus-component-configuration-iot-cred-endpoint"></a>The AWS IoT credentials endpoint for your AWS account.
<a name="nucleus-component-set-iot-endpoints"></a>When you run the AWS IoT Greengrass Core software with the `--provision true` option, the software gets your data and credentials endpoints from AWS IoT and sets them in the nucleus component.

`greengrassDataPlaneEndpoint`
This feature is available in v2.7.0 and later of this component.
(Optional) The Greengrass data plane endpoint to use. Set to **iotdata** to use the same endpoint as the IoT data endpoint specified in `iotDataEndpoint`.
You must set this option to **iotdata** in the following cases:
+ You use a device certificate signed by a private certificate authority (CA). For more information, see [Use a device certificate signed by a private CA](configure-greengrass-core-v2.md#configure-nucleus-private-ca).
+ You deploy nucleus configuration updates to switch the device's IoT connectivity to a different AWS account or Region. Without this setting, the data plane remains bound to the original account after the connectivity switch. This breaks component artifact downloads and control plane operations. For more information, see [Switch a Greengrass core device to a different AWS account or Region](switch-core-device-connectivity.md).
You can set this option during deployment or installation using the **--init-config** [installer argument](configure-installer.md).
Default: `""` (empty string – uses the Greengrass service endpoint)

`greengrassDataPlanePort`
This feature is available in v2.0.4 and later of this component.
(Optional) The port to use for data plane connections. For more information, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy).
You must specify a port where the device can make outbound connections. If you specify a port that is blocked, the device won't be able to connect to AWS IoT Greengrass to receive deployments.
Choose from the following options:
+ `443`
+ `8443`
Default: `8443`

`awsRegion`
The AWS Region to use.

`runWithDefault`
The system user to use to run components.
<a name="nucleus-component-parameter-restart-para"></a>When you deploy a change to this configuration parameter, the AWS IoT Greengrass Core software restarts for the change to take effect.
This object contains the following information:
`posixUser`
The name or ID of the system user and, optionally, system group that the core device uses to run generic and Lambda components. Specify the user and group separated by a colon (`:`) in the following format: `user:group`. The group is optional. If you don't specify a group, the AWS IoT Greengrass Core software uses the primary group for the user. For example, you can specify `ggc_user` or `ggc_user:ggc_group`. For more information, see [Configure the user that runs components](configure-greengrass-core-v2.md#configure-component-user).
When you run the AWS IoT Greengrass Core software installer with the `--component-default-user {{ggc_user}}:{{ggc_group}}` option, the software sets this parameter in the nucleus component.
`windowsUser`
This feature is available in v2.5.0 and later of this component.
The name of the Windows user to use to run this component on Windows core devices. The user must exist on each Windows core device, and its name and password must be stored in the LocalSystem account's Credentials Manager instance. For more information, see [Configure the user that runs components](configure-greengrass-core-v2.md#configure-component-user).
When you run the AWS IoT Greengrass Core software installer with the `--component-default-user {{ggc_user}}` option, the software sets this parameter in the nucleus component.
`systemResourceLimits`
This feature is available in v2.4.0 and later of this component. AWS IoT Greengrass doesn't currently support this feature on Windows core devices.
The system resource limits to apply to generic and non-containerized Lambda component processes by default. You can override system resource limits for individual components when you create a deployment. For more information, see [Configure system resource limits for components](configure-greengrass-core-v2.md#configure-component-system-resource-limits).
This object contains the following information:
`cpus`
 <a name="system-resource-limits-cpu-definition-each"></a>The maximum amount of CPU time that each component's processes can use on the core device. A core device's total CPU time is equivalent to the device's number of CPU cores. For example, on a core device with 4 CPU cores, you can set this value to `2` to limit each component's processes to 50 percent usage of each CPU core. On a device with 1 CPU core, you can set this value to `0.25` to limit each component's processes to 25 percent usage of the CPU. If you set this value to a number greater than the number of CPU cores, the AWS IoT Greengrass Core software doesn't limit the components' CPU usage.
`memory`
 <a name="system-resource-limits-memory-definition-each"></a>The maximum amount of RAM (in kilobytes) that each component's processes can use on the core device.

 `s3EndpointType`
(Optional) The S3 endpoint type. This parameter will only take effect for the US East (N. Virginia) (`us-east-1`) Region. Setting this parameter from any other Region will be ignored. Choose from the following options:
+ `REGIONAL` – S3 client and presigned URL uses the regional endpoint.
+ `GLOBAL` – S3 client and presigned URL uses the legacy endpoint.
+ `DUALSTACK` – S3 presigned URL uses the dualstack endpoint.
Default: `GLOBAL`

 `fipsMode`
(Optional) Causes Greengrass to use FIPS endpoints. For more information on how to enable FIPS endpoints, see [FIPS endpoints](FIPS.html).
Choose from the following options:
+ `true` When set to true the endpoints will use FIPS endpoint.
+ `false` When false the endpoints will not use FIPS endpoint.
Default: `false`

`logging`
(Optional) The logging configuration for the core device. For more information about how to configure and use Greengrass logs, see [Monitor AWS IoT Greengrass logs](monitor-logs.md).
This object contains the following information:
  `level`
(Optional) The minimum level of log messages to output.
Choose from the following log levels, listed here in level order:  <a name="nucleus-log-levels"></a>
+ `DEBUG`
+ `INFO`
+ `WARN`
+ `ERROR`
Default: `INFO`
  `format`
(Optional) The data format of the logs. Choose from the following options:
+ `TEXT` – Choose this option if you want to view logs in text form.
+ `JSON` – Choose this option if you want to view logs with the [Greengrass CLI logs command](gg-cli-logs.md) or interact with logs programmatically.
Default: `TEXT`
`outputType`
(Optional) The output type for logs. Choose from the following options:
+ `FILE` – The AWS IoT Greengrass Core software outputs logs to files in the directory that you specify in `outputDirectory`.
+ `CONSOLE` – The AWS IoT Greengrass Core software prints logs to `stdout`. Choose this option to view logs as the core device prints them.
Default: `FILE`
  `fileSizeKB`
(Optional) The maximum size of each log file (in kilobytes). After a log file exceeds this maximum file size, the AWS IoT Greengrass Core software creates a new log file.
<a name="nucleus-component-logging-parameter-file-only"></a>This parameter applies only when you specify `FILE` for `outputType`.
Default: `1024`
  `totalLogsSizeKB`
(Optional) The maximum total size of log files (in kilobytes) for each component, including the Greengrass nucleus. The Greengrass nucleus' log files also include logs from [plugin components](develop-greengrass-components.md#component-types). After a component's total size of log files exceeds this maximum size, the AWS IoT Greengrass Core software deletes that component's oldest log files.
This parameter is equivalent to the [log manager component's](log-manager-component.md) [disk space limit](log-manager-component.md#log-manager-component-configuration) parameter (`diskSpaceLimit`), which you can specify for the Greengrass nucleus (system) and each component. The AWS IoT Greengrass Core software uses the minimum of the two values as the maximum total log size for the Greengrass nucleus and each component.
<a name="nucleus-component-logging-parameter-file-only"></a>This parameter applies only when you specify `FILE` for `outputType`.
Default: `10240`
  `outputDirectory`
(Optional) The output directory for log files.
<a name="nucleus-component-logging-parameter-file-only"></a>This parameter applies only when you specify `FILE` for `outputType`.
Default: `{{/greengrass/v2}}/logs`, where `{{/greengrass/v2}}` is the AWS IoT Greengrass root folder.

  `fleetstatus`
This parameter is available in v2.1.0 and later of this component.
(Optional) The fleet status configuration for the core device.
This object contains the following information:
`periodicStatusPublishIntervalSeconds`
(Optional) The amount of time (in seconds) between which the core device publishes device status to the AWS Cloud.
Minimum: `86400` (24 hours)
Default: `86400` (24 hours)

  `telemetry`
(Optional) The system health telemetry configuration for the core device. For more information about telemetry metrics and how to act on telemetry data, see [Gather system health telemetry data from AWS IoT Greengrass core devices](telemetry.md).
This object contains the following information:
`enabled`
(Optional) You can enable or disable telemetry.
Default: `true`
`periodicAggregateMetricsIntervalSeconds`
(Optional) The interval (in seconds) over which the core device aggregates metrics.
If you set this value lower than the minimum supported value, the nucleus uses the default value instead.
Minimum: `3600`
Default: `3600`
`periodicPublishMetricsIntervalSeconds`
(Optional) The amount of time (in seconds) between which the core device publishes telemetry metrics to the AWS Cloud.
If you set this value lower than the minimum supported value, the nucleus uses the default value instead.
Minimum: `86400`
Default: `86400`

`deploymentPollingFrequencySeconds`
(Optional) The period in seconds at which to poll for deployment notifications.
Default: `15`

`componentStoreMaxSizeBytes`
(Optional) The maximum size on disk of the component store, which comprises component recipes and artifacts.
Default: `10000000000` (10 GB)

  `platformOverride`
(Optional) A dictionary of attributes that identify the core device's platform. Use this to define custom platform attributes that component recipes can use to identify the correct lifecycle and artifacts for the component. For example, you might define a hardware capability attribute to deploy only the minimal set of artifacts for a component to run. For more information, see the [manifest platform parameter](component-recipe-reference.md#component-platform-definition) in the component recipe.
You can also use this parameter to override the `os` and `architecture` platform attributes of the core device.

  `httpClient`
This parameter is available in v2.5.0 and later of this component.
(Optional) The HTTP client configuration for the core device. These configuration options apply to all HTTP requests made by this component. If a core device runs on a slower network, you can increase these timeout durations to prevent HTTP requests from timing out.
This object contains the following information:
`connectionTimeoutMs`
(Optional) The amount of time (in milliseconds) to wait for a connection to open before the connection request times out.
Default: `2000` (2 seconds)
`socketTimeoutMs`
(Optional) The amount of time (in milliseconds) to wait for data to transfer over an open connection before the connection times out.
Default: `30000` (30 seconds)

  `deploymentConfigurationTimeSource`
This parameter is available in v2.15.0 and later of this component.
(Optional) The timestamp to use when processing a deployment. The default is the `deploymentCreationTime`.
This object contains the following values:
`deploymentCreationTime`
The default value of `deploymentConfigurationTimeSource`. The device uses the deployment creation timestamp to resolve configuration key conflicts during processing. When this behavior is selected, local device configuration held by the nucleus may have a greater timestamp than that of the incoming deployment and rejects incoming configuration changes which are now considered outdated.
`deploymentProcessingTime`
The device uses its local timestamp to resolve configuration key conflicts during deployment processing. When processed, the device updates configurations based on the processing timestamp rather than the deployment creation timestamp. This behavior assumes the device clock is properly calibrated.
Configure this nucleus setting in your initial device image or installation rather than through a deployment when you want new devices to use this behavior on first connection. Use the [https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-installer.html](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-installer.html) option of the nucleus classic installer for this configuration.
This initial configuration is essential because devices process multiple deployments in arbitrary order. Without proper initial configuration, a device might process deployments using the default `deploymentCreationTime` behavior before receiving the deployment that sets the nucleus configuration to `deploymentProcessingTime`.

**Example: Configuration merge update**

```
{
  "iotRoleAlias": "GreengrassCoreTokenExchangeRoleAlias",
  "networkProxy": {
    "noProxyAddresses": "http://192.168.0.1,www.example.com",
    "proxy": {
      "url": "http://my-proxy-server:1100",
      "username": "Mary_Major",
      "password": "pass@word1357"
    }
  },
  "mqtt": {
    "port": 443
  },
  "greengrassDataPlanePort": 443,
  "jvmOptions": "-Xmx64m",
  "runWithDefault": {
    "posixUser": "ggc_user:ggc_group"
  }
}
```

## Local log file
<a name="greengrass-nucleus-component-log-file"></a>

This component uses the following log file.

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
<a name="greengrass-nucleus-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.18.2 |  **Bug fixes and improvements**<br />   Fixes an issue where the nucleus could write unchanged configuration values to the configuration store.     |
| 2.18.1 |  **Bug fixes and improvements**<br />   Fixes an issue where the nucleus might fail to fetch credentials after a transient connection failure.     |
| 2.18.0 |  **New features**<br />   Adds support for switching a core device's AWS IoT connectivity to a different AWS account or region through a nucleus configuration deployment. The nucleus validates connectivity to the new endpoints before it applies the change, and reports the terminal deployment status to the source account.   Adds support for Windows Server 2025.   <br />**Bug fixes and improvements**<br />   Fixes a startup timing issue on systemd devices by starting the AWS IoT Greengrass Core software only after the system clock synchronizes.   Fixes an issue where a component might encounter stale subscriptions after it closes a local IPC stream during an in-progress subscribe request.   General bug fixes and improvements.     |
| 2.17.0 |  **New features**<br />   Installs all Amazon Root CA certificates during auto-provisioning.   Adds an uninstall lifecycle that runs when a deployment removes a component.   Allows installing Greengrass Core software as a regular Linux user.     |
| 2.16.1 |  **Bug fixes and improvements**<br />   Adds configuration for credential retry intervals after Token Exchange Service failures.     |
| 2.16.0 |  **New features**<br />   Nucleus now supports cgroups V2.    **Bug fixes and improvements**<br />   Fixes an issue where the nucleus would not clean up stale deployments when a deployment was cancelled.     |
| 2.15.1 |  **Bug fixes and improvements**<br />   Fixes an issue where the nucleus failed to clean up component processes after the 30-second shutdown timeout during bootstrap deployments.     |
| 2.15.0 |  **New features**<br />   Adds telemetry feature to include host system information like CPU and OS details. For more information, see telemetry component page.   Adds `deploymentConfigurationTimeSource` configuration. For more information, see nucleus component configuration.    **Bug fixes and improvements**<br />   Nucleus now prioritizes the use of local versions and artifacts by default, improving deployment consistency and reducing external dependencies. Users can override this behavior by specifying alternative preferences in the deployment document.   Adds a new warning log when a provided Windows user doesn't match the character set normally accepted by Windows.     |
| 2.14.3 | Bug fixes and improvements+  Allows the token exchange service to restart on port configuration changes. <br />+  Fixes an issue where fleet status service doesn't send component status change messages for unpinned lambdas if they aren't triggered. <br />+  Fixes an issue where components aren't gracefully shutdown when a new component version is deployed. <br />+  Fixes an issue where built-in plugins’ injection hooks are executed twice resulting in extra lifecycle events and duplicate logging. <br />+  Improves component lifecycle logging on Windows devices.  |
| 2.14.2 | Bug fixes and improvements+  Fixes an issue where an HTTP client isn't configured with mutual auth.  |
| 2.14.1 | Bug fixes and improvements+  Fixes an issue where components weren't stopped properly on new installations of Greengrass.  |
| 2.14.0 |  This version is no longer available. The improvements in this version are available in later versions of this component.  **New features**<br />   New dual-stack endpoint support enables IPv6 network communication.   Enhanced resilience against nucleus restart failures and `Launch`directory corruption.   <br />**Bug fixes and improvements**<br />   Fixes memory leaks in IPC PubSub subscription closures.   Fixes run lifecycle of the component where it enters into ERRORED state due to startup timeout when skipif condition is true.   Fixes an issue where the core device fails to connect to AWS IoT Core when the TLS policy is set to TLS13\_1\_3\_2022\_10.      |
| 2.13.0 |  **New features**<br />   Support FIPS endpoint in Nucleus.   <br />**Bug fixes and improvements**<br />   Cancel deployment improvements: Deployments can now be cancelled while a new configuration is being merged and while waiting for services to start.     |
| 2.12.6 |  **Bug fixes and improvements**<br />   Fixes an issue that causes a crash at startup on certain ARMv8 processors, including the Jetson Nano.     |
| 2.12.5 |  **Bug fixes and improvements**<br />   Fixes an issue where deployment rollback occasionally gets stuck while rolling back a previously broken component with hard dependencies.   Fixes an issue where the nucleus doesn't publish status updates after fleet provisioning.   Adds retries for the `GetDeploymentConfiguration` API after getting 404 errors.     |
| 2.12.4 |  **Bug fixes and improvements**<br />   Fixes an issue where the nucleus enters a deadlock condition during startup on some Linux devices.     |
| 2.12.3 |  This version is no longer available. The improvements in this version are available in later versions of this component. Bug fixes and improvements+  Fixes an issue where the nucleus doesn't report the correct component status after the nucleus relaunches and during component recovery. <br />+  General bug fixes and improvements.  |
| 2.12.2 |  **Bug fixes and improvements**<br />   Fixes an issue where old logs weren't cleaned up properly.   General bug fixes and improvements.     |
| 2.12.1 |  **Bug fixes and improvements**<br />   Fixes an issue where the nucleus may duplicate MQTT subscriptions to deployment topics leading to additional logging and MQTT publishes.     |
| 2.12.0 |  <a name="changelog-nucleus-2.12.0"></a>**New features**<br />   Enables you to run the bootstrap lifecycle steps as part of a rollback deployment.     |
| 2.11.3 |  <a name="changelog-nucleus-2.11.3"></a>**Bug fixes and improvements**<br />   Fixes an issue in the nucleus where it may improperly start a component when its dependencies fail.   <br />**New features**<br />   Adds configurable s3 endpoint type.     |
| 2.11.2 |  <a name="changelog-nucleus-2.11.2"></a>**Bug fixes and improvements**<br />   Fixes an issue in the nucleus MQTT 5 client where it may appear offline when a large number (> 50) of subscriptions are in use.   Adds a retry for the docker dial TCP failure.     |
| 2.11.1 |  <a name="changelog-nucleus-2.11.1"></a>**Bug fixes and improvements**<br />   Fixes an issue where the nucleus doesn't start if a bootstrap task fails and the deployment metadata file is corrupted.   Fixes an issue where on-demand Lambda components aren't reported in deployment status updates.   Adds support for duplicate authorization policy IDs.     |
| 2.11.0 |  <a name="changelog-nucleus-2.11.0"></a>**New features**<br />   Enables you to cancel a local deployment.   Enables you to configure a failure handling policy for a local deployment.   Adds support for a disk spooler plugin.     |
| 2.10.3 |  <a name="changelog-nucleus-2.10.3"></a>**Bug fixes and improvements**<br />   Fixes an issue where Greengrass doesn't subscribe to deployment notifications when using the PKCS\#11 provider.     |
| 2.10.2 |  <a name="changelog-nucleus-2.10.2"></a>**Bug fixes and improvements**<br />   Allows case insensitive parsing of component lifecycles.   Fixes an issue where the environment PATH variable was not recreated correctly.   Fixes proxy URI encoding for components including stream manager for usernames with special characters.     |
| 2.10.1 |  <a name="changelog-nucleus-2.10.1"></a>**Bug fixes and improvements**<br />   Fixes an issue that could cause a crash at startup on certain ARMv8 processors, including the Jetson Nano.   Greengrass no longer closes a component's standard in, this reverts the behavior to the pre-2.10.0 behavior     |
| 2.10.0 |  <a name="changelog-nucleus-2.10.0"></a>**New features**<br />   Adds `interpolateComponentConfiguration` support for the empty regular expression. Greengrass now interpolates from the root config object.   Adds support for MQTT5.   Adds a mechanism for loading plugin components quickly without scanning.   Enables Greengrass to save disk space by deleting unused Docker images.   <br />**Bug fixes and improvements**<br />   Fixes an issue where rollback leaves certain configuration values in place from a deployment.   Fixes an issue where the Greengrass nucleus validates for an AWS domain sequence in custom non-AWS credentials and data endpoints.   Updates multi-group dependency resolution to re-resolve all group dependencies via AWS Cloud negotiation, instead of locking to the active version. This update also removes the deployment error code `INSTALLED_COMPONENT_NOT_FOUND`.   Updates the Greengrass nucleus to skip downloading Docker images when they already exist locally.   Updates the Greengrass nucleus to restart a component install step before timeout expires.   Additional minor fixes and improvements.     |
| 2.9.6 |  <a name="changelog-nucleus-2.9.6"></a>**Bug fixes and improvements**<br />   Fixes an issue where a Greengrass deployment fails with the error LAUNCH\_DIRECTORY\_CORRUPTED and a subsequent device reboot fails to start Greengrass. This error may occur when you move the Greengrass device between multiple thing groups with deployments that require Greengrass to restart.     |
| 2.9.5 |  <a name="changelog-nucleus-2.9.5"></a>**New features**<br />   Adds support for Greengrass nucleus software signature verification.   <br />**Bug fixes and improvements**<br />   Fixes an issue where a deployment fails when the local recipe metadata region doesn't match the Greengrass nucleus launch region. The Greengrass nucleus now renegotiates with the cloud when this happens.   Fixes an issue where the MQTT message spooler fills up and never removes messages.   Additional minor fixes and improvements.     |
| 2.9.4 |  <a name="changelog-nucleus-2.9.4"></a>**Bug fixes and improvements**<br />   Checks for a null message before it drops QOS 0 messages.   Truncates job status detail values if they exceed the 1024 character limit.   Updates the bootstrap script for Windows to correctly read the Greengrass root path if that path includes spaces.   Updates subscribing to AWS IoT Core so that it drops client messages if the subscription response wasn't sent.   Ensures that the nucleus loads its configuration from backup files when the main configuration file is corrupt or missing.      |
| 2.9.3 |  <a name="changelog-nucleus-2.9.3"></a>**Bug fixes and improvements**<br />   Ensures MQTT client IDs aren't duplicated.   Adds more robust file-reading and writing to avoid and recover from corruption.   Retries docker image pull on specific network-related errors.   Adds the `noProxyAddresses` option for MQTT connection.     |
| 2.9.2 |  <a name="changelog-nucleus-2.9.2"></a>**Bug fixes and improvements**<br />   Fixes an issue where configuring `interpolateComponentConfiguration` doesn't apply to an ongoing deployment.   Uses OSHI to list all child processes.     |
| 2.9.1 |  <a name="changelog-nucleus-2.9.1"></a>**Bug fixes and improvements**<br />   Adds fix where Greengrass restarts if a deployment removes a plugin component.     |
| 2.9.0 |  <a name="changelog-nucleus-2.9.0"></a>**New features**<br />   Adds the ability to create subdeployments that retry deployments with a smaller subset of devices. This feature creates a more efficient way to test and resolve unsuccessful deployments.   <br />**Bug fixes and improvements**<br />   Improves support for systems that don't have `useradd`, `groupadd`, and `usermod`.   Additional minor fixes and improvements.     |
| 2.8.1 |  <a name="changelog-nucleus-2.8.1"></a>**Bug fixes and improvements**<br />   Fixes an issue where deployment error codes were not generated correctly from Greengrass API errors.   Fixes an issue where fleet status updates send inaccurate information when a component reaches an `ERRORED` state during a deployment.   Fixes an issue where deployments couldn’t complete when Greengrass had more than 50 existing subscriptions.     |
| 2.8.0 |  <a name="changelog-nucleus-2.8.0"></a>**New features**<br />   Updates the Greengrass nucleus to report a [deployment health status](deployment-health-notifications.md) response that includes detailed error codes when there is a problem deploying components to a core device. For more information, see [Detailed deployment error codes](troubleshooting-deployment.md).   Updates the Greengrass nucleus to report a [component health status](deployment-health-notifications.md) response that includes detailed error codes when a component enters the `BROKEN` or `ERRORED` state. For more information, see [Detailed component status codes](troubleshooting-component.md).   Expands status message fields to improve cloud availability information for devices.   Improves fleet status service robustness.   <br />**Bug fixes and improvements**<br />   Allows a broken component to reinstall when its configuration changes.   Fixes an issue where a nucleus restart during bootstrap deployment causes a deployment to fail.   Fixes an issue in Windows where installation fails when a root path contains spaces.   Fixes an issue where a component shut down during a deployment uses the shutdown script of the new version.   Various shutdown improvements.   Additional minor fixes and improvements.     |
| 2.7.0 |  <a name="changelog-nucleus-2.7.0"></a>**New features**<br />   Updates the Greengrass nucleus to send status updates to the AWS IoT Greengrass cloud when the core device applies a local deployment.   Adds support for client certificates signed by a custom certificate authority (CA), where the CA isn't registered with AWS IoT. To use this feature, you can set the new `greengrassDataPlaneEndpoint` configuration option to `iotdata`. For more information, see [Use a device certificate signed by a private CA](configure-greengrass-core-v2.md#configure-nucleus-private-ca).    <br />**Bug fixes and improvements**<br />   Fixes an issue where the Greengrass nucleus rolls back a deployment in certain scenarios when the nucleus is stopped or restarted. The nucleus now resumes the deployment after the nucleus restarts.   Updates the Greengrass installer to respect the `--start` argument when you specify to set up the software as a system service.   Updates the behavior of [SubscribeToComponentUpdates](ipc-component-lifecycle.md#ipc-operation-subscribetocomponentupdates) to set the deployment ID in events where the nucleus updated a component.   Additional minor fixes and improvements.     |
| 2.6.0 |  <a name="changelog-nucleus-2.6.0"></a>**New features**<br />   Adds support for MQTT wildcards when you subscribe to local publish/subscribe topics. For more information, see [Publish/subscribe local messages](ipc-publish-subscribe.md) and [SubscribeToTopic](ipc-publish-subscribe.md#ipc-operation-subscribetotopic).   Adds support for recipe variables in component configurations, other than the `{{component_dependency_name}}:configuration:{{json_pointer}}` recipe variable. You can use these recipes variables when you define a component's `DefaultConfiguration` in a recipe or when you configure a component in a deployment. To enable this feature, set the [interpolateComponentConfiguration](#greengrass-nucleus-component-configuration-interpolate-component-configuration) configuration option to `true`. For more information, see [Recipe variables](component-recipe-reference.md#recipe-variables) and [Use recipe variables in merge updates](update-component-configurations.md#merge-configuration-update-recipe-variables).   Adds full support for the `*` wildcard in interprocess communication (IPC) authorization policies. You can now specify the `*` character in a resource string to match any combination of characters. For more information, see [Wildcards in authorization policies](interprocess-communication.md#ipc-authorization-policy-wildcards).   Adds support for custom components to call IPC operations that the Greengrass CLI uses. You can use these IPC operations to manage local deployments, view component details, and generate a password that you can use to sign in to the [local debug console](local-debug-console-component.md). For more information, see [IPC: Manage local deployments and components](ipc-local-deployments-components.md).   <br />**Bug fixes and improvements**<br />   Fixes an issue where dependent components wouldn't react when their hard dependencies restart or change states in certain scenarios.   Improves error messages that the core device reports to the AWS IoT Greengrass cloud service when a deployment fails.   Fixes an issue where the Greengrass nucleus applied a thing deployment twice in certain scenarios when the nucleus restarts.   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.     |
| 2.5.6 |  <a name="changelog-nucleus-2.5.6"></a>**New features**<br />   Adds support for hardware security modules that use ECC keys. You can use a hardware security module (HSM) to securely store the device's private key and certificate. For more information, see [Hardware security integration](hardware-security.md).   <br />**Bug fixes and improvements**<br />   Fixes an issue where the deployment never completes when you deploy a component with a broken install script in certain scenarios.   Improves performance during startup.   Additional minor fixes and improvements.     |
| 2.5.5 |  <a name="changelog-nucleus-2.5.5"></a>**New features**<br />   Adds the `GG_ROOT_CA_PATH` environment variable for components, so you can access the root certificate authority (CA) certificate in custom components.   <br />**Bug fixes and improvements**<br />   Adds support for Windows devices that use a display language other than English.   Updates how the Greengrass nucleus parses Boolean [installer arguments](configure-installer.md), so you can specify a Boolean argument without a Boolean value to specify a `true` value. For example, you can now specify `--provision` instead of `--provision true` to install with automatic resource provisioning.   Fixes an issue where the core device didn't report its status to the AWS IoT Greengrass cloud service after provisioning in certain scenarios.   Additional minor fixes and improvements.     |
| 2.5.4 |  <a name="changelog-nucleus-2.5.4"></a>**Bug fixes and improvements**<br />   General bug fixes and improvements.     |
| 2.5.3 |  <a name="changelog-nucleus-2.5.3"></a>**New features**<br />   Adds support for hardware security integration. You can use a hardware security module (HSM) to securely store the device's private key and certificate. For more information, see [Hardware security integration](hardware-security.md).   <br />**Bug fixes and improvements**<br />   Fixes an issue with runtime exceptions while the nucleus establishes MQTT connections with AWS IoT Core.     |
| 2.5.2 |  <a name="changelog-nucleus-2.5.2"></a>**Bug fixes and improvements**<br />   Fixes an issue where after the Greengrass nucleus updates, the Windows service fails to start again after you stop it or reboot the device.     |
| 2.5.1 |   This version is no longer available. The improvements in this version are available in later versions of this component.  <a name="changelog-nucleus-2.5.1"></a>**Bug fixes and improvements**<br />   Adds support for 32-bit versions of the Java Runtime Environment (JRE) on Windows.   Changes thing group removal behavior for core devices whose AWS IoT policy doesn't grant the `greengrass:ListThingGroupsForCoreDevice` permission. With this version, the deployment continues, logs a warning, and doesn't remove components when you remove the core device from a thing group. For more information, see [Deploy AWS IoT Greengrass components to devices](manage-deployments.md).   Fixes an issue with system environment variables that the Greengrass nucleus makes available to Greengrass component processes. You can now restart a component for it to use the latest system environment variables.     |
| 2.5.0 |  <a name="changelog-nucleus-2.5.0"></a>**New features**<br />   Adds support for core devices that run Windows.   Change the behavior of thing group removal. With this version, you can remove a core device from a thing group to uninstall that thing group's components in the next deployment. <br /><a name="greengrass-nucleus-v2.5.0-thing-group-removal-permission-requirement"></a>As a result of this change, a core device's AWS IoT policy must have the `greengrass:ListThingGroupsForCoreDevice` permission. If you used the [AWS IoT Greengrass Core software installer to provision resources](quick-installation.md), the default AWS IoT policy allows `greengrass:*`, which includes this permission. For more information, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).   Adds support for HTTPS proxy configurations. For more information, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy).   Adds the new `windowsUser` configuration parameter. You can use this parameter to specify the default user to use to run components on a Windows core device. For more information, see [Configure the user that runs components](configure-greengrass-core-v2.md#configure-component-user).   Adds the new `httpClient` configuration options that you can use to customize HTTP request timeouts to improve performance on slow networks. For more information, see the [httpClient](#greengrass-nucleus-component-configuration-http-client) configuration parameter.   <br />**Bug fixes and improvements**<br />   Fixes the bootstrap lifecycle option to restart the core device from a component.   Adds support for hyphens in recipe variables.   Fixes IPC authorization for on-demand Lambda function components.   Improves log messages and changes non-critical logs from `INFO` to `DEBUG` level, so logs are more useful.   Removes the `iot:DescribeCertificate` permission from the default [token exchange role](device-service-role.md) that the Greengrass nucleus creates when you [install the AWS IoT Greengrass Core software with automatic provisioning](quick-installation.md). This permission isn't used by the Greengrass nucleus.   Fixes an issue so that the automatic provisioning script doesn't require the `iam:GetPolicy` permission if `iam:CreatePolicy` is available for the same policy.   Additional minor fixes and improvements.     |
| 2.4.0 |  <a name="changelog-nucleus-2.4.0"></a>**New features**<br />   Adds support for system resource limits. You can configure the maximum amount of CPU and RAM usage that each component's processes can use on the core device. For more information, see [Configure system resource limits for components](configure-greengrass-core-v2.md#configure-component-system-resource-limits).   Adds IPC operations to pause and resume components. For more information, see [PauseComponent](ipc-component-lifecycle.md#ipc-operation-pausecomponent) and [ResumeComponent](ipc-component-lifecycle.md#ipc-operation-resumecomponent).   Adds support for provisioning plugins. You can specify a JAR file to run during installation to provision required AWS resources for a Greengrass core device. The Greengrass nucleus includes an interface that you can implement to develop custom provisioning plugins. For more information, see [Install AWS IoT Greengrass Core software with custom resource provisioning](custom-provisioning.md).   Adds the optional `thing-name-policy` argument to the AWS IoT Greengrass Core software installer. You can use this option to specify an existing or custom AWS IoT policy when you [install the AWS IoT Greengrass Core software with automatic resource provisioning](quick-installation.md).   <br />**Bug fixes and improvements**<br />   Updates logging configuration on startup. This fixes an issue where the logging configuration wasn't applied on startup.   Updates the nucleus loader symlink to point to the component store in the Greengrass root folder during installation. This update enables you to delete the JAR file and other nucleus artifacts that you download when you install the AWS IoT Greengrass Core software.   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.     |
| 2.3.0 |  <a name="changelog-nucleus-2.3.0"></a>**New features**<br />   Adds support for deployment configuration documents up to 10 MB, up from 7 KB (for deployments that target things) or 31 KB (for deployments that target thing groups). <br /><a name="greengrass-nucleus-v2.3.0-large-configuration-support-permission"></a>To use this feature, a core device's AWS IoT policy must allow the `greengrass:GetDeploymentConfiguration` permission. If you used the [AWS IoT Greengrass Core software installer to provision resources](quick-installation.md), your core device's AWS IoT policy allows `greengrass:*`, which includes this permission. For more information, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).     Adds the `iot:thingName` recipe variable. You can use this recipe variable to get the name of the core device's AWS IoT thing in a recipe. For more information, see [Recipe variables](component-recipe-reference.md#recipe-variables).   <br />**Bug fixes and improvements**<br />   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.     |
| 2.2.0 |  <a name="changelog-nucleus-2.2.0"></a>**New features**<br />   Adds IPC operations for local shadow management.   <br />**Bug fixes and improvements**<br />   Reduces the size of the JAR file.   Reduces memory usage.   Fixes issues where the log configuration wasn't updated in certain cases.   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.     |
| 2.1.0 |  <a name="changelog-nucleus-2.1.0"></a>**New features**<br />   Supports downloading Docker images from private repositories in Amazon ECR.    Adds the following parameters to customize the MQTT configuration on core devices:   `maxInFlightPublishes` – The maximum number of unacknowledged MQTT QoS 1 messages that can be in flight at the same time.   `maxPublishRetry` – The maximum number of times to retry a message that fails to publish.     Adds the `fleetstatusservice` configuration parameter to configure the interval at which the core device publishes device status to the AWS Cloud.   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.   <br />**Bug fixes and improvements**<br />   Fixes an issue that caused shadow deployments to be duplicated when the nucleus restarts.   Fixes an issue that caused the nucleus to crash when it encountered a service load exception.   Improves component dependency resolution to fail a deployment that includes a circular dependency.   Fixes an issue that prevented a plugin component from being redeployed if that component had been previously removed from the core device.   Fix an issue that caused the `HOME` environment variable to be set to the `{{/greengrass/v2}}/work` directory for Lambda components or for components that run as root. The `HOME` variable is now correctly set to the home directory for the user that runs the component.    Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.     |
| 2.0.5 |  <a name="changelog-nucleus-2.0.5"></a>**Bug fixes and improvements**<br />   Correctly routes traffic through a configured network proxy when downloading AWS-provided components.   Use the correct Greengrass data plane endpoint in AWS China Regions.     |
| 2.0.4 |  <a name="changelog-nucleus-2.0.4"></a>**New features**<br />   Enables HTTPS traffic over port 443. You can use the new `greengrassDataPlanePort` configuration parameter for version 2.0.4 of the nucleus component to configure HTTPS communication to travel over port 443 instead of the default port 8443. For more information, see [Configure HTTPS over port 443](configure-greengrass-core-v2.md#configure-https-port-443).   Adds the work path recipe variable. You can use this recipe variable to get the path to components' work folders, which you can use to share files between components and their dependencies. For more information, see the [work path recipe variable](component-recipe-reference.md#component-recipe-work-path).   <br />**Bug fixes and improvements**<br />   Prevents the creation of the token exchange AWS Identity and Access Management (IAM) role policy if a role policy already exists. <br />As a result of this change, the installer now requires the `iam:GetPolicy` and `sts:GetCallerIdentity` when run with `--provision true`. For more information, see [Minimal IAM policy for installer to provision resources](provision-minimal-iam-policy.md).   Correctly handles the cancellation of a deployment that has not yet been registered successfully.   Updates the configuration to remove older entries with newer timestamps when rolling back a deployment.   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.     |
| 2.0.3 | Initial version. |
