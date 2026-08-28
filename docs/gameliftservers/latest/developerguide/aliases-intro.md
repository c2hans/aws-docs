---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/aliases-intro.html
---

# Abstract an Amazon GameLift Servers fleet designation with an alias
<a name="aliases-intro"></a>

An Amazon GameLift Servers *alias* is used to abstract a hosting destination. Hosting destinations tell Amazon GameLift Servers where to look for available resources to host a new game session for players. Aliases are useful in the following scenarios:
+ If your game doesn't use multi-fleet queues for game session placement, it requests new game sessions by specifying an Amazon GameLift Servers fleet ID. During the life of a game, you'll replace the fleet multiple times, to update a server build, update hosting hardware and operating system, or resolve performance issues. Use an alias to abstract the fleet ID so that you can seamlessly switch player traffic from an existing fleet to the new one.
+ If you want to do something other than create a new game session when a game client requests one. For example, you might want to direct players who are using an out-of-date client to an upgrade website.

An alias must specify a routing strategy. There are two types. A *simple* routing strategy routes player traffic to a specified fleet ID, which you can update to redirect traffic. A *terminal* routing strategy passes a message back to the client instead of creating a new game session. You can change an alias's routing strategy at any time.

If you use a queue for game session placement, you don't need an alias to redirect traffic when replacing a fleet. With a queue, you can simply add the new fleet and remove the old fleet. This action is not visible to players, because new game session requests are automatically fulfilled using the new fleet. It doesn't impact existing game sessions. You can identify queues destinations by using either a fleet ID or alias.

**Topics**
+ [Create an Amazon GameLift Servers alias](aliases-creating.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
