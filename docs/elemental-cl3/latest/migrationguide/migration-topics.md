---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migration-topics.html
---

# Tasks for migrating an AWS Elemental Conductor Live cluster
<a name="migration-topics"></a>

This section lists the tasks that are part of migrating the nodes in a cluster. The tasks are listed alphabetically.

For information about the correct order for following these tasks, see the procedure for your setup:
+ [Performing a standard cluster migration on an AWS Elemental Conductor Live cluster](migrate-cl-std.md)
+ [Performing a split cluster migration](migrate-cl-split-cluster.md)

**Topics**
+ [Boot mode — UEFI](migrate-topic-uefi.md)
+ [Boot mode — Legacy](migrate-topic-bios.md)
+ [Boot USB drive — create](migrate-topic-create-boot.md)
+ [Cluster — add Conductor](migrate-topic-add-conductor.md)
+ [Cluster — add worker node](migrate-topic-add-w.md)
+ [Cluster — enable HA or disable HA](migrate-topic-disable-ha.md)
+ [Cluster — enable user authentication](migrate-topic-user-auth.md)
+ [Cluster — remove Conductor node](migrate-topic-remove-c-node.md)
+ [Cluster — remove worker node](migrate-topic-remove-worker.md)
+ [Cluster — restart channels](migrate-topic-channel-start.md)
+ [Database — back up](migrate-topic-lifeboat.md)
+ [Database — restore](migrate-topic-restore-database.md)
+ [Conductor Live — install](migrate-topic-install-cl3.md)
+ [Elemental Live — install](migrate-topic-install-worker.md)
+ [Firmware — update](migrate-topic-firmware.md)
+ [RHEL 9 — install](migrate-topic-install-rhel.md)
+ [RPM repository](migrate-topic-rpm-repository.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
