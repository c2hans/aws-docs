---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseSnapshotInfo.html
---

# DatabaseSnapshotInfo
<a name="API_DatabaseSnapshotInfo"></a>

 The structure that describes the snapshot information of a table in source database endpoint that Firehose reads.

Amazon Data Firehose is in preview release and is subject to change.

## Contents
<a name="API_DatabaseSnapshotInfo_Contents"></a>

 ** Id **   <a name="Firehose-Type-DatabaseSnapshotInfo-Id"></a>
 The identifier of the current snapshot of the table in source database endpoint.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: Yes

 ** RequestedBy **   <a name="Firehose-Type-DatabaseSnapshotInfo-RequestedBy"></a>
 The principal that sent the request to take the current snapshot on the table.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Valid Values: `USER | FIREHOSE`
Required: Yes

 ** RequestTimestamp **   <a name="Firehose-Type-DatabaseSnapshotInfo-RequestTimestamp"></a>
 The timestamp when the current snapshot is taken on the table.
Amazon Data Firehose is in preview release and is subject to change.
Type: Timestamp
Required: Yes

 ** Status **   <a name="Firehose-Type-DatabaseSnapshotInfo-Status"></a>
 The status of the current snapshot of the table.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | SUSPENDED`
Required: Yes

 ** Table **   <a name="Firehose-Type-DatabaseSnapshotInfo-Table"></a>
 The fully qualified name of the table in source database endpoint that Firehose reads.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 129.
Pattern: `[\u0001-\uFFFF]*`
Required: Yes

 ** FailureDescription **   <a name="Firehose-Type-DatabaseSnapshotInfo-FailureDescription"></a>
Provides details in case one of the following operations fails due to an error related to KMS: [CreateDeliveryStream](API_CreateDeliveryStream.md), [DeleteDeliveryStream](API_DeleteDeliveryStream.md), [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md), [StopDeliveryStreamEncryption](API_StopDeliveryStreamEncryption.md).
Type: [FailureDescription](API_FailureDescription.md) object
Required: No

## See Also
<a name="API_DatabaseSnapshotInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DatabaseSnapshotInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DatabaseSnapshotInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DatabaseSnapshotInfo)
