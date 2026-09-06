---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_RemoveFromGlobalCluster.html
---

# RemoveFromGlobalCluster
<a name="API_RemoveFromGlobalCluster"></a>

Detaches a Neptune DB cluster from a Neptune global database. A secondary cluster becomes a normal standalone cluster with read-write capability instead of being read-only, and no longer receives data from a the primary cluster.

## Request Parameters
<a name="API_RemoveFromGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DbClusterIdentifier **
The Amazon Resource Name (ARN) identifying the cluster to be detached from the Neptune global database cluster.
Type: String
Required: Yes

 ** GlobalClusterIdentifier **
The identifier of the Neptune global database from which to detach the specified Neptune DB cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

## Response Elements
<a name="API_RemoveFromGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **
Contains the details of an Amazon Neptune global database.
This data type is used as a response element for the [CreateGlobalCluster](API_CreateGlobalCluster.md), [DescribeGlobalClusters](API_DescribeGlobalClusters.md), [ModifyGlobalCluster](API_ModifyGlobalCluster.md), [DeleteGlobalCluster](API_DeleteGlobalCluster.md), [FailoverGlobalCluster](API_FailoverGlobalCluster.md), and [RemoveFromGlobalCluster](#API_RemoveFromGlobalCluster) actions.
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_RemoveFromGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** GlobalClusterNotFoundFault **
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.
HTTP Status Code: 404

 ** InvalidGlobalClusterStateFault **
The global cluster is in an invalid state and can't perform the requested operation.
HTTP Status Code: 400

## See Also
<a name="API_RemoveFromGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/RemoveFromGlobalCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/RemoveFromGlobalCluster)
