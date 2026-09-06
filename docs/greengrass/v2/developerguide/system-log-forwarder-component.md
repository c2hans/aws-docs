---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/system-log-forwarder-component.html
---

# System log forwarder
<a name="system-log-forwarder-component"></a>

The System log forwarder (`aws.greengrass.SystemLogForwarder`) uploads active system logs directly to Amazon CloudWatch using the CloudWatch HTTPS API.

**Important**
This component will only forward systemd-journald logs generated during runtime. For more information on systemd-journald logs, see [systemd-journald](https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html) and [journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html#).

**Note**
This component requires specific permissions to create and manage CloudWatch log groups and streams.

**Topics**
+ [Versions](#system-log-forwarder-component-versions)
+ [Type](#system-log-forwarder-component-type)
+ [Operating system](#system-log-forwarder-component-os-support)
+ [Requirements](#system-log-forwarder-component-requirements)
+ [Endpoints and ports](#system-log-forwarder-component-endpoints)
+ [Dependencies](#system-log-forwarder-component-dependencies)
+ [Configuration](#system-log-forwarder-component-configuration)
+ [Changelog](#system-log-forwarder-component-changelog)

## Versions
<a name="system-log-forwarder-component-versions"></a>

This component has the following versions:
+ 2.1.x
+ 2.0.x

## Type
<a name="system-log-forwarder-component-type"></a>

<a name="public-component-type-generic"></a>This <a name="public-component-type-generic-phrase"></a>component is a generic component (`aws.greengrass.generic`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs the component's lifecycle scripts.

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="system-log-forwarder-component-os-support"></a>

This component must be installed on systemd-based Linux systems.

## Requirements
<a name="system-log-forwarder-component-requirements"></a>

This component has the following requirements:

The component requires access to create log and stream groups in CloudWatch as well as permission to perform the PutLogEvents HTTP call. You must, at minimum, add the following policy permissions to your Greengrass device's role alias:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
    {
      "Effect": "Allow",
      "Action": ["logs:CreateLogGroup"],
      "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{greengrass/systemLogs}}:*"
    },
    {
      "Effect": "Allow",
      "Action": ["logs:CreateLogStream", "logs:PutLogEvents"],
      "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{greengrass/systemLogs}}:log-stream:${credentials-iot:ThingName}"
    }
  ]
}
```

------

**Note**
For more information, see the System Log Forwarder [Github](https://github.com/aws-greengrass/aws-greengrass-system-log-forwarder) page.

## Endpoints and ports
<a name="system-log-forwarder-component-endpoints"></a>

This component must be able to perform outbound requests to the following endpoints and ports, in addition to endpoints and ports required for basic operation. For more information, see [Allow device traffic through a proxy or firewall](allow-device-traffic.md).

| Endpoint | Port | Required | Description |
| --- | --- | --- | --- |
| `logs.{{region}}.amazonaws.com` | 443 | No | Required if you write logs to CloudWatch Logs. |

## Dependencies
<a name="system-log-forwarder-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#system-log-forwarder-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 2.1.x ]

The following table lists the dependencies for version 2.1.x of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Token exchange service](token-exchange-service-component.md) | >=2.0.0 | Hard |
| [Greengrass nucleus lite](greengrass-nucleus-lite-component.md) | >=2.3.0 | Soft |

------
#### [ 2.0.x ]

The following table lists the dependencies for version 2.0.x of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Token exchange service](token-exchange-service-component.md) | >=2.0.0 | Hard |

------

## Configuration
<a name="system-log-forwarder-component-configuration"></a>

This component provides the following configuration parameters that you can customize when you deploy the component.

------
#### [ 2.0.x-2.1.x ]

`maxUploadIntervalSec`
The maximum period at which system log forwarder will attempt to upload logs. Since log forwarder will upload logs when the memory fills, it may still upload more often than the configured maximum cadence.

`maxRetriesCount`
Number of times system log forwarder will attempt to retry a transient HTTP error.

`bufferCapacity`
The size of the ring buffer for in-memory log storage.

`logGroup`
The log path in CloudWatch.

`logStream`
The CloudWatch logStream.

`filters`
A map of filter configurations for the core device.
`services`
A list of service name filters that System Log Forwarder will use to determine which logs gets uploaded. A log will only be uploaded if the service it originated from matches at least one of the filters in this list. The filters in this list may either be a string that the service name must fully match, or a string ending with \*, which means the prefix must match.
Default: `[ggl.*]`
A log will only be uploaded if the service it originated from matches at least one of the filters in this list.
Using the value \* will include all available services.

**Example configuration:**
The example below will filter logs by all services included in Greengrass Nucleus Lite.

```
{
    "maxUploadIntervalSec": 300,
    "maxRetriesCount": 3,
    "bufferCapacity": 1048576,
    "logGroup": "greengrass/systemLogs",
    "logStream": "deviceName",
    "filters": {
        "services": ["ggl.*"]
    }
}
```

------

## Changelog
<a name="system-log-forwarder-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.1.0 |  **Bug fixes and improvements**<br />   Updates the component recipe to properly support Greengrass nucleus.   Improved logging output when there are no logs to upload.   General bug fixes and improvements.     |
| 2.0.1 |  **Bug fixes and improvements**<br /> Updates the component recipe to properly support aarch64 (arm64) systems.   |
| 2.0.0 | Initial version. |
