---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manually-delete-snapshots.html
---

# Deleting snapshots
<a name="manually-delete-snapshots"></a>

Use the [**volume snapshot delete**](https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-delete.html) ONTAP CLI command to manually delete snapshots, replacing the following placeholder values with your data:
+ Replace {{`svm_name`}} with the name of the SVM that the volume is created on.
+ Replace {{`vol_name`}} with name of the volume.
+ Replace {{`snapshot_name`}} with the name of the snapshot. This command supports wildcard characters (`*`) for {{`snapshot_name`}}. Therefore, you can delete all hourly snapshots, for example, by using `hourly*`.

**Important**
If you have Amazon FSx backups enabled, Amazon FSx retains a snapshot for the most recent Amazon FSx backup of each volume. Those snapshots are used to maintain incrementality between backups, and must not be deleted by using this method. For more information, see [Viewing the common snapshot](common-snapshot.md).

```
FsxIdabcdef01234567892::> volume snapshot delete -vserver {{svm_name}} -volume {{vol_name}} -snapshot {{snapshot_name}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
