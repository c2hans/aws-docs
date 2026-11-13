---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotOperationLocationDescription.html
---

# SnapshotOperationLocationDescription
<a name="API_SnapshotOperationLocationDescription"></a>

Describes the location of snapshot data for a snapshot operation.

## Contents
<a name="API_SnapshotOperationLocationDescription_Contents"></a>

 ** LocationType **   <a name="APIReference-Type-SnapshotOperationLocationDescription-LocationType"></a>
The type of the location. The only supported value is `S3`.
Type: String
Valid Values: `S3`
Required: Yes

 ** S3PrefixLocation **   <a name="APIReference-Type-SnapshotOperationLocationDescription-S3PrefixLocation"></a>
Describes the Amazon S3 bucket and key prefix of the location.
Type: [SnapshotOperationS3PrefixLocation](API_SnapshotOperationS3PrefixLocation.md) object
Required: Yes

## See Also
<a name="API_SnapshotOperationLocationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotOperationLocationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotOperationLocationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotOperationLocationDescription)
