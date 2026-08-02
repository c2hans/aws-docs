---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DisassociateGlobalReplicationGroup.html
---

# DisassociateGlobalReplicationGroup
<a name="API_DisassociateGlobalReplicationGroup"></a>

Remove a secondary cluster from the Global datastore using the Global datastore name. The secondary cluster will no longer receive updates from the primary cluster, but will remain as a standalone cluster in that Amazon region.

## Request Parameters
<a name="API_DisassociateGlobalReplicationGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalReplicationGroupId **
The name of the Global datastore
Type: String
Required: Yes

 ** ReplicationGroupId **
The name of the secondary cluster you wish to remove from the Global datastore
Type: String
Required: Yes

 ** ReplicationGroupRegion **
The Amazon region of secondary cluster you wish to remove from the Global datastore
Type: String
Required: Yes

## Response Elements
<a name="API_DisassociateGlobalReplicationGroup_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalReplicationGroup **
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different Amazon region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.
+ The **GlobalReplicationGroupIdSuffix** represents the name of the Global datastore, which is what you use to associate a secondary cluster.
Type: [GlobalReplicationGroup](API_GlobalReplicationGroup.md) object

## Errors
<a name="API_DisassociateGlobalReplicationGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalReplicationGroupNotFoundFault **
The Global datastore does not exist
HTTP Status Code: 404

 ** InvalidGlobalReplicationGroupState **
The Global datastore is not available or in primary-only state.
HTTP Status Code: 400

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
<a name="API_DisassociateGlobalReplicationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DisassociateGlobalReplicationGroup)
