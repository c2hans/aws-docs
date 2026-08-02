---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html
---

# Greengrass nucleus lite
<a name="greengrass-nucleus-lite-component"></a>

The Greengrass nucleus lite (`aws.greengrass.NucleusLite`) is a device runtime for constrained edge devices optimized for minimal memory footprint (uses less than 15MB RAM). It has been introduced with AWS IoT Greengrass version 2.14.0 release and is backward compatible with AWS IoT Greengrass generic components, Greengrass V2 API, and SDK.

The Greengrass nucleus lite is offered as an alternative to the common [Greengrass nucleus (`aws.greengrass.Nucleus`)](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html) and can be used in heterogeneous fleets of Greengrass devices.

**Topics**
+ [Versions](#greengrass-nucleus-lite-component-versions)
+ [Operating system](#greengrass-nucleus-lite-component-os-support)
+ [Requirements](#greengrass-nucleus-lite-component-requirements)
+ [Compatibility](#greengrass-nucleus-lite-component-compatibility)
+ [Download and installation](#greengrass-nucleus-lite-component-install)
+ [Configuration](#greengrass-nucleus-lite-component-configuration)
+ [Local log file](#greengrass-nucleus-lite-component-log-file)
+ [Changelog](#greengrass-nucleus-lite-component-changelog)

## Versions
<a name="greengrass-nucleus-lite-component-versions"></a>

This component has the following versions:
+ 2.5.x
+ 2.4.x
+ 2.3.x
+ 2.2.x
+ 2.1.x
+ 2.0.x

## Operating system
<a name="greengrass-nucleus-lite-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux (distributions with systemd)

For more information, see [Greengrass nucleus](https://docs.aws.amazon.com/greengrass/v2/developerguide/operating-system-feature-support-matrix.html).

## Requirements
<a name="greengrass-nucleus-lite-component-requirements"></a>

Devices must meet certain requirements to install and run the AWS IoT Greengrass nucleus lite and the AWS IoT Greengrass Core software. For more information, see [Setup guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/main/docs/SETUP.md#setting-up-greengrass-nucleus-lite).
+ 15MB of RAM space for the nucleus runtime.
+ 5MB of storage (disk/FLASH).

Additional system dependencies are documented in the [Setup Guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/main/docs/SETUP.md#dependencies).

The Greengrass nucleus component is supported to run in a VPC. To deploy this component in a VPC, the following is required:
+ The Greengrass nucleus must have connectivity to AWS IoT data, AWS IoT Credentials, and Amazon S3.

To run AWS IoT Greengrass nucleus lite as a non-root user, you can use a rootless container. For more information, see [Using Podman](https://github.com/aws-greengrass/aws-greengrass-lite/blob/main/docs/BUILD.md#optional-using-podman) in the AWS IoT Greengrass nucleus lite GitHub repository.

## Compatibility
<a name="greengrass-nucleus-lite-component-compatibility"></a>

The AWS IoT Greengrass nucleus lite is compatible with the AWS IoT Greengrass v2 API (subset of) and supported SDKs. It does not depend on any specific language runtimes/VMs but components added to a deployment can require the presence of specific runtimes (e.g.: Java JVM, Python). For more information about what features are supported with Greengrass nucleus lite, see [Greengrass feature compatibility](operating-system-feature-support-matrix.md).

## Download and installation
<a name="greengrass-nucleus-lite-component-install"></a>

You can download an apt package, [build from source](https://github.com/aws-greengrass/aws-greengrass-lite/blob/main/README.md#getting-started), [use a Yocto layer](https://github.com/aws4embeddedlinux/meta-aws), or [download a pre-built Yocto image](https://github.com/aws4embeddedlinux/meta-aws-demos) for compatible device (e.g., RaspberryPi). From the [AWS IoT Core Console](https://console.aws.amazon.com/iot/home) you will be able to download a **connection kit** containing all the credentials and initial configuration for your device. Instructions on how to install are included in each specific distribution method.

You can also follow a tutorial to install the AWS IoT Greengrass nucleus lite and explore Greengrass component development. For more information, see [Tutorial: Getting started with AWS IoT Greengrass V2](getting-started.md).

## Configuration
<a name="greengrass-nucleus-lite-component-configuration"></a>

The nucleus provides the following [configuration](https://github.com/aws-greengrass/aws-greengrass-lite/blob/main/docs/SETUP.md#configuring-greengrass) parameters. Some parameters require that the AWS IoT Greengrass Core software restarts to take effect.

`iotRoleAlias`
The AWS IoT role alias that points to a token exchange IAM role. The AWS IoT credentials provider assumes this role to allow the Greengrass core device to interact with AWS services. For more information, see [Authorize core devices to interact with AWS services.](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html)

`iotDataEndpoint`
<a name="nucleus-component-configuration-iot-data-endpoint"></a>The AWS IoT data endpoint for your AWS account.

`iotCredEndpoint`
<a name="nucleus-component-configuration-iot-cred-endpoint"></a>The AWS IoT credentials endpoint for your AWS account.

`greengrassDataPlanePort`
The port to use for data plane connections. For more information, see [Connect on port 443 or through a network proxy](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-alpn-network-proxy).
You must specify a port where the device can make outbound connections. If you specify a port that is blocked, the device won't be able to connect to AWS IoT Greengrass to receive deployments. Choose from the following options:
+ `443`
+ `8443`
+ Default: `8443`

`awsRegion`
The AWS Region to use.

`runWithDefault`
The system user to use to run components.
<a name="nucleus-component-parameter-restart-para"></a>When you deploy a change to this configuration parameter, the AWS IoT Greengrass Core software restarts for the change to take effect.
This object contains the following information:
`posixUser`
The name or ID of the system user and, optionally, system group that the core device uses to run generic components. Specify the user and group separated by a colon (`:`) in the following format: `user:group`. The group is optional. If you don't specify a group, the AWS IoT Greengrass Core software uses the primary group for the user. For example, you can specify `ggc_user` or `ggc_user:ggc_group`. For more information, see [Configure the user that runs components](configure-greengrass-core-v2.md#configure-component-user).

`networkProxy`
(Optional) The network proxy to use for all connections. For more information, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy).
When you deploy a change to this configuration parameter, the change will take effect after the next restart of the AWS IoT Greengrass Core software.
This object contains the following information:
`noProxyAddresses`
(Optional) A comma-separated list of IP addresses or hostnames that are exempt from the proxy.
`proxy`
The proxy to which to connect. This object contains the following information:
`url`
The URL of the proxy server in the format `http://host:port`.
+ `scheme` – The scheme, which must be `http`.
+ `host` – The host name or IP address of the proxy server.
+ `port` – (Optional) The port number. If you don't specify the port, then the Greengrass core device uses the following default value:
  + `http` – 80

## Local log file
<a name="greengrass-nucleus-lite-component-log-file"></a>

Messages are logged to stdout and log files are handled by systemd.

**To view this component's logs**
+ Use `journalctl` to view logs.

## Changelog
<a name="greengrass-nucleus-lite-component-changelog"></a>

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.5.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.5.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.4.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.3.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.3.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.3.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.3.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.2.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.2.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.2.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.1.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.0.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.0.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)  |
| 2.0.0 | Initial version. |
