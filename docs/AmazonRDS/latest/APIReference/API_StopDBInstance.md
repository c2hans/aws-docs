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
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/StopDBInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/StopDBInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
