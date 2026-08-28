---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/pacemaker-tutorial-setup1.html
---

# Active/passive AWS IoT Greengrass V2 service
<a name="pacemaker-tutorial-setup1"></a>

In this setup, you run AWS IoT Greengrass V2 as a systemd service on one instance at a time. Pacemaker manages the DRBD replication, filesystem mount, and AWS IoT Greengrass V2 service as ordered resources. If the primary instance fails, Pacemaker promotes the standby instance's DRBD to primary, mounts the filesystem, and starts AWS IoT Greengrass V2.

**Important**
Complete all steps in [Prerequisites and cluster setup](pacemaker-tutorial-prerequisites.md) before proceeding.

**Warning**
Run the following commands on the primary instance only, unless otherwise noted.

## Attach the DRBD resource
<a name="pacemaker-tutorial-setup1-drbd-resource"></a>

Verify that Pacemaker is running before proceeding.

```
sudo systemctl status pacemaker
```

Disable STONITH before creating any resources. Without a fencing device configured, Pacemaker will refuse to start resources if STONITH is enabled (the default).

```
sudo pcs property set stonith-enabled=false
```

**Warning**
STONITH is disabled here to simplify this tutorial. In a production environment, you must enable STONITH and configure a fencing agent (for example, `fence_aws` for Amazon EC2 instances) to prevent split-brain and data corruption.

Unmount the DRBD device on the primary instance and bring DRBD down on all instances so that Pacemaker has clean control of the DRBD lifecycle.

```
# On the primary instance only
sudo umount /greengrass/v2

# On all instances
sudo drbdadm down greengrass
```

Create the DRBD resource in Pacemaker.

```
sudo pcs resource create drbd-greengrass \
  ocf:linbit:drbd drbd_resource=greengrass \
  op monitor interval=15s role=Promoted \
  op monitor interval=30s role=Unpromoted
```

Configure the resource as promotable so that only one instance is primary at a time. Set `clone-max` to the number of instances in your cluster.

```
sudo pcs resource promotable drbd-greengrass \
  promoted-max=1 promoted-node-max=1 clone-max=2 clone-node-max=1 notify=true
```

## Attach the filesystem resource
<a name="pacemaker-tutorial-setup1-fs-resource"></a>

All AWS IoT Greengrass V2 resources are stored under `/greengrass/v2`. This step tells Pacemaker to mount the DRBD device at that path on the promoted instance. This ensures the AWS IoT Greengrass V2 data directory is replicated and available during failover.

Create the filesystem resource in a disabled state. You will enable it after all constraints are in place.

```
sudo pcs resource create fs_greengrass Filesystem \
    device="/dev/drbd0" \
    directory="/greengrass/v2" \
    fstype="ext4" \
    op start timeout=15s \
    op stop timeout=15s \
    --disabled
```

## Verify resources
<a name="pacemaker-tutorial-setup1-verify-resources"></a>

Verify that the resources are created and propagated to all instances.

```
sudo pcs status
```

## Provision and attach the AWS IoT Greengrass V2 systemd resource
<a name="pacemaker-tutorial-setup1-greengrass-resource"></a>

1. **Provision AWS IoT Greengrass V2.** Because you unmounted the DRBD device earlier, enable maintenance mode and remount it for provisioning:

   ```
   # Enable maintenance mode to prevent Pacemaker from interfering
   sudo pcs property set maintenance-mode=true

   # Check which node Pacemaker promoted to Primary
   sudo pcs status | grep drbd-greengrass

   # On the Promoted node, mount the DRBD device
   sudo mount /dev/drbd0 /greengrass/v2
   ```

   Provision AWS IoT Greengrass V2 on the primary instance using automatic provisioning. Follow the instructions in [Install AWS IoT Greengrass V2 Core software with automatic resource provisioning](https://docs.aws.amazon.com/greengrass/v2/developerguide/quick-installation.html).

   Ensure that AWS IoT Greengrass V2 is installed to the `/greengrass/v2` directory (the DRBD-mounted path). After provisioning, unmount the device and disable maintenance mode:

   ```
   sudo umount /greengrass/v2
   sudo pcs property set maintenance-mode=false
   ```

1. **Disable the AWS IoT Greengrass V2 service** so that Pacemaker can manage it instead of systemd.

   ```
   sudo systemctl disable greengrass
   sudo systemctl stop greengrass
   ```

1. **Install runtime prerequisites on all standby instances.** AWS IoT Greengrass V2 requires Java and other dependencies that the automatic provisioner installs outside the DRBD-replicated directory. Install the same JDK version on each standby instance. See [AWS IoT Greengrass V2 requirements](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html) for the full list of prerequisites.

1. **Create systemd unit file on other instances.** Copy the AWS IoT Greengrass V2 systemd unit file to the standby instances so that Pacemaker can start the service on any instance during failover.

   ```
   # On the primary instance, view the unit file location
   systemctl show -p FragmentPath greengrass
   ```

   Copy that file to the same path on each other instance. Then reload systemd on each standby instance so it recognizes the new unit file.

   ```
   # On each standby instance
   sudo systemctl daemon-reload
   ```

1. **Attach the AWS IoT Greengrass V2 resource.**

   ```
   sudo pcs resource create greengrass systemd:greengrass \
     op monitor interval=10s \
     op start timeout=60s \
     op stop timeout=60s \
     --disabled
   ```

## Create resource constraints
<a name="pacemaker-tutorial-setup1-constraints"></a>

Create constraint ordering so that Pacemaker manages the resources in the correct order during failover.

```
sudo pcs constraint order promote drbd-greengrass-clone then start fs_greengrass
sudo pcs constraint colocation add fs_greengrass with Promoted drbd-greengrass-clone score=INFINITY
sudo pcs resource group add greengrass-group fs_greengrass greengrass
sudo pcs constraint location greengrass-group prefers {{instance1}}=200
```

Enable the resources now that constraints are in place.

```
sudo pcs resource enable fs_greengrass
sudo pcs resource enable greengrass
```

Verify the final state of the resource constraints.

```
sudo pcs constraint show
```

The output should show the following constraints:
+ **Location Constraints** – The `greengrass-group` resource group prefers the primary instance.
+ **Colocation Constraints** – `fs_greengrass` runs with the promoted `drbd-greengrass-clone`, and `greengrass` runs with `fs_greengrass`.
+ **Order Constraints** – DRBD promotes before the filesystem starts, and the filesystem starts before AWS IoT Greengrass V2.

## Verify failover
<a name="pacemaker-tutorial-setup1-failover"></a>

Simulate a failover to verify that the setup works.

1. **Check the initial state.** Verify that AWS IoT Greengrass V2 is running on the primary instance.

   ```
   sudo pcs status
   ```

1. **Simulate primary instance failure.** Put the primary node in standby mode to trigger resource migration.

   ```
   sudo pcs node standby {{primary-node-name}}
   ```

1. **Verify failover.** On the standby instance, check the cluster status. The DRBD, filesystem, and AWS IoT Greengrass V2 resources should now be running on the standby instance.

   ```
   sudo pcs status
   ```

1. **Recover the failed instance.**

   ```
   sudo pcs node unstandby {{primary-node-name}}
   ```

   When the node is brought back online, it rejoins the cluster as a standby instance. The instance that was promoted during failover remains the primary instance.

**Troubleshooting**
If resources enter a failed state, you can clean up and restart them with the following command.

```
sudo pcs resource cleanup
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
