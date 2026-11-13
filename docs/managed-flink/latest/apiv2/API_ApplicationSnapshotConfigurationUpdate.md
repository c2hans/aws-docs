---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationSnapshotConfigurationUpdate.html
---

# ApplicationSnapshotConfigurationUpdate
<a name="API_ApplicationSnapshotConfigurationUpdate"></a>

Describes updates to whether snapshots are enabled for a Managed Service for Apache Flink application.

## Contents
<a name="API_ApplicationSnapshotConfigurationUpdate_Contents"></a>

 ** SnapshotsEnabledUpdate **   <a name="APIReference-Type-ApplicationSnapshotConfigurationUpdate-SnapshotsEnabledUpdate"></a>
Describes updates to whether snapshots are enabled for an application.
Type: Boolean
Required: Yes

 ** SnapshotModeUpdate **   <a name="APIReference-Type-ApplicationSnapshotConfigurationUpdate-SnapshotModeUpdate"></a>
Describes updates to the snapshot mode of a Managed Service for Apache Flink application. You can update the snapshot mode from `APPLICATION_SNAPSHOTS_LEGACY` to `ENHANCED_SNAPSHOTS`. You can't use `UpdateApplication` to change the snapshot mode back to `APPLICATION_SNAPSHOTS_LEGACY`.
To return to `APPLICATION_SNAPSHOTS_LEGACY`, use `RollbackApplication`. After you update an application that uses `ENHANCED_SNAPSHOTS`, you can't roll it back to `APPLICATION_SNAPSHOTS_LEGACY`.
To use `ENHANCED_SNAPSHOTS`, the application must use Apache Flink version 1.20 or later.
Type: String
Valid Values: `APPLICATION_SNAPSHOTS_LEGACY | ENHANCED_SNAPSHOTS`
Required: No

## See Also
<a name="API_ApplicationSnapshotConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationSnapshotConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationSnapshotConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationSnapshotConfigurationUpdate)
