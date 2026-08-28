---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DescribeDBClusterSnapshots.html
---

# DescribeDBClusterSnapshots
<a name="API_DescribeDBClusterSnapshots"></a>

Returns information about DB cluster snapshots. This API action supports pagination.

## Request Parameters
<a name="API_DescribeDBClusterSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **
The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can't be used in conjunction with the `DBClusterSnapshotIdentifier` parameter. This parameter is not case-sensitive.
Constraints:
+ If supplied, must match the identifier of an existing DBCluster.
Type: String
Required: No

 ** DBClusterSnapshotIdentifier **
A specific DB cluster snapshot identifier to describe. This parameter can't be used in conjunction with the `DBClusterIdentifier` parameter. This value is stored as a lowercase string.
Constraints:
+ If supplied, must match the identifier of an existing DBClusterSnapshot.
+ If this identifier is for an automated snapshot, the `SnapshotType` parameter must also be specified.
Type: String
Required: No

 **Filters.Filter.N**
This parameter is not currently supported.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** IncludePublic **
True to include manual DB cluster snapshots that are public and can be copied or restored by any Amazon account, and otherwise false. The default is `false`. The default is false.
You can share a manual DB cluster snapshot as public by using the [ModifyDBClusterSnapshotAttribute](API_ModifyDBClusterSnapshotAttribute.md) API action.
Type: Boolean
Required: No

 ** IncludeShared **
True to include shared manual DB cluster snapshots from other Amazon accounts that this Amazon account has been given permission to copy or restore, and otherwise false. The default is `false`.
You can give an Amazon account permission to restore a manual DB cluster snapshot from another Amazon account by the [ModifyDBClusterSnapshotAttribute](API_ModifyDBClusterSnapshotAttribute.md) API action.
Type: Boolean
Required: No

 ** Marker **
An optional pagination token provided by a previous `DescribeDBClusterSnapshots` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** SnapshotType **
The type of DB cluster snapshots to be returned. You can specify one of the following values:
+  `automated` - Return all DB cluster snapshots that have been automatically taken by Amazon Neptune for my Amazon account.
+  `manual` - Return all DB cluster snapshots that have been taken by my Amazon account.
+  `shared` - Return all manual DB cluster snapshots that have been shared to my Amazon account.
+  `public` - Return all DB cluster snapshots that have been marked as public.
If you don't specify a `SnapshotType` value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the `IncludeShared` parameter to `true`. You can include public DB cluster snapshots with these results by setting the `IncludePublic` parameter to `true`.
The `IncludeShared` and `IncludePublic` parameters don't apply for `SnapshotType` values of `manual` or `automated`. The `IncludePublic` parameter doesn't apply when `SnapshotType` is set to `shared`. The `IncludeShared` parameter doesn't apply when `SnapshotType` is set to `public`.
Type: String
Required: No

## Response Elements
<a name="API_DescribeDBClusterSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 **DBClusterSnapshots.DBClusterSnapshot.N**
Provides a list of DB cluster snapshots for the user.
Type: Array of [DBClusterSnapshot](API_DBClusterSnapshot.md) objects

 ** Marker **
 An optional pagination token provided by a previous [DescribeDBClusterSnapshots](#API_DescribeDBClusterSnapshots) request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

## Errors
<a name="API_DescribeDBClusterSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **
 *DBClusterSnapshotIdentifier* does not refer to an existing DB cluster snapshot.
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBClusterSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DescribeDBClusterSnapshots)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
