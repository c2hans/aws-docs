---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DataReplicationInfoReplicatedDisk.html
---

# DataReplicationInfoReplicatedDisk
<a name="API_DataReplicationInfoReplicatedDisk"></a>

Request to query disks replicated.

## Contents
<a name="API_DataReplicationInfoReplicatedDisk_Contents"></a>

 ** backloggedStorageBytes **   <a name="mgn-Type-DataReplicationInfoReplicatedDisk-backloggedStorageBytes"></a>
Request to query data replication backlog size in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** deviceName **   <a name="mgn-Type-DataReplicationInfoReplicatedDisk-deviceName"></a>
Request to query device name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** replicatedStorageBytes **   <a name="mgn-Type-DataReplicationInfoReplicatedDisk-replicatedStorageBytes"></a>
Request to query amount of data replicated in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** rescannedStorageBytes **   <a name="mgn-Type-DataReplicationInfoReplicatedDisk-rescannedStorageBytes"></a>
Request to query amount of data rescanned in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** totalStorageBytes **   <a name="mgn-Type-DataReplicationInfoReplicatedDisk-totalStorageBytes"></a>
Request to query total amount of data replicated in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_DataReplicationInfoReplicatedDisk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DataReplicationInfoReplicatedDisk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DataReplicationInfoReplicatedDisk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DataReplicationInfoReplicatedDisk)
