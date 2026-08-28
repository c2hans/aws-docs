---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/setup-greengrass-non-root.html
---

# Set up AWS IoT Greengrass V2 core devices as non-root
<a name="setup-greengrass-non-root"></a>

This page presents four solutions for running the AWS IoT Greengrass Core software as non-root. Review the comparison table to understand the features and tradeoffs of each solution, then use the decision flowchart to identify which one fits your requirements.

**Note**
The non-root solutions on this page apply to the AWS IoT Greengrass nucleus on Linux devices only. Windows is not included because AWS IoT Greengrass V2 must run as a system service on Windows. For standard root installation on Linux, see [Install AWS IoT Greengrass Core software with automatic resource provisioning](quick-installation.md).
To run AWS IoT Greengrass nucleus lite as a non-root user, see [Using Podman](https://github.com/aws-greengrass/aws-greengrass-lite/blob/main/docs/BUILD.md#optional-using-podman) in the AWS IoT Greengrass nucleus lite GitHub repository.

**Topics**
+ [Choose a non-root solution](#non-root-choose-solution)
+ [Solution 1: Set up AWS IoT Greengrass V2 without root access](#non-root-solution-1)
+ [Solution 2: Set up AWS IoT Greengrass V2 as non-root without component user separation](#non-root-solution-2)
+ [Solution 3: Set up AWS IoT Greengrass V2 as non-root with component user separation](#non-root-solution-3)
+ [Solution 4: Set up AWS IoT Greengrass V2 as root with limited capabilities](#non-root-solution-4)
+ [Linux capabilities required by AWS IoT Greengrass V2](#linux-capabilities-reference)

## Choose a non-root solution
<a name="non-root-choose-solution"></a>

Use the following table to compare the non-root solutions and understand their tradeoffs. Each solution offers different capabilities depending on your security requirements and device constraints.

**Non-root solutions**

| Solution | Requires root access | Can run components as different users | Runs Greengrass as system service | Best for |
| --- | --- | --- | --- | --- |
| [Solution 1: No root access](#non-root-solution-1) | No | No | No (user service optional) | Devices where you don't have root access |
| [Solution 2: Non-root, single user](#non-root-solution-2) | Yes (setup only) | No | Yes | Running Greengrass as a non-root user with all components running as the same user |
| [Solution 3: Non-root, multi-user](#non-root-solution-3) | Yes (setup only) | Yes | Yes | Running Greengrass as a non-root user while running components as different users |
| [Solution 4: Root with limited capabilities](#non-root-solution-4) | Yes | Yes | Yes | Running Greengrass as root with a limited set of Linux capabilities |

The following flowchart guides you through selecting the appropriate solution based on your device constraints and requirements.

![Flowchart showing decision process for choosing a non-root solution. Start by asking if you have root access on your core device. If no, use Solution 1. If yes, ask if you need to run components as different Linux users. If no, use Solution 2. If yes, ask if you want Greengrass to run as root user with limited capabilities. If yes, use Solution 4. If no, use Solution 3.](http://docs.aws.amazon.com/greengrass/v2/developerguide/images/non-root-solution-decision-flow.png)

## Solution 1: Set up AWS IoT Greengrass V2 without root access
<a name="non-root-solution-1"></a>

Use this solution when you don't have root access on the device. In this configuration, the AWS IoT Greengrass Core software runs entirely as a non-root user without elevated privileges.

**Tradeoffs**
This solution has the following limitations:
+ **No component user separation** – All components run as the same user that runs the AWS IoT Greengrass Core software. You cannot use the `posixUser` configuration to run components as different users.
+ **RequiresPrivilege ignored** – The AWS IoT Greengrass Core software ignores the `RequiresPrivilege` option in component recipes. Components cannot request elevated privileges.
+ **No system service** – You cannot install the AWS IoT Greengrass Core software as a system service. You can optionally configure AWS IoT Greengrass V2 to run as a systemd user service.

**Prerequisites**
This solution requires:
+ A non-root user account on the device
+ Write access to the directory where you want to install the AWS IoT Greengrass Core software

**To install and run AWS IoT Greengrass V2 without root access**

1. Complete the following steps from [Install AWS IoT Greengrass Core software with automatic resource provisioning](quick-installation.md): set up your device environment, provide credentials, and download the AWS IoT Greengrass Core software.

1. Create the installation directory and ensure your user owns it.

   ```
   mkdir -p $HOME/greengrass/v2
   ```

1. Run the installer without `sudo`. Set `--component-default-user` to your current user.

   ```
   java -Droot="$HOME/greengrass/v2" -Dlog.store=FILE \
     -jar ./GreengrassInstaller/lib/Greengrass.jar \
     --aws-region {{region}} \
     --thing-name {{MyGreengrassCore}} \
     --thing-group-name {{MyGreengrassCoreGroup}} \
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} \
     --tes-role-name {{GreengrassV2TokenExchangeRole}} \
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} \
     --component-default-user $USER \
     --provision true
   ```

   Do not use `--setup-system-service true` because you don't have root access to create a system service.

**(Optional) Set up a systemd user service**
You can configure a systemd user service to manage the AWS IoT Greengrass Core software. This allows the software to start automatically when you log in.

**To set up a systemd user service**

1. Stop the AWS IoT Greengrass Core software if it is currently running.

   ```
   kill $(cat $HOME/greengrass/v2/alts/loader.pid)
   ```

1. Create the systemd user service directory.

   ```
   mkdir -p $HOME/.config/systemd/user
   ```

1. Create the service file at `$HOME/.config/systemd/user/greengrass.service` with the following content.

   ```
   [Unit]
   Description=Greengrass Core

   [Service]
   Type=simple
   PIDFile=%h/greengrass/v2/alts/loader.pid
   RemainAfterExit=no
   Restart=on-failure
   RestartSec=10
   ExecStart=/bin/sh %h/greengrass/v2/alts/current/distro/bin/loader
   Environment="JAVA_HOME={{/path/to/java}}"

   [Install]
   WantedBy=default.target
   ```

   In systemd user unit files, `%h` is a specifier that resolves to the home directory of the user running the service.

   Replace {{/path/to/java}} with the path to your Java installation.

1. Enable and start the service.

   ```
   systemctl --user daemon-reload
   systemctl --user enable greengrass.service
   systemctl --user start greengrass.service
   ```

**Restart and OTA update behavior**
The behavior depends on whether you configured a systemd user service.

With a user service
+ **Device reboot** – The AWS IoT Greengrass Core software starts automatically when the user logs in.
+ **OTA update** – OTA updates succeed and the software restarts automatically.

Without a user service
+ **Device reboot** – The AWS IoT Greengrass Core software does not restart automatically. You must manually start it.
+ **OTA update** – OTA updates succeed, but you must manually start the AWS IoT Greengrass Core software afterward.

**System resource limits**
Per-component resource limits using cgroups do not work in this solution because non-root users cannot create cgroup directories in `/sys/fs/cgroup/`. If you deploy a component with resource limits configured, the AWS IoT Greengrass Core software ignores the configured limits.

You can use the following alternatives to manage resource usage:
+ **Systemd user service limits** – If you run the AWS IoT Greengrass Core software as a systemd user service, you can add resource limits to the service file at `$HOME/.config/systemd/user/greengrass.service`. These limits apply to the entire service, including the Greengrass nucleus and all components.

  ```
  MemoryMax=2G
  CPUQuota=100%
  ```
+ **Greengrass nucleus JVM limits** – You can limit the Greengrass nucleus process memory by configuring JVM options. For more information, see [Configure the AWS IoT Greengrass Core software](configure-greengrass-core-v2.md).

## Solution 2: Set up AWS IoT Greengrass V2 as non-root without component user separation
<a name="non-root-solution-2"></a>

Use this solution when you have root access for initial setup and want the AWS IoT Greengrass Core software to run as a non-root system service, but you don't need to run components as different users. This is similar to Solution 1, but the software runs as a system service that starts automatically on boot.

**Tradeoffs**
This solution has the following limitations:
+ **No component user separation** – All components run as the same user that runs the AWS IoT Greengrass Core software. You cannot use the `posixUser` configuration to run components as different users.
+ **RequiresPrivilege ignored** – The AWS IoT Greengrass Core software ignores the `RequiresPrivilege` option in component recipes. Components cannot request elevated privileges.

**Prerequisites**
This solution requires:
+ Root access for initial setup
+ systemd on your device

**To install and run AWS IoT Greengrass V2 as non-root without component user separation**

1. Complete the following steps from [Install AWS IoT Greengrass Core software with automatic resource provisioning](quick-installation.md): set up your device environment, provide credentials, and download the AWS IoT Greengrass Core software.

1. Create a non-root user that will run the AWS IoT Greengrass Core software and all components.

   ```
   sudo useradd --create-home gg_non_root
   ```

1. Log in as the non-root user and run the installer. Set `--component-default-user` to the same user. Do not use `sudo` and do not set up a system service.

   ```
   java -Droot="/home/gg_non_root/greengrass/v2" -Dlog.store=FILE \
     -jar ./GreengrassInstaller/lib/Greengrass.jar \
     --aws-region {{region}} \
     --thing-name {{MyGreengrassCore}} \
     --thing-group-name {{MyGreengrassCoreGroup}} \
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} \
     --tes-role-name {{GreengrassV2TokenExchangeRole}} \
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} \
     --component-default-user gg_non_root \
     --provision true \
     --setup-system-service false
   ```

1. As root, create the system service file at `/etc/systemd/system/greengrass.service` with the following content.

   ```
   [Unit]
   Description=Greengrass Core
   After=network.target

   [Service]
   Type=simple
   User=gg_non_root
   PIDFile=/home/gg_non_root/greengrass/v2/alts/loader.pid
   RemainAfterExit=no
   Restart=on-failure
   RestartSec=10
   ExecStart=/bin/sh -c "exec /home/gg_non_root/greengrass/v2/alts/current/distro/bin/loader >> /home/gg_non_root/greengrass/v2/logs/loader.log 2>&1"
   KillMode=mixed
   NoNewPrivileges=true
   ProtectSystem=strict
   ReadWritePaths=/home/gg_non_root/greengrass /tmp

   [Install]
   WantedBy=multi-user.target
   ```

1. Stop the running AWS IoT Greengrass Core instance, then enable and start the system service.

   ```
   sudo systemctl daemon-reload
   sudo systemctl enable greengrass.service
   sudo systemctl start greengrass.service
   ```

**Restart and OTA update behavior**
In this solution:
+ The AWS IoT Greengrass Core software runs as a system service and restarts automatically on failure or device reboot.
+ OTA updates to the AWS IoT Greengrass Core software work. The service restarts automatically as the configured non-root user.

**System resource limits**
Per-component resource limits using cgroups do not work in this solution because non-root users without Linux capabilities cannot create cgroup directories in `/sys/fs/cgroup/`. If you deploy a component with resource limits configured, the AWS IoT Greengrass Core software ignores the configured limits.

You can use the following alternatives to manage resource usage:
+ **Systemd service limits** – You can add resource limits to the system service file at `/etc/systemd/system/greengrass.service`. These limits apply to the entire service, including the Greengrass nucleus and all components.

  ```
  MemoryMax=2G
  CPUQuota=100%
  ```
+ **Greengrass nucleus JVM limits** – You can limit the Greengrass nucleus process memory by configuring JVM options. For more information, see [Configure the AWS IoT Greengrass Core software](configure-greengrass-core-v2.md).

## Solution 3: Set up AWS IoT Greengrass V2 as non-root with component user separation
<a name="non-root-solution-3"></a>

Use this solution when you have root access for initial setup but want the AWS IoT Greengrass Core software to run as a non-root user while maintaining the ability to run components as different users. This configuration uses Linux capabilities and sudoers to allow the non-root user to switch to other users when running components.

**Tradeoffs**
This solution has the following limitations:
+ **Requires sudoers configuration** – You must configure sudoers to allow the AWS IoT Greengrass V2 user to run commands as other users.

**Prerequisites**
This solution requires:
+ Root access for initial setup
+ systemd version 229 or later, which supports `AmbientCapabilities`. To check your version, run `systemctl --version`.

**To install and run AWS IoT Greengrass V2 as non-root with component user separation**

1. Complete the following steps from [Install AWS IoT Greengrass Core software with automatic resource provisioning](quick-installation.md): set up your device environment, provide credentials, and download the AWS IoT Greengrass Core software.

1. Create a non-root user that will run the AWS IoT Greengrass Core software.

   ```
   sudo useradd --create-home gg_non_root
   ```

1. Add the non-root user to sudoers so that it can run commands as the component user. Create a file at `/etc/sudoers.d/gg_non_root`.

   ```
   gg_non_root ALL=(ggc_user:ggc_group) NOPASSWD: SETENV: /bin/sh, /bin/bash
   ```

   If you configure components to run as additional users with `posixUser`, add a sudoers entry for each user. For example:

   ```
   gg_non_root ALL=(ggc_user:ggc_group) NOPASSWD: SETENV: /bin/sh, /bin/bash
   gg_non_root ALL=(another_user:another_group) NOPASSWD: SETENV: /bin/sh, /bin/bash
   ```

1. Log in as the non-root user and run the installer. Do not use `sudo` and do not set up a system service.

   ```
   java -Droot="/home/gg_non_root/greengrass/v2" -Dlog.store=FILE \
     -jar ./GreengrassInstaller/lib/Greengrass.jar \
     --aws-region {{region}} \
     --thing-name {{MyGreengrassCore}} \
     --thing-group-name {{MyGreengrassCoreGroup}} \
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} \
     --tes-role-name {{GreengrassV2TokenExchangeRole}} \
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} \
     --component-default-user ggc_user:ggc_group \
     --provision true \
     --setup-system-service false
   ```

1. As root, create the system service file at `/etc/systemd/system/greengrass.service` with the following content.

   ```
   [Unit]
   Description=Greengrass Core
   After=network.target

   [Service]
   Type=simple
   User=gg_non_root
   PIDFile=/home/gg_non_root/greengrass/v2/alts/loader.pid
   RemainAfterExit=no
   Restart=on-failure
   RestartSec=10
   ExecStart=/bin/sh -c "exec /home/gg_non_root/greengrass/v2/alts/current/distro/bin/loader >> /home/gg_non_root/greengrass/v2/logs/loader.log 2>&1"
   KillMode=mixed
   AmbientCapabilities=CAP_CHOWN CAP_DAC_OVERRIDE CAP_DAC_READ_SEARCH CAP_FOWNER CAP_SETUID CAP_SETGID CAP_SYS_RESOURCE CAP_AUDIT_WRITE CAP_SYS_BOOT
   CapabilityBoundingSet=CAP_CHOWN CAP_DAC_OVERRIDE CAP_DAC_READ_SEARCH CAP_FOWNER CAP_SETUID CAP_SETGID CAP_SYS_RESOURCE CAP_AUDIT_WRITE CAP_SYS_BOOT
   ProtectSystem=strict
   ReadWritePaths=/home/gg_non_root/greengrass /tmp

   [Install]
   WantedBy=multi-user.target
   ```

   For information about the required capabilities, see [Linux capabilities required by AWS IoT Greengrass V2](#linux-capabilities-reference).
   + `AmbientCapabilities` grants the specified Linux capabilities to the non-root user running the service. This allows the AWS IoT Greengrass Core software to perform privileged operations such as switching users when running components, without running as root.
   + `CapabilityBoundingSet` limits the maximum set of capabilities that the service and its child processes can use. Capabilities not in this set are permanently dropped.
   + `ProtectSystem=strict` makes the entire file system read-only for the service, preventing modification of the operating system.
   + `ReadWritePaths` specifies the only directories that the service can write to.

1. Stop the running AWS IoT Greengrass Core instance, then enable and start the system service.

   ```
   sudo systemctl daemon-reload
   sudo systemctl enable greengrass.service
   sudo systemctl start greengrass.service
   ```

**Restart and OTA update behavior**
In this solution:
+ The AWS IoT Greengrass Core software runs as a system service and restarts automatically on failure or device reboot.
+ OTA updates to the AWS IoT Greengrass Core software work. The service restarts automatically as the configured non-root user.

**System resource limits**
Per-component resource limits for memory and CPU work in this solution the same way as when running the AWS IoT Greengrass Core software as root.

## Solution 4: Set up AWS IoT Greengrass V2 as root with limited capabilities
<a name="non-root-solution-4"></a>

Use this solution when you want the AWS IoT Greengrass Core software to run as root but with a reduced set of Linux capabilities. This configuration provides the full functionality of running as root while limiting the attack surface by restricting the capabilities available to the software and its components.

**Tradeoffs**
This solution has the following considerations:
+ **Components with RequiresPrivilege have limited capabilities** – Components that use `RequiresPrivilege` run with the same limited set of capabilities as the AWS IoT Greengrass Core software, not full root privileges.

**Prerequisites**
This solution requires:
+ Root access
+ systemd on your device

**To install and run AWS IoT Greengrass V2 as root with limited capabilities**

1. Complete the following steps from [Install AWS IoT Greengrass Core software with automatic resource provisioning](quick-installation.md): set up your device environment, provide credentials, and download the AWS IoT Greengrass Core software.

1. Modify the service template file at `GreengrassInstaller/bin/greengrass.service.template`, in the directory where you downloaded the AWS IoT Greengrass Core software. Add the following lines to the `[Service]` section before you run the installer:

   ```
   CapabilityBoundingSet=CAP_CHOWN CAP_DAC_OVERRIDE CAP_DAC_READ_SEARCH CAP_FOWNER CAP_SETUID CAP_SETGID CAP_SYS_RESOURCE CAP_AUDIT_WRITE CAP_SYS_BOOT
   ProtectSystem=strict
   ReadWritePaths=/greengrass /tmp
   ```
   + `CapabilityBoundingSet` is a systemd security feature that limits the Linux capabilities available to the AWS IoT Greengrass Core software and all of its child processes. By configuring a bounding set, you restrict what the Greengrass nucleus process and components can do, even when running as root. For information about each capability, see [Linux capabilities required by AWS IoT Greengrass V2](#linux-capabilities-reference).
   + `ProtectSystem=strict` makes the entire file system read-only for the service, preventing modification of the operating system. This provides systemd sandboxing that protects system files even if a malicious component runs with elevated privileges.
   + `ReadWritePaths` specifies the only directories that the service can write to. Together with `ProtectSystem=strict`, this limits the service to writing only to the AWS IoT Greengrass V2 root directory and `/tmp`.

1. Run the installer with `--setup-system-service true`.

   ```
   sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE \
     -jar ./GreengrassInstaller/lib/Greengrass.jar \
     --aws-region {{region}} \
     --thing-name {{MyGreengrassCore}} \
     --thing-group-name {{MyGreengrassCoreGroup}} \
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} \
     --tes-role-name {{GreengrassV2TokenExchangeRole}} \
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} \
     --component-default-user ggc_user:ggc_group \
     --provision true \
     --setup-system-service true
   ```

**Restart and OTA update behavior**
In this solution:
+ The AWS IoT Greengrass Core software runs as a system service and restarts automatically on failure or device reboot.
+ OTA updates to the AWS IoT Greengrass Core software work. The software updates and restarts automatically.

**System resource limits**
Per-component resource limits for memory and CPU work in this solution the same way as when running the AWS IoT Greengrass Core software as root.

## Linux capabilities required by AWS IoT Greengrass V2
<a name="linux-capabilities-reference"></a>

The following table describes the Linux capabilities required by the AWS IoT Greengrass Core software when running in non-root configurations. These capabilities are used in Solutions 3 and 4.

**Required Linux capabilities**

| Capability | Description | Required for |
| --- | --- | --- |
| `CAP_CHOWN` | Make arbitrary changes to file UIDs and GIDs | Changing file ownership depending on the user executing the component |
| `CAP_DAC_OVERRIDE` | Bypass file read, write, and execute permission checks | Allowing the Greengrass nucleus user to execute files when used for scripts with `RequiresPrivilege` |
| `CAP_DAC_READ_SEARCH` | Bypass file read permission checks and directory read and execute permission checks | Walking the folder hierarchy even for folders the Greengrass nucleus user does not have permission to read |
| `CAP_FOWNER` | Bypass permission checks on operations that normally require the filesystem UID of the process to match the UID of the file | Bypassing file ownership checks |
| `CAP_SETUID` | Make arbitrary manipulations of process UIDs | Using `sudo` when executing scripts as a different user than the user running the Greengrass nucleus |
| `CAP_SETGID` | Make arbitrary manipulations of process GIDs | Using `sudo` when executing scripts as a different group than the group running the Greengrass nucleus |
| `CAP_SYS_RESOURCE` | Override resource limits | Setting resource limits on component processes, even if limits are not specified in deployments |
| `CAP_AUDIT_WRITE` | Write records to kernel auditing log | Allowing `sudo` to write to the kernel audit log |
| `CAP_SYS_BOOT` | Use `reboot(2)` and `kexec_load(2)` | Allowing the AWS IoT Greengrass Core software to reboot the device when components manage system restarts |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
