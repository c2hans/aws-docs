---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-publisher-component.html
---

# IoT SiteWise publisher
<a name="iotsitewise-publisher-component"></a>

The IoT SiteWise publisher component (`aws.iot.SiteWiseEdgePublisher`) enables AWS IoT SiteWise gateways to export data from the edge to the AWS Cloud.

For more information about AWS IoT SiteWise gateways, see [Using AWS IoT SiteWise at the edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html) in the *AWS IoT SiteWise User Guide*.

**Topics**
+ [Versions](#iotsitewise-publisher-component-versions)
+ [Type](#iotsitewise-publisher-component-type)
+ [Operating system](#iotsitewise-publisher-component-os-support)
+ [Requirements](#iotsitewise-publisher-component-requirements)
+ [Dependencies](#iotsitewise-publisher-component-dependencies)
+ [Configuration](#iotsitewise-publisher-component-configuration)
+ [Input data](#iotsitewise-publisher-component-input-data)
+ [Local log file](#iotsitewise-publisher-component-log-file)
+ [Troubleshooting and debugging](#iotsitewise-publisher-component-debug)
+ [Licenses](#iotsitewise-publisher-component-licenses)
+ [Changelog](#iotsitewise-publisher-component-changelog)
+ [See also](#iotsitewise-publisher-component-see-also)

## Versions
<a name="iotsitewise-publisher-component-versions"></a>

This component has the following versions:
+ 4.1.x
+ 4.0.x
+ 3.2.x
+ 3.1.x
+ 3.0.x
+ 2.4.x
+ 2.3.x
+ 2.2.x
+ 2.1.x
+ 2.0.x

## Type
<a name="iotsitewise-publisher-component-type"></a>

<a name="public-component-type-generic"></a>This <a name="public-component-type-generic-phrase"></a>component is a generic component (`aws.greengrass.generic`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs the component's lifecycle scripts.

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="iotsitewise-publisher-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Requirements
<a name="iotsitewise-publisher-component-requirements"></a>

This component has the following requirements:
+ The Greengrass core device must run on one of the following platforms:
  + os: Ubuntu 18.04 or later

    architecture: x86\_64 (AMD64) or ARMv8 (Aarch64)
  + os: Red Hat Enterprise Linux (RHEL) 8

    architecture: x86\_64 (AMD64) or ARMv8 (Aarch64)
  + os: Amazon Linux 2

    architecture: x86\_64 (AMD64) or ARMv8 (Aarch64)
  + os: Debian 11

    architecture: x86\_64 (AMD64) or ARMv8 (Aarch64)
  + os: Windows Server 2019 or later

    architecture: x86\_64 (AMD64)
+ The Greengrass core device must connect to the Internet.
+ The Greengrass core device must be authorized to perform the `iotsitewise:BatchPutAssetPropertyValue` action. For more information, see [Authorize core devices to interact with AWS services](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html).
**Example permissions policy**

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "iotsitewise:BatchPutAssetPropertyValue",
              "Resource": "*"
          }
      ]
  }
  ```

------

### Endpoints and ports
<a name="iotsitewise-publisher-component-endpoints"></a>

This component must be able to perform outbound requests to the following endpoints and ports, in addition to endpoints and ports required for basic operation. For more information, see [Allow device traffic through a proxy or firewall](allow-device-traffic.md).

| Endpoint | Port | Required | Description |
| --- | --- | --- | --- |
| `data.iotsitewise.{{region}}.amazonaws.com` | 443 | Yes | Publish data to AWS IoT SiteWise. |

## Dependencies
<a name="iotsitewise-publisher-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#iotsitewise-publisher-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass). On the component details page, look for the **Dependencies** list.

The following table lists the dependencies for versions 2.0.x to 2.2.x of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.3.0<3.0.0 | Hard |
| [Stream manager](stream-manager-component.md) | >=2.0.10<3.0.0 | Hard |

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="iotsitewise-publisher-component-configuration"></a>

This component doesn't have any configuration parameters.

You can use the AWS IoT SiteWise console or API to configure the IoT SiteWise publisher component. For more information, see [Step 3: Configure publisher - optional](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-gateway-ggv2.html#configure-publisher) in the *AWS IoT SiteWise User Guide*.

## Input data
<a name="iotsitewise-publisher-component-input-data"></a>

This component reads `PutAssetPropertyValueEntry` messages from AWS IoT Greengrass stream manager. For more information, see [PutAssetPropertyValueEntry](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutAssetPropertyValueEntry.html) in the *AWS IoT SiteWise API Reference*.

## Local log file
<a name="iotsitewise-publisher-component-log-file"></a>

This component uses the following log file.

------
#### [ Linux ]

```
{{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgePublisher.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgePublisher.log
```

------

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

  ```
  sudo tail -f {{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgePublisher.log
  ```

------
#### [ Windows (PowerShell) ]

  ```
  Get-Content {{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgePublisher.log -Tail 10 -Wait
  ```

------

## Troubleshooting and debugging
<a name="iotsitewise-publisher-component-debug"></a>

This component includes a new events log to help customers identify and fix problems. The log file is separate from the local log file, and is found in the following location. Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

```
{{/greengrass/v2}}/work/aws.iot.SiteWiseEdgePublisher/logs/IotSiteWisePublisherEvents.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\work\aws.iot.SiteWiseEdgePublisher\logs\IotSiteWisePublisherEvents.log
```

------

This log includes detailed information and troubleshooting instructions. Troubleshooting information is provided alongside the diagnostics, with a description of how to remedy the issue, and sometimes with links to further information. Diagnostic information includes the following:
+ Severity level
+ Timestamp
+ Additional event-specific information

**Example log**

```
accountBeingThrottled:
  Summary: Data upload speed slowed due to quota limits
  Level: WARN
  Timestamp: '2023-06-09T21:30:24.654Z'
  Description: The IoT SiteWise Publisher is limited to the "Rate of data points ingested"
    quota for a customers account. See the associated documentation and associated
    metric for the number of requests that were limited for more information. Note
    that this may be temporary and not require any change, although if the issue continues
    you may need to request an increase for the mentioned quota.
  FurtherInformation:
  - https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html
  - https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshooting-gateway.html#gateway-issue-data-streams
  AssociatedMetrics:
  - Name: TotalErrorCount
    Description: The total number of errors of this type that occurred.
    Value: 327724.0
  AssociatedData:
  - Name: AggregatePropertyAliases
    Description: The aggregated property aliases of the throttled data.
    FileLocation: /greengrass/v2/work/aws.iot.SiteWiseEdgePublisher/./logs/data/AggregatePropertyAliases_1686346224654.log
```

## Licenses
<a name="iotsitewise-publisher-component-licenses"></a>

<a name="component-core-software-license"></a>This component is released under the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

## Changelog
<a name="iotsitewise-publisher-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 4.1.4 |  **Bug fixes and improvements**<br />   IoT SiteWise publisher now reports system health metrics, such as memory and CPU usage of the IoT SiteWise publisher, to CloudWatch.   Updated error reporting to AWS IoT Greengrass so that IoT SiteWise publisher is restarted if the startup workflow has partial failure.     |
| 4.1.3 |  **Bug fixes and improvements**<br />   Fixes a memory leak in the data checkpointing process.  Fixes security vulnerabilities.     |
| 4.1.2 |  **Bug fixes and improvements**<br />   Fixes an issue involved with syncing large configurations.  Delays in subscription to AWS IoT Core no longer affect the start up process.  Delays in initializing checkpoints no longer affect the start up process.    |
| 4.1.1 |  **Bug fixes and improvements**<br />   Fixes an issue that causes high CPU and memory usage on Classic streams, V2 gateways when sending data through an AWS IoT SiteWise buffered using Amazon S3 destination after restarting the publisher.   Adds support for overriding default component logging behavior by creating an optional file located at: `/greengrass/v2/work/aws.iot.SiteWiseEdgePublisher/log4j2.xml`.     |
| 4.1.0 |  **New features**<br />   Adds a command-line tool to manage built-in EMQX MQTT broker users. This interface enables user account management and configures access control policies for MQTT topic publishing and subscription permissions.    **Bug fixes and improvements**<br />   Fixes the calculation that determines how many unique aliases can fit into a single Buffered ingestion Parquet file.     |
| 4.0.3 |  **Bug fixes and improvements**<br />   Updates the maximum of unique aliases per AWS IoT SiteWise buffered ingestion file to match the cloud limit of 10,000.   Fixes an AWS IoT Greengrass logging issue that incorrectly reports invalid service states.   Adds validation to prevent duplicate stream names across Amazon S3 destination configurations in Classic streams, V2 gateways.    Fixes a compatibility issue with AWS IoT SiteWise buffered ingestion in non-standard AWS partitions.   Fixes an issue that causes duplicate data ingestion.     |
| 4.0.2 |  **Bug fixes and improvements**<br />   Fixes an issue that prevents data upload after the batch wait time expires.   Adds validation to verify that each destination in MQTT-enabled, V3 gateway configurations are unique.     |
| 4.0.1 |  **Bug fixes and improvements**<br />   Fixes an issue that prevents data upload to AWS IoT SiteWise when you disable the maximum batch wait time configuration.   Fixes an issue where the `IoTSiteWisePublisher.NumberOfSubscriptionsToMqttBroker` metric inaccurately reports the count of unique topics subscribed to the MQTT broker.     |
| 4.0.0 |  **New features**<br /> Adds support for MQTT-enabled, V3 gateways in addition to Classic streams, V2 gateways (formerly known as self-hosted SiteWise Edge gateways).   Adds the ability to subscribe to and receive data from the AWS IoT Greengrass MQTT 5 broker (EMQX). For more information, see [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/mqtt-enabled-v3-gateway.html).   Adds configuration options for data destinations using path filters. For more information, see [Understand path filters for AWS IoT SiteWise Edge destinations](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/destinations-path-filters.html).   <br />**Bug fixes and improvements**<br />   Fixes an issue where the `PublishSuccessCount` metric reports negative values.   Fixes an issue where the publisher doesn't start up within 100 seconds and enters the `BROKEN` state.   Fixes security vulnerabilities.     |
| 3.2.0 |  **New features**<br />   Added support for ingestion of Null and NaN values if ingestion is enabled in AWS IoT SiteWise. To view or modify the Null and NaN configuration in AWS IoT SiteWise, see the [DescribeStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeStorageConfiguration.html) and [PutStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html) APIs.   <br />**Bug fixes and improvements**<br />   Fixes issues causing corrupted checkpoint database files.   Fixes issues generating duplicated metrics.     |
| 3.1.4 |   Version 3.1.4 was discontinued on February 20, 2025. The improvements in this version are available in later versions of this component.  **Bug fixes and improvements**<br />   Fixes issues that could cause longer-than-expected startup times after being offline.     |
| 3.1.3 |  **Bug fixes and improvements**<br />   Fixes an issue where the events log file located at `/greengrass/v2/work/aws.iot.SiteWiseEdgePublisher/logs/IoTSiteWisePublisherEvents.log` was created but no events were being logged.   Adds the following CloudWatch metrics for monitoring the connection with the MQTT broker:   `IoTSiteWisePublisher.IsConnectedToMqttBroker`   `IoTSiteWisePublisher.NumberOfSubscriptionsToMqttBroker`   `IoTSiteWisePublisher.NumberOfUniqueMqttTopicsReceived`   `IoTSiteWisePublisher.MqttMessageReceivedSuccessCount`   `IoTSiteWisePublisher.MqttReceivedSuccessBytes`   <br />For more information about these metrics, see [AWS IoT Greengrass Version 2 gateway metrics](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-metrics-ggv2.html).   Fixes an issue where the `BatchCreateJob` API is still called even if uploading a parquet file to S3 fails.     |
| 3.1.2 |  **Bug fixes and improvements**<br />   Fixes the issue of high CPU usage introduced in version 3.1.1.     |
| 3.1.1 |   Version 3.1.1 was discontinued on March 12, 2024. The improvements in this version are available in later versions of this component.  **Bug fixes and improvements**<br />   Adds additional logging that identifies the affected data aliases when an error occurs.   Adds local enforcement of AWS IoT SiteWise API limits on the age of the data ingested.   Fixes the issue where Publisher mixes up the checkpoints of the StreamManager streams when there are multiple Amazon S3 destinations.   Fixes performance bottleneck with how the publisher reads from the StreamManager streams.     |
| 3.1.0 |  **New features**<br />   Adds support to publish data as parquet files to Amazon S3.   Adds support for AWS IoT SiteWise buffered ingestion.     |
| 3.0.0 |  **Bug fixes and improvements**<br />   Fixes issues related to proxy support.   <br />**New features**<br />   Enables support of data ingestion from an MQTT broker.     |
| 2.4.1 |  **Bug fixes and improvements**<br />   Enable component to work with Java Corretto 11 versions 11.0.20.8.1 and later. Component versions 2.4.0 and 2.3.3 show the `"Could not find or load main class"` error message when used with Java Corretto version 11.0.20.8.1.     |
| 2.4.0 |  **New features**<br />   Adds a new events log to make it easier to identify and remediate problems.   <br />**Bug fixes and improvements**<br />   Improves Publisher checkpoint recovery.     |
| 2.3.3 |  **Bug fixes and improvements**<br />   Improves ability to support high throughput.     |
| 2.3.2 |  **Bug fixes and improvements**<br />   Fixes HTTP proxy support when downloading Publisher configuration.     |
| 2.3.1 |  **New features**<br />   Adds support for installing Data Collection Pack on Linux ARMv8 architecture.   Minimum requirements for Linux ARMv8:   Memory: 4 GB   CPU: ARM Cortex-A72 or equivalent specification       |
| 2.2.3 |  **Bug fixes and improvements**<br />   Removes retry for generic exception which was not in the retriable exception list.     |
| 2.2.2 |  **Bug fixes and improvements**<br />   Reintroduces data upload support to AWS IoT SiteWise through an HTTP proxy server.     |
| 2.2.1 |   This version doesn't support HTTP proxy configuration. Version 2.2.2 and higher reintroduces support for this feature.  **New features**<br />   Adds support to this component to toggle compression when uploading data to AWS IoT SiteWise.     |
| 2.2.0 |   This version doesn't support HTTP proxy configuration. Version 2.2.2 and higher reintroduces support for this feature.  **New features**<br />   Updates this component to compress data before sending it to the AWS IoT SiteWise service.   In most cases, this change reduces bandwidth usage by 75 percent compared to previous versions of this component.   In most cases, this change increases CPU usage by up to 5 percent. On gateways that process large amounts of data, this change can increase CPU usage by up to 15 percent.   This change doesn't affect AWS IoT SiteWise service charges or service quota usage.   Adds support for Windows Server 2019 or higher.     <br />**Bug fixes and improvements**<br />   Fixes an issue that prevents this component from starting when the checkpoint file is corrupted.     |
| 2.1.4 |  **Bug fixes and improvements**<br />   Fixes compatibility with Java version 8.     |
| 2.1.3 |   This version is no longer available, except in the US East (Ohio), Canada (Central), and AWS GovCloud (US-East) Regions. This component version requires Java version 11 or greater to run. The improvements in this version are available in later versions of this component.  **Bug fixes and improvements**<br />   Improves error messages when you deploy this component on unsupported devices.   Updates to log errors when data uploads fail.     |
| 2.1.2 |  **Bug fixes and improvements**<br />   Updates to invoke the expired data export feature as soon as data expires.     |
| 2.1.1 | Bug fixes and improvements. |
| 2.1.0 |  **New features**<br />   Adds support for publishing the newest data to the cloud first.   Adds support for not publishing expired data to the cloud.   Adds support for storing expired data locally.   <br />**Bug fixes and improvements**<br />   Reduces disk I/O and corresponding latency.     |
| 2.0.2 | Bug fixes and improvements. |
| 2.0.1 | Initial version. |

## See also
<a name="iotsitewise-publisher-component-see-also"></a>
+ [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) in the *AWS IoT SiteWise User Guide*.
