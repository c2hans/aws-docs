---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migration-notes.html
---

# Important notes
<a name="migration-notes"></a>

Following is some key advice about migration.

**Monitor ongoing migration issues**

Before you start the migration, read the [ current Release Notes](https://docs.aws.amazon.com/elemental-live/). The Essential Notes section of the release notes includes topics about recently discovered issues.

For each issue, the release notes initially describe the issue and specify the conditions for continuing with the migration. These issues might affect assets such as the lifeboat script that you use to create a database backup. We can often fix issues without waiting for a new release of the AWS Elemental software.

When an issue is fixed, we either revise the current release notes or include new information in the release notes for the new software release.

**Test in a lab**

We strongly recommend that you test the entire migration procedure in your lab. This strategy lets you test the migration process itself, and test the entire workflow on the new software.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
