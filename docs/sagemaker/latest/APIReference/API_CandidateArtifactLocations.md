---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateArtifactLocations.html
---

# CandidateArtifactLocations
<a name="API_CandidateArtifactLocations"></a>

The location of artifacts for an AutoML candidate job.

## Contents
<a name="API_CandidateArtifactLocations_Contents"></a>

 ** Explainability **   <a name="sagemaker-Type-CandidateArtifactLocations-Explainability"></a>
The Amazon S3 prefix to the explainability artifacts generated for the AutoML candidate.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** BacktestResults **   <a name="sagemaker-Type-CandidateArtifactLocations-BacktestResults"></a>
The Amazon S3 prefix to the accuracy metrics and the inference results observed over the testing window. Available only for the time-series forecasting problem type.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ModelInsights **   <a name="sagemaker-Type-CandidateArtifactLocations-ModelInsights"></a>
The Amazon S3 prefix to the model insight artifacts generated for the AutoML candidate.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_CandidateArtifactLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CandidateArtifactLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CandidateArtifactLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CandidateArtifactLocations)
