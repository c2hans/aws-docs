---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_WarmPoolStatus.html
---

# WarmPoolStatus
<a name="API_WarmPoolStatus"></a>

Status and billing information about the warm pool.

## Contents
<a name="API_WarmPoolStatus_Contents"></a>

 ** Status **   <a name="sagemaker-Type-WarmPoolStatus-Status"></a>
The status of the warm pool.
+  `InUse`: The warm pool is in use for the training job.
+  `Available`: The warm pool is available to reuse for a matching training job.
+  `Reused`: The warm pool moved to a matching training job for reuse.
+  `Terminated`: The warm pool is no longer available. Warm pools are unavailable if they are terminated by a user, terminated for a patch update, or terminated for exceeding the specified `KeepAlivePeriodInSeconds`.
Type: String
Valid Values: `Available | Terminated | Reused | InUse`
Required: Yes

 ** ResourceRetainedBillableTimeInSeconds **   <a name="sagemaker-Type-WarmPoolStatus-ResourceRetainedBillableTimeInSeconds"></a>
The billable time in seconds used by the warm pool. Billable time refers to the absolute wall-clock time.
Multiply `ResourceRetainedBillableTimeInSeconds` by the number of instances (`InstanceCount`) in your training cluster to get the total compute time SageMaker bills you if you run warm pool training. The formula is as follows: `ResourceRetainedBillableTimeInSeconds * InstanceCount`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ReusedByJob **   <a name="sagemaker-Type-WarmPoolStatus-ReusedByJob"></a>
The name of the matching training job that reused the warm pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_WarmPoolStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/WarmPoolStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/WarmPoolStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/WarmPoolStatus)
