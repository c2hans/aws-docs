---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/queues-design.html
---

# Customize a game session queue
<a name="queues-design"></a>

This topic describes how to customize your game session queues to make the best possible decisions about game session placement. For more information about game session queues and how they work, see [Configure game session placement](queues-intro.md).

These Amazon GameLift Servers features require queues:
+ [Matchmaking with FlexMatch](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-tasks.html)
+ [Build a queue for Spot Instances](spot-tasks.md)

**Topics**
+ [Define a queue's scope](queues-design-scope.md)
+ [Build a multi-location queue](queues-design-multiregion.md)
+ [Evaluate queue metrics](queues-design-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
