---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyGlobalReplicationGroup.html
---

# ModifyGlobalReplicationGroup
<a name="API_ModifyGlobalReplicationGroup"></a>

Modifies the settings for a Global datastore.

## Request Parameters
<a name="API_ModifyGlobalReplicationGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplyImmediately **
This parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible. Modifications to Global Replication Groups cannot be requested to be applied in PreferredMaintenceWindow.
Type: Boolean
Required: Yes

 ** GlobalReplicationGroupId **
The name of the Global datastore
Type: String
Required: Yes

 ** AutomaticFailoverEnabled **
Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.
Type: Boolean
Required: No

 ** CacheNodeType **
A valid cache node type that you want to scale this Global datastore to.
Type: String
Required: No

 ** CacheParameterGroupName **
The name of the cache parameter group to use with the Global datastore. It must be compatible with the major engine version used by the Global datastore.
Type: String
Required: No

 ** Engine **
Modifies the engine listed in a global replication group message. The options are valkey, memcached or redis.
Type: String
Required: No

 ** EngineVersion **
The upgraded version of the cache engine to be run on the clusters in the Global datastore.
Type: String
Required: No

 ** GlobalReplicationGroupDescription **
A description of the Global datastore
Type: String
Required: No

## Response Elements
<a name="API_ModifyGlobalReplicationGroup_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalReplicationGroup **
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different Amazon region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.
+ The **GlobalReplicationGroupIdSuffix** represents the name of the Global datastore, which is what you use to associate a secondary cluster.
Type: [GlobalReplicationGroup](API_GlobalReplicationGroup.md) object

## Errors
<a name="API_ModifyGlobalReplicationGroup_Errors"></a>

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
<a name="API_ModifyGlobalReplicationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ModifyGlobalReplicationGroup)
