---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-to-nonroot.html
---

# Migrate AWS IoT Greengrass V2 core devices to non-root
<a name="migrate-to-nonroot"></a>

**Important**
This topic describes a recommended migration approach. You might need to adapt these steps for your device configuration, operating system, and installed software.

By default, AWS IoT Greengrass runs as the root user on Linux devices. You can improve the security posture of your devices by migrating AWS IoT Greengrass core devices to run as a non-root user with only the Linux capabilities that AWS IoT Greengrass requires. You can migrate a single device or scale the migration across a fleet.

## Considerations
<a name="migrate-nonroot-considerations"></a>

Consider the following before you migrate to non-root:
+ This migration procedure applies to AWS IoT Greengrass core devices running the AWS IoT Greengrass nucleus (Java-based) on Linux with systemd. It does not apply to devices running AWS IoT Greengrass nucleus lite.
+ Test the migration on a single device in a development environment before you migrate your production fleet.

## Migrate a single device
<a name="migrate-nonroot-single-device"></a>

This migration procedure follows the approach described in [Solution 3: Set up AWS IoT Greengrass V2 as non-root with component user separation](setup-greengrass-non-root.md#non-root-solution-3). Before you begin, complete the prerequisites in that topic, including the sudoers configuration that allows the non-root user to run components as separate users.

Use this procedure to migrate a single device before you migrate your fleet.

### Step 1: Create the non-root user and group
<a name="migrate-nonroot-step1"></a>

Connect to your device and create the system user and group that AWS IoT Greengrass runs as. Replace {{user-name}} and {{group-name}} with the names that you want to use.

```
sudo groupadd --system {{group-name}}
sudo useradd --system --create-home --shell /sbin/nologin -g {{group-name}} {{user-name}}
```

### Step 2: Back up the file ownership
<a name="migrate-nonroot-step2"></a>

Stop AWS IoT Greengrass and save the current file ownership structure so that you can restore it if you need to roll back.

```
sudo systemctl stop greengrass.service
sudo mkdir -p /opt/greengrass-backup
sudo find /greengrass/v2 -exec stat -c 'chown %U:%G "%n"' {} \; | sudo tee /opt/greengrass-backup/restore_ownership.sh > /dev/null
sudo chmod 700 /opt/greengrass-backup/restore_ownership.sh
```

**Note**
The commands in this topic use `/greengrass/v2` as the AWS IoT Greengrass root path. If you installed AWS IoT Greengrass to a different location, replace `/greengrass/v2` with your actual AWS IoT Greengrass root path.

### Step 3: Change file ownership
<a name="migrate-nonroot-step3"></a>

Transfer ownership of the AWS IoT Greengrass directory to the non-root user.

```
sudo chown -R {{user-name}}:{{group-name}} /greengrass/v2
```

### Step 4: Create the systemd drop-in override
<a name="migrate-nonroot-step4"></a>

Create a drop-in directory and configuration file that tells systemd to run AWS IoT Greengrass as the non-root user with the required Linux capabilities.

```
sudo mkdir -p /etc/systemd/system/greengrass.service.d
```

The migration uses a systemd drop-in override file at `/etc/systemd/system/greengrass.service.d/10-nonroot.conf`. A drop-in override replaces settings in the base service file without modifying it directly. This override configures systemd to run the AWS IoT Greengrass service as the non-root user with a limited set of Linux capabilities. Removing the drop-in directory causes systemd to revert to the base `greengrass.service` file, which runs as root with the original configuration.

Create the file `/etc/systemd/system/greengrass.service.d/10-nonroot.conf` with the following content:

```
[Service]
User={{user-name}}
AmbientCapabilities=CAP_CHOWN CAP_DAC_OVERRIDE CAP_DAC_READ_SEARCH CAP_FOWNER CAP_SETUID CAP_SETGID CAP_SYS_RESOURCE CAP_AUDIT_WRITE
CapabilityBoundingSet=CAP_CHOWN CAP_DAC_OVERRIDE CAP_DAC_READ_SEARCH CAP_FOWNER CAP_SETUID CAP_SETGID CAP_SYS_RESOURCE CAP_AUDIT_WRITE
ProtectSystem=strict
ReadWritePaths=/greengrass/v2 /tmp
```

For information about these systemd directives and the required capabilities, see [Solution 3: Set up AWS IoT Greengrass V2 as non-root with component user separation](setup-greengrass-non-root.md#non-root-solution-3).

### Step 5: Reload systemd and start AWS IoT Greengrass
<a name="migrate-nonroot-step5"></a>

Run the following commands to reload the systemd daemon and start AWS IoT Greengrass.

```
sudo systemctl daemon-reload
sudo systemctl start greengrass.service
```

### Step 6: Verify the migration
<a name="migrate-nonroot-step6"></a>

Confirm that AWS IoT Greengrass is running as the non-root user.

```
sudo systemctl status greengrass.service
ps -ef | grep greengrass
```

The output shows the non-root user as the process owner instead of `root`.

Next, confirm that all deployed components are running. You must deploy the `aws.greengrass.Cli` component on the device to run this command.

```
sudo /greengrass/v2/bin/greengrass-cli component list
```

Each component should report a `State` of `RUNNING` or `FINISHED`. `FINISHED` is the expected terminal state for `aws.greengrass.Nucleus`. Investigate any component in the `BROKEN` or `ERRORED` state before you consider the migration complete.

### Roll back a single device
<a name="migrate-nonroot-single-rollback"></a>

If you need to restore AWS IoT Greengrass to run as root, remove the drop-in override, restore file ownership, and restart AWS IoT Greengrass.

```
sudo systemctl stop greengrass.service
sudo rm -rf /etc/systemd/system/greengrass.service.d
sudo bash /opt/greengrass-backup/restore_ownership.sh
sudo systemctl daemon-reload
sudo systemctl start greengrass.service
```

Run the verification commands from [Step 6: Verify the migration](#migrate-nonroot-step6) again to confirm that AWS IoT Greengrass is running as root. The process should show `root` as the owner.

After you confirm the rollback succeeded, you can optionally clean up the migration artifacts:
+ **Backup directory** — You can keep `/opt/greengrass-backup` if you plan to retry the migration later, or remove it:

  ```
  sudo rm -r /opt/greengrass-backup
  ```
+ **Non-root user and group** — If you no longer plan to run AWS IoT Greengrass as a non-root user, you can remove the user and group that you created in Step 1:

  ```
  sudo userdel {{user-name}}
  sudo groupdel {{group-name}}
  ```

  If other services or components use this user, do not remove the user.

## Migrate a fleet of devices
<a name="migrate-nonroot-fleet"></a>

After you verify the migration on a single device, you can scale the migration across your fleet. Choose one of the following methods:
+ [Use a custom AWS IoT Greengrass bootstrap component](#migrate-nonroot-fleet-bootstrap)
+ [Use AWS Systems Manager](#migrate-nonroot-fleet-ssm)

### Use a custom AWS IoT Greengrass bootstrap component
<a name="migrate-nonroot-fleet-bootstrap"></a>

You can create a custom AWS IoT Greengrass component that automates the single-device migration steps across your fleet. This approach is self-contained and uses only AWS IoT Greengrass deployments. It does not require external tools such as Systems Manager.

The component uses the Bootstrap lifecycle with `RequiresPrivilege` set to `true`, which runs the component as root during deployment. The bootstrap script performs the same privileged operations as the single-device procedure:
+ Create the non-root user and group if they do not already exist.
+ Back up the file ownership structure for rollback.
+ Change ownership of the AWS IoT Greengrass root directory to the non-root user.
+ Create the systemd drop-in override file.
+ Reload the systemd daemon.
+ Exit with code 101 to reboot the device.

**Important**
The component must exit with code 101, not 100. Exit code 100 restarts only the AWS IoT Greengrass JVM process, which uses the systemd service configuration already cached in memory. A full reboot forces systemd to read the new drop-in override from disk and start AWS IoT Greengrass as the non-root user. The reboot temporarily disrupts all services on the device.

Make the component idempotent so that redeployments do not fail if you already migrated the device.

After the migration deployment completes, verify that your devices are running as the non-root user. For more information, see [Step 6: Verify the migration](#migrate-nonroot-step6). You can deploy a verification component that checks the running user and reports the result, or monitor the deployment status in the AWS IoT Greengrass console.

#### Set up a rollback mechanism
<a name="migrate-nonroot-fleet-bootstrap-rollback"></a>

To restore the root configuration remotely across your fleet, your migration component must set up a rollback mechanism. One approach is to use systemd to monitor for a trigger file. This approach requires the following systemd resources:
+ A *rollback script* that removes the drop-in override, restores the original file ownership from the backup, reloads the systemd daemon, and restarts AWS IoT Greengrass as root.
+ A systemd *oneshot service* that runs the rollback script as root. A oneshot service runs a single task and then exits, rather than running as a long-lived daemon.
+ A systemd *path unit* that monitors a specific file path, such as `/greengrass/v2/rollback/.rollback-trigger`. When the file appears, the path unit automatically starts the oneshot rollback service.

With this mechanism in place, you can roll back a device by deploying a simple AWS IoT Greengrass component that creates the trigger file. The systemd path unit detects the file, runs the rollback service as root, and restores AWS IoT Greengrass to its original root configuration.

### Use AWS Systems Manager
<a name="migrate-nonroot-fleet-ssm"></a>

If you use Systems Manager to manage your devices, you can create an SSM document that automates the single-device migration steps. Because SSM runs independently of AWS IoT Greengrass, it can stop and restart the AWS IoT Greengrass service directly without rebooting the device.

Your SSM document must meet the following requirements:
+ Stop AWS IoT Greengrass and back up the current service configuration and file ownership structure.
+ Create the non-root user and group.
+ Change ownership of the AWS IoT Greengrass directory to the non-root user.
+ Create the systemd drop-in override file.
+ Reload the systemd daemon and start AWS IoT Greengrass.
+ Verify that AWS IoT Greengrass started successfully as the non-root user.

To run the migration across your fleet, use Systems Manager Run Command to execute the SSM document against your devices using tags or resource groups. You can monitor the command execution status in the Systems Manager console, which shows the result for each target device, including any errors.

To roll back, create a separate SSM document that stops AWS IoT Greengrass, removes the drop-in override, restores the original file ownership, reloads the systemd daemon, and restarts AWS IoT Greengrass as root. Run this document against the devices that you need to roll back.

For more information about running commands on managed nodes, see [Running commands using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html).
