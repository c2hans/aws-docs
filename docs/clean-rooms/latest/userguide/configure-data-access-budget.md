---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/configure-data-access-budget.html
---

# Configuring a data access budget
<a name="configure-data-access-budget"></a>

A collaborator can view, add, edit, and delete a *data access budget* to set a limit on the number of times a table can be used in queries, PySpark jobs, and ML jobs. Use these budgets to manage data and costs.

Each time a table is queried, a PySpark job is run on the table, or an ML job is run using an ML input channel derived from a table, the budget for that table is reduced by one. When the budget reaches zero, you can't run queries, PySpark jobs, or ML jobs on that table.

You can establish a per period budget that refreshes periodically, a lifetime budget for overall usage, or both. By default, table usage is unlimited.
+ Per period budget – A renewable allocation that limits the amount of times this table can be used within a specified time period. You can set the period to daily, weekly, or monthly. This budget can be set to automatically refresh on a daily, weekly, or monthly basis.
+ Lifetime budget – A running allocation that limits the total amount of times this table can be used.

**Topics**
+ [Adding a data access budget to an existing associated table](add-access-budget-to-existing-associated-table.md)
+ [Viewing a data access budget](view-access-budget.md)
+ [Editing a data access budget](edit-access-budget.md)
+ [Deleting a data access budget](delete-access-budget.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
