---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-integrate-gameclient.html
---

# Integrate Amazon GameLift Servers FleetIQ into a game client
<a name="gsg-integrate-gameclient"></a>

This topic describes the tasks required to prepare your game client or matchmaking service to communicate with Amazon GameLift Servers FleetIQ in order to acquire a game server to host a game session.

Create a method that allows your game client or matchmaker to request a game server resource for players. You have a couple of options for how to do this:
+ Have Amazon GameLift Servers FleetIQ choose an available game server. This option takes advantage of Amazon GameLift Servers FleetIQ optimizations to use low-cost Spot Instances and for automatic scaling.
+ Request all available game servers and select one to use (often referred to as "list and pick").

**Topics**
+ [Let Amazon GameLift Servers FleetIQ choose a game server](gsg-integrate-gameclient-automatic.md)
+ [Choose your own game server](gsg-integrate-gameclient-optimized.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
