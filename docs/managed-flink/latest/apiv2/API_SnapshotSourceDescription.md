---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotSourceDescription.html
---

# SnapshotSourceDescription
<a name="API_SnapshotSourceDescription"></a>

Describes the source of an enhanced snapshot. For a snapshot that was created from an application, `SourceApplicationDescription` is present. For an imported snapshot, `S3PrefixLocation` is present.

## Contents
<a name="API_SnapshotSourceDescription_Contents"></a>

 ** S3PrefixLocation **   <a name="APIReference-Type-SnapshotSourceDescription-S3PrefixLocation"></a>
The Amazon S3 location that the snapshot was imported from. This field is present only if `SnapshotInitiatorOperation` is `ImportSnapshot`.
Type: [S3PrefixLocation](API_S3PrefixLocation.md) object
Required: No

 ** SourceApplicationDescription **   <a name="APIReference-Type-SnapshotSourceDescription-SourceApplicationDescription"></a>
Describes the application that the snapshot was created from. This field is not present for imported snapshots.
Type: [SourceApplicationDescription](API_SourceApplicationDescription.md) object
Required: No

## See Also
<a name="API_SnapshotSourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotSourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotSourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotSourceDescription)
