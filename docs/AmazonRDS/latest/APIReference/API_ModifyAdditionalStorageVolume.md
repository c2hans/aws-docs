---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyAdditionalStorageVolume.html
---

# ModifyAdditionalStorageVolume
<a name="API_ModifyAdditionalStorageVolume"></a>

Contains details about the modification of an additional storage volume.

## Contents
<a name="API_ModifyAdditionalStorageVolume_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VolumeName **
The name of the additional storage volume that you want to modify.
Valid Values: `RDSDBDATA2 | RDSDBDATA3 | RDSDBDATA4`
Type: String
Required: Yes

 ** AllocatedStorage **
The amount of storage allocated for the additional storage volume, in gibibytes (GiB). The minimum is 20 GiB. The maximum is 65,536 GiB (64 TiB).
Type: Integer
Required: No

 ** IOPS **
The number of I/O operations per second (IOPS) provisioned for the additional storage volume. This setting is only supported for Provisioned IOPS SSD (`io1` and `io2`) storage types.
Type: Integer
Required: No

 ** MaxAllocatedStorage **
The upper limit in gibibytes (GiB) to which RDS can automatically scale the storage of the additional storage volume. You must provide a value greater than or equal to `AllocatedStorage`.
Type: Integer
Required: No

 ** SetForDelete **
Indicates whether to delete the additional storage volume. The value `true` schedules the volume for deletion. You can delete an additional storage volume only when it doesn't contain database files or other data.
Type: Boolean
Required: No

 ** StorageThroughput **
The storage throughput value for the additional storage volume, in mebibytes per second (MiBps). This setting applies only to the General Purpose SSD (`gp3`) storage type.
Type: Integer
Required: No

 ** StorageType **
The new storage type for the additional storage volume.
Valid Values: `GP3 | IO2`
Type: String
Required: No

## See Also
<a name="API_ModifyAdditionalStorageVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyAdditionalStorageVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyAdditionalStorageVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyAdditionalStorageVolume)
