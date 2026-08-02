---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ModifyGlobalCluster.html
---

# ModifyGlobalCluster
<a name="API_ModifyGlobalCluster"></a>

Modify a setting for an Amazon Neptune global cluster. You can change one or more database configuration parameters by specifying these parameters and their new values in the request.

## Request Parameters
<a name="API_ModifyGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AllowMajorVersionUpgrade **
A value that indicates whether major version upgrades are allowed.
Constraints: You must allow major version upgrades if you specify a value for the `EngineVersion` parameter that is a different major version than the DB cluster's current version.
If you upgrade the major version of a global database, the cluster and DB instance parameter groups are set to the default parameter groups for the new version, so you will need to apply any custom parameter groups after completing the upgrade.
Type: Boolean
Required: No

 ** DeletionProtection **
Indicates whether the global database has deletion protection enabled. The global database cannot be deleted when deletion protection is enabled.
Type: Boolean
Required: No

 ** EngineVersion **
The version number of the database engine to which you want to upgrade. Changing this parameter will result in an outage. The change is applied during the next maintenance window unless `ApplyImmediately` is enabled.
To list all of the available Neptune engine versions, use the following command:
Type: String
Required: No

 ** GlobalClusterIdentifier **
The DB cluster identifier for the global cluster being modified. This parameter is not case-sensitive.
Constraints: Must match the identifier of an existing global database cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: Yes

 ** NewGlobalClusterIdentifier **
A new cluster identifier to assign to the global database. This value is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens
Example: `my-cluster2`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: No

## Response Elements
<a name="API_ModifyGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **
Contains the details of an Amazon Neptune global database.
This data type is used as a response element for the [CreateGlobalCluster](API_CreateGlobalCluster.md), [DescribeGlobalClusters](API_DescribeGlobalClusters.md), [ModifyGlobalCluster](#API_ModifyGlobalCluster), [DeleteGlobalCluster](API_DeleteGlobalCluster.md), [FailoverGlobalCluster](API_FailoverGlobalCluster.md), and [RemoveFromGlobalCluster](API_RemoveFromGlobalCluster.md) actions.
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_ModifyGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalClusterNotFoundFault **
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.
HTTP Status Code: 404

 ** InvalidGlobalClusterStateFault **
The global cluster is in an invalid state and can't perform the requested operation.
HTTP Status Code: 400

## See Also
<a name="API_ModifyGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ModifyGlobalCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ModifyGlobalCluster)
