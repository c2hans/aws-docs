---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/iotsitewise-processor-component.html
---

# IoT SiteWise processor
<a name="iotsitewise-processor-component"></a>

The IoT SiteWise processor component (`aws.iot.SiteWiseEdgeProcessor`) enables AWS IoT SiteWise Classic streams, V2 gateways to process data at the edge.

With this component, AWS IoT SiteWise gateways can use asset models and assets to process data on gateway devices. For more information about AWS IoT SiteWise gateways, see [Using AWS IoT SiteWise at the edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html) in the *AWS IoT SiteWise User Guide*.

**Note**
The data processing pack (DPP) feature will no longer be open to new customers starting November 7, 2025. If you would like to use DPP, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Data processing pack availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-dpp-availability-change.html) in the *AWS IoT SiteWise User Guide*.

**Topics**
+ [Versions](#iotsitewise-processor-component-versions)
+ [Type](#iotsitewise-processor-component-type)
+ [Operating system](#iotsitewise-processor-component-os-support)
+ [Requirements](#iotsitewise-processor-component-requirements)
+ [Dependencies](#iotsitewise-processor-component-dependencies)
+ [Configuration](#iotsitewise-processor-component-configuration)
+ [Local log file](#iotsitewise-processor-component-log-file)
+ [Licenses](#iotsitewise-processor-component-licenses)
+ [Changelog](#iotsitewise-processor-component-changelog)
+ [See also](#iotsitewise-processor-component-see-also)

## Versions
<a name="iotsitewise-processor-component-versions"></a>

This component has the following versions:
+ 3.5.x
+ 3.4.x
+ 3.3.x
+ 3.2.x
+ 3.1.x
+ 3.0.x
+ 2.2.x
+ 2.1.x
+ 2.0.x

## Type
<a name="iotsitewise-processor-component-type"></a>

<a name="public-component-type-generic"></a>This <a name="public-component-type-generic-phrase"></a>component is a generic component (`aws.greengrass.generic`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs the component's lifecycle scripts.

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="iotsitewise-processor-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Requirements
<a name="iotsitewise-processor-component-requirements"></a>

This component has the following requirements:
+ The Greengrass core device must run on one of the following platforms:
  + os: Ubuntu 20.04 or later

    architecture: x86\_64 (AMD64)
  + os: Red Hat Enterprise Linux (RHEL) 8

    architecture: x86\_64 (AMD64)
  + os: Amazon Linux 2

    architecture: x86\_64 (AMD64)
  + os: Windows Server 2019 or later

    architecture: x86\_64 (AMD64)
  + os: Debian 11 (Bullseye) or later

    architecture: x86\_64 (AMD64)
+ The Greengrass core device must allow inbound traffic on port 443.
+ The Greengrass core device must allow outbound traffic on port 443 and 8883.
+ The following ports are reserved for use by AWS IoT SiteWise: 80, 443, 3001, 4569, 4572, 8000, 8081, 8082, 8084, 8085, 8086, 8445, 9000, 9500, 11080, and 50010. Using a reserved port for traffic can result in a terminated connection.
**Note**
Port 8087 is required only for version 2.0.15 and later of this component.
+ The [Greengrass device role](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html) must have permissions that allow you to use AWS IoT SiteWise gateways on your AWS IoT Greengrass V2 devices. For more information, see [Requirements](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-gateway-ggv2.html#gateway-requirements) in the *AWS IoT SiteWise User Guide*.

### Endpoints and ports
<a name="iotsitewise-processor-component-endpoints"></a>

This component must be able to perform outbound requests to the following endpoints and ports, in addition to endpoints and ports required for basic operation. For more information, see [Allow device traffic through a proxy or firewall](allow-device-traffic.md).

| Endpoint | Port | Required | Description |
| --- | --- | --- | --- |
| `model.iotsitewise.{{region}}.amazonaws.com` | 443 | Yes | Get information about your AWS IoT SiteWise assets and asset models. |
| `edge.iotsitewise.{{region}}.amazonaws.com` | 443 | Yes | Get information about the core device's AWS IoT SiteWise gateway configuration. |
| `ecr.{{region}}.amazonaws.com` | 443 | Yes | Download AWS IoT SiteWise Edge gateway Docker images from Amazon Elastic Container Registry. |
| `iot.{{region}}.amazonaws.com` | 443 | Yes | Get device endpoints for your AWS account. |
| `sts.{{region}}.amazonaws.com` | 443 | Yes | Get the ID of your AWS account. |
| `monitor.iotsitewise.{{region}}.amazonaws.com` | 443 | No | Required if you access AWS IoT SiteWise Monitor portals on the core device. |

## Dependencies
<a name="iotsitewise-processor-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#iotsitewise-processor-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass). On the component details page, look for the **Dependencies** list.

The following table lists the dependencies for versions 2.0.x to 2.1.x of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Token exchange service](token-exchange-service-component.md) | >=2.0.3 <3.0.0 | Hard |
| [Stream manager](stream-manager-component.md) | >=2.0.10 <3.0.0 | Hard |
| [Greengrass CLI](greengrass-cli-component.md) | >=2.3.0 <3.0.0 | Hard |

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="iotsitewise-processor-component-configuration"></a>

This component doesn't have any configuration parameters.

## Local log file
<a name="iotsitewise-processor-component-log-file"></a>

This component uses the following log file.

------
#### [ Linux ]

```
{{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgeProcessor.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgeProcessor.log
```

------

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

  ```
  sudo tail -f {{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgeProcessor.log
  ```

------
#### [ Windows (PowerShell) ]

  ```
  Get-Content {{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgeProcessor.log -Tail 10 -Wait
  ```

------

## Licenses
<a name="iotsitewise-processor-component-licenses"></a>

This component includes the following third-party software/licensing:

### Third-party Licenses
<a name="w2ab1c24b8d120c25b5b1b1"></a>
+ Apache-2.0
+ MIT
+ BSD-2-Clause
+ BSD-3-Clause
+ CDDL-1.0
+ CDDL-1.1
+ ISC
+ Zlib
+ GPL-3.0-with-GCC-exception
+ Public Domain
+ Python-2.0
+ Unicode-DFS-2015
+ BSD-1-Clause
+ OpenSSL
+ EPL-1.0
+ EPL-2.0
+ GPL-2.0-with-classpath-exception
+ MPL-2.0
+ CC0-1.0
+ JSON

<a name="component-core-software-license"></a>This component is released under the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

## Changelog
<a name="iotsitewise-processor-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 3.5.1 | **New features**<br /> Added support for ingestion of Null and NaN values if ingestion is enabled in AWS IoT SiteWise. To view or modify the Null and NaN configuration in AWS IoT SiteWise, see the [DescribeStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeStorageConfiguration.html) and [PutStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html) APIs. <br />**Bug fixes and improvements**<br /> Updated dependencies to address potential security vulnerabilities.   |
| 3.4.0 | **New features**<br />   Added optional HTTP and HTTPS proxy support to enable gateway communication through proxy servers that require custom certificates. For more information on setting up an HTTP proxy for the AWS IoT Greengrass core, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy). For more information on proxy support specific to SiteWise Edge, see [Manage trust stores for AWS IoT SiteWise Edge proxy support](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-apis-manage-trust-stores-proxy.html) in the *AWS IoT SiteWise User Guide*.   Added configurable session timeout settings to manage inactivity periods for AWS OpsHub and SiteWise Edge APIs. For more information, see [Configure session timeouts for AWS IoT SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-apis-session-timeout.html) in the *AWS IoT SiteWise User Guide*.   <br />**Performance improvements**<br /> Reduced the time for incoming data to reach edge device storage from 5 seconds to less than 1 second. The latency for data uploads to AWS IoT SiteWise remains unchanged.   |
| 3.3.1 | **New feature**<br />   Added optional CORS support to SiteWise Edge APIs, enhancing cross-origin resource sharing capabilities. This feature improves flexibility for web applications interacting with the APIs.     |
| 3.3.0 | **Performance improvements**<br />   Optimized cache refresh mechanism to reduce I/O usage between AWS IoT SiteWise asset syncs by only refreshing entries for new or updated assets.   Reduced memory footprint for maintaining a cache with a large number of synced asset properties.    **Bug fixes and improvements**<br />   Suppressed logs for ingesting individual property values when there are no ingestion errors, which reduces log noise during high ingestion rates.   Improved log readability by using human-readable formatting for certain log entries.   Added support for Java 17 and higher.    |
| 3.2.1 |  **Bug fixes and improvements**<br />   Fix issue where the AWS IoT SiteWise API calls do not paginate synchronously with SiteWise Edge.   Fix issue to not publish the `MessageRemaining.SiteWise_Edge_Stream` metric anymore.   Added the following CloudWatch metrics to monitor the connection with the MQTT broker.   `IoTSiteWiseProcessor.IsConnectedToMqttBroker`   `IoTSiteWiseProcessor.NumberOfSubscriptionsToMqttBroker`   `IoTSiteWiseProcessor.NumberOfUniqueMqttTopicsReceived`   `IoTSiteWiseProcessor.MqttMessageReceivedSuccessCount`   `IoTSiteWiseProcessor.MqttReceivedSuccessBytes`   <br />For more information about these metrics, see [AWS IoT Greengrass Version 2 gateway metrics](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-metrics-ggv2.html).     |
| 3.2.0 |  **Performance improvements**<br />   Optimize API services to have smaller memory footprint and require less disk space to install   This provides a 2 GB reduction in initial memory usage (now uses 7.5 GB of memory on startup, however 16 GB is still recommended) and 500 MB reduction in download size (now requires a 1.4 GB download) for the entire component.     <br />**New features**<br />   `GetAssetPropertyValueAggregates` API now supports 15 minute aggregation windows on the edge.   Ports 8081 and 8082 no longer need to be available for this component to run correctly.  The local endpoint for AWS IoT SiteWise data plane APIs, such as `get-asset-property-value`, is being changed from `http://localhost:8081` to `http://localhost:11080/data`. The local endpoint for AWS IoT SiteWise control plane APIs, such as `list-asset-models`, is being changed from `http://localhost:11080` to `http://localhost:11080/control`. AWS always recommends that you use the SiteWise Edge gateway HTTPS endpoints. Those endpoints have not changed.    <br />**Bug fixes and improvements**<br />   Syncing from AWS IoT SiteWise will now transition resources into a valid state if the previous sync was interrupted. This will fix issues with some resources being corrupted after a forced restart.   Fixes a rare condition where a resource may be corrupted on the edge if it is modified during sync. Sync will now fail if this condition is detected, and the resource will be retried in the next sync.   Fixes an issue that could have allowed the HTTP endpoint for APIs to be called externally. Only HTTPS can be used to call APIs outside of the local loopback address now.   `ListAssets` API now shows the asset hierarchies for assets stored on the edge.   Fixes an issue where the Data Processing Pack failed to restart, upgrade, or downgrade on Windows.   Fixes a bug in the Data Processing Pack for Windows OS that prevented customers from using credentials to connect with an MQTT Broker.     |
| 3.1.3 |  **Bug fixes and improvements**<br />   Fix issue where the Data Processing Pack incorrectly reported a successful sync when some of the resources actually failed.   Allow multiple assets to have the same name as long as they don’t have the same parent.     |
| 3.1.1 |  **Bug fixes and improvements**<br />   Fix issue where SigV4 request fails due to a timezone mismatch.   Fix issue where transform and metric properties stop calculating when they rely on attributes after restarting.   Enable support of custom Stream Manager Port configuration.   Fix an issue where properties that are synced to the edge might stop getting updated.     |
| 3.1.0 |  **Bug fixes and improvements**<br />   Fix issue where `ListAssetModels` API fails to generate next token.     |
| 3.0.0 |  **New features**<br />   Enables support of data ingestion from an MQTT broker.     |
| 2.2.1 |  **Bug fixes and improvements**<br />   Adjust the sync process in order to make control plane data storage more consistent with how cloud operates. This slightly impacts upgrading.  Control plane data synced on version 2.2.1 or higher won't be compatible with previous versions. To downgrade to previous versions, you'll need to complete a fresh install. This doesn't impact upgrades, data synced on previous versions will work with version 2.2.1.    Additional modifications to the AWS credentials chain to prioritize AWS IoT Greengrass V2 credentials.     |
| 2.1.37 |  **Bug fixes and improvements**<br />   Deprecate dependency-routing-service process and move its functionality into the property-state-service process to reduce resource usage from the processes communicating.   Increase maximum result limit for the `get-asset-property-value-history` API to 20,000 to match the limit used by AWS IoT SiteWise.   Fix an issue where next token wasn't being provided in paginated results for the `get-asset-property-value-history` API when no max result limit was specified.     |
| 2.1.35 |  **Bug fixes and improvements**<br />   Modifies the AWS credentials chain to prioritize AWS IoT Greengrass credentials.   Fixes an issue with account detection when deploying as part of an AWS IoT Thing group.     |
| 2.1.34 |  **Bug fixes and improvements**<br />   Adjusts metric/transform computations to use multi-threading on Linux. Windows continues to run single-threaded computations for compatibility.   Fixes an issue where metric computations would be missing for some computation windows.     |
| 2.1.33 |  **Bug fixes and improvements**<br />   Fixes an issue with error state reporting to the Greengrass console.     |
| 2.1.32 |  **Bug fixes and improvements**<br />   Adds support for customized user names and groups.     |
| 2.1.31 |  **Bug fixes and improvements**<br />   Adds support to compute the time-weighted average and the time-weighted standard deviation for data that is modeled in AWS IoT SiteWise.     |
| 2.1.29 |  **Bug fixes and improvements**<br />   Adds support to filter assets on the edge functionality.     |
| 2.1.28 |  **Bug fixes and improvements**<br />   Optimizes resource synchronization to enable a large number of assets to sync from the AWS Cloud to the edge.     |
| 2.1.24 |  **Bug fixes and improvements**<br />    Fixes an issue that caused the dashboard to disappear when syncing a resource for the second time.      |
| 2.1.23 |  **Bug fixes and improvements**<br />   Added a timeout for the `aws.iot.SiteWiseEdgeProcessor` install process to avoid installation failure if internet connectivity is slow.   Optimized resource sync to improve sync efficiency between the cloud and edge.     |
| 2.1.21 |   Upgrading from 2.0.x to 2.1.x will result in loss of local data.  **New features**<br />   Adds support for Windows Server 2019 or higher.   Removes docker for Linux-based operating systems.     |
| 2.0.16 | This version contains bug fixes and improvements. |
| 2.0.15 |  **Bug fixes and improvements**<br />   Changes the port that this component uses for resource sync API operations from 8085 to 8087. As a result, this component now requires port 8087 to be available. This component still requires port 8085 to be available.   Updates AWS OpsHub authentication to deny unauthorized users during login instead of when a user attempts to call API operations.     |
| 2.0.14 | This version contains bug fixes and improvements. |
| 2.0.13 |  **Bug fixes and improvements**<br />   Fixes an issue so that when this component reports data to Amazon CloudWatch metrics, it now correctly indicates which data is unmodeled.     |
| 2.0.9 |  **Bug fixes and improvements**<br />   Improves reliability to create and update AWS IoT SiteWise resources on the core device.   Adds additional local API operations that you can use to monitor which components are installed on the core device, the version of each component, and the status of each component. You can view this information on the **Settings** tab in the AWS OpsHub for AWS IoT SiteWise application on the core device.   Adds a health status for the Docker containers that this component runs. You can run the `docker ps` command to view the containers' health status.     |
| 2.0.7 |  **Bug fixes and improvements**<br />   Fixes support for viewing AWS IoT SiteWise Monitor portals on the core device.     |
| 2.0.6 |  **Bug fixes and improvements**<br />   Fixes the AWS IoT SiteWise `statetime()`, `earliest()`, and `latest()` functions that this component computes on the core device.     |
| 2.0.5 |  **Bug fixes and improvements**<br />   Adds support for the AWS IoT SiteWise `pretrigger()` function in transforms that this component computes on the core device.   Changes the path where this component stores the Lightweight Directory Access Protocol (LDAP) configuration for authentication.     |
| 2.0.2 | Initial version. |

## See also
<a name="iotsitewise-processor-component-see-also"></a>
+ [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) in the *AWS IoT SiteWise User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
