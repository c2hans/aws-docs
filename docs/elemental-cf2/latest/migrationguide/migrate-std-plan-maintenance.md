---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-std-plan-maintenance.html
---

# Plan maintenance windows for migrating an AWS Elemental Conductor File cluster
<a name="migrate-std-plan-maintenance"></a>

You should plan to perform the cluster migration in several phases:

**First phase**

You can perform the tasks in [Step A: Get ready to migrate an AWS Elemental Conductor File cluster](migrate-std-get-ready.md) outside of a maintenance window.

**Second phase**

Perform the following tasks in one or more maintenance windows. The number of windows depends on the number of nodes you can complete in one maintenance window.
+ [Step B: Prepare each AWS Elemental Conductor File node for migration](migrate-std-prepare-node.md)

**Third phase**

Perform all the following tasks on every node, all in one maintenance window.
+ [Step C: Tear down an AWS Elemental Conductor File cluster](migrate-std-decluster.md)
+ [Step D: Create backups](migrate-std-backup.md)
+ [Step F: Rebuild the cluster](migrate-std-rebuild-cluster.md)

These steps upgrade all the nodes at one time. You must perform the upgrade in this way because you can't have a cluster where some nodes are on the previous version of the AWS Elemental software and some are on the new version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
