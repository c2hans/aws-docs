---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotInfo.html
---

# SnapshotInfo
<a name="API_SnapshotInfo"></a>

Provides summary information about an enhanced snapshot.

## Contents
<a name="API_SnapshotInfo_Contents"></a>

 ** SnapshotArn **   <a name="APIReference-Type-SnapshotInfo-SnapshotArn"></a>
The ARN of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** SnapshotCreationTimestamp **   <a name="APIReference-Type-SnapshotInfo-SnapshotCreationTimestamp"></a>
The timestamp that indicates when the snapshot was created.
Type: Timestamp
Required: Yes

 ** SnapshotFormat **   <a name="APIReference-Type-SnapshotInfo-SnapshotFormat"></a>
The format of the snapshot.
Type: String
Valid Values: `CANONICAL`
Required: Yes

 ** SnapshotInitiator **   <a name="APIReference-Type-SnapshotInfo-SnapshotInitiator"></a>
Indicates who initiated the snapshot. `USER` indicates a snapshot that you created or imported. `SYSTEM` indicates a snapshot that Managed Service for Apache Flink created.
Type: String
Valid Values: `USER | SYSTEM`
Required: Yes

 ** SnapshotInitiatorOperation **   <a name="APIReference-Type-SnapshotInfo-SnapshotInitiatorOperation"></a>
The operation that created the snapshot.
Type: String
Valid Values: `CreateSnapshot | ImportSnapshot | SystemCreateSnapshot`
Required: Yes

 ** SnapshotName **   <a name="APIReference-Type-SnapshotInfo-SnapshotName"></a>
The name of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** SnapshotStatus **   <a name="APIReference-Type-SnapshotInfo-SnapshotStatus"></a>
The status of the enhanced snapshot.
Type: String
Valid Values: `CREATING | READY | DELETING | FAILED`
Required: Yes

 ** SourceApplicationName **   <a name="APIReference-Type-SnapshotInfo-SourceApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_SnapshotInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotInfo)
