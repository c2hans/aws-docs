---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SnapshotRecycleBinInfo.html
---

# SnapshotRecycleBinInfo
<a name="API_SnapshotRecycleBinInfo"></a>

Information about a snapshot that is currently in the Recycle Bin.

## Contents
<a name="API_SnapshotRecycleBinInfo_Contents"></a>

 ** description **
The description for the snapshot.
Type: String
Required: No

 ** recycleBinEnterTime **
The date and time when the snapshot entered the Recycle Bin.
Type: Timestamp
Required: No

 ** recycleBinExitTime **
The date and time when the snapshot is to be permanently deleted from the Recycle Bin.
Type: Timestamp
Required: No

 ** snapshotId **
The ID of the snapshot.
Type: String
Required: No

 ** volumeId **
The ID of the volume from which the snapshot was created.
Type: String
Required: No

## See Also
<a name="API_SnapshotRecycleBinInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SnapshotRecycleBinInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SnapshotRecycleBinInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SnapshotRecycleBinInfo)
