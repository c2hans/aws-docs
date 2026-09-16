---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeUpdateActions.html
---

# DescribeUpdateActions
<a name="API_DescribeUpdateActions"></a>

Returns details of the update actions

## Request Parameters
<a name="API_DescribeUpdateActions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **CacheClusterIds.member.N**
The cache cluster IDs
Type: Array of strings
Array Members: Maximum number of 20 items.
Required: No

 ** Engine **
The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.
Type: String
Required: No

 ** Marker **
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
The maximum number of records to include in the response
Type: Integer
Required: No

 **ReplicationGroupIds.member.N**
The replication group IDs
Type: Array of strings
Array Members: Maximum number of 20 items.
Required: No

 ** ServiceUpdateName **
The unique ID of the service update
Type: String
Required: No

 **ServiceUpdateStatus.member.N**
The status of the service update
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `available | cancelled | expired`
Required: No

 ** ServiceUpdateTimeRange **
The range of time specified to search for service updates that are in available status
Type: [TimeRangeFilter](API_TimeRangeFilter.md) object
Required: No

 ** ShowNodeLevelUpdateStatus **
Dictates whether to include node level update status in the response
Type: Boolean
Required: No

 **UpdateActionStatus.member.N**
The status of the update action.
Type: Array of strings
Array Members: Maximum number of 9 items.
Valid Values: `not-applied | waiting-to-start | in-progress | stopping | stopped | complete | scheduling | scheduled | not-applicable`
Required: No

## Response Elements
<a name="API_DescribeUpdateActions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 **UpdateActions.UpdateAction.N**
Returns a list of update actions
Type: Array of [UpdateAction](API_UpdateAction.md) objects

## Errors
<a name="API_DescribeUpdateActions_Errors"></a>

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

## See Also
<a name="API_DescribeUpdateActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeUpdateActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeUpdateActions)
