---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_AddRoleToDBCluster.html
---

# AddRoleToDBCluster
<a name="API_AddRoleToDBCluster"></a>

Associates an Identity and Access Management (IAM) role with an Neptune DB cluster.

## Request Parameters
<a name="API_AddRoleToDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **
The name of the DB cluster to associate the IAM role with.
Type: String
Required: Yes

 ** FeatureName **
The name of the feature for the Neptune DB cluster that the IAM role is to be associated with. For the list of supported feature names, see [DBEngineVersion](API_DBEngineVersion.md).
Type: String
Required: No

 ** RoleArn **
The Amazon Resource Name (ARN) of the IAM role to associate with the Neptune DB cluster, for example `arn:aws:iam::123456789012:role/NeptuneAccessRole`.
Type: String
Required: Yes

## Errors
<a name="API_AddRoleToDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** DBClusterRoleAlreadyExists **
The specified IAM role Amazon Resource Name (ARN) is already associated with the specified DB cluster.
HTTP Status Code: 400

 ** DBClusterRoleQuotaExceeded **
You have exceeded the maximum number of IAM roles that can be associated with the specified DB cluster.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

## See Also
<a name="API_AddRoleToDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/AddRoleToDBCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/AddRoleToDBCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
