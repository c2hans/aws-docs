---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_OrderableDBInstanceOption.html
---

# OrderableDBInstanceOption
<a name="API_OrderableDBInstanceOption"></a>

Contains a list of available options for a DB instance.

This data type is used as a response element in the `DescribeOrderableDBInstanceOptions` action.

## Contents
<a name="API_OrderableDBInstanceOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityZoneGroup **
The Availability Zone group for a DB instance.
Type: String
Required: No

 ** AvailabilityZones.AvailabilityZone.N **
A list of Availability Zones for a DB instance.
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects
Required: No

 ** AvailableAdditionalStorageVolumesOptions.AvailableAdditionalStorageVolumesOption.N **
The available options for additional storage volumes for the DB instance class.
Type: Array of [AvailableAdditionalStorageVolumesOption](API_AvailableAdditionalStorageVolumesOption.md) objects
Required: No

 ** AvailableProcessorFeatures.AvailableProcessorFeature.N **
A list of the available processor features for the DB instance class of a DB instance.
Type: Array of [AvailableProcessorFeature](API_AvailableProcessorFeature.md) objects
Required: No

 ** DBInstanceClass **
The DB instance class for a DB instance.
Type: String
Required: No

 ** Engine **
The engine type of a DB instance.
Type: String
Required: No

 ** EngineVersion **
The engine version of a DB instance.
Type: String
Required: No

 ** LicenseModel **
The license model for a DB instance.
Type: String
Required: No

 ** MaxIopsPerDbInstance **
Maximum total provisioned IOPS for a DB instance.
Type: Integer
Required: No

 ** MaxIopsPerGib **
Maximum provisioned IOPS per GiB for a DB instance.
Type: Double
Required: No

 ** MaxStorageSize **
Maximum storage size for a DB instance.
Type: Integer
Required: No

 ** MaxStorageThroughputPerDbInstance **
Maximum storage throughput for a DB instance.
Type: Integer
Required: No

 ** MaxStorageThroughputPerIops **
Maximum storage throughput to provisioned IOPS ratio for a DB instance.
Type: Double
Required: No

 ** MinIopsPerDbInstance **
Minimum total provisioned IOPS for a DB instance.
Type: Integer
Required: No

 ** MinIopsPerGib **
Minimum provisioned IOPS per GiB for a DB instance.
Type: Double
Required: No

 ** MinStorageSize **
Minimum storage size for a DB instance.
Type: Integer
Required: No

 ** MinStorageThroughputPerDbInstance **
Minimum storage throughput for a DB instance.
Type: Integer
Required: No

 ** MinStorageThroughputPerIops **
Minimum storage throughput to provisioned IOPS ratio for a DB instance.
Type: Double
Required: No

 ** MultiAZCapable **
Indicates whether a DB instance is Multi-AZ capable.
Type: Boolean
Required: No

 ** OutpostCapable **
Indicates whether a DB instance supports RDS on Outposts.
For more information about RDS on Outposts, see [Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide.*
Type: Boolean
Required: No

 ** ReadReplicaCapable **
Indicates whether a DB instance can have a read replica.
Type: Boolean
Required: No

 ** StorageType **
The storage type for a DB instance.
Type: String
Required: No

 ** SupportedActivityStreamModes.member.N **
The list of supported modes for Database Activity Streams. Aurora PostgreSQL returns the value `[sync, async]`. Aurora MySQL and RDS for Oracle return `[async]` only. If Database Activity Streams isn't supported, the return value is an empty list.
Type: Array of strings
Required: No

 ** SupportedEngineModes.member.N **
A list of the supported DB engine modes.
Type: Array of strings
Required: No

 ** SupportedNetworkTypes.member.N **
The network types supported by the DB instance (`IPV4` or `DUAL`).
A DB instance can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*
Type: Array of strings
Required: No

 ** SupportsAdditionalStorageVolumes **
Indicates whether the DB instance class supports additional storage volumes.
Type: Boolean
Required: No

 ** SupportsClusters **
Indicates whether DB instances can be configured as a Multi-AZ DB cluster.
For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*
Type: Boolean
Required: No

 ** SupportsDedicatedLogVolume **
Indicates whether a DB instance supports using a dedicated log volume (DLV).
Type: Boolean
Required: No

 ** SupportsEnhancedMonitoring **
Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.
Type: Boolean
Required: No

 ** SupportsGlobalDatabases **
Indicates whether you can use Aurora global databases with a specific combination of other DB engine attributes.
Type: Boolean
Required: No

 ** SupportsHttpEndpoint **
Indicates whether a DB instance supports HTTP endpoints.
Type: Boolean
Required: No

 ** SupportsIAMDatabaseAuthentication **
Indicates whether a DB instance supports IAM database authentication.
Type: Boolean
Required: No

 ** SupportsIops **
Indicates whether a DB instance supports provisioned IOPS.
Type: Boolean
Required: No

 ** SupportsKerberosAuthentication **
Indicates whether a DB instance supports Kerberos Authentication.
Type: Boolean
Required: No

 ** SupportsPerformanceInsights **
Indicates whether a DB instance supports Performance Insights.
Type: Boolean
Required: No

 ** SupportsStorageAutoscaling **
Indicates whether Amazon RDS can automatically scale storage for DB instances that use the specified DB instance class.
Type: Boolean
Required: No

 ** SupportsStorageEncryption **
Indicates whether a DB instance supports encrypted storage.
Type: Boolean
Required: No

 ** SupportsStorageThroughput **
Indicates whether a DB instance supports storage throughput.
Type: Boolean
Required: No

 ** Vpc **
Indicates whether a DB instance is in a VPC.
Type: Boolean
Required: No

## See Also
<a name="API_OrderableDBInstanceOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/OrderableDBInstanceOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/OrderableDBInstanceOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/OrderableDBInstanceOption)
