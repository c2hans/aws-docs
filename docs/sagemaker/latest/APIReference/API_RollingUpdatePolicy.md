---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RollingUpdatePolicy.html
---

# RollingUpdatePolicy
<a name="API_RollingUpdatePolicy"></a>

Specifies a rolling deployment strategy for updating a SageMaker endpoint.

## Contents
<a name="API_RollingUpdatePolicy_Contents"></a>

 ** MaximumBatchSize **   <a name="sagemaker-Type-RollingUpdatePolicy-MaximumBatchSize"></a>
Batch size for each rolling step to provision capacity and turn on traffic on the new endpoint fleet, and terminate capacity on the old endpoint fleet. Value must be between 5% to 50% of the variant's total instance count.
Type: [CapacitySize](API_CapacitySize.md) object
Required: Yes

 ** WaitIntervalInSeconds **   <a name="sagemaker-Type-RollingUpdatePolicy-WaitIntervalInSeconds"></a>
The length of the baking period, during which SageMaker monitors alarms for each batch on the new fleet.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: Yes

 ** MaximumExecutionTimeoutInSeconds **   <a name="sagemaker-Type-RollingUpdatePolicy-MaximumExecutionTimeoutInSeconds"></a>
The time limit for the total deployment. Exceeding this limit causes a timeout.
Type: Integer
Valid Range: Minimum value of 600. Maximum value of 28800.
Required: No

 ** RollbackMaximumBatchSize **   <a name="sagemaker-Type-RollingUpdatePolicy-RollbackMaximumBatchSize"></a>
Batch size for rollback to the old endpoint fleet. Each rolling step to provision capacity and turn on traffic on the old endpoint fleet, and terminate capacity on the new endpoint fleet. If this field is absent, the default value will be set to 100% of total capacity which means to bring up the whole capacity of the old fleet at once during rollback.
Type: [CapacitySize](API_CapacitySize.md) object
Required: No

## See Also
<a name="API_RollingUpdatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RollingUpdatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RollingUpdatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RollingUpdatePolicy)
