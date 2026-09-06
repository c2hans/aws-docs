---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EMRStepMetadata.html
---

# EMRStepMetadata
<a name="API_EMRStepMetadata"></a>

The configurations and outcomes of an Amazon EMR step execution.

## Contents
<a name="API_EMRStepMetadata_Contents"></a>

 ** ClusterId **   <a name="sagemaker-Type-EMRStepMetadata-ClusterId"></a>
The identifier of the EMR cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** LogFilePath **   <a name="sagemaker-Type-EMRStepMetadata-LogFilePath"></a>
The path to the log file where the cluster step's failure root cause is recorded.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** StepId **   <a name="sagemaker-Type-EMRStepMetadata-StepId"></a>
The identifier of the EMR cluster step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** StepName **   <a name="sagemaker-Type-EMRStepMetadata-StepName"></a>
The name of the EMR cluster step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_EMRStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EMRStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EMRStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EMRStepMetadata)
