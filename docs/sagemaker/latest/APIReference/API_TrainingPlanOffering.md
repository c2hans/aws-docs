---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanOffering.html
---

# TrainingPlanOffering
<a name="API_TrainingPlanOffering"></a>

Details about a training plan offering.

For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.

## Contents
<a name="API_TrainingPlanOffering_Contents"></a>

 ** TargetResources **   <a name="sagemaker-Type-TrainingPlanOffering-TargetResources"></a>
The target resources (e.g., SageMaker Training Jobs, SageMaker HyperPod, SageMaker Endpoints, Studio apps) for this training plan offering.
Training plans are specific to their target resource.
+ A training plan designed for SageMaker training jobs can only be used to schedule and run training jobs.
+ A training plan for HyperPod clusters can be used exclusively to provide compute resources to a cluster's instance group.
+ A training plan for SageMaker endpoints can be used exclusively to provide compute resources to SageMaker endpoints for model deployment.
+ A training plan for Studio apps can be used to launch JupyterLab and Code Editor apps on reserved training plan capacity.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `training-job | hyperpod-cluster | endpoint | studio-apps`
Required: Yes

 ** TrainingPlanOfferingId **   <a name="sagemaker-Type-TrainingPlanOffering-TrainingPlanOfferingId"></a>
The unique identifier for this training plan offering.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9\-]+`
Required: Yes

 ** CurrencyCode **   <a name="sagemaker-Type-TrainingPlanOffering-CurrencyCode"></a>
The currency code for the upfront fee (e.g., USD).
Type: String
Required: No

 ** DurationHours **   <a name="sagemaker-Type-TrainingPlanOffering-DurationHours"></a>
The number of whole hours in the total duration for this training plan offering.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 87600.
Required: No

 ** DurationMinutes **   <a name="sagemaker-Type-TrainingPlanOffering-DurationMinutes"></a>
The additional minutes beyond whole hours in the total duration for this training plan offering.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 59.
Required: No

 ** ReservedCapacityOfferings **   <a name="sagemaker-Type-TrainingPlanOffering-ReservedCapacityOfferings"></a>
A list of reserved capacity offerings associated with this training plan offering.
Type: Array of [ReservedCapacityOffering](API_ReservedCapacityOffering.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** UpfrontFee **   <a name="sagemaker-Type-TrainingPlanOffering-UpfrontFee"></a>
The upfront fee for this training plan offering.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_TrainingPlanOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingPlanOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingPlanOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingPlanOffering)
