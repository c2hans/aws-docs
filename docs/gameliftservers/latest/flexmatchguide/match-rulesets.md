---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets.html
---

# Build a FlexMatch rule set
<a name="match-rulesets"></a>

Every FlexMatch matchmaker must have a rule set. The rule set determines the two key elements of a match: your game's team structure and size, and how to group players together for the best possible match.

For example, a rule set might describe a match like this: Create a match with two teams of five players each, one team is the defenders and the other team the invaders. A team can have novice and experienced players, but the average skill of the two teams must be within 10 points of each other. If no match is made after 30 seconds, gradually relax the skill requirements.

The topics in this section describe how design and build a matchmaking rule set. When creating a rule set, you can use either the Amazon GameLift Servers console or the AWS CLI.

**Topics**
+ [Design a FlexMatch rule set](match-design-ruleset.md)
+ [Design a FlexMatch large-match rule set](match-design-rulesets-large.md)
+ [Tutorial: Create a matchmaking rule set](match-create-ruleset.md)
+ [FlexMatch rule set examples](match-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
