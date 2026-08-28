---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-delete-snapshot.html
---

# Deleting a Neptune Snapshot
<a name="backup-restore-delete-snapshot"></a>

You can delete a DB snapshot using the AWS Management Console, the AWS CLI, or the Neptune management API:

## Deleting Using the Console
<a name="backup-restore-delete-snapshot-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Snapshots**.

1. Choose the DB snapshot that you want to delete.

1. For **Actions**, choose **Delete Snapshot**.

1. Choose **Delete** on the confirmation page.

## Deleting Using the AWS CLI
<a name="backup-restore-delete-snapshot-cli"></a>

You can also delete a DB snapshot using the AWS CLI [delete\_db\_cluster\_snapshot](api-snapshots.md#DeleteDBClusterSnapshot) command, using the `--db-snapshot-identifier` parameter to identify the snapshot you want to delete:

For Linux, OS X, or Unix:

```
1. aws neptune delete-db-cluster-snapshot \
2.     --db-snapshot-identifier {{<name-of-the-snapshot-to-delete>}}
```

For Windows:

```
1. aws neptune delete-db-cluster-snapshot ^
2.     --db-snapshot-identifier {{<name-of-the-snapshot-to-delete>}}
```

## Deleting Using the Neptune Management API
<a name="backup-restore-delete-snapshot-api"></a>

You can use one of the SDKs to delete a DB snapshot by calling the [DeleteDBClusterSnapshot](api-snapshots.md#DeleteDBClusterSnapshot) API and use the `DBSnapshotIdentifier` parameters to identify the DB snapshot to be deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
