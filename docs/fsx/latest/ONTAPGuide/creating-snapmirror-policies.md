---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-snapmirror-policies.html
---

# Creating a SnapMirror policy

A SnapMirror policy defines how the SnapMirror relationships that use the policy replicate data, including which snapshots to transfer, the maximum number of snapshots to retain on the destination volume, and when to transfer data. If you don't choose a policy when you create a SnapMirror relationship, the relationship uses the `MirrorAllSnapshots` policy. Create a custom policy when you need different retention or a different transfer schedule. You can create a policy on a file system or on a storage virtual machine (SVM). FSx for ONTAP supports only asynchronous SnapMirror policies.

When you create a policy, the snapshot copy mode determines which snapshots SnapMirror transfers to the destination volume.

**Snapshot copy modes**

| Snapshot copy mode | What SnapMirror transfers |
| --- | --- |
| COPY\_ALL\_SOURCE\_SNAPSHOTS | All snapshots of the source volume, on each transfer. |
| COPY\_LATEST\_SOURCE\_SNAPSHOT | The latest snapshot of the source volume, on each transfer. |
| NO\_CREATE\_SNAPSHOT\_ON\_SOURCE | Source snapshots selected by the retention rules. SnapMirror doesn't create a snapshot on the source volume at the beginning of an update or resync. |

Retention rules determine which snapshots SnapMirror retains on the destination volume, based on their SnapMirror labels. Each rule specifies a label and the number of snapshots with that label to retain. For example, a rule with the label `daily` and a count of `7` retains the seven most recent snapshots labeled `daily`. The label must match the SnapMirror label on the source snapshots. You set SnapMirror labels when you create a snapshot or in a snapshot policy. For more information, see [Creating a snapshot](creating-snapshots.md) and [Creating a snapshot policy](creating-snapshot-policies.md). A rule can also specify a creation schedule, which creates snapshots with the label directly on the destination volume.

## To create a SnapMirror policy (AWS Management Console)
<a name="create-a-snapmirror-policy-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, under **ONTAP**, choose **SnapMirror policies**. Then choose **Create SnapMirror policy**.

1. In the **Policy configuration** section, for **Scope**, choose **File system** or **SVM**, and then choose the file system and, if applicable, the SVM. For **Policy name**, enter a name that is unique within the file system.

1. For **Snapshot copy mode**, choose which snapshots SnapMirror transfers. For more information, see the preceding table.

1. Under **Retention rules**, choose **Add rule** for each set of snapshots that you want to retain on the destination volume. For each rule, enter the **Label** and the **Count**. (Optional) To create snapshots directly on the destination volume, choose a **Creation schedule**. Retention rules are required for `NO_CREATE_SNAPSHOT_ON_SOURCE`, and not allowed for `COPY_ALL_SOURCE_SNAPSHOTS` or `COPY_LATEST_SOURCE_SNAPSHOT`.

1. (Optional) Configure the transfer settings:
   + For **Transfer schedule**, choose the ONTAP schedule that determines when SnapMirror transfers data. Leave it empty for on-demand transfers only.
   + To compress data when SnapMirror transfers it over the network, turn on **Enable network compression**. The default is off.
   + For **Throttle (KB/s)**, enter the maximum bandwidth in kilobytes per second. A value of `0` means that the bandwidth is unlimited.

1. (Optional) Under **Tags**, add tags. Then choose **Create SnapMirror policy**.

## To create a SnapMirror policy (AWS CLI)
<a name="create-a-snapmirror-policy-cli"></a>

1. Create a SnapMirror policy by using the **create-snapmirror-policy** command. Specify either `--file-system-id` or `--storage-virtual-machine-id`, but not both.

   ```
   aws fsx create-snapmirror-policy \
        --file-system-id {{fs-0123456789abcdef0}} \
        --name CustomDRPolicy \
        --snapshot-copy-mode NO_CREATE_SNAPSHOT_ON_SOURCE \
        --retention-rules Label=hourly,Count=24 Label=daily,Count=7 Label=weekly,Count=4,CreationSchedule=weekly \
        --transfer-schedule hourly \
        --network-compression-enabled \
        --throttle-in-kbps 0
   ```

1. Use the **describe-snapmirror-policies** command to verify that the policy's `Lifecycle` is `CREATED`.
