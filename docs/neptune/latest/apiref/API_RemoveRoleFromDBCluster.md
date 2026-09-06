---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_RemoveRoleFromDBCluster.html
---

# RemoveRoleFromDBCluster
<a name="API_RemoveRoleFromDBCluster"></a>

Disassociates an Identity and Access Management (IAM) role from a DB cluster.

## Request Parameters
<a name="API_RemoveRoleFromDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **
The name of the DB cluster to disassociate the IAM role from.
Type: String
Required: Yes

 ** FeatureName **
The name of the feature for the DB cluster that the IAM role is to be disassociated from. For the list of supported feature names, see [DescribeDBEngineVersions](API_DescribeDBEngineVersions.md).
Type: String
Required: No

 ** RoleArn **
The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB cluster, for example `arn:aws:iam::123456789012:role/NeptuneAccessRole`.
Type: String
Required: Yes

## Errors
<a name="API_RemoveRoleFromDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** DBClusterRoleNotFound **
The specified IAM role Amazon Resource Name (ARN) is not associated with the specified DB cluster.
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

## See Also
<a name="API_RemoveRoleFromDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/RemoveRoleFromDBCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/RemoveRoleFromDBCluster)
