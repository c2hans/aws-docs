---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/disk-spooler-component.html
---

# Disk spooler
<a name="disk-spooler-component"></a>

The disk spooler component (`aws.greengrass.DiskSpooler`) offers a persistent storage option for messages spooled from Greengrass core devices to AWS IoT Core. This component will store these outbound messages on disk.

**Topics**
+ [Versions](#disk-spooler-component-versions)
+ [Type](#disk-spooler-component-type)
+ [Operating system](#disk-spooler-component-os-support)
+ [Requirements](#disk-spooler-component-requirements)
+ [Dependencies](#disk-spooler-component-dependencies)
+ [Usage](#disk-spooler-component-usage)
+ [Local log file](#disk-spooler-component-log-file)
+ [Changelog](#disk-spooler-component-changelog)

## Versions
<a name="disk-spooler-component-versions"></a>

This component has the following versions:
+ 1.0.x

## Type
<a name="disk-spooler-component-type"></a>

<a name="public-component-type-plugin-para1"></a>This component is a plugin component (`aws.greengrass.plugin`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs this component in the same Java Virtual Machine (JVM) as the nucleus. The nucleus restarts when you change this component's version on the core device.

<a name="public-component-type-plugin-para2"></a>This component uses the same log file as the Greengrass nucleus. For more information, see [Monitor AWS IoT Greengrass logs](monitor-logs.md).

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="disk-spooler-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Requirements
<a name="disk-spooler-component-requirements"></a>

This component has the following requirements:
+ `storageType` should be set to `Disk` to use this component. You can set this in the [Greengrass nucleus configuration](greengrass-nucleus-component.md#greengrass-nucleus-component-configuration).
+ `maxSizeInBytes` must not be configured to be greater than the available space on the device. You can set this in the [Greengrass nucleus configuration](greengrass-nucleus-component.md#greengrass-nucleus-component-configuration).
+ The disk spooler component is supported to run in a VPC.

## Dependencies
<a name="disk-spooler-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#disk-spooler-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 1.0.7 ]

The following table lists the dependencies for version 1.0.7 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.11.0 <2.17.0 | Hard |

------
#### [ 1.0. ]

The following table lists the dependencies for version 1.0.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.11.0 <2.16.0 | Hard |

------
#### [ 1.0.5 ]

The following table lists the dependencies for version 1.0.5 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.11.0 <2.15.0 | Hard |

------
#### [ 1.0.4 ]

The following table lists the dependencies for version 1.0.4 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.11.0 <2.14.0 | Hard |

------
#### [ 1.0.1 – 1.0.3 ]

The following table lists the dependencies for versions 1.0.1 to 1.0.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.11.0 <2.13.0 | Hard |

------
#### [ 1.0.0 ]

The following table lists the dependencies for version 1.0.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.11.0 <2.12.0 | Hard |

------

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Usage
<a name="disk-spooler-component-usage"></a>

To use the disk spooler component, `aws.greengrass.DiskSpooler` must be deployed.

To configure and use this component, you must set the `pluginName` to `aws.greengrass.DiskSpooler`.

## Local log file
<a name="disk-spooler-component-log-file"></a>

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
<a name="disk-spooler-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 1.0.9 | Updates the component version for the Greengrass nucleus version 2.18.0 release. |
| 1.0.8 | Updates the component version for the Greengrass nucleus version 2.17.0 release. |
| 1.0.7 | Version updated for Greengrass nucleus version 2.16.0 release. |
| 1.0.6 | Version updated for Greengrass nucleus version 2.15.0 release. |
| 1.0.5 | Version updated for Greengrass nucleus version 2.14.0 release. |
| 1.0.4 |  **Bug fixes and improvements**<br /> General bug fixes.   |
| 1.0.3 |  **Bug fixes and improvements**<br /> Improves performance by reusing database connections.   |
| 1.0.2 |  **Bug fixes and improvements**<br /> Fixes an issue where the MQTT message format field isn't persisted in certain cases.   |
| 1.0.1 | Version updated for Greengrass nucleus version 2.12.0 release. |
| 1.0.0 | Initial version. |
