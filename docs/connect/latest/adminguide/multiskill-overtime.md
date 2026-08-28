---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/multiskill-overtime.html
---

# Overtime for multi-skill forecast groups
<a name="multiskill-overtime"></a>

Supervisors and Managers can restrict over time slots to specific demand groups.

For information on multi-skill, see [Multi skill scheduling](multiskill-scheduling.md)

## To use the feature
<a name="multiskill-ovetime-use"></a>

Mention the demand group while requesting for overtime. Only agents who are associated with the demand group will be approved for over time slots

![Restrict over time by demand group.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-overtime-multiskill.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
