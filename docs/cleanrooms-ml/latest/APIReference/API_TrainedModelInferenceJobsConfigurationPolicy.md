---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainedModelInferenceJobsConfigurationPolicy.html
---

# TrainedModelInferenceJobsConfigurationPolicy
<a name="API_TrainedModelInferenceJobsConfigurationPolicy"></a>

Provides configuration information for the trained model inference job.

## Contents
<a name="API_TrainedModelInferenceJobsConfigurationPolicy_Contents"></a>

 ** containerLogs **   <a name="API-Type-TrainedModelInferenceJobsConfigurationPolicy-containerLogs"></a>
The logs container for the trained model inference job.
Type: Array of [LogsConfigurationPolicy](API_LogsConfigurationPolicy.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** maxOutputSize **   <a name="API-Type-TrainedModelInferenceJobsConfigurationPolicy-maxOutputSize"></a>
The maximum allowed size of the output of the trained model inference job.
Type: [TrainedModelInferenceMaxOutputSize](API_TrainedModelInferenceMaxOutputSize.md) object
Required: No

## See Also
<a name="API_TrainedModelInferenceJobsConfigurationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/TrainedModelInferenceJobsConfigurationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/TrainedModelInferenceJobsConfigurationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/TrainedModelInferenceJobsConfigurationPolicy)
