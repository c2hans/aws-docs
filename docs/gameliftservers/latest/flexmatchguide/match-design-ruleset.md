---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-ruleset.html
---

# Design a FlexMatch rule set
<a name="match-design-ruleset"></a>

This topic covers the basic structure of a rule set and how to build a rule set for small matches up to 40 players. A matchmaking rule set does two things: lay out a match's team structure and size and tell the matchmaker how to choose players to form the best possible match.

But your matchmaking rule set can do more. For example, you can:
+ Optimize the matchmaking algorithm for your game.
+ Set up minimum player latency requirements to protect the quality of gameplay.
+ Gradually relax team requirements and match rules over time so all active players can find an acceptable match when they want one.
+ Define handling for group matchmaking requests using party aggregation.
+ Process large matches of 40 or more players. For more information about building large matches, see [Design a FlexMatch large-match rule set](match-design-rulesets-large.md).

When building a matchmaking rule set, consider the following optional and required tasks:
+ [Describe the rule set (required)](match-rulesets-components-set.md)
+ [Customize the match algorithm](match-rulesets-components-algorithm.md)
+ [Declare player attributes](match-rulesets-components-attributes.md)
+ [Define match teams](match-rulesets-components-teams.md)
+ [Set rules for player matching](match-rulesets-components-rules.md)
+ [Allow requirements to relax over time](match-rulesets-components-expansion.md)

You can build your rule set using the Amazon GameLift Servers console or the `[CreateMatchmakingRuleSet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateMatchmakingRuleSet.html)` operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
