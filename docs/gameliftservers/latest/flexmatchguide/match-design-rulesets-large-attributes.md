---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-rulesets-large-attributes.html
---

# Declare player attributes
<a name="match-design-rulesets-large-attributes"></a>

Make sure that you declare the player attribute that is used as a balancing attribute in the rule set algorithm. This attribute should be included for each player in a matchmaking request. You can provide a default value for the player attribute, but attribute balancing works best when player-specific values are provided.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
