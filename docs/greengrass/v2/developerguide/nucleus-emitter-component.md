---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/nucleus-emitter-component.html
---

# Nucleus telemetry emitter
<a name="nucleus-emitter-component"></a>

The nucleus telemetry emitter component (`aws.greengrass.telemetry.NucleusEmitter`) gathers system health telemetry data and publishes it continually to a local topic and an AWS IoT Core MQTT topic. This component enables you to gather real-time system telemetry on your Greengrass core devices. For information about the Greengrass telemetry agent that publishes system telemetry data to Amazon EventBridge, see [Gather system health telemetry data from AWS IoT Greengrass core devices](telemetry.md).

By default, the nucleus telemetry emitter component publishes telemetry data every 60 seconds to the following local publish/subscribe topic.

```
$local/greengrass/telemetry
```

The nucleus telemetry emitter component doesn't publish to an AWS IoT Core MQTT topic by default. You can configure this component to publish to an AWS IoT Core MQTT topic when you deploy it. The use of an MQTT topic to publish data to the AWS Cloud is subject to [AWS IoT Core pricing](https://aws.amazon.com/iot-core/pricing/).

<a name="greengrass-software-catalog-influxdb-telemetry-publisher"></a>AWS IoT Greengrass provides several [community components](greengrass-software-catalog.md) to help you analyze and visualize telemetry data locally on your core device using InfluxDB and Grafana. These components use telemetry data from the nucleus emitter component. For more information, see the README for the [InfluxDB publisher component](https://github.com/awslabs/aws-greengrass-labs-telemetry-influxdbpublisher).

**Topics**
+ [Versions](#nucleus-emitter-component-versions)
+ [Type](#nucleus-emitter-component-type)
+ [Operating system](#nucleus-emitter-component-os-support)
+ [Dependencies](#nucleus-emitter-component-dependencies)
+ [Configuration](#nucleus-emitter-component-configuration)
+ [Output data](#nucleus-emitter-component-output-data)
+ [Usage](#nucleus-emitter-component-usage)
+ [Local log file](#nucleus-emitter-component-log-file)
+ [Changelog](#nucleus-emitter-component-changelog)

## Versions
<a name="nucleus-emitter-component-versions"></a>

This component has the following versions:
+ 1.0.x

## Type
<a name="nucleus-emitter-component-type"></a>

<a name="public-component-type-plugin-para1"></a>This component is a plugin component (`aws.greengrass.plugin`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs this component in the same Java Virtual Machine (JVM) as the nucleus. The nucleus restarts when you change this component's version on the core device.

<a name="public-component-type-plugin-para2"></a>This component uses the same log file as the Greengrass nucleus. For more information, see [Monitor AWS IoT Greengrass logs](monitor-logs.md).

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="nucleus-emitter-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Dependencies
<a name="nucleus-emitter-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#nucleus-emitter-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 1.0.12 ]

The following table lists the dependencies for version 1.0.12 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.4.0 <2.17.0 | Soft |

------
#### [ 1.0.11 ]

The following table lists the dependencies for version 1.0.11 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.16.0  | Hard |

------
#### [ 1.0.10 ]

The following table lists the dependencies for version 1.0.10 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.15.0  | Hard |

------
#### [ 1.0.9 ]

The following table lists the dependencies for version 1.0.9 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.14.0  | Hard |

------
#### [ 1.0.8 ]

The following table lists the dependencies for version 1.0.8 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.13.0  | Hard |

------
#### [ 1.0.7 ]

The following table lists the dependencies for version 1.0.7 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.12.0  | Hard |

------
#### [ 1.0.6 ]

The following table lists the dependencies for version 1.0.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.11.0  | Hard |

------
#### [ 1.0.5 ]

The following table lists the dependencies for version 1.0.5 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.10.0  | Hard |

------
#### [ 1.0.4 ]

The following table lists the dependencies for version 1.0.4 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.9.0  | Hard |

------
#### [ 1.0.3 ]

The following table lists the dependencies for version 1.0.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.8.0  | Hard |

------
#### [ 1.0.2 ]

The following table lists the dependencies for version 1.0.2 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.7.0  | Hard |

------
#### [ 1.0.1 ]

The following table lists the dependencies for version 1.0.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.6.0  | Hard |

------
#### [ 1.0.0 ]

The following table lists the dependencies for version 1.0.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.4.0 <2.5.0  | Hard |

------

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="nucleus-emitter-component-configuration"></a>

This component provides the following configuration parameters that you can customize when you deploy the component.

`pubSubPublish`
(Optional) Defines whether to publish telemetry data to the `$local/greengrass/telemetry` topic. Supported values are `true` and `false`.
Default: `true`

`mqttTopic`
(Optional) The AWS IoT Core MQTT topic to which this component publishes telemetry data.
Set this value to the AWS IoT Core MQTT topic to which you want to publish telemetry data. When this value is empty, the nucleus emitter doesn't publish telemetry data to the AWS Cloud.
The use of an MQTT topic to publish data to the AWS Cloud is subject to [AWS IoT Core pricing](https://aws.amazon.com/iot-core/pricing/).
Default: `""`

`telemetryPublishIntervalMs`
(Optional) The amount of time (in milliseconds) between which the component publishes telemetry data. If you set this value lower than the minimum supported value, the component uses the minimum value instead.
Lower publish intervals result in higher CPU usage on your core device. We recommend that you start with the default publish interval and adjust it based on your device's CPU usage.
Minimum: `500`
Default: `60000`

**Example: Configuration merge update**
The following example shows a sample configuration merge update that enables publishing telemetry data every 5 seconds to the `$local/greengrass/telemetry` topic and the `greengrass/myTelemetry` AWS IoT Core MQTT topic.

```
{
  "pubSubPublish": "true",
  "mqttTopic": "greengrass/myTelemetry",
  "telemetryPublishIntervalMs": 5000
}
```

## Output data
<a name="nucleus-emitter-component-output-data"></a>

This component publishes telemetry metrics as a JSON array on the following topic.

**Local topic:** `$local/greengrass/telemetry`

You can optionally choose to also publish telemetry metrics to an AWS IoT Core MQTT topic. For more information about topics, see [MQTT topics](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html) in the *AWS IoT Core Developer Guide*.

**Example data**

```
[
  {
    "A": "Average",
    "N": "CpuUsage",
    "NS": "SystemMetrics",
    "TS": 1627597331445,
    "U": "Percent",
    "V": 26.21981271562346
  },
  {
    "A": "Count",
    "N": "TotalNumberOfFDs",
    "NS": "SystemMetrics",
    "TS": 1627597331445,
    "U": "Count",
    "V": 7316
  },
  {
    "A": "Count",
    "N": "SystemMemUsage",
    "NS": "SystemMetrics",
    "TS": 1627597331445,
    "U": "Megabytes",
    "V": 10098
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsStarting",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 0
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsInstalled",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 0
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsStateless",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 0
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsStopping",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 0
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsBroken",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 0
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsRunning",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 7
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsErrored",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 0
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsNew",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 0
  },
  {
    "A": "Count",
    "N": "NumberOfComponentsFinished",
    "NS": "GreengrassComponents",
    "TS": 1627597331446,
    "U": "Count",
    "V": 2
  }
]
```<a name="telemetry-json-array-config"></a>

The output array contains a list of metrics that have the following properties:

`A`
The aggregation type for the metric.
For the `CpuUsage` metric, this property is set to `Average` because the published value of the metric is the average CPU usage amount since the last publish event.
For all other metrics, the nucleus emitter doesn't aggregate the metric value, and this property is set to `Count`.

`N`
The name of the metric.

`NS`
The metric namespace.

`TS`
The timestamp of when the data was gathered.

`U`
The unit of the metric value.

`V`
The metric value.

The nucleus emitter publishes the following metrics:

<a name="telemetry-metrics-table-nucleus-emitter"></a>
<table>
<thead>
  <tr><th>Name</th><th>Description</th><th></th></tr>
</thead>
<tbody>
  <tr><td><b>System</b></td><td></td><td></td></tr>
  <tr><td><code>SystemMemUsage</code></td><td>The amount of memory currently in use by all applications on the Greengrass core device, including the operating system.</td><td></td></tr>
  <tr><td><code>CpuUsage</code></td><td>The amount of CPU currently in use by all applications on the Greengrass core device, including the operating system.</td><td></td></tr>
  <tr><td><code>TotalNumberOfFDs</code></td><td>The number of file descriptors stored by the operating system of the Greengrass core device. One file descriptor uniquely identifies one open file.</td><td></td></tr>
  <tr><td><b>Greengrass nucleus</b></td><td></td><td></td></tr>
  <tr><td><code>NumberOfComponentsRunning</code></td><td>The number of components that are running on the Greengrass core device.</td><td></td></tr>
  <tr><td><code>NumberOfComponentsErrored</code></td><td>The number of components that are in error state on the Greengrass core device.</td><td></td></tr>
  <tr><td><code>NumberOfComponentsInstalled</code></td><td>The number of components that are installed on the Greengrass core device.</td><td></td></tr>
  <tr><td><code>NumberOfComponentsStarting</code></td><td>The number of components that are starting on the Greengrass core device.</td><td></td></tr>
  <tr><td><code>NumberOfComponentsNew</code></td><td>The number of components that are new on the Greengrass core device.</td><td></td></tr>
  <tr><td><code>NumberOfComponentsStopping</code></td><td>The number of components that are stopping on the Greengrass core device.</td><td></td></tr>
  <tr><td><code>NumberOfComponentsFinished</code></td><td>The number of components that are finished on the Greengrass core device.</td><td></td></tr>
  <tr><td><code>NumberOfComponentsBroken</code></td><td>The number of components that are broken on the Greengrass core device.</td><td></td></tr>
  <tr><td><code>NumberOfComponentsStateless</code></td><td>The number of components that are stateless on the Greengrass core device.</td><td></td></tr>
</tbody>
</table>

## Usage
<a name="nucleus-emitter-component-usage"></a>

To use system health telemetry data, you can create custom components that subscribe to the topics to which the nucleus emitter publishes the telemetry data, and react to that data as needed. Because the nucleus emitter component provides the option to publish telemetry data to a local topic, you can subscribe to that topic, and use the published data to act locally on your core device. The core device can then react to telemetry data even when it has limited connectivity to the cloud.

For example, you can configure a component that listens on the `$local/greengrass/telemetry` topic for telemetry data and send the data to the stream manager component to stream your data to the AWS Cloud. For more information about creating such a component, see [Publish/subscribe local messages](ipc-publish-subscribe.md) and [Create custom components that use stream manager](use-stream-manager-in-custom-components.md).

## Local log file
<a name="nucleus-emitter-component-log-file"></a>

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
<a name="nucleus-emitter-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 1.0.14 | Updates the component version for the Greengrass nucleus version 2.18.0 release. |
| 1.0.13 | Updates the component version for the Greengrass nucleus version 2.17.0 release. |
| 1.0.12 | Version updated for Greengrass nucleus version 2.16.0 release. |
| 1.0.11 | Version updated for Greengrass nucleus version 2.15.0 release. |
| 1.0.10 | Version updated for Greengrass nucleus version 2.14.0 release. |
| 1.0.9 | Version updated for Greengrass nucleus version 2.13.0 release. |
| 1.0.8 | Version updated for Greengrass nucleus version 2.12.0 release. |
| 1.0.7 | Version updated for Greengrass nucleus version 2.11.0 release. |
| 1.0.6 | Version updated for Greengrass nucleus version 2.10.0 release. |
| 1.0.5 | Version updated for Greengrass nucleus version 2.9.0 release. |
| 1.0.4 | Version updated for Greengrass nucleus version 2.8.0 release. |
| 1.0.3 | Version updated for Greengrass nucleus version 2.7.0 release. |
| 1.0.2 | Version updated for Greengrass nucleus version 2.6.0 release. |
| 1.0.1 | Version updated for Greengrass nucleus version 2.5.0 release. |
| 1.0.0 | Initial version. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
