---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-snapmirror-relationships.html
---

# Creating a SnapMirror relationship

A SnapMirror relationship replicates data from a source volume to a data protection (DP) destination volume. You create the relationship on the destination file system. The source volume can be on another FSx for ONTAP file system or on an on-premises ONTAP cluster. Before you create a relationship between two clusters, create a cluster peer and an SVM peer. For more information, see [Creating a cluster peer](creating-cluster-peers.md) and [Creating an SVM peer](creating-svm-peers.md).

When you create a relationship, Amazon FSx starts the initial (baseline) transfer automatically. After the baseline transfer, SnapMirror transfers changes on the schedule that you choose.

## To create a SnapMirror relationship (AWS Management Console)
<a name="create-a-snapmirror-relationship-console"></a>

1. Create a DP volume on the destination file system to receive the replicated data. For more information, see [Creating volumes](creating-volumes.md).

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, under **ONTAP**, choose **SnapMirror relationships**.

1. Choose **Create SnapMirror relationship**.

1. In the **Destination** section, for **Destination file system ID**, choose the file system that hosts the destination volume. Then for **Destination volume ID**, choose the DP volume that will receive the replicated data. Only ONTAP volumes in this AWS account and Region can receive replicated data.

1. In the **Source** section, for **Source location**, do one of the following:
   + Choose **In this AWS account** if the source volume is on an FSx for ONTAP file system in the same AWS account. Then choose the **Source file system ID** and the **Source volume ID** from the dropdown menus. Amazon FSx generates the source path from the SVM and volume names.
   + Choose **In another AWS account or on premises** if the source volume is on an FSx for ONTAP file system in a different AWS account or on an on-premises ONTAP cluster. Then enter the source volume's path on the source cluster, in {{svm\_name}}:{{volume\_name}} format.

   If the source volume is on another file system or on an on-premises cluster, a cluster peer and an SVM peer must already exist.

1. (Optional) In the **Replication settings** section, provide the following information:
   + For **SnapMirror policy**, choose the policy that governs which snapshots are replicated and how. The policy must belong to the destination file system. The default is `MirrorAllSnapshots`.
   + For **Transfer schedule**, choose how often to transfer data. The schedule overrides the policy's schedule. Leave it empty for on-demand transfers only.
   + For **Throttle (KB/s)**, enter the maximum transfer rate in KB/s. The default is `0`, which means unlimited.

1. Choose **Create SnapMirror relationship**. Amazon FSx creates the relationship and starts the initial (baseline) transfer. If the required cluster peer or SVM peer doesn't exist, the console shows an error with a link to create it.

## To create a SnapMirror relationship (AWS CLI)
<a name="create-a-snapmirror-relationship-cli"></a>

1. Create a DP volume on the destination SVM by using the **create-volume** command with `OntapVolumeType=DP`. For more information, see [Creating volumes](creating-volumes.md).

1. Create the SnapMirror relationship on the destination file system by using the **create-snapmirror-relationship** command. Specify the source as {{svm\_name}}:{{volume\_name}}.

   ```
   aws fsx create-snapmirror-relationship \
      --source Path=source-svm:source_vol \
      --destination VolumeId={{fsvol-0123456789abcdef0}} \
      --transfer-schedule hourly \
      --throttle-in-kbps 0
   ```

   Amazon FSx creates the relationship and starts the initial (baseline) transfer. Use the **describe-snapmirror-relationships** command to monitor the relationship's `State`, `Healthy`, and `LagTimeInMinutes` values.

## Deleting a SnapMirror relationship
<a name="delete-snapmirror-relationship"></a>

When you delete a SnapMirror relationship, Amazon FSx deletes the relationship on the destination file system and also removes the relationship information and the common snapshot on the source. The destination volume and its data aren't deleted.

**Important**
After you delete a relationship, replicating the volume again requires a full baseline transfer, because the common snapshot is deleted.

### To delete a SnapMirror relationship (AWS Management Console)
<a name="delete-snapmirror-relationship-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, under **ONTAP**, choose **SnapMirror relationships**.

1. Choose the relationship, and then choose **Delete SnapMirror relationship**.

### To delete a SnapMirror relationship (AWS CLI)
<a name="delete-snapmirror-relationship-cli"></a>
+ Use the **delete-snapmirror-relationship** command.

  ```
  aws fsx delete-snapmirror-relationship \
      --snapmirror-relationship-id {{snapmirror-0123456789abcdef0}}
  ```
