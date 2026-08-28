---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/player-sessions-player-identifiers.html
---

# Generate player IDs
<a name="player-sessions-player-identifiers"></a>

Amazon GameLift Servers uses a player session to represent a player connected to a game session. Amazon GameLift Servers creates a player session each time a player connects to a game session using a game client integrated with Amazon GameLift Servers. When a player leaves a game, the player session ends. Amazon GameLift Servers doesn't reuse player sessions.

**Important**
When using FlexMatch matchmaking, if you create a new matchmaking request that contains a player ID that is already included in an existing active matchmaking request, the existing request is automatically cancelled. However, a `MatchmakingCancelled` event is not sent for the cancelled request. To monitor the status of existing matchmaking requests, use [DescribeMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmaking.html) to poll the request status at infrequent intervals (30-60 seconds). The cancelled request will show a status of `CANCELLED` with the reason `Cancelled due to duplicate player`.

The following code example randomly generates unique player IDs:

```
bool includeBrackets = false;
bool includeDashes = true;
string playerId = AZ::Uuid::CreateRandom().ToString<string>(includeBrackets, includeDashes);
```

For more information about player sessions, see [Game and player sessions in the Amazon GameLift Servers console](gamelift-console-game-player-sessions-metrics.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
