---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationInfoReplicatedDisk.html
---

# DataReplicationInfoReplicatedDisk
<a name="API_DataReplicationInfoReplicatedDisk"></a>

A disk that should be replicated.

## Contents
<a name="API_DataReplicationInfoReplicatedDisk_Contents"></a>

 ** backloggedStorageBytes **   <a name="drs-Type-DataReplicationInfoReplicatedDisk-backloggedStorageBytes"></a>
The size of the replication backlog in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** deviceName **   <a name="drs-Type-DataReplicationInfoReplicatedDisk-deviceName"></a>
The name of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** replicatedStorageBytes **   <a name="drs-Type-DataReplicationInfoReplicatedDisk-replicatedStorageBytes"></a>
The amount of data replicated so far in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** rescannedStorageBytes **   <a name="drs-Type-DataReplicationInfoReplicatedDisk-rescannedStorageBytes"></a>
The amount of data to be rescanned in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** totalStorageBytes **   <a name="drs-Type-DataReplicationInfoReplicatedDisk-totalStorageBytes"></a>
The total amount of data to be replicated in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** volumeStatus **   <a name="drs-Type-DataReplicationInfoReplicatedDisk-volumeStatus"></a>
The status of the volume.
Type: String
Valid Values: `REGULAR | CONTAINS_MARKETPLACE_PRODUCT_CODES | MISSING_VOLUME_ATTRIBUTES | MISSING_VOLUME_ATTRIBUTES_AND_PRECHECK_UNAVAILABLE | PENDING`
Required: No

## See Also
<a name="API_DataReplicationInfoReplicatedDisk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DataReplicationInfoReplicatedDisk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DataReplicationInfoReplicatedDisk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DataReplicationInfoReplicatedDisk)
