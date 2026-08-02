---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ComputeQuotaSummary.html
---

# ComputeQuotaSummary
<a name="API_ComputeQuotaSummary"></a>

Summary of the compute allocation definition.

## Contents
<a name="API_ComputeQuotaSummary_Contents"></a>

 ** ComputeQuotaArn **   <a name="sagemaker-Type-ComputeQuotaSummary-ComputeQuotaArn"></a>
ARN of the compute allocation definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:compute-quota/[a-z0-9]{12}`
Required: Yes

 ** ComputeQuotaId **   <a name="sagemaker-Type-ComputeQuotaSummary-ComputeQuotaId"></a>
ID of the compute allocation definition.
Type: String
Pattern: `[a-z0-9]{12}`
Required: Yes

 ** ComputeQuotaTarget **   <a name="sagemaker-Type-ComputeQuotaSummary-ComputeQuotaTarget"></a>
The target entity to allocate compute resources to.
Type: [ComputeQuotaTarget](API_ComputeQuotaTarget.md) object
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-ComputeQuotaSummary-CreationTime"></a>
Creation time of the compute allocation definition.
Type: Timestamp
Required: Yes

 ** Name **   <a name="sagemaker-Type-ComputeQuotaSummary-Name"></a>
Name of the compute allocation definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** Status **   <a name="sagemaker-Type-ComputeQuotaSummary-Status"></a>
Status of the compute allocation definition.
Type: String
Valid Values: `Creating | CreateFailed | CreateRollbackFailed | Created | Updating | UpdateFailed | UpdateRollbackFailed | Updated | Deleting | DeleteFailed | DeleteRollbackFailed | Deleted`
Required: Yes

 ** ActivationState **   <a name="sagemaker-Type-ComputeQuotaSummary-ActivationState"></a>
The state of the compute allocation being described. Use to enable or disable compute allocation.
Default is `Enabled`.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** ClusterArn **   <a name="sagemaker-Type-ComputeQuotaSummary-ClusterArn"></a>
ARN of the cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: No

 ** ComputeQuotaConfig **   <a name="sagemaker-Type-ComputeQuotaSummary-ComputeQuotaConfig"></a>
Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks.
Type: [ComputeQuotaConfig](API_ComputeQuotaConfig.md) object
Required: No

 ** ComputeQuotaVersion **   <a name="sagemaker-Type-ComputeQuotaSummary-ComputeQuotaVersion"></a>
Version of the compute allocation definition.
Type: Integer
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ComputeQuotaSummary-LastModifiedTime"></a>
Last modified time of the compute allocation definition.
Type: Timestamp
Required: No

## See Also
<a name="API_ComputeQuotaSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ComputeQuotaSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ComputeQuotaSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ComputeQuotaSummary)
