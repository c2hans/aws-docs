---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manually-delete-snapshots.html
---

# Deleting snapshots

You can delete a snapshot using the Amazon FSx console, the AWS CLI, the Amazon FSx API, or the ONTAP CLI. You can't delete a snapshot before its expiry time has elapsed, or while a FlexClone volume was created from it.

## To delete a snapshot (console)
<a name="delete-a-snapshot-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, choose **Snapshots**.

1. Choose the snapshot that you want to delete.

1. From **Actions**, choose **Delete snapshot**.

## To delete a snapshot (CLI)
<a name="delete-a-snapshot-cli"></a>
+ Use the [delete-snapshot](https://docs.aws.amazon.com/cli/latest/reference/fsx/delete-snapshot.html) CLI command (or the equivalent [DeleteSnapshot](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteSnapshot.html) API operation), as shown in the following example.

  ```
  aws fsx delete-snapshot --snapshot-id {{fsvolsnap-0123456789abcdef0}}
  ```

To delete snapshots using the ONTAP CLI, use the [**volume snapshot delete**](https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-delete.html) ONTAP CLI command to manually delete snapshots, replacing the following placeholder values with your data:
+ Replace {{`svm_name`}} with the name of the SVM that the volume is created on.
+ Replace {{`vol_name`}} with name of the volume.
+ Replace {{`snapshot_name`}} with the name of the snapshot. This command supports wildcard characters (`*`) for {{`snapshot_name`}}. Therefore, you can delete all hourly snapshots, for example, by using `hourly*`.

**Important**
If you have Amazon FSx backups enabled, Amazon FSx retains a snapshot for the most recent Amazon FSx backup of each volume. Those snapshots are used to maintain incrementality between backups, and must not be deleted by using this method. For more information, see [Viewing the common snapshot](common-snapshot.md).

```
FsxIdabcdef01234567892::> volume snapshot delete -vserver {{svm_name}} -volume {{vol_name}} -snapshot {{snapshot_name}}
```
