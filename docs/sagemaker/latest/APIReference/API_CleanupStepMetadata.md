---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CleanupStepMetadata.html
---

# CleanupStepMetadata
<a name="API_CleanupStepMetadata"></a>

The cleanup outcomes for Amazon S3 output resources associated with upstream steps.

## Contents
<a name="API_CleanupStepMetadata_Contents"></a>

 ** CleanedSteps **   <a name="sagemaker-Type-CleanupStepMetadata-CleanedSteps"></a>
The names of upstream steps whose Amazon S3 output resources the Cleanup step deleted successfully.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** FailedSteps **   <a name="sagemaker-Type-CleanupStepMetadata-FailedSteps"></a>
The upstream steps whose Amazon S3 output resources the Cleanup step could not delete.
Type: Array of [CleanupFailure](API_CleanupFailure.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** SkippedSteps **   <a name="sagemaker-Type-CleanupStepMetadata-SkippedSteps"></a>
The names of upstream steps that the Cleanup step skipped. The Cleanup step skips a step when the output properties needed to locate its resources are unavailable.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CleanupStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CleanupStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CleanupStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CleanupStepMetadata)
