---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentRollingUpdatePolicy.html
---

# InferenceComponentRollingUpdatePolicy
<a name="API_InferenceComponentRollingUpdatePolicy"></a>

Specifies a rolling deployment strategy for updating a SageMaker AI inference component.

## Contents
<a name="API_InferenceComponentRollingUpdatePolicy_Contents"></a>

 ** MaximumBatchSize **   <a name="sagemaker-Type-InferenceComponentRollingUpdatePolicy-MaximumBatchSize"></a>
The batch size for each rolling step in the deployment process. For each step, SageMaker AI provisions capacity on the new endpoint fleet, routes traffic to that fleet, and terminates capacity on the old endpoint fleet. The value must be between 5% to 50% of the copy count of the inference component.
Type: [InferenceComponentCapacitySize](API_InferenceComponentCapacitySize.md) object
Required: Yes

 ** WaitIntervalInSeconds **   <a name="sagemaker-Type-InferenceComponentRollingUpdatePolicy-WaitIntervalInSeconds"></a>
The length of the baking period, during which SageMaker AI monitors alarms for each batch on the new fleet.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: Yes

 ** MaximumExecutionTimeoutInSeconds **   <a name="sagemaker-Type-InferenceComponentRollingUpdatePolicy-MaximumExecutionTimeoutInSeconds"></a>
The time limit for the total deployment. Exceeding this limit causes a timeout.
Type: Integer
Valid Range: Minimum value of 600. Maximum value of 28800.
Required: No

 ** RollbackMaximumBatchSize **   <a name="sagemaker-Type-InferenceComponentRollingUpdatePolicy-RollbackMaximumBatchSize"></a>
The batch size for a rollback to the old endpoint fleet. If this field is absent, the value is set to the default, which is 100% of the total capacity. When the default is used, SageMaker AI provisions the entire capacity of the old fleet at once during rollback.
Type: [InferenceComponentCapacitySize](API_InferenceComponentCapacitySize.md) object
Required: No

## See Also
<a name="API_InferenceComponentRollingUpdatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentRollingUpdatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentRollingUpdatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentRollingUpdatePolicy)
