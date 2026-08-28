---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/pacemaker-tutorial-setup2.html
---

# Active/passive load balancer
<a name="pacemaker-tutorial-setup2"></a>

In this setup, you run HAProxy as a load balancer on one instance at a time. The HAProxy configuration files are stored on DRBD-replicated storage so that when Pacemaker fails over to a standby instance, the configuration is available immediately.

**Important**
Complete all steps in [Prerequisites and cluster setup](pacemaker-tutorial-prerequisites.md) before proceeding.

**Warning**
Run the following commands on the primary instance only, unless otherwise noted.

## Install HAProxy on all instances
<a name="pacemaker-tutorial-setup2-install-haproxy"></a>

Install HAProxy and disable the service so that Pacemaker can manage it. Run this on each instance.

```
sudo apt install -y haproxy
sudo systemctl disable haproxy
sudo systemctl stop haproxy
```

## Configure the DRBD mount for HAProxy
<a name="pacemaker-tutorial-setup2-drbd-mount"></a>

Mount the DRBD device to a directory for the load balancer.

Create the mount point directory. Run this on each instance.

```
sudo mkdir -p /drbd/loadbalancer/
```

Mount the DRBD device on the primary instance. First unmount the previous mount point from the prerequisites.

```
sudo umount /greengrass/v2
sudo mount /dev/drbd0 /drbd/loadbalancer/
```

Verify the mount with `lsblk`. You should see `drbd0` mounted at `/drbd/loadbalancer`.

## Configure HAProxy
<a name="pacemaker-tutorial-setup2-configure-haproxy"></a>

The configuration files must be on the DRBD mount directory so they are replicated to the failover instance.

1. **Copy the HAProxy configuration** to the DRBD mount directory.

   ```
   sudo mkdir -p /drbd/loadbalancer/etc/haproxy/
   sudo cp /etc/haproxy/haproxy.cfg /drbd/loadbalancer/etc/haproxy/haproxy.cfg
   ```

1. **Edit the HAProxy systemd unit file** to use the configuration from the DRBD mount path. Run this on each instance.

   ```
   sudo systemctl edit haproxy
   ```

   Add the following lines to update the configuration file path to the DRBD mount path.

   ```
   [Service]
   Environment="CONFIG=/drbd/loadbalancer/etc/haproxy/haproxy.cfg"
   ```

1. **Reload systemd.** Run this on each instance.

   ```
   sudo systemctl daemon-reload
   ```

## Attach the DRBD resource
<a name="pacemaker-tutorial-setup2-drbd-resource"></a>

Unmount the DRBD device and bring DRBD down so that Pacemaker can manage it. Run the unmount on the primary instance and `drbdadm down` on all instances.

```
# On the primary instance only
sudo umount /drbd/loadbalancer

# On all instances
sudo drbdadm down greengrass
```

```
sudo pcs resource create drbd-greengrass \
  ocf:linbit:drbd drbd_resource=greengrass \
  op monitor interval=15s role=Promoted \
  op monitor interval=30s role=Unpromoted
```

```
sudo pcs resource promotable drbd-greengrass \
  promoted-max=1 promoted-node-max=1 clone-max=2 clone-node-max=1 notify=true
```

## Attach the filesystem resource
<a name="pacemaker-tutorial-setup2-fs-resource"></a>

```
sudo pcs resource create fs_loadbalancer Filesystem \
    device="/dev/drbd0" \
    directory="/drbd/loadbalancer" \
    fstype="ext4" \
    op start timeout=15s \
    op stop timeout=15s \
    --disabled
```

## Attach the HAProxy systemd resource
<a name="pacemaker-tutorial-setup2-haproxy-resource"></a>

```
sudo pcs resource create haproxy systemd:haproxy \
  op monitor interval=10s \
  op start timeout=60s \
  op stop timeout=60s \
  --disabled
```

## Create resource constraints
<a name="pacemaker-tutorial-setup2-constraints"></a>

```
sudo pcs constraint colocation add haproxy with fs_loadbalancer
sudo pcs constraint order fs_loadbalancer then start haproxy
sudo pcs constraint colocation add fs_loadbalancer with Promoted drbd-greengrass-clone
sudo pcs constraint order promote drbd-greengrass-clone then start fs_loadbalancer
```

Enable the resources now that constraints are in place.

```
sudo pcs resource enable fs_loadbalancer
sudo pcs resource enable haproxy
```

Disable STONITH for this tutorial setup.

```
sudo pcs property set stonith-enabled=false
```

**Warning**
STONITH is disabled here to simplify this tutorial. In a production environment, you must enable STONITH and configure a fencing agent (for example, `fence_aws` for Amazon EC2 instances) to prevent split-brain and data corruption.

## Verify failover
<a name="pacemaker-tutorial-setup2-failover"></a>

1. **Check the initial state.** Verify that HAProxy is running on the primary instance.

   ```
   sudo pcs status
   ```

1. **Simulate failover.** Put the primary node in standby mode to force all resources off the primary node.

   ```
   sudo pcs node standby {{primary-node-name}}
   ```

1. **Verify failover.** On the standby instance, check the cluster status. The DRBD, filesystem, and HAProxy resources should now be running on the standby instance with up-to-date configuration files.

   ```
   sudo pcs status
   ```

   When the failed instance recovers, the load balancer service remains on the standby instance unless you configure Pacemaker to migrate it.

1. **Bring the node back online.**

   ```
   sudo pcs node unstandby {{primary-node-name}}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
