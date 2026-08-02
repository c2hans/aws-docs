---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbClusterSnapshotDetails.html
---

# AwsRdsDbClusterSnapshotDetails
<a name="API_AwsRdsDbClusterSnapshotDetails"></a>

Information about an Amazon RDS DB cluster snapshot.

## Contents
<a name="API_AwsRdsDbClusterSnapshotDetails_Contents"></a>

 ** AllocatedStorage **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-AllocatedStorage"></a>
Specifies the allocated storage size in gibibytes (GiB).
Type: Integer
Required: No

 ** AvailabilityZones **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-AvailabilityZones"></a>
A list of Availability Zones where instances in the DB cluster can be created.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ClusterCreateTime **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-ClusterCreateTime"></a>
Indicates when the DB cluster was created, in Universal Coordinated Time (UTC).
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbClusterIdentifier **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-DbClusterIdentifier"></a>
The DB cluster identifier.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbClusterSnapshotAttributes **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-DbClusterSnapshotAttributes"></a>
 Contains the name and values of a manual DB cluster snapshot attribute.
Type: Array of [AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute](API_AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute.md) objects
Required: No

 ** DbClusterSnapshotIdentifier **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-DbClusterSnapshotIdentifier"></a>
The identifier of the DB cluster snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Engine **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-Engine"></a>
The name of the database engine that you want to use for this DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineVersion **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-EngineVersion"></a>
The version of the database engine to use.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IamDatabaseAuthenticationEnabled **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-IamDatabaseAuthenticationEnabled"></a>
Whether mapping of IAM accounts to database accounts is enabled.
Type: Boolean
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-KmsKeyId"></a>
The ARN of the AWS KMS master key that is used to encrypt the database instances in the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LicenseModel **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-LicenseModel"></a>
The license model information for this DB cluster snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MasterUsername **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-MasterUsername"></a>
The name of the master user for the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PercentProgress **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-PercentProgress"></a>
Specifies the percentage of the estimated data that has been transferred.
Type: Integer
Required: No

 ** Port **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-Port"></a>
The port number on which the DB instances in the DB cluster accept connections.
Type: Integer
Required: No

 ** SnapshotCreateTime **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-SnapshotCreateTime"></a>
Indicates when the snapshot was taken.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** SnapshotType **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-SnapshotType"></a>
The type of DB cluster snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-Status"></a>
The status of this DB cluster snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StorageEncrypted **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-StorageEncrypted"></a>
Whether the DB cluster is encrypted.
Type: Boolean
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDetails-VpcId"></a>
The VPC ID that is associated with the DB cluster snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbClusterSnapshotDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbClusterSnapshotDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbClusterSnapshotDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbClusterSnapshotDetails)
