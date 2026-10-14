---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EMRServerlessStepMetadata.html
---

# EMRServerlessStepMetadata
<a name="API_EMRServerlessStepMetadata"></a>

The configurations and outcomes of an Amazon EMR Serverless step execution.

## Contents
<a name="API_EMRServerlessStepMetadata_Contents"></a>

 ** ApplicationId **   <a name="sagemaker-Type-EMRServerlessStepMetadata-ApplicationId"></a>
The identifier of the Amazon EMR Serverless application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-z]+.*`
Required: No

 ** JobRunId **   <a name="sagemaker-Type-EMRServerlessStepMetadata-JobRunId"></a>
The identifier of the Amazon EMR Serverless job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-z]+.*`
Required: No

 ** JobRunName **   <a name="sagemaker-Type-EMRServerlessStepMetadata-JobRunName"></a>
The name of the Amazon EMR Serverless job run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** LogFilePath **   <a name="sagemaker-Type-EMRServerlessStepMetadata-LogFilePath"></a>
The path to the log file for the Amazon EMR Serverless job run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_EMRServerlessStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EMRServerlessStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EMRServerlessStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EMRServerlessStepMetadata)
