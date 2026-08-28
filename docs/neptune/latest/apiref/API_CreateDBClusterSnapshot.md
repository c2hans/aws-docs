---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_CreateDBClusterSnapshot.html
---

# CreateDBClusterSnapshot
<a name="API_CreateDBClusterSnapshot"></a>

Creates a snapshot of a DB cluster.

## Request Parameters
<a name="API_CreateDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **
The identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.
Constraints:
+ Must match the identifier of an existing DBCluster.
Example: `my-cluster1`
Type: String
Required: Yes

 ** DBClusterSnapshotIdentifier **
The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster1-snapshot1`
Type: String
Required: Yes

 **Tags.Tag.N**
The tags to be assigned to the DB cluster snapshot.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreateDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **
Contains the details for an Amazon Neptune DB cluster snapshot
This data type is used as a response element in the [DescribeDBClusterSnapshots](API_DescribeDBClusterSnapshots.md) action.
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_CreateDBClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** DBClusterSnapshotAlreadyExistsFault **
User already has a DB cluster snapshot with the given identifier.
HTTP Status Code: 400

 ** InvalidDBClusterSnapshotStateFault **
The supplied value is not a valid DB cluster snapshot state.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **
Request would result in user exceeding the allowed number of DB snapshots.
HTTP Status Code: 400

## See Also
<a name="API_CreateDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBClusterSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/CreateDBClusterSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
