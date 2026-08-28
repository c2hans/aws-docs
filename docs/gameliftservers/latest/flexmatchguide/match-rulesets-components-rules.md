---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-rulesets-components-rules.html
---

# Set rules for player matching
<a name="match-rulesets-components-rules"></a>

Create a set of rule statements that evaluate players for acceptance in to a match. Rules might set requirements that apply to individual players, teams, or an entire match. When Amazon GameLift Servers processes a match request, it starts with the oldest player in the pool of available players and builds a match around that player. For detailed help on creating FlexMatch rules, see [FlexMatch rule types](match-rules-reference-ruletype.md).
+ *name* (required) – A meaningful name that uniquely identifies the rule within a rule set. Rule names are also referenced in event logs and metrics that track activity related to this rule.
+ *description* (optional) – Use this element to attach a free-form text description.
+ *type* (required) – The type element identifies the operation to use when processing the rule. Each rule type requires a set of additional properties. See a list of valid rule types and properties in [FlexMatch rules language](match-rules-reference.md).
+ Rule type property (may be required) – Depending on the type of rule defined, you may need to set certain rule properties. Learn more about properties and how to use the FlexMatch property expression language in [FlexMatch rules language](match-rules-reference.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
