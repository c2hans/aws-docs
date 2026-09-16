---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DescribeDBClusters.html
---

# DescribeDBClusters
<a name="API_DescribeDBClusters"></a>

Returns information about provisioned DB clusters, and supports pagination.

**Note**
This operation can also return information for Amazon RDS clusters and Amazon DocDB clusters.

## Request Parameters
<a name="API_DescribeDBClusters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **
The user-supplied DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn't case-sensitive.
Constraints:
+ If supplied, must match an existing DBClusterIdentifier.
Type: String
Required: No

 **Filters.Filter.N**
A filter that specifies one or more DB clusters to describe.
Supported filters:
+  `db-cluster-id` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB clusters identified by these ARNs.
+  `engine` - Accepts an engine name (such as `neptune`), and restricts the results list to DB clusters created by that engine.
For example, to invoke this API from the Amazon CLI and filter so that only Neptune DB clusters are returned, you could use the following command:
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** Marker **
An optional pagination token provided by a previous [DescribeDBClusters](#API_DescribeDBClusters) request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

## Response Elements
<a name="API_DescribeDBClusters_ResponseElements"></a>

The following elements are returned by the service.

 **DBClusters.DBCluster.N**
Contains a list of DB clusters for the user.
Type: Array of [DBCluster](API_DBCluster.md) objects

 ** Marker **
A pagination token that can be used in a subsequent DescribeDBClusters request.
Type: String

## Errors
<a name="API_DescribeDBClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DescribeDBClusters)
