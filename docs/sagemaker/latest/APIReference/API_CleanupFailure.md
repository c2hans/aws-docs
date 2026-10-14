---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CleanupFailure.html
---

# CleanupFailure
<a name="API_CleanupFailure"></a>

The Amazon S3 output resources associated with an upstream step that the Cleanup step could not delete.

## Contents
<a name="API_CleanupFailure_Contents"></a>

 ** ErrorCode **   <a name="sagemaker-Type-CleanupFailure-ErrorCode"></a>
The error code that identifies why the Cleanup step could not delete the output resources associated with the upstream step.
Type: String
Valid Values: `ClientError | InternalFailure`
Required: No

 ** ErrorMessage **   <a name="sagemaker-Type-CleanupFailure-ErrorMessage"></a>
A message describing why the Cleanup step could not delete the output resources associated with the upstream step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** StepName **   <a name="sagemaker-Type-CleanupFailure-StepName"></a>
The name of the upstream step whose Amazon S3 output resources the Cleanup step could not delete.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CleanupFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CleanupFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CleanupFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CleanupFailure)
