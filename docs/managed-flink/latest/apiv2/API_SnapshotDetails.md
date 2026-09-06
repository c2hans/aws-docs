---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotDetails.html
---

# SnapshotDetails
<a name="API_SnapshotDetails"></a>

Provides details about a snapshot of application state.

## Contents
<a name="API_SnapshotDetails_Contents"></a>

 ** ApplicationVersionId **   <a name="APIReference-Type-SnapshotDetails-ApplicationVersionId"></a>
The current application version ID when the snapshot was created.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** SnapshotName **   <a name="APIReference-Type-SnapshotDetails-SnapshotName"></a>
The identifier for the application snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** SnapshotStatus **   <a name="APIReference-Type-SnapshotDetails-SnapshotStatus"></a>
The status of the application snapshot.
Type: String
Valid Values: `CREATING | READY | DELETING | FAILED`
Required: Yes

 ** ApplicationEncryptionConfigurationDescription **   <a name="APIReference-Type-SnapshotDetails-ApplicationEncryptionConfigurationDescription"></a>
Specifies the encryption settings of data at rest for the application snapshot.
Type: [ApplicationEncryptionConfigurationDescription](API_ApplicationEncryptionConfigurationDescription.md) object
Required: No

 ** RuntimeEnvironment **   <a name="APIReference-Type-SnapshotDetails-RuntimeEnvironment"></a>
The Flink Runtime for the application snapshot.
Type: String
Valid Values: `SQL-1_0 | FLINK-1_6 | FLINK-1_8 | ZEPPELIN-FLINK-1_0 | FLINK-1_11 | FLINK-1_13 | ZEPPELIN-FLINK-2_0 | FLINK-1_15 | ZEPPELIN-FLINK-3_0 | FLINK-1_18 | FLINK-1_19 | FLINK-1_20`
Required: No

 ** SnapshotCreationTimestamp **   <a name="APIReference-Type-SnapshotDetails-SnapshotCreationTimestamp"></a>
The timestamp of the application snapshot.
Type: Timestamp
Required: No

## See Also
<a name="API_SnapshotDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotDetails)
