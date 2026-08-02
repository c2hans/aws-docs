---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_FailoverGlobalCluster.html
---

# FailoverGlobalCluster
<a name="API_FailoverGlobalCluster"></a>

Initiates the failover process for a Neptune global database.

A failover for a Neptune global database promotes one of secondary read-only DB clusters to be the primary DB cluster and demotes the primary DB cluster to being a secondary (read-only) DB cluster. In other words, the role of the current primary DB cluster and the selected target secondary DB cluster are switched. The selected secondary DB cluster assumes full read/write capabilities for the Neptune global database.

**Note**
This action applies **only** to Neptune global databases. This action is only intended for use on healthy Neptune global databases with healthy Neptune DB clusters and no region-wide outages, to test disaster recovery scenarios or to reconfigure the global database topology.

## Request Parameters
<a name="API_FailoverGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AllowDataLoss **
Specifies whether to allow data loss for this global database cluster operation. Allowing data loss triggers a global failover operation.
If you don't specify `AllowDataLoss`, the global database cluster operation defaults to a switchover.
Constraints:Can't be specified together with the `Switchover` parameter.
Type: Boolean
Required: No

 ** GlobalClusterIdentifier **
Identifier of the Neptune global database that should be failed over. The identifier is the unique key assigned by the user when the Neptune global database was created. In other words, it's the name of the global database that you want to fail over.
Constraints: Must match the identifier of an existing Neptune global database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** Switchover **
Specifies whether to switch over this global database cluster.
Constraints:Can't be specified together with the `AllowDataLoss` parameter.
Type: Boolean
Required: No

 ** TargetDbClusterIdentifier **
The Amazon Resource Name (ARN) of the secondary Neptune DB cluster that you want to promote to primary for the global database.
Type: String
Required: Yes

## Response Elements
<a name="API_FailoverGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **
Contains the details of an Amazon Neptune global database.
This data type is used as a response element for the [CreateGlobalCluster](API_CreateGlobalCluster.md), [DescribeGlobalClusters](API_DescribeGlobalClusters.md), [ModifyGlobalCluster](API_ModifyGlobalCluster.md), [DeleteGlobalCluster](API_DeleteGlobalCluster.md), [FailoverGlobalCluster](#API_FailoverGlobalCluster), and [RemoveFromGlobalCluster](API_RemoveFromGlobalCluster.md) actions.
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_FailoverGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** GlobalClusterNotFoundFault **
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** InvalidGlobalClusterStateFault **
The global cluster is in an invalid state and can't perform the requested operation.
HTTP Status Code: 400

## See Also
<a name="API_FailoverGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/FailoverGlobalCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/FailoverGlobalCluster)
