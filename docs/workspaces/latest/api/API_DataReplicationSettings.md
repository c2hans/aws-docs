---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DataReplicationSettings.html
---

# DataReplicationSettings
<a name="API_DataReplicationSettings"></a>

Describes the data replication settings.

## Contents
<a name="API_DataReplicationSettings_Contents"></a>

 ** DataReplication **   <a name="WorkSpaces-Type-DataReplicationSettings-DataReplication"></a>
Indicates whether data replication is enabled, and if enabled, the type of data replication.
Type: String
Valid Values: `NO_REPLICATION | PRIMARY_AS_SOURCE`
Required: No

 ** RecoverySnapshotTime **   <a name="WorkSpaces-Type-DataReplicationSettings-RecoverySnapshotTime"></a>
The date and time at which the last successful snapshot was taken of the primary WorkSpace used for replicating data.
Type: Timestamp
Required: No

## See Also
<a name="API_DataReplicationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DataReplicationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DataReplicationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DataReplicationSettings)
