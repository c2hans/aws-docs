---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp01.html
---

# GAMEPERF07-BP01 Define network latency thresholds for your game
<a name="gameperf07-bp01"></a>

 When developing a multiplayer game, verify that your game infrastructure does not introduce unnecessary latency for players. If your game is sensitive to network latency, then you should set latency thresholds in your matchmaking logic to prioritize placing players on game server sessions that are hosted in nearby game server locations or AWS Regions that meet your objective for ideal player experience.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-61"></a>

 In many latency-sensitive games it is common to instrument the game clients to ping each of the game's infrastructure locations to gather performance data such as network latency, jitter, and packet loss, and report this data to the metrics collection backend so that it can be analyzed. When matching players into game sessions, you can configure your game to incorporate the game client's perceived network latency to your game server infrastructure as one of the inputs used in your matchmaking service logic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
