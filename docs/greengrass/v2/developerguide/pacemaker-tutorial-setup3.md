---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/pacemaker-tutorial-setup3.html
---

# Active/active AWS IoT Greengrass V2 component
<a name="pacemaker-tutorial-setup3"></a>

In this setup, you manage a AWS IoT Greengrass V2 component with Pacemaker using a custom OCF (Open Cluster Framework) resource agent. This allows Pacemaker to monitor the health of a AWS IoT Greengrass V2 component and trigger recovery actions when the component enters a broken state.

**Important**
Complete all steps in [Prerequisites and cluster setup](pacemaker-tutorial-prerequisites.md) before proceeding, except for the DRBD setup steps. This setup does not use DRBD. Install AWS IoT Greengrass V2 to a local path on each instance instead. AWS IoT Greengrass V2 must be provisioned and running on all instances. This tutorial assumes AWS IoT Greengrass V2 is installed at `/greengrass/v2`. If you chose a different path, update the `GG_CLI` variable in the OCF script accordingly.

## Create a custom OCF resource agent
<a name="pacemaker-tutorial-setup3-ocf-agent"></a>

Create the custom resource agent directory and script on all instances. This example manages a component named `PythonWebServer`.

```
sudo mkdir -p /usr/lib/ocf/resource.d/custom
```

Create the resource agent script at `/usr/lib/ocf/resource.d/custom/gg-webserver` with the following content.

```
#!/bin/bash
# OCF Resource Agent for Greengrass Web Server component
. /usr/lib/ocf/lib/heartbeat/ocf-shellfuncs

GG_CLI="/greengrass/v2/bin/greengrass-cli"
COMPONENT="PythonWebServer"
STATE_FILE="/run/gg-webserver.ocf-state"

case "$1" in
  meta-data)
  cat <<EOF
<?xml version="1.0"?>
<resource-agent name="gg-webserver">
  <version>1.0</version>
  <longdesc lang="en">Greengrass webserver component agent</longdesc>
  <shortdesc lang="en">GG Webserver</shortdesc>
  <parameters>
  </parameters>
  <actions>
    <action name="start" timeout="60"/>
    <action name="stop" timeout="10"/>
    <action name="monitor" timeout="5" interval="10"/>
    <action name="meta-data" timeout="5"/>
  </actions>
</resource-agent>
EOF
;;
  start)
    touch "$STATE_FILE"
    systemctl restart greengrass
    if [ $? -eq 0 ]; then
      exit $OCF_SUCCESS
    else
      rm -f "$STATE_FILE"
      exit $OCF_ERR_GENERIC
    fi
    ;;
  stop)
    rm -f "$STATE_FILE"
    exit $OCF_SUCCESS
    ;;
  monitor)
    # Check state file first — if absent, resource is stopped
    [ ! -f "$STATE_FILE" ] && exit $OCF_NOT_RUNNING
    # Check if the Greengrass service is running
    if ! systemctl is-active --quiet greengrass; then
      exit $OCF_NOT_RUNNING
    fi
    STATE=$($GG_CLI component details -n=$COMPONENT 2>/dev/null | grep '^[[:space:]]*State:' | awk '{print $2}')
    if [[ -z "$STATE" ]]; then
      ocf_log warn "Component $COMPONENT state is empty — component may not be deployed"
      exit $OCF_SUCCESS
    elif [[ "$STATE" == "BROKEN" ]]; then
      exit $OCF_ERR_GENERIC
    else
      exit $OCF_SUCCESS
    fi
    ;;
  *)
    echo "Usage: $0 {start|stop|monitor|meta-data}"
    exit $OCF_ERR_UNIMPLEMENTED
    ;;
esac
```

Make the script executable.

```
sudo chmod +x /usr/lib/ocf/resource.d/custom/gg-webserver
```

**Note**
The `start` action restarts the entire AWS IoT Greengrass V2 service, which restarts all components on the instance, not just `PythonWebServer`. This is the only practical recovery path because AWS IoT Greengrass V2 does not support restarting individual components. The `stop` action is intentionally a no-op because this agent is a monitoring wrapper — the AWS IoT Greengrass V2 service lifecycle is managed by systemd, not by this agent. If a component remains persistently `BROKEN` (for example, due to a bad deployment), Pacemaker will retry up to `migration-threshold` times, then ban the resource on that node until `failure-timeout` expires. You must fix the root cause (for example, redeploy a valid component version) to stop the retry cycle.

## Attach the resource
<a name="pacemaker-tutorial-setup3-attach-resource"></a>

Create the Pacemaker resource using the custom OCF agent.

```
sudo pcs property set stonith-enabled=false
```

**Warning**
STONITH is disabled here to simplify this tutorial. In a production environment, you must enable STONITH and configure a fencing agent (for example, `fence_aws` for Amazon EC2 instances) to prevent split-brain and data corruption.

```
sudo pcs resource create gg-webserver ocf:custom:gg-webserver \
  op monitor interval=30s \
  op start timeout=60s \
  meta migration-threshold=3 failure-timeout=60s \
  clone
```

## Verify recovery
<a name="pacemaker-tutorial-setup3-verify-recovery"></a>

1. **Check the initial state.** Verify that the AWS IoT Greengrass V2 component is running and healthy on all instances.

   ```
   sudo pcs status
   ```

1. **Simulate component failure.** Kill the component's process to simulate a transient failure. AWS IoT Greengrass V2 might attempt internal recovery first. If the component enters a `BROKEN` state, Pacemaker detects it and triggers a service restart. If AWS IoT Greengrass V2 recovers the component internally, Pacemaker takes no action.

   ```
   sudo pkill -f "PythonWebServer"

   # Wait 30-60 seconds, then check the component state
   sudo /greengrass/v2/bin/greengrass-cli component details -n=PythonWebServer
   ```

1. **Verify recovery.** Pacemaker detects that the component is unhealthy and performs recovery steps as defined in the custom OCF script. No failover is needed — Pacemaker restarts the service on the same instance.

   Other services such as HAProxy and AWS IoT Greengrass V2 continue to operate normally on all instances. The application on the standby instances continues to take requests without interruption.

   ```
   sudo pcs status
   ```

   When the recovered instance comes back up, the load balancer identifies it and distributes client requests as needed.
