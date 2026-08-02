---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingFeatureStoreOutput.html
---

# ProcessingFeatureStoreOutput
<a name="API_ProcessingFeatureStoreOutput"></a>

Configuration for processing job outputs in Amazon SageMaker Feature Store.

## Contents
<a name="API_ProcessingFeatureStoreOutput_Contents"></a>

 ** FeatureGroupName **   <a name="sagemaker-Type-ProcessingFeatureStoreOutput-FeatureGroupName"></a>
The name of the Amazon SageMaker FeatureGroup to use as the destination for processing job output. Note that your processing script is responsible for putting records into your Feature Store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`
Required: Yes

## See Also
<a name="API_ProcessingFeatureStoreOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProcessingFeatureStoreOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProcessingFeatureStoreOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProcessingFeatureStoreOutput)
