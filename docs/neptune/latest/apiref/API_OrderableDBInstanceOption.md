---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_OrderableDBInstanceOption.html
---

# OrderableDBInstanceOption
<a name="API_OrderableDBInstanceOption"></a>

Contains a list of available options for a DB instance.

 This data type is used as a response element in the [DescribeOrderableDBInstanceOptions](API_DescribeOrderableDBInstanceOptions.md) action.

## Contents
<a name="API_OrderableDBInstanceOption_Contents"></a>

 ** AvailabilityZones.AvailabilityZone.N **
A list of Availability Zones for a DB instance.
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects
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

 ** MultiAZCapable **
Indicates whether a DB instance is Multi-AZ capable.
Type: Boolean
Required: No

 ** ReadReplicaCapable **
Indicates whether a DB instance can have a Read Replica.
Type: Boolean
Required: No

 ** StorageType **
Not applicable. In Neptune the storage type is managed at the DB Cluster level.
Type: String
Required: No

 ** SupportsEnhancedMonitoring **
Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.
Type: Boolean
Required: No

 ** SupportsGlobalDatabases **
A value that indicates whether you can use Neptune global databases with a specific combination of other DB engine attributes.
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

 ** SupportsPerformanceInsights **
 *(Not supported by Neptune)*
Type: Boolean
Required: No

 ** SupportsStorageEncryption **
Indicates whether a DB instance supports encrypted storage.
Type: Boolean
Required: No

 ** Vpc **
Indicates whether a DB instance is in a VPC.
Type: Boolean
Required: No

## See Also
<a name="API_OrderableDBInstanceOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/OrderableDBInstanceOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/OrderableDBInstanceOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/OrderableDBInstanceOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
