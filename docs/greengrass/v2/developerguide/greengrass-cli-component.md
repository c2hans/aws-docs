---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-cli-component.html
---

# Greengrass CLI
<a name="greengrass-cli-component"></a>

The Greengrass CLI component (`aws.greengrass.Cli`) provides a local command-line interface that you can use on core devices to develop and debug components locally. The Greengrass CLI lets you create local deployments and restart components on the core device, for example.

You can install this component when you install the AWS IoT Greengrass Core software. For more information, see [Tutorial: Getting started with AWS IoT Greengrass V2](getting-started.md).

**Important**
 <a name="local-dev-tools-production-environment-warning"></a>We recommend that you use this component in only development environments, not production environments. This component provides access to information and operations that you typically won't need in a production environment. Follow the principle of least privilege by deploying this component to only core devices where you need it.

After you install this component, run the following command to view its help documentation. When this component installs, it adds a symbolic link to `greengrass-cli` in the `{{/greengrass/v2}}/bin` folder. You can run the Greengrass CLI from this path or add it to your `PATH` environment variable to run `greengrass-cli` without its absolute path.

------
#### [ Linux or Unix ]

```
{{/greengrass/v2}}/bin/greengrass-cli help
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\bin\greengrass-cli help
```

------

The following command restarts a component named `com.example.HelloWorld`, for example.

------
#### [ Linux or Unix ]

```
sudo {{/greengrass/v2}}/bin/greengrass-cli component restart --names "com.example.HelloWorld"
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\bin\greengrass-cli component restart --names "com.example.HelloWorld"
```

------

For more information, see [Greengrass Command Line Interface](gg-cli.md).

**Topics**
+ [Versions](#greengrass-cli-component-versions)
+ [Type](#greengrass-cli-component-type)
+ [Operating system](#greengrass-cli-component-os-support)
+ [Requirements](#greengrass-cli-component-requirements)
+ [Dependencies](#greengrass-cli-component-dependencies)
+ [Configuration](#greengrass-cli-component-configuration)
+ [Local log file](#greengrass-cli-component-log-file)
+ [Changelog](#greengrass-cli-component-changelog)

## Versions
<a name="greengrass-cli-component-versions"></a>

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

## Type
<a name="greengrass-cli-component-type"></a>

<a name="public-component-type-plugin-para1"></a>This component is a plugin component (`aws.greengrass.plugin`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs this component in the same Java Virtual Machine (JVM) as the nucleus. The nucleus restarts when you change this component's version on the core device.

<a name="public-component-type-plugin-para2"></a>This component uses the same log file as the Greengrass nucleus. For more information, see [Monitor AWS IoT Greengrass logs](monitor-logs.md).

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="greengrass-cli-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Requirements
<a name="greengrass-cli-component-requirements"></a>

This component has the following requirements:
+ <a name="greengrass-cli-authorization-requirement"></a>You must be authorized to use the Greengrass CLI to interact with the AWS IoT Greengrass Core software. Do one of the following to use the Greengrass CLI:
  + Use the system user that runs the AWS IoT Greengrass Core software.
  + Use a user with root or adminstrative permissions. On Linux core devices, you can use `sudo` to gain root permissions.
  + Use a system user that's in a group that you specify in the `AuthorizedPosixGroups` or `AuthorizedWindowsGroups` configuration parameters when you deploy the component. For more information, see [Greengrass CLI component configuration](#greengrass-cli-component-configuration).
+ The Greengrass CLI component is supported to run in a VPC.

## Dependencies
<a name="greengrass-cli-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#greengrass-cli-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 2.16.0 ]

The following table lists the dependencies for version 2.16.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.12.0 <2.17.0 | Soft |

------
#### [ 2.15.1 ]

The following table lists the dependencies for version 2.15.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.12.0 <2.16.0 | Soft |

------
#### [ 2.15.0 ]

The following table lists the dependencies for version 2.15.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.12.0 <2.16.0 | Soft |

------
#### [ 2.14.0 – 2.14.3 ]

The following table lists the dependencies for versions 2.14.0 and 2.14.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.12.0 <2.15.0 | Soft |

------
#### [ 2.13.0 ]

The following table lists the dependencies for version 2.13.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.12.0 <2.14.0 | Soft |

------
#### [ 2.12.0 – 2.12.6 ]

The following table lists the dependencies for version 2.12.0 through 2.12.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.12.0 <2.13.0 | Soft |

------
#### [ 2.11.0 – 2.11.3 ]

The following table lists the dependencies for versions 2.11.0 through 2.11.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.11.0 <2.12.0 | Soft |

------
#### [ 2.10.0 – 2.10.3 ]

The following table lists the dependencies for versions 2.10.0 through 2.10.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.11.0 | Soft |

------
#### [ 2.9.0 – 2.9.6 ]

The following table lists the dependencies for versions 2.9.0 through 2.9.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.10.0 | Soft |

------
#### [ 2.8.0 – 2.8.1 ]

The following table lists the dependencies for version 2.8.0 and 2.8.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.9.0 | Soft |

------
#### [ 2.7.0 ]

The following table lists the dependencies for version 2.7.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.8.0 | Soft |

------
#### [ 2.6.0 ]

The following table lists the dependencies for version 2.6.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.7.0 | Soft |

------
#### [ 2.5.0 – 2.5.6 ]

The following table lists the dependencies for versions 2.5.0 through 2.5.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.6.0 | Soft |

------
#### [ 2.4.0 ]

The following table lists the dependencies for version 2.4.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.1.0 <2.5.0 | Soft |

------
#### [ 2.3.0 ]

The following table lists the dependencies for version 2.3.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.1.0 <2.4.0 | Soft |

------
#### [ 2.2.0 ]

The following table lists the dependencies for version 2.2.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.1.0 <2.3.0 | Soft |

------
#### [ 2.1.0 ]

The following table lists the dependencies for version 2.1.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.1.0 <2.2.0 | Soft |

------
#### [ 2.0.x ]

The following table lists the dependencies for version 2.0.x of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.0.0 <2.1.0 | Soft |

**Note**
The minimum compatible version of the Greengrass nucleus corresponds to the patch version of the Greengrass CLI component.

------

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="greengrass-cli-component-configuration"></a>

This component provides the following configuration parameters that you can customize when you deploy the component.

------
#### [ 2.5.x - 2.14.x ]

`AuthorizedPosixGroups`  <a name="greengrass-cli-component-configuration-authorizedposixgroups"></a>
(Optional) A string that contains a comma-separated list of system groups. You authorize these system groups to use the Greengrass CLI to interact with the AWS IoT Greengrass Core software. You can specify group names or group IDs. For example, `group1,1002,group3` authorizes three system groups (`group1`, `1002`, and `group3`) to use the Greengrass CLI.
If you don't specify any groups to authorize, you can use the Greengrass CLI as the root user (`sudo`) or as the system user that runs the AWS IoT Greengrass Core software.

`AuthorizedWindowsGroups`  <a name="greengrass-cli-component-configuration-authorizedwindowsgroups"></a>
(Optional) A string that contains a comma-separated list of system groups. You authorize these system groups to use the Greengrass CLI to interact with the AWS IoT Greengrass Core software. You can specify group names or group IDs. For example, `group1,1002,group3` authorizes three system groups (`group1`, `1002`, and `group3`) to use the Greengrass CLI.
If you don't specify any groups to authorize, you can use the Greengrass CLI as an administrator or as the system user that runs the AWS IoT Greengrass Core software.

**Example: Configuration merge update**
The following example configuration specifies to authorize three POSIX system groups (`group1`, `1002`, and `group3`) and two Windows user groups (`Device Operators` and `QA Engineers`) to use the Greengrass CLI.

```
{
  "AuthorizedPosixGroups": "group1,1002,group3",
  "AuthorizedWindowsGroups": "Device Operators,QA Engineers"
}
```

------
#### [ 2.4.x - 2.0.x ]

`AuthorizedPosixGroups`  <a name="greengrass-cli-component-configuration-authorizedposixgroups"></a>
(Optional) A string that contains a comma-separated list of system groups. You authorize these system groups to use the Greengrass CLI to interact with the AWS IoT Greengrass Core software. You can specify group names or group IDs. For example, `group1,1002,group3` authorizes three system groups (`group1`, `1002`, and `group3`) to use the Greengrass CLI.
If you don't specify any groups to authorize, you can use the Greengrass CLI as the root user (`sudo`) or as the system user that runs the AWS IoT Greengrass Core software.

**Example: Configuration merge update**
The following example configuration specifies to authorize three system groups (`group1`, `1002`, and `group3`) to use the Greengrass CLI.

```
{
  "AuthorizedPosixGroups": "group1,1002,group3"
}
```

------

## Local log file
<a name="greengrass-cli-component-log-file"></a>

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
<a name="greengrass-cli-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.18.3 | Updates the component version for the Greengrass nucleus version 2.18.3 release. |
| 2.18.2 | Updates the component version for the Greengrass nucleus version 2.18.2 release. |
| 2.18.1 | Updates the component version for the Greengrass nucleus version 2.18.1 release. |
| 2.18.0 | Updates the component version for the Greengrass nucleus version 2.18.0 release. |
| 2.17.0 | Updates the component version for the Greengrass nucleus version 2.17.0 release. |
| 2.16.1 | Version updated for Greengrass nucleus version 2.16.1 release. |
| 2.16.0 | Version updated for Greengrass nucleus version 2.16.0 release. |
| 2.15.1 | Version updated for Greengrass nucleus version 2.15.1 release. |
| 2.15.0 |  **Bug fixes and improvements**<br />   Adds a fix so that when the auth configuration changes, the component won't reinstall but will still restart.   General bug fixes and improvements.     |
| 2.14.3 | Version updated for Greengrass nucleus version 2.14.3 release. |
| 2.14.2 | Version updated for Greengrass nucleus version 2.14.2 release. |
| 2.14.1 | Version updated for Greengrass nucleus version 2.14.1 release. |
| 2.14.0 |  **Bug fixes and improvements**<br />   Validate deployment target parameter in the cli command.     |
| 2.13.0 | Version updated for Greengrass nucleus version 2.13.0 release. |
| 2.12.6 | Version updated for Greengrass nucleus version 2.12.6 release. |
| 2.12.5 | Version updated for Greengrass nucleus version 2.12.5 release. |
| 2.12.4 | Version updated for Greengrass nucleus version 2.12.4 release. |
| 2.12.3 |  This version is no longer available. The improvements in this version are available in later versions of this component. Version updated for Greengrass nucleus version 2.12.3 release. |
| 2.12.2 | Version updated for Greengrass nucleus version 2.12.2 release. |
| 2.12.1 | Version updated for Greengrass nucleus version 2.12.1 release. |
| 2.12.0 | Version updated for Greengrass nucleus version 2.12.0 release. |
| 2.11.3 | Version updated for Greengrass nucleus version 2.11.3 release. |
| 2.11.2 | Version updated for Greengrass nucleus version 2.11.2 release. |
| 2.11.1 | Version updated for Greengrass nucleus version 2.11.1 release. |
| 2.11.0 |  <a name="changelog-cli-2.11.0"></a>**New features**<br />   Enables you to cancel a local deployment.   Enables you to configure a failure handling policy for a local deployment.   Improves detailed deployment status reporting.     |
| 2.10.3 | Version updated for Greengrass nucleus version 2.10.3 release. |
| 2.10.2 | Version updated for Greengrass nucleus version 2.10.2 release. |
| 2.10.1 | Version updated for Greengrass nucleus version 2.10.1 release. |
| 2.10.0 | Version updated for Greengrass nucleus version 2.10.0 release. |
| 2.9.6 | Version updated for Greengrass nucleus version 2.9.6 release. |
| 2.9.5 | Version updated for Greengrass nucleus version 2.9.5 release. |
| 2.9.4 | Version updated for Greengrass nucleus version 2.9.4 release. |
| 2.9.3 | Version updated for Greengrass nucleus version 2.9.3 release. |
| 2.9.2 | Version updated for Greengrass nucleus version 2.9.2 release. |
| 2.9.1 | Version updated for Greengrass nucleus version 2.9.1 release. |
| 2.9.0 | Version updated for Greengrass nucleus version 2.9.0 release. |
| 2.8.1 | Version updated for Greengrass nucleus version 2.8.1 release. |
| 2.8.0 | Version updated for Greengrass nucleus version 2.8.0 release. |
| 2.7.0 | Version updated for Greengrass nucleus version 2.7.0 release. |
| 2.6.0 |  <a name="changelog-greengrass-cli-2.6.0"></a>**New features**<br />   Adds support for custom components to call interprocess communication (IPC) operations that the Greengrass CLI uses. You can use these IPC operations to manage local deployments, view component details, and generate a password that you can use to sign in to the [local debug console](local-debug-console-component.md). For more information, see [IPC: Manage local deployments and components](ipc-local-deployments-components.md).   <br />**Bug fixes and improvements**<br />   Additional minor fixes and improvements.     |
| 2.5.6 | Version updated for Greengrass nucleus version 2.5.6 release. |
| 2.5.5 | Version updated for Greengrass nucleus version 2.5.5 release. |
| 2.5.4 | Version updated for Greengrass nucleus version 2.5.4 release. |
| 2.5.3 | Version updated for Greengrass nucleus version 2.5.3 release. |
| 2.5.2 | Version updated for Greengrass nucleus version 2.5.2 release. |
| 2.5.1 | Version updated for Greengrass nucleus version 2.5.1 release. |
| 2.5.0 |  <a name="changelog-greengrass-cli-2.5.0"></a>**New features**<br />   Adds support for core devices that run Windows.   Adds the new `AuthorizedWindowsGroups` configuration parameter that you can specify to authorize system groups to use the Greengrass CLI on Windows devices.   Adds the `windowsUser` parameter for local deployments. You can use this parameter specify the user to use to run components on a Windows core device.     |
| 2.4.0 |  <a name="changelog-greengrass-cli-2.4.0"></a>**New features**<br />   Adds support for system resource limits. When you create a local deployment, you can configure the maximum amount of CPU and RAM usage that each component's processes can use on the core device. For more information, see [Configure system resource limits for components](configure-greengrass-core-v2.md#configure-component-system-resource-limits) and the [deployment create command](gg-cli-deployment.md#deployment-create).     |
| 2.3.0 | Version updated for Greengrass nucleus version 2.3.0 release. |
| 2.2.0 | Version updated for Greengrass nucleus version 2.2.0 release. |
| 2.1.0 | Version updated for Greengrass nucleus version 2.1.0 release. |
| 2.0.5 | Version updated for Greengrass nucleus version 2.0.5 release. |
| 2.0.4 | Version updated for Greengrass nucleus version 2.0.4 release. |
| 2.0.3 | Initial version. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
