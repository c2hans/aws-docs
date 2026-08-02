---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-lustreconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem LustreConfiguration
<a name="aws-properties-fsx-filesystem-lustreconfiguration"></a>

The configuration for the Amazon FSx for Lustre file system.

## Syntax
<a name="aws-properties-fsx-filesystem-lustreconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-lustreconfiguration-syntax.json"></a>

```
{
  "[AutoImportPolicy](#cfn-fsx-filesystem-lustreconfiguration-autoimportpolicy)" : {{String}},
  "[AutomaticBackupRetentionDays](#cfn-fsx-filesystem-lustreconfiguration-automaticbackupretentiondays)" : {{Integer}},
  "[CopyTagsToBackups](#cfn-fsx-filesystem-lustreconfiguration-copytagstobackups)" : {{Boolean}},
  "[DailyAutomaticBackupStartTime](#cfn-fsx-filesystem-lustreconfiguration-dailyautomaticbackupstarttime)" : {{String}},
  "[DataCompressionType](#cfn-fsx-filesystem-lustreconfiguration-datacompressiontype)" : {{String}},
  "[DataReadCacheConfiguration](#cfn-fsx-filesystem-lustreconfiguration-datareadcacheconfiguration)" : {{DataReadCacheConfiguration}},
  "[DeploymentType](#cfn-fsx-filesystem-lustreconfiguration-deploymenttype)" : {{String}},
  "[DriveCacheType](#cfn-fsx-filesystem-lustreconfiguration-drivecachetype)" : {{String}},
  "[EfaEnabled](#cfn-fsx-filesystem-lustreconfiguration-efaenabled)" : {{Boolean}},
  "[ExportPath](#cfn-fsx-filesystem-lustreconfiguration-exportpath)" : {{String}},
  "[ImportedFileChunkSize](#cfn-fsx-filesystem-lustreconfiguration-importedfilechunksize)" : {{Integer}},
  "[ImportPath](#cfn-fsx-filesystem-lustreconfiguration-importpath)" : {{String}},
  "[MetadataConfiguration](#cfn-fsx-filesystem-lustreconfiguration-metadataconfiguration)" : {{MetadataConfiguration}},
  "[PerUnitStorageThroughput](#cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput)" : {{Integer}},
  "[ThroughputCapacity](#cfn-fsx-filesystem-lustreconfiguration-throughputcapacity)" : {{Integer}},
  "[WeeklyMaintenanceStartTime](#cfn-fsx-filesystem-lustreconfiguration-weeklymaintenancestarttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-lustreconfiguration-syntax.yaml"></a>

```
  [AutoImportPolicy](#cfn-fsx-filesystem-lustreconfiguration-autoimportpolicy): {{String}}
  [AutomaticBackupRetentionDays](#cfn-fsx-filesystem-lustreconfiguration-automaticbackupretentiondays): {{Integer}}
  [CopyTagsToBackups](#cfn-fsx-filesystem-lustreconfiguration-copytagstobackups): {{Boolean}}
  [DailyAutomaticBackupStartTime](#cfn-fsx-filesystem-lustreconfiguration-dailyautomaticbackupstarttime): {{String}}
  [DataCompressionType](#cfn-fsx-filesystem-lustreconfiguration-datacompressiontype): {{String}}
  [DataReadCacheConfiguration](#cfn-fsx-filesystem-lustreconfiguration-datareadcacheconfiguration): {{
    DataReadCacheConfiguration}}
  [DeploymentType](#cfn-fsx-filesystem-lustreconfiguration-deploymenttype): {{String}}
  [DriveCacheType](#cfn-fsx-filesystem-lustreconfiguration-drivecachetype): {{String}}
  [EfaEnabled](#cfn-fsx-filesystem-lustreconfiguration-efaenabled): {{Boolean}}
  [ExportPath](#cfn-fsx-filesystem-lustreconfiguration-exportpath): {{String}}
  [ImportedFileChunkSize](#cfn-fsx-filesystem-lustreconfiguration-importedfilechunksize): {{Integer}}
  [ImportPath](#cfn-fsx-filesystem-lustreconfiguration-importpath): {{String}}
  [MetadataConfiguration](#cfn-fsx-filesystem-lustreconfiguration-metadataconfiguration): {{
    MetadataConfiguration}}
  [PerUnitStorageThroughput](#cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput): {{Integer}}
  [ThroughputCapacity](#cfn-fsx-filesystem-lustreconfiguration-throughputcapacity): {{Integer}}
  [WeeklyMaintenanceStartTime](#cfn-fsx-filesystem-lustreconfiguration-weeklymaintenancestarttime): {{String}}
```

## Properties
<a name="aws-properties-fsx-filesystem-lustreconfiguration-properties"></a>

`AutoImportPolicy`  <a name="cfn-fsx-filesystem-lustreconfiguration-autoimportpolicy"></a>
 (Optional) When you create your file system, your existing S3 objects appear as file and directory listings. Use this property to choose how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. `AutoImportPolicy` can have the following values:
+ `NONE` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
+ `NEW` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system.
+ `NEW_CHANGED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
+ `NEW_CHANGED_DELETED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.
For more information, see [ Automatically import updates from your S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoimport-data-repo.html).
This parameter is not supported for Lustre file systems with a data repository association.
*Required*: No
*Type*: String
*Allowed values*: `NONE | NEW | NEW_CHANGED | NEW_CHANGED_DELETED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomaticBackupRetentionDays`  <a name="cfn-fsx-filesystem-lustreconfiguration-automaticbackupretentiondays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `0`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `90`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CopyTagsToBackups`  <a name="cfn-fsx-filesystem-lustreconfiguration-copytagstobackups"></a>
(Optional) Not available for use with file systems that are linked to a data repository. A boolean flag indicating whether tags for the file system should be copied to backups. The default value is false. If `CopyTagsToBackups` is set to true, all file system tags are copied to all automatic and user-initiated backups when the user doesn't specify any backup-specific tags. If `CopyTagsToBackups` is set to true and you specify one or more backup tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.
(Default = `false`)
For more information, see [ Working with backups](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html) in the *Amazon FSx for Lustre User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DailyAutomaticBackupStartTime`  <a name="cfn-fsx-filesystem-lustreconfiguration-dailyautomaticbackupstarttime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataCompressionType`  <a name="cfn-fsx-filesystem-lustreconfiguration-datacompressiontype"></a>
Sets the data compression configuration for the file system. `DataCompressionType` can have the following values:
+ `NONE` - (Default) Data compression is turned off when the file system is created.
+ `LZ4` - Data compression is turned on with the LZ4 algorithm.
For more information, see [Lustre data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html) in the *Amazon FSx for Lustre User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `NONE | LZ4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataReadCacheConfiguration`  <a name="cfn-fsx-filesystem-lustreconfiguration-datareadcacheconfiguration"></a>
Specifies the optional provisioned SSD read cache on FSx for Lustre file systems that use the Intelligent-Tiering storage class. Required when `StorageType` is set to `INTELLIGENT_TIERING`.
*Required*: No
*Type*: [DataReadCacheConfiguration](aws-properties-fsx-filesystem-datareadcacheconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentType`  <a name="cfn-fsx-filesystem-lustreconfiguration-deploymenttype"></a>
(Optional) Choose `SCRATCH_1` and `SCRATCH_2` deployment types when you need temporary storage and shorter-term processing of data. The `SCRATCH_2` deployment type provides in-transit encryption of data and higher burst throughput capacity than `SCRATCH_1`.
Choose `PERSISTENT_1` for longer-term storage and for throughput-focused workloads that aren’t latency-sensitive. `PERSISTENT_1` supports encryption of data in transit, and is available in all AWS Regions in which FSx for Lustre is available.
Choose `PERSISTENT_2` for longer-term storage and for latency-sensitive workloads that require the highest levels of IOPS/throughput. `PERSISTENT_2` supports the SSD and Intelligent-Tiering storage classes. You can optionally specify a metadata configuration mode for `PERSISTENT_2` which supports increasing metadata performance. `PERSISTENT_2` is available in a limited number of AWS Regions. For more information, and an up-to-date list of AWS Regions in which `PERSISTENT_2` is available, see [Deployment and storage class options for FSx for Lustre file systems](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html) in the *Amazon FSx for Lustre User Guide*.
If you choose `PERSISTENT_2`, and you set `FileSystemTypeVersion` to `2.10`, the `CreateFileSystem` operation fails.
Encryption of data in transit is automatically turned on when you access `SCRATCH_2`, `PERSISTENT_1`, and `PERSISTENT_2` file systems from Amazon EC2 instances that support automatic encryption in the AWS Regions where they are available. For more information about encryption in transit for FSx for Lustre file systems, see [Encrypting data in transit](https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-in-transit-fsxl.html) in the *Amazon FSx for Lustre User Guide*.
(Default = `SCRATCH_1`)
*Required*: No
*Type*: String
*Allowed values*: `SCRATCH_1 | SCRATCH_2 | PERSISTENT_1 | PERSISTENT_2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DriveCacheType`  <a name="cfn-fsx-filesystem-lustreconfiguration-drivecachetype"></a>
The type of drive cache used by `PERSISTENT_1` file systems that are provisioned with HDD storage devices. This parameter is required when storage type is HDD. Set this property to `READ` to improve the performance for frequently accessed files by caching up to 20% of the total storage capacity of the file system.
This parameter is required when `StorageType` is set to `HDD` and `DeploymentType` is `PERSISTENT_1`.
*Required*: Conditional
*Type*: String
*Allowed values*: `NONE | READ`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EfaEnabled`  <a name="cfn-fsx-filesystem-lustreconfiguration-efaenabled"></a>
(Optional) Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.
(Default = `false`)
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportPath`  <a name="cfn-fsx-filesystem-lustreconfiguration-exportpath"></a>
(Optional) Specifies the path in the Amazon S3 bucket where the root of your Amazon FSx file system is exported. The path must use the same Amazon S3 bucket as specified in ImportPath. You can provide an optional prefix to which new and changed data is to be exported from your Amazon FSx for Lustre file system. If an `ExportPath` value is not provided, Amazon FSx sets a default export path, `s3://import-bucket/FSxLustre[creation-timestamp]`. The timestamp is in UTC format, for example `s3://import-bucket/FSxLustre20181105T222312Z`.
The Amazon S3 export bucket must be the same as the import bucket specified by `ImportPath`. If you specify only a bucket name, such as `s3://import-bucket`, you get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is overwritten on export. If you provide a custom prefix in the export path, such as `s3://import-bucket/[custom-optional-prefix]`, Amazon FSx exports the contents of your file system to that export prefix in the Amazon S3 bucket.
This parameter is not supported for file systems with a data repository association.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`
*Minimum*: `3`
*Maximum*: `4357`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImportedFileChunkSize`  <a name="cfn-fsx-filesystem-lustreconfiguration-importedfilechunksize"></a>
(Optional) For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.
This parameter is not supported for Lustre file systems with a data repository association.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `512000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImportPath`  <a name="cfn-fsx-filesystem-lustreconfiguration-importpath"></a>
(Optional) The path to the Amazon S3 bucket (including the optional prefix) that you're using as the data repository for your Amazon FSx for Lustre file system. The root of your FSx for Lustre file system will be mapped to the root of the Amazon S3 bucket you select. An example is `s3://import-bucket/optional-prefix`. If you specify a prefix after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.
This parameter is not supported for Lustre file systems with a data repository association.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`
*Minimum*: `3`
*Maximum*: `4357`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataConfiguration`  <a name="cfn-fsx-filesystem-lustreconfiguration-metadataconfiguration"></a>
The Lustre metadata performance configuration for the creation of an FSx for Lustre file system using a `PERSISTENT_2` deployment type.
*Required*: No
*Type*: [MetadataConfiguration](aws-properties-fsx-filesystem-metadataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerUnitStorageThroughput`  <a name="cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput"></a>
Required with `PERSISTENT_1` and `PERSISTENT_2` deployment types, provisions the amount of read and write throughput for each 1 tebibyte (TiB) of file system storage capacity, in MB/s/TiB. File system throughput capacity is calculated by multiplying ﬁle system storage capacity (TiB) by the `PerUnitStorageThroughput` (MB/s/TiB). For a 2.4-TiB ﬁle system, provisioning 50 MB/s/TiB of `PerUnitStorageThroughput` yields 120 MB/s of ﬁle system throughput. You pay for the amount of throughput that you provision.
Valid values:
+ For `PERSISTENT_1` SSD storage: 50, 100, 200 MB/s/TiB.
+ For `PERSISTENT_1` HDD storage: 12, 40 MB/s/TiB.
+ For `PERSISTENT_2` SSD storage: 125, 250, 500, 1000 MB/s/TiB.
*Required*: Conditional
*Type*: Integer
*Minimum*: `12`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThroughputCapacity`  <a name="cfn-fsx-filesystem-lustreconfiguration-throughputcapacity"></a>
Specifies the throughput of an FSx for Lustre file system using the Intelligent-Tiering storage class, measured in megabytes per second (MBps). Valid values are 4000 MBps or multiples of 4000 MBps. You pay for the amount of throughput that you provision.
*Required*: No
*Type*: Integer
*Minimum*: `4000`
*Maximum*: `2000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeeklyMaintenanceStartTime`  <a name="cfn-fsx-filesystem-lustreconfiguration-weeklymaintenancestarttime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.
For example, `1:05:00` specifies maintenance at 5 AM Monday.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
