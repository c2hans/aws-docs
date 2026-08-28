---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameserver-register.html
---

# Register game servers
<a name="gsg-integrate-gameserver-register"></a>

When a game server process is launched and ready to host live gameplay, it must register with Amazon GameLift Servers FleetIQ by calling [RegisterGameServer()](https://docs.aws.amazon.com/gamelift/latest/apireference/API_RegisterGameServer.html). Registering allows Amazon GameLift Servers FleetIQ to respond to matchmaking systems or other client services when they request information on server capacity or claim a game server. When registering, the game server can provide Amazon GameLift Servers FleetIQ with relevant game server data and connection information, including the port and IP address that it uses for inbound client connections.

```
AWS gamelift register-game-server \
    --game-server-id UniqueId-1234 \
    --game-server-group-name MyLiveGroup \
    --instance-id i-1234567890 \
    --connection-info "1.2.3.4:123" \
    --game-server-data "{\"key\": \"value\"}"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
