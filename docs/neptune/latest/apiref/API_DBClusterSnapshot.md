---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBClusterSnapshot.html
---

# DBClusterSnapshot
<a name="API_DBClusterSnapshot"></a>

Contains the details for an Amazon Neptune DB cluster snapshot

This data type is used as a response element in the [DescribeDBClusterSnapshots](API_DescribeDBClusterSnapshots.md) action.

## Contents
<a name="API_DBClusterSnapshot_Contents"></a>

 ** AllocatedStorage **
Specifies the allocated storage size in gibibytes (GiB).
Type: Integer
Required: No

 ** AvailabilityZones.AvailabilityZone.N **
Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
Type: Array of strings
Required: No

 ** ClusterCreateTime **
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
Type: Timestamp
Required: No

 ** DBClusterIdentifier **
Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.
Type: String
Required: No

 ** DBClusterSnapshotArn **
The Amazon Resource Name (ARN) for the DB cluster snapshot.
Type: String
Required: No

 ** DBClusterSnapshotIdentifier **
Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.
After you restore a DB cluster using a `DBClusterSnapshotIdentifier`, you must specify the same `DBClusterSnapshotIdentifier` for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.
However, if you don't specify the `DBClusterSnapshotIdentifier`, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the `DBClusterSnapshotIdentifier`, and the original DB cluster is deleted.
Type: String
Required: No

 ** Engine **
Specifies the name of the database engine.
Type: String
Required: No

 ** EngineVersion **
Provides the version of the database engine for this DB cluster snapshot.
Type: String
Required: No

 ** IAMDatabaseAuthenticationEnabled **
True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
Type: Boolean
Required: No

 ** KmsKeyId **
If `StorageEncrypted` is true, the Amazon KMS key identifier for the encrypted DB cluster snapshot.
Type: String
Required: No

 ** LicenseModel **
Provides the license model information for this DB cluster snapshot.
Type: String
Required: No

 ** MasterUsername **
Not supported by Neptune.
Type: String
Required: No

 ** PercentProgress **
Specifies the percentage of the estimated data that has been transferred.
Type: Integer
Required: No

 ** Port **
Specifies the port that the DB cluster was listening on at the time of the snapshot.
Type: Integer
Required: No

 ** SnapshotCreateTime **
Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).
Type: Timestamp
Required: No

 ** SnapshotType **
Provides the type of the DB cluster snapshot.
Type: String
Required: No

 ** SourceDBClusterSnapshotArn **
If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.
Type: String
Required: No

 ** Status **
Specifies the status of this DB cluster snapshot.
Type: String
Required: No

 ** StorageEncrypted **
Specifies whether the DB cluster snapshot is encrypted.
Type: Boolean
Required: No

 ** StorageType **
The storage type associated with the DB cluster snapshot.
Type: String
Required: No

 ** VpcId **
Provides the VPC ID associated with the DB cluster snapshot.
Type: String
Required: No

## See Also
<a name="API_DBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBClusterSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBClusterSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBClusterSnapshot)
