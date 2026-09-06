---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_SourceConfiguration.html
---

# SourceConfiguration
<a name="API_SourceConfiguration"></a>

The configuration details for the source used to create an Autonomous Database. This is a union, so only one of the following members can be specified.

## Contents
<a name="API_SourceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloneToRefreshable **   <a name="odb-Type-SourceConfiguration-cloneToRefreshable"></a>
The configuration for creating the Autonomous Database as a refreshable clone.
Type: [CloneToRefreshableConfiguration](API_CloneToRefreshableConfiguration.md) object
Required: No

 ** crossRegionDataGuard **   <a name="odb-Type-SourceConfiguration-crossRegionDataGuard"></a>
The configuration for creating the Autonomous Database as a cross-Region Oracle Data Guard peer.
Type: [CrossRegionDataGuardConfiguration](API_CrossRegionDataGuardConfiguration.md) object
Required: No

 ** crossRegionDisasterRecovery **   <a name="odb-Type-SourceConfiguration-crossRegionDisasterRecovery"></a>
The configuration for creating the Autonomous Database as a cross-Region disaster recovery peer.
Type: [CrossRegionDisasterRecoveryConfiguration](API_CrossRegionDisasterRecoveryConfiguration.md) object
Required: No

 ** databaseClone **   <a name="odb-Type-SourceConfiguration-databaseClone"></a>
The configuration for creating the Autonomous Database as a clone of an existing database.
Type: [DatabaseCloneConfiguration](API_DatabaseCloneConfiguration.md) object
Required: No

 ** pointInTimeRestore **   <a name="odb-Type-SourceConfiguration-pointInTimeRestore"></a>
The configuration for creating the Autonomous Database by restoring to a point in time.
Type: [PointInTimeRestoreConfiguration](API_PointInTimeRestoreConfiguration.md) object
Required: No

 ** restoreFromBackup **   <a name="odb-Type-SourceConfiguration-restoreFromBackup"></a>
The configuration for creating the Autonomous Database by restoring from a backup.
Type: [RestoreFromBackupConfiguration](API_RestoreFromBackupConfiguration.md) object
Required: No

## See Also
<a name="API_SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/SourceConfiguration)
