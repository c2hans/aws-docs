---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_SwitchoverGlobalCluster.html
---

# SwitchoverGlobalCluster
<a name="API_SwitchoverGlobalCluster"></a>

Switches over the specified secondary DB cluster to be the new primary DB cluster in the global database cluster. Switchover operations were previously called "managed planned failovers."

Promotes the specified secondary cluster to assume full read/write capabilities and demotes the current primary cluster to a secondary (read-only) cluster, maintaining the original replication topology. All secondary clusters are synchronized with the primary at the beginning of the process so the new primary continues operations for the global database without losing any data. Your database is unavailable for a short time while the primary and selected secondary clusters are assuming their new roles.

**Note**
This operation is intended for controlled environments, for operations such as "regional rotation" or to fall back to the original primary after a global database failover.

## Request Parameters
<a name="API_SwitchoverGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **
The identifier of the global database cluster to switch over. This parameter isn't case-sensitive.
Constraints: Must match the identifier of an existing global database cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** TargetDbClusterIdentifier **
The Amazon Resource Name (ARN) of the secondary Neptune DB cluster that you want to promote to primary for the global database.
Type: String
Required: Yes

## Response Elements
<a name="API_SwitchoverGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **
Contains the details of an Amazon Neptune global database.
This data type is used as a response element for the [CreateGlobalCluster](API_CreateGlobalCluster.md), [DescribeGlobalClusters](API_DescribeGlobalClusters.md), [ModifyGlobalCluster](API_ModifyGlobalCluster.md), [DeleteGlobalCluster](API_DeleteGlobalCluster.md), [FailoverGlobalCluster](API_FailoverGlobalCluster.md), and [RemoveFromGlobalCluster](API_RemoveFromGlobalCluster.md) actions.
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_SwitchoverGlobalCluster_Errors"></a>

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
<a name="API_SwitchoverGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/SwitchoverGlobalCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/SwitchoverGlobalCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
