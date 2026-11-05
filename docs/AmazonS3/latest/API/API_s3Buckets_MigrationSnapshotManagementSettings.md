---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationSnapshotManagementSettings.html
---

# MigrationSnapshotManagementSettings
<a name="API_s3Buckets_MigrationSnapshotManagementSettings"></a>

The snapshot management settings that a migration applies to the destination table.

## Contents
<a name="API_s3Buckets_MigrationSnapshotManagementSettings_Contents"></a>

 ** maxSnapshotAgeHours **   <a name="AmazonS3-Type-s3Buckets_MigrationSnapshotManagementSettings-maxSnapshotAgeHours"></a>
The maximum age, in hours, of a snapshot before it can be expired. The default is 120.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

 ** minSnapshotsToKeep **   <a name="AmazonS3-Type-s3Buckets_MigrationSnapshotManagementSettings-minSnapshotsToKeep"></a>
The minimum number of snapshots to keep. The value must be 3 or more. The default is 3.
Type: Integer
Valid Range: Minimum value of 3.
Required: No

## See Also
<a name="API_s3Buckets_MigrationSnapshotManagementSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationSnapshotManagementSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationSnapshotManagementSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationSnapshotManagementSettings)
