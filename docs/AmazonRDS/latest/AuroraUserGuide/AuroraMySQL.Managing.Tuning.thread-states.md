---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Tuning.thread-states.html
---

# Tuning Aurora MySQL with thread states
<a name="AuroraMySQL.Managing.Tuning.thread-states"></a>

The following table summarizes the most common general thread states for Aurora MySQL.

| General thread state | Description |
| --- | --- |
| [creating sort index](ams-states.sort-index.md) | This thread state indicates that a thread is processing a `SELECT` statement that requires the use of an internal temporary table to sort the data. |
| [sending data](ams-states.sending-data.md) | This thread state indicates that a thread is reading and filtering rows for a query to determine the correct result set. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
