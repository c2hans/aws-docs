---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanFilter.html
---

# TrainingPlanFilter
<a name="API_TrainingPlanFilter"></a>

A filter to apply when listing or searching for training plans.

For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.

## Contents
<a name="API_TrainingPlanFilter_Contents"></a>

 ** Name **   <a name="sagemaker-Type-TrainingPlanFilter-Name"></a>
The name of the filter field (e.g., Status, InstanceType).
Type: String
Valid Values: `Status`
Required: Yes

 ** Value **   <a name="sagemaker-Type-TrainingPlanFilter-Value"></a>
The value to filter by for the specified field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: Yes

## See Also
<a name="API_TrainingPlanFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingPlanFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingPlanFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingPlanFilter)
