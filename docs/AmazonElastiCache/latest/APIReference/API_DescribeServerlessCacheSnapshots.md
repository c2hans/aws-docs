---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeServerlessCacheSnapshots.html
---

# DescribeServerlessCacheSnapshots
<a name="API_DescribeServerlessCacheSnapshots"></a>

Returns information about serverless cache snapshots. By default, this API lists all of the customer’s serverless cache snapshots. It can also describe a single serverless cache snapshot, or the snapshots associated with a particular serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.

## Request Parameters
<a name="API_DescribeServerlessCacheSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MaxResults **
The maximum number of records to include in the response. If more records exist than the specified max-results value, a market is included in the response so that remaining results can be retrieved. Available for Valkey, Redis OSS and Serverless Memcached only.The default is 50. The Validation Constraints are a maximum of 50.
Type: Integer
Required: No

 ** NextToken **
An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by max-results. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** ServerlessCacheName **
The identifier of serverless cache. If this parameter is specified, only snapshots associated with that specific serverless cache are described. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** ServerlessCacheSnapshotName **
The identifier of the serverless cache’s snapshot. If this parameter is specified, only this snapshot is described. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** SnapshotType **
The type of snapshot that is being described. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

## Response Elements
<a name="API_DescribeServerlessCacheSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by max-results. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String

 **ServerlessCacheSnapshots.ServerlessCacheSnapshot.N**
The serverless caches snapshots associated with a given description request. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: Array of [ServerlessCacheSnapshot](API_ServerlessCacheSnapshot.md) objects

## Errors
<a name="API_DescribeServerlessCacheSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombination **
Two or more incompatible parameters were specified.
 ** message **
Two or more parameters that must not be used together were used together.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** ServerlessCacheNotFoundFault **
The serverless cache was not found or does not exist.
HTTP Status Code: 404

 ** ServerlessCacheSnapshotNotFoundFault **
This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 404

## See Also
<a name="API_DescribeServerlessCacheSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeServerlessCacheSnapshots)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
