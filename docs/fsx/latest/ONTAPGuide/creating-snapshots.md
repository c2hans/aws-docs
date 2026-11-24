---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-snapshots.html
---

# Creating a snapshot

In addition to the snapshots that a snapshot policy creates automatically, you can create a snapshot of a volume at any time, for example before an application upgrade. When you create a snapshot, you can optionally set the following:
+ *SnapMirror label* – A label that SnapMirror policies use to select the snapshot for replication. The label must match a retention rule label in the SnapMirror policy. For more information, see [Creating a SnapMirror policy](creating-snapmirror-policies.md).
+ *Expiry time* – The date and time until which the snapshot is retained. You can't delete the snapshot until this time has elapsed. You can extend, shorten, or clear the expiry time later by updating the snapshot.

## To create a snapshot (console)
<a name="create-a-snapshot-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, choose **Snapshots**. Then choose **Create snapshot**.

1. In the **Snapshot details** section, for **File system**, choose the file system that holds the volume, and for **Volume**, choose the volume that you want to take a snapshot of.

1. For **Snapshot name**, enter a name for the snapshot. The name must be unique within the volume.

1. (Optional) For **SnapMirror label**, enter the label that a SnapMirror policy uses to select this snapshot for replication.

1. (Optional) For **Expiry time**, enter the **Date** (YYYY/MM/DD) and **Time** (hh:mm:ss, 24-hour) until which the snapshot is retained.

1. (Optional) Choose **Add new tag** to add tags to the snapshot.

1. Choose **Create snapshot**.

The snapshot is ready for use when its status is **Available**.

## To create a snapshot (CLI)
<a name="create-a-snapshot-cli"></a>

1. To create an FSx for ONTAP snapshot, use the [create-snapshot](https://docs.aws.amazon.com/cli/latest/reference/fsx/create-snapshot.html) CLI command (or the equivalent [CreateSnapshot](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateSnapshot.html) API operation), as shown in the following example. The `--ontap-configuration` parameter is optional.

   ```
   aws fsx create-snapshot \
        --volume-id {{fsvol-0123456789abcdef0}} \
        --name pre-upgrade-snap \
        --ontap-configuration SnapmirrorLabel=daily,ExpiryTime=2026-12-31T23:00:00Z
   ```

1. Use the [describe-snapshots](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-snapshots.html) CLI command to verify that the snapshot's `Lifecycle` is `AVAILABLE`. If the snapshot can't be created, its `Lifecycle` is `FAILED` and `LifecycleTransitionReason` contains the error from ONTAP.
