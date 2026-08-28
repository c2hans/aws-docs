---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-pitr-recovery.html
---

# Best practices for PITR recovery in DynamoDB
<a name="bp-pitr-recovery"></a>

The following are the best practices for using point-in-time recovery (PITR) to return a table to a previous state.

Use these best practices if you notice mistaken writes to your table that you want to reverse. You can either restore the full table from a point in time, or roll back specific unwanted writes in-place.

**Topics**
+ [Recovery by initiating a table restore](bp-pitr-recovery-table-restore.md)
+ [Recovery by rolling back unwanted writes in-place](bp-pitr-recovery-inplace-rollback.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
