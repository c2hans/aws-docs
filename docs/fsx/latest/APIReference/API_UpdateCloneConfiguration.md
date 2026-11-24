---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateCloneConfiguration.html
---

# UpdateCloneConfiguration

Specifies changes to the clone configuration of an FSx for ONTAP volume.

## Contents
<a name="API_UpdateCloneConfiguration_Contents"></a>

 ** SplitAction **   <a name="FSx-Type-UpdateCloneConfiguration-SplitAction"></a>
Set to `START` to split the clone from its parent volume. Splitting copies the data that the clone shares with the parent volume, so that the clone becomes an independent volume that no longer depends on the parent. After the split, the volume uses storage for all of its data.
When you split a clone, keep the following in mind:
+  `SplitAction` must be the only property that you change in the `UpdateVolume` request.
+ You can't split a data protection (`DP`) clone.
+ The split fails if the clone has locked snapshots, such as snapshots that a SnapMirror relationship uses or that a retention period protects, or if a backup of the clone is in progress. To allow the split, Amazon FSx deletes the snapshots that it created for backups of the clone, so the next backup transfers more data. Amazon FSx doesn't delete snapshots that you created.
The split runs in the background. To monitor its progress, use the `VOLUME_CLONE_SPLIT` administrative action in the volume's `AdministrativeActions`. When the split completes, the volume no longer has a `CloneConfiguration`.
Type: String
Valid Values: `START`
Required: No

## See Also
<a name="API_UpdateCloneConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateCloneConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateCloneConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateCloneConfiguration)
