---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_CreateGlobalCluster.html
---

# CreateGlobalCluster
<a name="API_CreateGlobalCluster"></a>

Creates a Neptune global database spread across multiple Amazon Regions. The global database contains a single primary cluster with read-write capability, and read-only secondary clusters that receive data from the primary cluster through high-speed replication performed by the Neptune storage subsystem.

You can create a global database that is initially empty, and then add a primary cluster and secondary clusters to it, or you can specify an existing Neptune cluster during the create operation to become the primary cluster of the global database.

## Request Parameters
<a name="API_CreateGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DeletionProtection **
The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
Type: Boolean
Required: No

 ** Engine **
The name of the database engine to be used in the global database.
Valid values: `neptune`
Type: String
Required: No

 ** EngineVersion **
The Neptune engine version to be used by the global database.
Valid values: `1.2.0.0` or above.
Type: String
Required: No

 ** GlobalClusterIdentifier **
The cluster identifier of the new global database cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** SourceDBClusterIdentifier **
(*Optional*) The Amazon Resource Name (ARN) of an existing Neptune DB cluster to use as the primary cluster of the new global database.
Type: String
Required: No

 ** StorageEncrypted **
The storage encryption setting for the new global database cluster.
Type: Boolean
Required: No

## Response Elements
<a name="API_CreateGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **
Contains the details of an Amazon Neptune global database.
This data type is used as a response element for the [CreateGlobalCluster](#API_CreateGlobalCluster), [DescribeGlobalClusters](API_DescribeGlobalClusters.md), [ModifyGlobalCluster](API_ModifyGlobalCluster.md), [DeleteGlobalCluster](API_DeleteGlobalCluster.md), [FailoverGlobalCluster](API_FailoverGlobalCluster.md), and [RemoveFromGlobalCluster](API_RemoveFromGlobalCluster.md) actions.
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_CreateGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** GlobalClusterAlreadyExistsFault **
The `GlobalClusterIdentifier` already exists. Choose a new global database identifier (unique name) to create a new global database cluster.
HTTP Status Code: 400

 ** GlobalClusterQuotaExceededFault **
The number of global database clusters for this account is already at the maximum allowed.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

## See Also
<a name="API_CreateGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateGlobalCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/CreateGlobalCluster)
