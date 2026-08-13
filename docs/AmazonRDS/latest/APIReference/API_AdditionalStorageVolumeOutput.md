---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AdditionalStorageVolumeOutput.html
---

# AdditionalStorageVolumeOutput
<a name="API_AdditionalStorageVolumeOutput"></a>

Contains information about an additional storage volume for a DB instance.

## Contents
<a name="API_AdditionalStorageVolumeOutput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllocatedStorage **
The amount of storage allocated for the additional storage volume, in gibibytes (GiB). The minimum is 20 GiB. The maximum is 65,536 GiB (64 TiB).
Type: Integer
Required: No

 ** IOPS **
The number of I/O operations per second (IOPS) provisioned for the additional storage volume.
Type: Integer
Required: No

 ** MaxAllocatedStorage **
The upper limit in gibibytes (GiB) to which RDS can automatically scale the storage of the additional storage volume.
Type: Integer
Required: No

 ** StorageOperationPercentProgress **
The percentage of the in-progress storage operation on the additional storage volume that has completed, from `0` to `100`. This field appears only while a storage operation is in progress. It isn't present when no storage operation is active.
Type: Integer
Required: No

 ** StorageOperationStatus **
The status of an in-progress storage operation on the additional storage volume. This field appears only while a storage operation is in progress. It isn't present when no storage operation is active. Possible values:
+  `Initializing` - The volume is initializing from a snapshot, such as during a snapshot restore, point-in-time restore, read replica creation, or blue/green deployment. Performance can be lower than provisioned until initialization completes.
+  `Optimizing` - The volume is optimizing following a storage scaling or modification operation.
Type: String
Required: No

 ** StorageThroughput **
The storage throughput value for the additional storage volume, in mebibytes per second (MiBps).
Type: Integer
Required: No

 ** StorageType **
The storage type for the additional storage volume.
Valid Values: `GP3 | IO2`
Type: String
Required: No

 ** StorageVolumeStatus **
The status of the additional storage volume.
Valid Values: `ACTIVE | CREATING | DELETING | MODIFYING | NOT-IN-USE | STORAGE-OPTIMIZATION | VOLUME-FULL`
Type: String
Required: No

 ** VolumeName **
The name of the additional storage volume.
Type: String
Required: No

## See Also
<a name="API_AdditionalStorageVolumeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/AdditionalStorageVolumeOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/AdditionalStorageVolumeOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/AdditionalStorageVolumeOutput)
