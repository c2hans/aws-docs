---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBInstance.html
---

# StopDBInstance
<a name="API_StopDBInstance"></a>

Stops an Amazon RDS DB instance temporarily. When you stop a DB instance, Amazon RDS retains the DB instance's metadata, including its endpoint, DB parameter group, and option group membership. Amazon RDS also retains the transaction logs so you can do a point-in-time restore if necessary. The instance restarts automatically after 7 days.

For more information, see [ Stopping an Amazon RDS DB Instance Temporarily](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html) in the *Amazon RDS User Guide.*

**Note**
This command doesn't apply to RDS Custom, Aurora MySQL, and Aurora PostgreSQL. For Aurora clusters, use `StopDBCluster` instead.

## Request Parameters
<a name="API_StopDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **
The user-supplied instance identifier.
Type: String
Required: Yes

 ** DBSnapshotIdentifier **
The user-supplied instance identifier of the DB Snapshot created immediately before the DB instance is stopped.
Type: String
Required: No

 ** DetachFromDBCapacityReservation **
Specifies whether the DB instance stops using its DB capacity reservation when the DB instance stops. When you specify `true`, the DB instance belongs to no reservation after it stops, and a later start launches it outside the reservation.
By default, a stopped DB instance keeps its DB capacity reservation, and a later start returns the DB instance to the same reservation.
Every stop releases the unit of reserved capacity that the DB instance holds, for either value of this parameter. Another DB instance can then use that capacity. This parameter controls the reservation that the DB instance belongs to, and it does not control the release of the capacity.
If the DB instance uses no DB capacity reservation, this parameter has no effect.
Amazon RDS holds no capacity for a stopped DB instance. When the reservation has no available capacity in the Availability Zone of the DB instance, a later start waits for capacity in that Availability Zone. When the DB instance belongs to no reservation, a later start can fail because the AWS Region has insufficient capacity for the DB instance class.
Type: Boolean
Required: No

## Response Elements
<a name="API_StopDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **
Contains the details of an Amazon RDS DB instance.
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_StopDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.
HTTP Status Code: 404

 ** DBSnapshotAlreadyExists **
 `DBSnapshotIdentifier` is already used by an existing snapshot.
HTTP Status Code: 400

 ** InvalidDBCapacityReservationState **
The DB capacity reservation isn't in a valid state.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The requested operation can't be performed while the cluster is in this state.
HTTP Status Code: 400

 ** InvalidDBInstanceState **
The DB instance isn't in a valid state.
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **
The request would result in the user exceeding the allowed number of DB snapshots.
HTTP Status Code: 400

## See Also
<a name="API_StopDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/StopDBInstance)
