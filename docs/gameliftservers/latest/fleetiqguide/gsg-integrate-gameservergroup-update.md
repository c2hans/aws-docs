---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameservergroup-update.html
---

# Update a game server group
<a name="gsg-integrate-gameservergroup-update"></a>

You can update game server group properties that affect how Amazon GameLift Servers FleetIQ manages hosting for game servers, including resource type optimizations. To update these properties, call [UpdateGameServerGroup()](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameServerGroup.html). After the changes to the game server group take effect, Amazon GameLift Servers FleetIQ may overwrite certain properties in the Auto Scaling group.

For all other Auto Scaling group properties, such as `MinSize`, `MaxSize`, and `LaunchTemplate`, you can modify these directly on the Auto Scaling group.

In the example below, the instance type definitions are updated to switch over to c4.xlarge and c5.xlarge instances types.

```
AWS gamelift update-game-server-group \
    --game-server-group-name MyLiveGroup \
    --instance-definitions '[{"InstanceType": "c4.xlarge"}, {"InstanceType": "c5.xlarge"}]'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
