---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotOperationInfoDetails.html
---

# SnapshotOperationInfoDetails
<a name="API_SnapshotOperationInfoDetails"></a>

A description of a snapshot operation that provides information about the operation that was performed on an enhanced snapshot.

## Contents
<a name="API_SnapshotOperationInfoDetails_Contents"></a>

 ** SnapshotArn **   <a name="APIReference-Type-SnapshotOperationInfoDetails-SnapshotArn"></a>
The ARN of the enhanced snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** SnapshotOperation **   <a name="APIReference-Type-SnapshotOperationInfoDetails-SnapshotOperation"></a>
The type of operation that was performed on the snapshot.
Type: String
Valid Values: `CreateSnapshot | DeleteSnapshot | ImportSnapshot | ExportSnapshot | SystemCreateSnapshot`
Required: Yes

 ** SnapshotOperationId **   <a name="APIReference-Type-SnapshotOperationInfoDetails-SnapshotOperationId"></a>
The ID of the snapshot operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** SnapshotOperationStatus **   <a name="APIReference-Type-SnapshotOperationInfoDetails-SnapshotOperationStatus"></a>
The status of the snapshot operation.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | CANCELLED`
Required: Yes

 ** ApplicationOperationDescription **   <a name="APIReference-Type-SnapshotOperationInfoDetails-ApplicationOperationDescription"></a>
Describes the application operation that initiated the snapshot operation. This field is present only for `SystemCreateSnapshot` operations.
Type: [ApplicationOperationDescription](API_ApplicationOperationDescription.md) object
Required: No

 ** DestinationEncryptionConfigurationDescription **   <a name="APIReference-Type-SnapshotOperationInfoDetails-DestinationEncryptionConfigurationDescription"></a>
Describes the encryption configuration of the destination data. This field is present only for `ImportSnapshot` and `ExportSnapshot` operations.
Type: [EncryptionConfigurationDescription](API_EncryptionConfigurationDescription.md) object
Required: No

 ** EndTime **   <a name="APIReference-Type-SnapshotOperationInfoDetails-EndTime"></a>
The timestamp that indicates when the operation finished. This field is present only after the operation completes.
Type: Timestamp
Required: No

 ** SnapshotDestinationLocationDescription **   <a name="APIReference-Type-SnapshotOperationInfoDetails-SnapshotDestinationLocationDescription"></a>
Describes the location that the snapshot data was written to. This field is present only for `ExportSnapshot` operations, after the operation completes.
Type: [SnapshotOperationLocationDescription](API_SnapshotOperationLocationDescription.md) object
Required: No

 ** SnapshotOperationFailureDetails **   <a name="APIReference-Type-SnapshotOperationInfoDetails-SnapshotOperationFailureDetails"></a>
Provides a description of the operation failure. This field is present only if `SnapshotOperationStatus` is `FAILED`.
Type: [SnapshotOperationFailureDetails](API_SnapshotOperationFailureDetails.md) object
Required: No

 ** SnapshotSourceLocationDescription **   <a name="APIReference-Type-SnapshotOperationInfoDetails-SnapshotSourceLocationDescription"></a>
Describes the location that the snapshot data was read from. This field is present only for `ImportSnapshot` operations.
Type: [SnapshotOperationLocationDescription](API_SnapshotOperationLocationDescription.md) object
Required: No

 ** SourceEncryptionConfigurationDescription **   <a name="APIReference-Type-SnapshotOperationInfoDetails-SourceEncryptionConfigurationDescription"></a>
Describes the encryption configuration of the source data. This field is present only for `ImportSnapshot` operation.
Type: [EncryptionConfigurationDescription](API_EncryptionConfigurationDescription.md) object
Required: No

 ** StartTime **   <a name="APIReference-Type-SnapshotOperationInfoDetails-StartTime"></a>
The timestamp that indicates when the operation was created.
Type: Timestamp
Required: No

## See Also
<a name="API_SnapshotOperationInfoDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotOperationInfoDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotOperationInfoDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotOperationInfoDetails)
