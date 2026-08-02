---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html
---

# IoT SiteWise OPC UA collector
<a name="iotsitewise-opcua-collector-component"></a>

The IoT SiteWise OPC UA collector component (`aws.iot.SiteWiseEdgeCollectorOpcua`) enables AWS IoT SiteWise gateways to collect data from local OPC UA servers.

With this component, AWS IoT SiteWise gateways can connect to multiple OPC UA servers. For more information about AWS IoT SiteWise gateways, see [Using AWS IoT SiteWise at the edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html) in the *AWS IoT SiteWise User Guide*.

**Topics**
+ [Versions](#iotsitewise-opcua-collector-component-versions)
+ [Type](#iotsitewise-opcua-collector-component-type)
+ [Operating system](#iotsitewise-opcua-collector-component-os-support)
+ [Requirements](#iotsitewise-opcua-collector-component-requirements)
+ [Dependencies](#iotsitewise-opcua-collector-component-dependencies)
+ [Configuration](#iotsitewise-opcua-collector-component-configuration)
+ [Input data](#iotsitewise-opcua-collector-component-input-data)
+ [Output data](#iotsitewise-opcua-collector-component-output-data)
+ [Local log file](#iotsitewise-opcua-collector-component-log-file)
+ [Licenses](#iotsitewise-opcua-collector-component-licenses)
+ [Changelog](#iotsitewise-opcua-collector-component-changelog)
+ [See also](#iotsitewise-opcua-collector-component-see-also)

## Versions
<a name="iotsitewise-opcua-collector-component-versions"></a>

This component has the following versions:
+ 3.1.x
+ 3.0.x
+ 2.6.x
+ 2.5.x
+ 2.4.x
+ 2.3.x
+ 2.2.x
+ 2.1.x
+ 2.0.x

## Type
<a name="iotsitewise-opcua-collector-component-type"></a>

<a name="public-component-type-generic"></a>This <a name="public-component-type-generic-phrase"></a>component is a generic component (`aws.greengrass.generic`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs the component's lifecycle scripts.

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="iotsitewise-opcua-collector-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Requirements
<a name="iotsitewise-opcua-collector-component-requirements"></a>

This component has the following requirements:
+ The Greengrass core device must run on one of the following platforms:
  + os: Ubuntu 20.04 or later

    architecture: x86\_64 (AMD64) or ARMv8 (Aarch64)
  + os: Red Hat Enterprise Linux (RHEL) 8

    architecture: x86\_64 (AMD64) or ARMv8 (Aarch64)
  + os: Amazon Linux 2

    architecture: x86\_64 (AMD64) or ARMv8 (Aarch64)
  + os: Debian 11

    architecture: x86\_64 (AMD64) or ARMv8 (Aarch64)
  + os: Windows Server 2019 or later

    architecture: x86\_64 (AMD64)
+ The Greengrass core device must allow outbound network connectivity to OPC UA servers.

## Dependencies
<a name="iotsitewise-opcua-collector-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#iotsitewise-opcua-collector-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com//greengrass). On the component details page, look for the **Dependencies** list.

The following table lists the dependencies for all versions of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.3.0 <3.0.0 | Hard |
| [Stream manager](stream-manager-component.md) | >2.0.10<3.0.0 | Hard |
| [Secret manager](secret-manager-component.md) | >=2.0.8 <3.0.0 | Hard |

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="iotsitewise-opcua-collector-component-configuration"></a>

This component doesn't have any configuration parameters.

You can use the AWS IoT SiteWise console or API to configure the IoT SiteWise OPC UA collector component. For more information, see [Step 4: Add data sources - optional](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-gateway-ggv2.html#add-data-sources-console) in the *AWS IoT SiteWise User Guide*.

## Input data
<a name="iotsitewise-opcua-collector-component-input-data"></a>

This component only accepts data in the following formats, all others will be ignored and discarded. The table below maps the OPC UA data types to their SiteWise equivalent.

|  **SiteWise data type**  |  **OPC UA data type**  |  **Description**  |
| --- | --- | --- |
| `STRING` | `String`<br />`Guid`<br />`XmlElement` | A string of maximum length 1024 bytes. |
| `INTEGER` | `SByte`<br />`Byte`<br />`Int16`<br />`UInt16`<br />`Int32`<br />`UInt32`\*<br />`Int64`\* | A signed 32-bit integer with a range from `-2,147,483,648 to 2,147,483,647` . |
| `DOUBLE` | `UInt32`\*<br />`Int64`\*<br />`Float`<br />`Double` | A floating point number with range from `–10^100 to 10^100` and `IEEE 754` double precision. |
| `BOOLEAN` | `Boolean` | `true` or `false`. |

\* For OPC UA data types `UInt32` and `Int64`, its SiteWise data type will be `INTEGER` if SiteWise is able to represent its value, otherwise it will be `DOUBLE`.

## Output data
<a name="iotsitewise-opcua-collector-component-output-data"></a>

This component writes `BatchPutAssetPropertyValue` messages to AWS IoT Greengrass stream manager. For more information, see [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html) in the *AWS IoT SiteWise API Reference*.

## Local log file
<a name="iotsitewise-opcua-collector-component-log-file"></a>

This component uses the following log file.

------
#### [ Linux ]

```
{{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgeCollectorOpcua.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgeCollectorOpcua.log
```

------

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

  ```
  sudo tail -f {{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgeCollectorOpcua.log
  ```

------
#### [ Windows (PowerShell) ]

  ```
  Get-Content {{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgeCollectorOpcua.log -Tail 10 -Wait
  ```

------

## Licenses
<a name="iotsitewise-opcua-collector-component-licenses"></a>

<a name="component-core-software-license"></a>This component is released under the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

## Changelog
<a name="iotsitewise-opcua-collector-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 3.1.0 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 3.0.3 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 3.0.2 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 3.0.1 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 3.0.0 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 2.6.0 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 2.5.1 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 2.5.0 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 2.4.2 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html) |
| 2.4.1 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html) |
| 2.4.0 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 2.3.0 | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html) |
| 2.2.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 2.1.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 2.1.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-opcua-collector-component.html)  |
| 2.0.3 | Bug fixes and improvements. |
| 2.0.2 | Bug fixes and improvements to asset priority syncing with edge. |
| 2.0.1 | Initial version. |

## See also
<a name="iotsitewise-opcua-collector-component-see-also"></a>
+ [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) in the *AWS IoT SiteWise User Guide*.
