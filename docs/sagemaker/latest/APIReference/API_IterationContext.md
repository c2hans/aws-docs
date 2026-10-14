---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IterationContext.html
---

# IterationContext
<a name="API_IterationContext"></a>

The context for an iteration of a ForEach step.

## Contents
<a name="API_IterationContext_Contents"></a>

 ** Index **   <a name="sagemaker-Type-IterationContext-Index"></a>
The index of the iteration within the ForEach step.
Type: Integer
Required: No

 ** Item **   <a name="sagemaker-Type-IterationContext-Item"></a>
The input item that is being processed in this iteration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12800.
Required: No

 ** ParentStepName **   <a name="sagemaker-Type-IterationContext-ParentStepName"></a>
The name of the ForEach step that generated this iteration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_IterationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/IterationContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/IterationContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/IterationContext)
