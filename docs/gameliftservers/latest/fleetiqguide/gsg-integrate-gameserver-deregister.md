---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameserver-deregister.html
---

# Deregister game servers
<a name="gsg-integrate-gameserver-deregister"></a>

When a game concludes, the game server must deregister from Amazon GameLift Servers FleetIQ using [DeregisterGameServer()](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeregisterGameServer.html).

```
AWS gamelift deregister-game-server \
    --game-server-group-name MyLiveGroup \
    --game-server-id UniqueId-1234
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
