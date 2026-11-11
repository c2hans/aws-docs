---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtensionDetails.html
---

# ExtensionDetails
<a name="API_ExtensionDetails"></a>

Details of an extension installed on a SageMaker HyperPod cluster.

## Contents
<a name="API_ExtensionDetails_Contents"></a>

 ** ClusterArn **   <a name="sagemaker-Type-ExtensionDetails-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the extension is installed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** ExtensionArn **   <a name="sagemaker-Type-ExtensionDetails-ExtensionArn"></a>
The Amazon Resource Name (ARN) of the extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:extension/(sagemaker|eks|pcs)-[a-z0-9-]+/[a-z0-9-]+/[a-z0-9]+`
Required: Yes

 ** ExtensionName **   <a name="sagemaker-Type-ExtensionDetails-ExtensionName"></a>
The name of the extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-z]([a-z0-9]|-[a-z0-9])*`
Required: Yes

 ** ExtensionVersion **   <a name="sagemaker-Type-ExtensionDetails-ExtensionVersion"></a>
The version of the extension. While SageMaker HyperPod creates or updates the extension, some nodes might still run a different version. To see how many nodes run this version, see `NodeSummary`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: Yes

 ** Status **   <a name="sagemaker-Type-ExtensionDetails-Status"></a>
The status of the extension can be one of the following values:
Creating
SageMaker HyperPod is installing the extension on the cluster's nodes.
Active
The extension runs its current version and configuration on all of the cluster's nodes.
Updating
SageMaker HyperPod is applying a configuration change or version update to the cluster's nodes.
Degraded
The extension runs its current version and configuration on some of the cluster's nodes but not all of them. Or, at least one node recently reported that the extension is unhealthy.
CreateFailed
SageMaker HyperPod couldn't install the extension on any of the cluster's nodes.
UpdateFailed
SageMaker HyperPod couldn't apply the update on any of the cluster's nodes.
Deleting
SageMaker HyperPod is removing the extension from the cluster's nodes.
DeleteFailed
SageMaker HyperPod couldn't remove the extension from any of the cluster's nodes.
Type: String
Valid Values: `Creating | Active | CreateFailed | Updating | Deleting | DeleteFailed | Degraded | UpdateFailed`
Required: Yes

 ** ConfigurationValues **   <a name="sagemaker-Type-ExtensionDetails-ConfigurationValues"></a>
The configuration of the extension, as a JSON object serialized as a string. The configuration includes the default value of every setting that you didn't specify.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ExtensionDetails-CreationTime"></a>
The time when the extension was created.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ExtensionDetails-LastModifiedTime"></a>
The time when the extension was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ExtensionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ExtensionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ExtensionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ExtensionDetails)
