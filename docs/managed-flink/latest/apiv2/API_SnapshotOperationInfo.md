---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotOperationInfo.html
---

# SnapshotOperationInfo
<a name="API_SnapshotOperationInfo"></a>

Provides summary information about an operation that was performed on an enhanced snapshot.

## Contents
<a name="API_SnapshotOperationInfo_Contents"></a>

 ** SnapshotOperation **   <a name="APIReference-Type-SnapshotOperationInfo-SnapshotOperation"></a>
The type of operation that was performed on the snapshot.
Type: String
Valid Values: `CreateSnapshot | DeleteSnapshot | ImportSnapshot | ExportSnapshot | SystemCreateSnapshot`
Required: Yes

 ** SnapshotOperationId **   <a name="APIReference-Type-SnapshotOperationInfo-SnapshotOperationId"></a>
The ID of the snapshot operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** SnapshotOperationStatus **   <a name="APIReference-Type-SnapshotOperationInfo-SnapshotOperationStatus"></a>
The status of the snapshot operation.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED`
Required: Yes

 ** EndTime **   <a name="APIReference-Type-SnapshotOperationInfo-EndTime"></a>
The timestamp that indicates when the operation finished. This field is present only after the operation completes.
Type: Timestamp
Required: No

 ** StartTime **   <a name="APIReference-Type-SnapshotOperationInfo-StartTime"></a>
The timestamp that indicates when the operation was created.
Type: Timestamp
Required: No

## See Also
<a name="API_SnapshotOperationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotOperationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotOperationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotOperationInfo)
