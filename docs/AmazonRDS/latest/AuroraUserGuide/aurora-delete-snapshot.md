---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-delete-snapshot.html
---

# Deleting a DB cluster snapshot
<a name="aurora-delete-snapshot"></a>

You can delete DB cluster snapshots managed by Amazon RDS when you no longer need them.

**Note**
To delete backups managed by AWS Backup, use the AWS Backup console. For information about AWS Backup, see the [*AWS Backup Developer Guide*](https://docs.aws.amazon.com/aws-backup/latest/devguide).

## Deleting a DB cluster snapshot
<a name="DeleteDBClusterSnapshot"></a>

You can delete a DB cluster snapshot using the console, the AWS CLI, or the RDS API.

To delete a shared or public snapshot, you must sign in to the AWS account that owns the snapshot.

### Console
<a name="aurora-delete-snapshot.CON"></a>

**To delete a DB cluster snapshot**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Snapshots**.

1. Choose the DB cluster snapshot that you want to delete.

1. For **Actions**, choose **Delete snapshot**.

1. Choose **Delete** on the confirmation page.

### AWS CLI
<a name="aurora-delete-snapshot.CLI"></a>

You can delete a DB cluster snapshot by using the AWS CLI command [delete-db-cluster-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-cluster-snapshot.html).

The following options are used to delete a DB cluster snapshot.
+ `--db-cluster-snapshot-identifier` – The identifier for the DB cluster snapshot.

**Example**
The following code deletes the `mydbclustersnapshot` DB cluster snapshot.
For Linux, macOS, or Unix:

```
1. aws rds delete-db-cluster-snapshot \
2.     --db-cluster-snapshot-identifier {{mydbclustersnapshot}}
```
For Windows:

```
1. aws rds delete-db-cluster-snapshot ^
2.     --db-cluster-snapshot-identifier {{mydbclustersnapshot}}
```

### RDS API
<a name="aurora-delete-snapshot.API"></a>

You can delete a DB cluster snapshot by using the Amazon RDS API operation [DeleteDBClusterSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterSnapshot.html).

The following parameters are used to delete a DB cluster snapshot.
+ `DBClusterSnapshotIdentifier` – The identifier for the DB cluster snapshot.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
