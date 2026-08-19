---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/lambda-manager-component.html
---

# Lambda manager
<a name="lambda-manager-component"></a>

The Lambda manager component (`aws.greengrass.LambdaManager`) manages work items and interprocess communication for AWS Lambda functions that run on the Greengrass core device.

**Note**  <a name="lambda-component-dependency-note"></a>
When you deploy a Lambda function component to a core device, the deployment also includes this component. For more information, see [Run AWS Lambda functions](run-lambda-functions.md).

**Topics**
+ [Versions](#lambda-manager-component-versions)
+ [Operating system](#lambda-manager-component-os-support)
+ [Type](#lambda-manager-component-type)
+ [Requirements](#lambda-manager-component-requirements)
+ [Dependencies](#lambda-manager-component-dependencies)
+ [Configuration](#lambda-manager-component-configuration)
+ [Local log file](#lambda-manager-component-log-file)
+ [Changelog](#lambda-manager-component-changelog)

## Versions
<a name="lambda-manager-component-versions"></a>

This component has the following versions:
+ 2.3.x
+ 2.2.x
+ 2.1.x
+ 2.0.x

## Operating system
<a name="lambda-manager-component-os-support"></a>

This component can be installed on Linux core devices only.

## Type
<a name="lambda-manager-component-type"></a>

<a name="public-component-type-plugin-para1"></a>This component is a plugin component (`aws.greengrass.plugin`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs this component in the same Java Virtual Machine (JVM) as the nucleus. The nucleus restarts when you change this component's version on the core device.

<a name="public-component-type-plugin-para2"></a>This component uses the same log file as the Greengrass nucleus. For more information, see [Monitor AWS IoT Greengrass logs](monitor-logs.md).

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Requirements
<a name="lambda-manager-component-requirements"></a>

This component has the following requirements:
+ <a name="core-device-lambda-function-requirements"></a>Your core device must meet the requirements to run Lambda functions. If you want the core device to run containerized Lambda functions, the device must meet the requirements to do so. For more information, see [Lambda function requirements](setting-up.md#greengrass-v2-lambda-requirements).
+ The Lambda manager component is supported to run in a VPC.

## Dependencies
<a name="lambda-manager-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#lambda-manager-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 2.3.7 ]

The following table lists the dependencies for version 2.3.7 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.0.0 <2.17.0 | Soft |

------
#### [ 2.3.6 ]

The following table lists the dependencies for version 2.3.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.16.0  | Soft |

------
#### [ 2.3.5 ]

The following table lists the dependencies for version 2.3.5 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.15.0  | Soft |

------
#### [ 2.3.4 ]

The following table lists the dependencies for version 2.3.4 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.14.0  | Soft |

------
#### [ 2.3.2 and 2.3.3 ]

The following table lists the dependencies for version 2.3.2 and 2.3.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.13.0  | Soft |

------
#### [ 2.2.10 and 2.3.1 ]

The following table lists the dependencies for version 2.2.10 and 2.3.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.12.0  | Soft |

------
#### [ 2.2.8 and 2.2.9 ]

The following table lists the dependencies for version 2.2.8 and 2.2.9 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.11.0  | Soft |

------
#### [ 2.2.7 ]

The following table lists the dependencies for version 2.2.7 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.10.0  | Soft |

------
#### [ 2.2.6 ]

The following table lists the dependencies for version 2.2.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.9.0  | Soft |

------
#### [ 2.2.5 ]

The following table lists the dependencies for version 2.2.5 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.8.0  | Soft |

------
#### [ 2.2.4 ]

The following table lists the dependencies for version 2.2.4 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.7.0  | Soft |

------
#### [ 2.2.1 - 2.2.3 ]

The following table lists the dependencies for versions 2.2.1 to 2.2.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.6.0  | Soft |

------
#### [ 2.2.0 ]

The following table lists the dependencies for version 2.2.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.5.0 <2.6.0  | Soft |

------
#### [ 2.1.3 and 2.1.4 ]

The following table lists the dependencies for versions 2.1.3 and 2.1.4 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.5.0  | Soft |

------
#### [ 2.1.2 ]

The following table lists the dependencies for version 2.1.2 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.4.0  | Soft |

------
#### [ 2.1.1 ]

The following table lists the dependencies for version 2.1.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.3.0  | Soft |

------
#### [ 2.1.0 ]

The following table lists the dependencies for version 2.1.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.2.0  | Soft |

------
#### [ 2.0.x ]

The following table lists the dependencies for version 2.0.x of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.3 <2.1.0  | Soft |

------

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="lambda-manager-component-configuration"></a>

This component provides the following configuration parameters that you can customize when you deploy the component.

`logHandlerMode`
Only for lambda manager versions 2.3.0\+
Used to choose the implementation of the Lambda log manager to use. Set the value to `optimized` to use fewer threads to read lambda logs.

`getResultTimeoutInSecond`
(Optional) The maximum amount of time in seconds that Lambda functions can run before they time out.
Default: `60`

## Local log file
<a name="lambda-manager-component-log-file"></a>

This component uses the same log file as the [Greengrass nucleus](greengrass-nucleus-component.md) component.

```
{{/greengrass/v2}}/logs/greengrass.log
```

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace `{{/greengrass/v2}}` with the path to the AWS IoT Greengrass root folder.

  ```
  sudo tail -f {{/greengrass/v2}}/logs/greengrass.log
  ```

## Changelog
<a name="lambda-manager-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.3.9 | Updates the component version for the Greengrass nucleus version 2.18.0 release. |
| 2.3.8 | Updates the component version for the Greengrass nucleus version 2.17.0 release. |
| 2.3.7 | Version updated for Greengrass nucleus version 2.16.0 release. |
| 2.3.6 | Version updated for Greengrass nucleus version 2.15.0 release. |
| 2.3.5 |  **Bug fixes and improvements**<br />   Improves performance by using epoll instead of nio when available.     |
| 2.3.4 | Version updated for Greengrass nucleus version 2.13.0 release. |
| 2.3.3 |  **Bug fixes and improvements**<br />   General bug fixes and improvements.     |
| 2.3.2 | Version updated for Greengrass nucleus version 2.12.0 release. |
| 2.3.1 |  <a name="changelog-lambda-manager-2.3.1"></a>**Bug fixes and improvements**<br />   Adjusts log levels for certain errors.     |
| 2.3.0 |  **New features**<br />   Log handler was optimized to reduce CPU load. Use this feature by setting the configuration option `logHandlerMode` to `optimized`.   <br />**Bug fixes and improvements**<br />   No longer logs the full stacktrace for `WorkQueueFullException`, improving logs and performance.   Sets lambda shutdown timeout from 15 seconds to 300 seconds in order to prevent shutdown timeouts.   Fixes an issue where on-demand lambdas may fail to restart after changing configuration.     |
| 2.2.11 |  <a name="changelog-lambda-manager-2.2.11"></a>**Bug fixes and improvements**<br />   Fixes an issue where the LegacySubscriptionRouter configuration does not update when the Lambda configuration changes.     |
| 2.2.10 | Version updated for Greengrass nucleus version 2.11.0 release. |
| 2.2.9 |  <a name="changelog-lambda-manager-2.2.9"></a>**Bug fixes and improvements**<br /> Fixes an issue where the port number is corrupted due to a skewed clock.   |
| 2.2.8 | Version updated for Greengrass nucleus version 2.10.0 release. |
| 2.2.7 | Version updated for Greengrass nucleus version 2.9.0 release. |
| 2.2.6 | Version updated for Greengrass nucleus version 2.8.0 release. |
| 2.2.5 |  <a name="changelog-lambda-manager-2.2.5"></a>**New features**<br />   Adds support for MQTT topic wildcards in event sources where you subscribe to local publish/subscribe messages. <br />This feature requires v2.6.0 or later of the [Greengrass nucleus component](greengrass-nucleus-component.md).   Version updated for Greengrass nucleus version 2.7.0 release.     |
| 2.2.4 | Version updated for Greengrass nucleus version 2.6.0 release. |
| 2.2.3 |  **Bug fixes and improvements**<br />   Fixes an issue where multiple instances of a Lambda function share a single cgroup. This component uses cgroups to manage resource usage for Lambda functions.     |
| 2.2.2 |  **Bug fixes and improvements**<br />   Fixes an issue where pinned Lambda function components restart unexpectedly in certain scenarios.     |
| 2.2.1 |  **Bug fixes and improvements**<br />   Changes this component's [Greengrass nucleus](greengrass-nucleus-component.md) dependency version constraints to fix a dependency resolution issue.     |
| 2.2.0 |  <a name="changelog-lambda-manager-2.2.0"></a>**Bug fixes and improvements**<br />   Fixes an issue where Lambda functions couldn't write logs after a restart.   Fixes an issue where the legacy subscription router sends duplicate messages when there are wildcards in the topic.   Fixes an issue where non-pinned Lambda functions couldn't use the Greengrass interprocess communication (IPC) library in the AWS IoT Device SDK.     |
| 2.1.4 |  **Bug fixes and improvements**<br />   Fixes an issue that caused Lambda functions that use NodeJS runtimes to process only one message.   Version updated for Greengrass nucleus version 2.5.0 release.     |
| 2.1.3 | Version updated for Greengrass nucleus version 2.4.0 release. |
| 2.1.2 | Version updated for Greengrass nucleus version 2.3.0 release. |
| 2.1.1 | Version updated for Greengrass nucleus version 2.2.0 release. |
| 2.1.0 | Version updated for Greengrass nucleus version 2.1.0 release. |
| 2.0.3 | Initial version. |
