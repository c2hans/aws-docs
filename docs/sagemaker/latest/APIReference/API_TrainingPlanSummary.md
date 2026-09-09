---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanSummary.html
---

# TrainingPlanSummary
<a name="API_TrainingPlanSummary"></a>

Details of the training plan.

For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.

## Contents
<a name="API_TrainingPlanSummary_Contents"></a>

 ** Status **   <a name="sagemaker-Type-TrainingPlanSummary-Status"></a>
The current status of the training plan (e.g., Pending, Active, Expired). To see the complete list of status values available for a training plan, refer to the `Status` attribute within the ` [TrainingPlanSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanSummary.html) ` object.
Type: String
Valid Values: `Pending | Active | Scheduled | Expired | Failed`
Required: Yes

 ** TrainingPlanArn **   <a name="sagemaker-Type-TrainingPlanSummary-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the training plan.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: Yes

 ** TrainingPlanName **   <a name="sagemaker-Type-TrainingPlanSummary-TrainingPlanName"></a>
The name of the training plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** AvailableInstanceCount **   <a name="sagemaker-Type-TrainingPlanSummary-AvailableInstanceCount"></a>
The number of instances currently available for use in this training plan.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** CurrencyCode **   <a name="sagemaker-Type-TrainingPlanSummary-CurrencyCode"></a>
The currency code for the upfront fee (e.g., USD).
Type: String
Required: No

 ** DurationHours **   <a name="sagemaker-Type-TrainingPlanSummary-DurationHours"></a>
The number of whole hours in the total duration for this training plan.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 87600.
Required: No

 ** DurationMinutes **   <a name="sagemaker-Type-TrainingPlanSummary-DurationMinutes"></a>
The additional minutes beyond whole hours in the total duration for this training plan.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 59.
Required: No

 ** InUseInstanceCount **   <a name="sagemaker-Type-TrainingPlanSummary-InUseInstanceCount"></a>
The number of instances currently in use from this training plan.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ReservedCapacitySummaries **   <a name="sagemaker-Type-TrainingPlanSummary-ReservedCapacitySummaries"></a>
A list of reserved capacities associated with this training plan, including details such as instance types, counts, and availability zones.
Type: Array of [ReservedCapacitySummary](API_ReservedCapacitySummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** StatusMessage **   <a name="sagemaker-Type-TrainingPlanSummary-StatusMessage"></a>
A message providing additional information about the current status of the training plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** TargetResources **   <a name="sagemaker-Type-TrainingPlanSummary-TargetResources"></a>
The target resources (e.g., training jobs, HyperPod clusters, Endpoints, Studio apps) that can use this training plan.
Training plans are specific to their target resource.
+ A training plan designed for SageMaker training jobs can only be used to schedule and run training jobs.
+ A training plan for HyperPod clusters can be used exclusively to provide compute resources to a cluster's instance group.
+ A training plan for SageMaker endpoints can be used exclusively to provide compute resources to SageMaker endpoints for model deployment.
+ A training plan for Studio apps can be used to launch JupyterLab and Code Editor apps on reserved training plan capacity.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `training-job | hyperpod-cluster | endpoint | studio-apps`
Required: No

 ** TotalInstanceCount **   <a name="sagemaker-Type-TrainingPlanSummary-TotalInstanceCount"></a>
The total number of instances reserved in this training plan.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TotalUltraServerCount **   <a name="sagemaker-Type-TrainingPlanSummary-TotalUltraServerCount"></a>
The total number of UltraServers allocated to this training plan.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** UpfrontFee **   <a name="sagemaker-Type-TrainingPlanSummary-UpfrontFee"></a>
The upfront fee for the training plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_TrainingPlanSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingPlanSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingPlanSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingPlanSummary)
