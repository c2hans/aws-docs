---
source_url: https://docs.aws.amazon.com/dcv/latest/access-console/managing-component-process.html
---

# Managing the component processes
<a name="managing-component-process"></a>

The Amazon DCV Access Console components, such as Authentication Server, Handler, Web Client, run while processes on their hosts and can be managed using the command `systemctl`. You can use this command to:
+ Check the status of a component
+ Stop a component
+ Start a component
+ Restart a component

If your components are running on separate hosts, then each command must be executed on each corresponding host.

## Checking status of the components
<a name="checking-status-components"></a>

To check the statuses of the components, run the following commands on the hosts that the components are installed on.

```
sudo systemctl status dcv-access-console-auth-server
sudo systemctl status dcv-access-console-handler
sudo systemctl status dcv-access-console-webclient
```

## Stopping the components
<a name="stopping-components"></a>

To stop the component processes, run the following commands on the hosts that the components are installed on.

```
sudo systemctl stop dcv-access-console-auth-server
sudo systemctl stop dcv-access-console-handler
sudo systemctl stop dcv-access-console-webclient
```

## Starting the components
<a name="starting-components"></a>

To start the component processes, run the following commands on the hosts that the components are installed on.

```
sudo systemctl start dcv-access-console-auth-server
sudo systemctl start dcv-access-console-handler
sudo systemctl start dcv-access-console-webclient
```

## Restarting the components
<a name="restarting-components"></a>

To restart the component processes, run the following commands on the hosts that the components are installed on.

```
sudo systemctl restart dcv-access-console-auth-server
sudo systemctl restart dcv-access-console-handler
sudo systemctl restart dcv-access-console-webclient
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
