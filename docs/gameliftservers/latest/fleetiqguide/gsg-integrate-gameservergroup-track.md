---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameservergroup-track.html
---

# Track game server group instances
<a name="gsg-integrate-gameservergroup-track"></a>

After you create and deploy instances to your game server group and Auto Scaling group, you can track the status of game server instances by calling [DescribeGameServerInstances()](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameServerInstances.html). You can use this operation to track instance status.. For more information on game server group status, see [Life of a game server group](gsg-howitworks-lifecycle-gameservergroup.md).

You can also use the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/), under **Game server groups**, to monitor the status of your game server groups.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
