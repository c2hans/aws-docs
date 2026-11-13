---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotInfoDetails.html
---

# SnapshotInfoDetails
<a name="API_SnapshotInfoDetails"></a>

Provides details about an enhanced snapshot.

## Contents
<a name="API_SnapshotInfoDetails_Contents"></a>

 ** SnapshotArn **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotArn"></a>
The ARN of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** SnapshotCreationTimestamp **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotCreationTimestamp"></a>
The timestamp that indicates when the snapshot was created.
Type: Timestamp
Required: Yes

 ** SnapshotFormat **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotFormat"></a>
The format of the snapshot.
Type: String
Valid Values: `CANONICAL`
Required: Yes

 ** SnapshotInitiator **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotInitiator"></a>
Indicates who initiated the snapshot. `USER` indicates a snapshot that you created or imported. `SYSTEM` indicates a snapshot that Managed Service for Apache Flink created.
Type: String
Valid Values: `USER | SYSTEM`
Required: Yes

 ** SnapshotInitiatorOperation **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotInitiatorOperation"></a>
The operation that created the snapshot.
Type: String
Valid Values: `CreateSnapshot | ImportSnapshot | SystemCreateSnapshot`
Required: Yes

 ** SnapshotName **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotName"></a>
The name of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** SnapshotSourceDescription **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotSourceDescription"></a>
Describes the source of the snapshot.
Type: [SnapshotSourceDescription](API_SnapshotSourceDescription.md) object
Required: Yes

 ** SnapshotStatus **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotStatus"></a>
The status of the enhanced snapshot.
Type: String
Valid Values: `CREATING | READY | DELETING | FAILED`
Required: Yes

 ** RuntimeEnvironment **   <a name="APIReference-Type-SnapshotInfoDetails-RuntimeEnvironment"></a>
The Flink runtime of the application that the snapshot was created from. This field is not present for imported snapshots.
Type: String
Valid Values: `SQL-1_0 | FLINK-1_6 | FLINK-1_8 | ZEPPELIN-FLINK-1_0 | FLINK-1_11 | FLINK-1_13 | ZEPPELIN-FLINK-2_0 | FLINK-1_15 | ZEPPELIN-FLINK-3_0 | FLINK-1_18 | FLINK-1_19 | FLINK-1_20 | FLINK-2_2 | FLINK-2_3`
Required: No

 ** SnapshotDescription **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotDescription"></a>
The summary description of the snapshot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[^\u0000-\u001F\u007F]*`
Required: No

 ** SnapshotEncryptionConfigurationDescription **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotEncryptionConfigurationDescription"></a>
Describes the encryption settings of data at rest for the snapshot.
Type: [SnapshotEncryptionConfiguration](API_SnapshotEncryptionConfiguration.md) object
Required: No

 ** SnapshotSizeInBytes **   <a name="APIReference-Type-SnapshotInfoDetails-SnapshotSizeInBytes"></a>
The size of the snapshot, in bytes. The value is `0` until the snapshot status is `READY`.
Type: Long
Required: No

## See Also
<a name="API_SnapshotInfoDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotInfoDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotInfoDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotInfoDetails)
