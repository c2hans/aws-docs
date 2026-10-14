---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ForEachStepMetadata.html
---

# ForEachStepMetadata
<a name="API_ForEachStepMetadata"></a>

The status, the iteration-step counts, and the selector information for a ForEach step execution.

## Contents
<a name="API_ForEachStepMetadata_Contents"></a>

 ** FailedStepCount **   <a name="sagemaker-Type-ForEachStepMetadata-FailedStepCount"></a>
The number of iteration steps that failed.
Type: Integer
Required: No

 ** InputItemCount **   <a name="sagemaker-Type-ForEachStepMetadata-InputItemCount"></a>
The number of input items that the ForEach step iterates over.
Type: Integer
Required: No

 ** Selector **   <a name="sagemaker-Type-ForEachStepMetadata-Selector"></a>
Identifies the body step and iteration selected within the ForEach step.
Type: [ForEachSelectorResult](API_ForEachSelectorResult.md) object
Required: No

 ** Status **   <a name="sagemaker-Type-ForEachStepMetadata-Status"></a>
The status of the ForEach step execution.
Type: String
Valid Values: `Succeeded | Failed | Stopped`
Required: No

 ** StoppedStepCount **   <a name="sagemaker-Type-ForEachStepMetadata-StoppedStepCount"></a>
The number of iteration steps that were stopped.
Type: Integer
Required: No

 ** SucceededStepCount **   <a name="sagemaker-Type-ForEachStepMetadata-SucceededStepCount"></a>
The number of iteration steps that completed successfully.
Type: Integer
Required: No

 ** TotalStepCount **   <a name="sagemaker-Type-ForEachStepMetadata-TotalStepCount"></a>
The total number of steps generated across all iterations of the ForEach step.
Type: Integer
Required: No

## See Also
<a name="API_ForEachStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ForEachStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ForEachStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ForEachStepMetadata)
