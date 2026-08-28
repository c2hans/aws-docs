---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-std-backup.html
---

# Step D: Create backups
<a name="migrate-std-backup"></a>

Create a backup of the data on every node — the primary Conductor node, the secondary Conductor node, and all the workers.

**Important**
After you make a backup of the first node in the cluster , don't make any changes to any worker node or Conductor node or to cluster until you've finished this migration process. Don't change the setup of the Conductor node, don't create channels, don't create new node assignments for any channel, and so on.

To create database backups, see [Backing up data](migrate-topic-lifeboat.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
