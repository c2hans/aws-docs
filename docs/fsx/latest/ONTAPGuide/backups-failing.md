---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/backups-failing.html
---

# Your backups fail due to insufficient volume capacity
<a name="backups-failing"></a>

Automatic daily backups of your volume fails with the following message:

```
Amazon FSx could not create a backup of your volume because the backup snapshot was deleted.
```

Automatic daily backups are failing because there is insufficient free storage capacity on the volume. To mitigate this condition, you will need to free up storage capacity on the volume. You can accomplish this using one or more of the following options, depending on your situation:
+ [Increase the volume's storage capacity](manage-volume-capacity.md#increase-volume-size)
+ [Increase the volume's snapshot reserve](snapshots-ontap.md#snapshot-reserve)
+ [Disable snapshot auto-delete](snapshot-autodelete-policy.md)
+ [Don't delete the backup-snapshot](common-snapshot.md) using the ONTAP CLI

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
