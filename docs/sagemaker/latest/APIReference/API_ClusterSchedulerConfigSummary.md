---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterSchedulerConfigSummary.html
---

# ClusterSchedulerConfigSummary
<a name="API_ClusterSchedulerConfigSummary"></a>

Summary of the cluster policy.

## Contents
<a name="API_ClusterSchedulerConfigSummary_Contents"></a>

 ** ClusterSchedulerConfigArn **   <a name="sagemaker-Type-ClusterSchedulerConfigSummary-ClusterSchedulerConfigArn"></a>
ARN of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:cluster-scheduler-config/[a-z0-9]{12}`
Required: Yes

 ** ClusterSchedulerConfigId **   <a name="sagemaker-Type-ClusterSchedulerConfigSummary-ClusterSchedulerConfigId"></a>
ID of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `[a-z0-9]{12}`
Required: Yes

 ** Name **   <a name="sagemaker-Type-ClusterSchedulerConfigSummary-Name"></a>
Name of the cluster policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** Status **   <a name="sagemaker-Type-ClusterSchedulerConfigSummary-Status"></a>
Status of the cluster policy.
Type: String
Valid Values: `Creating | CreateFailed | CreateRollbackFailed | Created | Updating | UpdateFailed | UpdateRollbackFailed | Updated | Deleting | DeleteFailed | DeleteRollbackFailed | Deleted`
Required: Yes

 ** ClusterArn **   <a name="sagemaker-Type-ClusterSchedulerConfigSummary-ClusterArn"></a>
ARN of the cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: No

 ** ClusterSchedulerConfigVersion **   <a name="sagemaker-Type-ClusterSchedulerConfigSummary-ClusterSchedulerConfigVersion"></a>
Version of the cluster policy.
Type: Integer
Required: No

## See Also
<a name="API_ClusterSchedulerConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterSchedulerConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterSchedulerConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterSchedulerConfigSummary)
