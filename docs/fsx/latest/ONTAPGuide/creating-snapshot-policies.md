---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-snapshot-policies.html
---

# Creating a snapshot policy

If the built-in snapshot policies don't meet your needs, you can create a custom snapshot policy. A snapshot policy contains up to five schedules. Each schedule specifies when snapshots are created and how many to retain. When the retention count is reached, the oldest snapshot is deleted the next time a snapshot is created. You can create a policy on a file system, where every SVM on the file system can use it, or on a single SVM. After you create a policy, assign it to volumes when you create or update them. For more information, see [Creating volumes](creating-volumes.md) and [Updating volumes](updating-volumes.md).

Each schedule in a policy refers to an existing ONTAP job schedule by name, such as `5min`, `10min`, `hourly`, `3-hourly`, `6-hourly`, `8hour`, `12-hourly`, `daily`, `weekly`, or `monthly`.

**Note**
After you create a snapshot policy, you can enable or disable it, but you can't change its schedules. To use different schedules, create a new policy and assign it to your volumes.

## To create a snapshot policy (console)
<a name="create-a-snapshot-policy-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, under **ONTAP**, choose **Snapshot policies**. Then choose **Create snapshot policy**.

1. In the **Policy details** section, provide the following information:
   + For **Policy name**, enter a name that is unique within its scope. You can use up to 255 alphanumeric, hyphen (-), or underscore (\_) characters.
   + For **Scope**, choose **File system** to let every SVM on the file system use the policy, or **SVM** to create the policy on a single SVM.
   + For **File system ID**, choose the file system. If you chose **SVM**, also choose the SVM.
   + For **Enabled**, keep **Enable policy** turned on to start creating snapshots.

1. In the **Schedules** section, for each schedule, provide the following information. Choose **Add schedule** to add up to five schedules.
   + For **Schedule name**, choose when snapshots are created.
   + For **Count**, enter the maximum number of snapshots to retain for this schedule.
   + (Optional) For **Prefix**, enter a prefix for the snapshot names. The default is the schedule name.
   + (Optional) For **SnapMirror label**, enter the label that SnapMirror policies use to select these snapshots for replication.

1. (Optional) Choose **Add new tag** to add tags to the policy.

1. Choose **Create snapshot policy**.

## To create a snapshot policy (CLI)
<a name="create-a-snapshot-policy-cli"></a>

1. Create a snapshot policy by using the **create-snapshot-policy** command. Specify either `--file-system-id` or `--storage-virtual-machine-id`, but not both. To create the policy on a single SVM, use `--storage-virtual-machine-id` instead of `--file-system-id`.

   ```
   aws fsx create-snapshot-policy \
        --file-system-id {{fs-0123456789abcdef0}} \
        --name nightly-retention-policy \
        --schedules Name=hourly,Count=24,Prefix=hourly Name=daily,Count=7,Prefix=daily,SnapmirrorLabel=daily
   ```

1. Use the **describe-snapshot-policies** command to verify that the policy's `Lifecycle` is `CREATED`. To pause or resume a policy, use the **update-snapshot-policy** command with `--enabled` or `--no-enabled`.
