---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableMaintenanceSettings.html
---

# TableMaintenanceSettings
<a name="API_s3Buckets_TableMaintenanceSettings"></a>

Contains details about maintenance settings for the table.

## Contents
<a name="API_s3Buckets_TableMaintenanceSettings_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** icebergCompaction **   <a name="AmazonS3-Type-s3Buckets_TableMaintenanceSettings-icebergCompaction"></a>
Contains details about the Iceberg compaction settings for the table.
Type: [IcebergCompactionSettings](API_s3Buckets_IcebergCompactionSettings.md) object
Required: No

 ** icebergSnapshotManagement **   <a name="AmazonS3-Type-s3Buckets_TableMaintenanceSettings-icebergSnapshotManagement"></a>
Contains details about the Iceberg snapshot management settings for the table.
Type: [IcebergSnapshotManagementSettings](API_s3Buckets_IcebergSnapshotManagementSettings.md) object
Required: No

## See Also
<a name="API_s3Buckets_TableMaintenanceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableMaintenanceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableMaintenanceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableMaintenanceSettings)
