---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle2postgresql.rollback.html
---

# Rolling Back the Migration
<a name="chap-oracle2postgresql.rollback"></a>

If there are major issues with the migration that cannot be resolved in a timely manner, you can roll back the migration. These steps assume that you have already prepared for the rollback as described in [Step 8: Cut Over to PostgreSQL](chap-rdsoracle2postgresql.steps.cutover.md).

1. Stop all application services on the target PostgreSQL database.

1. Let the AWS DMS task replicate remaining changes back to the source Oracle database.

1. Stop the PostgreSQL to Oracle AWS DMS task.

1. Start all applications back on the source Oracle database.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
