---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationSnapshotConfiguration.html
---

# ApplicationSnapshotConfiguration
<a name="API_ApplicationSnapshotConfiguration"></a>

Describes whether snapshots are enabled for a Managed Service for Apache Flink application.

## Contents
<a name="API_ApplicationSnapshotConfiguration_Contents"></a>

 ** SnapshotsEnabled **   <a name="APIReference-Type-ApplicationSnapshotConfiguration-SnapshotsEnabled"></a>
Describes whether snapshots are enabled for a Managed Service for Apache Flink application.
Type: Boolean
Required: Yes

 ** SnapshotMode **   <a name="APIReference-Type-ApplicationSnapshotConfiguration-SnapshotMode"></a>
Specifies the snapshot mode for a Managed Service for Apache Flink application. To use enhanced snapshots, specify `ENHANCED_SNAPSHOTS`. If you don't specify this parameter, the application uses `APPLICATION_SNAPSHOTS_LEGACY`. For more information, see [Enhanced Snapshots](https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html).
To use `ENHANCED_SNAPSHOTS`, the application must use Apache Flink version 1.20 or later.
Type: String
Valid Values: `APPLICATION_SNAPSHOTS_LEGACY | ENHANCED_SNAPSHOTS`
Required: No

## See Also
<a name="API_ApplicationSnapshotConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationSnapshotConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationSnapshotConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationSnapshotConfiguration)
