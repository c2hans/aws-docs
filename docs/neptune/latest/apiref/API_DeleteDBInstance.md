---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DeleteDBInstance.html
---

# DeleteDBInstance
<a name="API_DeleteDBInstance"></a>

The DeleteDBInstance action deletes a previously provisioned DB instance. When you delete a DB instance, all automated backups for that instance are deleted and can't be recovered. Manual DB snapshots of the DB instance to be deleted by `DeleteDBInstance` are not deleted.

 If you request a final DB snapshot the status of the Amazon Neptune DB instance is `deleting` until the DB snapshot is created. The API action `DescribeDBInstance` is used to monitor the status of this operation. The action can't be canceled or reverted once submitted.

Note that when a DB instance is in a failure state and has a status of `failed`, `incompatible-restore`, or `incompatible-network`, you can only delete it when the `SkipFinalSnapshot` parameter is set to `true`.

You can't delete a DB instance if it is the only instance in the DB cluster, or if it has deletion protection enabled.

## Request Parameters
<a name="API_DeleteDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **
The DB instance identifier for the DB instance to be deleted. This parameter isn't case-sensitive.
Constraints:
+ Must match the name of an existing DB instance.
Type: String
Required: Yes

 ** FinalDBSnapshotIdentifier **
 The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot is set to `false`.
Specifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.
Constraints:
+ Must be 1 to 255 letters or numbers.
+ First character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
+ Cannot be specified when deleting a Read Replica.
Type: String
Required: No

 ** SkipFinalSnapshot **
 Determines whether a final DB snapshot is created before the DB instance is deleted. If `true` is specified, no DBSnapshot is created. If `false` is specified, a DB snapshot is created before the DB instance is deleted.
Note that when a DB instance is in a failure state and has a status of 'failed', 'incompatible-restore', or 'incompatible-network', it can only be deleted when the SkipFinalSnapshot parameter is set to "true".
Specify `true` when deleting a Read Replica.
The FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot is `false`.
Default: `false`
Type: Boolean
Required: No

## Response Elements
<a name="API_DeleteDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the [DescribeDBInstances](API_DescribeDBInstances.md) action.
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_DeleteDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **
 *DBInstanceIdentifier* does not refer to an existing DB instance.
HTTP Status Code: 404

 ** DBSnapshotAlreadyExists **
 *DBSnapshotIdentifier* is already used by an existing snapshot.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** InvalidDBInstanceState **
The specified DB instance is not in the *available* state.
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **
Request would result in user exceeding the allowed number of DB snapshots.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DeleteDBInstance)
