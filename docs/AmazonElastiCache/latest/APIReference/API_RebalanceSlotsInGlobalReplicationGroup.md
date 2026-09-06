---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RebalanceSlotsInGlobalReplicationGroup.html
---

# RebalanceSlotsInGlobalReplicationGroup
<a name="API_RebalanceSlotsInGlobalReplicationGroup"></a>

Redistribute slots to ensure uniform distribution across existing shards in the cluster.

## Request Parameters
<a name="API_RebalanceSlotsInGlobalReplicationGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplyImmediately **
If `True`, redistribution is applied immediately.
Type: Boolean
Required: Yes

 ** GlobalReplicationGroupId **
The name of the Global datastore
Type: String
Required: Yes

## Response Elements
<a name="API_RebalanceSlotsInGlobalReplicationGroup_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalReplicationGroup **
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different Amazon region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.
+ The **GlobalReplicationGroupIdSuffix** represents the name of the Global datastore, which is what you use to associate a secondary cluster.
Type: [GlobalReplicationGroup](API_GlobalReplicationGroup.md) object

## Errors
<a name="API_RebalanceSlotsInGlobalReplicationGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalReplicationGroupNotFoundFault **
The Global datastore does not exist
HTTP Status Code: 404

 ** InvalidGlobalReplicationGroupState **
The Global datastore is not available or in primary-only state.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_RebalanceSlotsInGlobalReplicationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/RebalanceSlotsInGlobalReplicationGroup)
