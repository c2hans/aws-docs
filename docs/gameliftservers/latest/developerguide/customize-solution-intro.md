---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/customize-solution-intro.html
---

# Customize to your game hosting solution
<a name="customize-solution-intro"></a>

With a basic game hosting solution in place, use the following topics to customize and enhance it to improve the player experience, optimize costs, and add advanced functionality. This section covers various customization options organized by the component they primarily affect. Choose the customizations that best fit your game's requirements and player base.

**Topics**
+ [Game server build customizations](customize-game-server-builds.md)
  + [Connect your Amazon GameLift Servers hosted game server to other AWS resources](gamelift-sdk-server-resources.md)
  + [Let your game server access Amazon GameLift Servers fleet data](gamelift-sdk-server-fleetinfo.md)
  + [Set up VPC peering for Amazon GameLift Servers](vpc-peering.md)
+ [Player sessions and matchmaking customizations](customize-player-sessions-matchmaking.md)
  + [Generate player IDs](player-sessions-player-identifiers.md)
  + [Add FlexMatch matchmaking to Amazon GameLift Servers](gamelift-match-intro.md)
+ [Game session placement customizations](customize-game-session-placement.md)
  + [Customize a game session queue](queues-design.md)
  + [Prioritize game session placement](queues-design-priority.md)
  + [Queue configuration examples](queues-examples.md)
  + [Build a queue for Spot Instances](spot-tasks.md)
+ [Hosting resource customizations](fleets-design.md)
  + [Choose compute resources for a managed fleet](gamelift-compute.md)
  + [Customize an Amazon GameLift Servers container fleet](containers-design-fleet.md)
  + [Reduce game hosting costs with Spot fleets](fleets-spot.md)
  + [Optimize game server runtime configuration on managed Amazon GameLift Servers](fleets-multiprocess.md)
  + [Work with the Amazon GameLift Servers Agent](integration-dev-iteration-agent.md)
  + [Abstract an Amazon GameLift Servers fleet designation with an alias](aliases-intro.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
