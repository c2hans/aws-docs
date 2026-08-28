---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/multiskill-shiftexchange.html
---

# Shift exchange for multi-skill forecast groups
<a name="multiskill-shiftexchange"></a>

Shift exchanges can be allowed between agents regardless of demand group associations. This feature is disabled by default, allowing agents to only trade shifts with other agents who have identical demand group associations. When enabled, agents can exchange shifts with others regardless of demand group assignments.

For information on multi-skill, see [Multi skill scheduling](multiskill-scheduling.md)

## To enable shift exchange regardless of demand groups
<a name="multiskill-shiftexchange-enable"></a>

Check the option to enable cross demand group trade.

![Restrict shift exchange by demand group.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shiftexchange-multiskill.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
