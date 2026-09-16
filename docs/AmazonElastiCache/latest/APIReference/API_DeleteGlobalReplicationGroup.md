---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteGlobalReplicationGroup.html
---

# DeleteGlobalReplicationGroup
<a name="API_DeleteGlobalReplicationGroup"></a>

Deleting a Global datastore is a two-step process:
+ First, you must [DisassociateGlobalReplicationGroup](API_DisassociateGlobalReplicationGroup.md) to remove the secondary clusters in the Global datastore.
+ Once the Global datastore contains only the primary cluster, you can use the `DeleteGlobalReplicationGroup` API to delete the Global datastore while retainining the primary cluster using `RetainPrimaryReplicationGroup=true`.

Since the Global Datastore has only a primary cluster, you can delete the Global Datastore while retaining the primary by setting `RetainPrimaryReplicationGroup=true`. The primary cluster is never deleted when deleting a Global Datastore. It can only be deleted when it no longer is associated with any Global Datastore.

When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.

## Request Parameters
<a name="API_DeleteGlobalReplicationGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalReplicationGroupId **
The name of the Global datastore
Type: String
Required: Yes

 ** RetainPrimaryReplicationGroup **
The primary replication group is retained as a standalone replication group.
Type: Boolean
Required: Yes

## Response Elements
<a name="API_DeleteGlobalReplicationGroup_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalReplicationGroup **
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different Amazon region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.
+ The **GlobalReplicationGroupIdSuffix** represents the name of the Global datastore, which is what you use to associate a secondary cluster.
Type: [GlobalReplicationGroup](API_GlobalReplicationGroup.md) object

## Errors
<a name="API_DeleteGlobalReplicationGroup_Errors"></a>

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
<a name="API_DeleteGlobalReplicationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DeleteGlobalReplicationGroup)
