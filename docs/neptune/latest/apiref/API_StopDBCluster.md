---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_StopDBCluster.html
---

# StopDBCluster
<a name="API_StopDBCluster"></a>

Stops an Amazon Neptune DB cluster. When you stop a DB cluster, Neptune retains the DB cluster's metadata, including its endpoints and DB parameter groups.

Neptune also retains the transaction logs so you can do a point-in-time restore if necessary.

## Request Parameters
<a name="API_StopDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **
The DB cluster identifier of the Neptune DB cluster to be stopped. This parameter is stored as a lowercase string.
Type: String
Required: Yes

## Response Elements
<a name="API_StopDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the [DescribeDBClusters](API_DescribeDBClusters.md).
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_StopDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** InvalidDBInstanceState **
The specified DB instance is not in the *available* state.
HTTP Status Code: 400

## See Also
<a name="API_StopDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/StopDBCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/StopDBCluster)
