---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MLPaymentConfig.html
---

# MLPaymentConfig
<a name="API_MLPaymentConfig"></a>

An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.

## Contents
<a name="API_MLPaymentConfig_Contents"></a>

 ** modelInference **   <a name="API-Type-MLPaymentConfig-modelInference"></a>
The payment responsibilities accepted by the member for model inference.
Type: [ModelInferencePaymentConfig](API_ModelInferencePaymentConfig.md) object
Required: No

 ** modelTraining **   <a name="API-Type-MLPaymentConfig-modelTraining"></a>
The payment responsibilities accepted by the member for model training.
Type: [ModelTrainingPaymentConfig](API_ModelTrainingPaymentConfig.md) object
Required: No

 ** syntheticDataGeneration **   <a name="API-Type-MLPaymentConfig-syntheticDataGeneration"></a>
The payment configuration for machine learning synthetic data generation.
Type: [SyntheticDataGenerationPaymentConfig](API_SyntheticDataGenerationPaymentConfig.md) object
Required: No

## See Also
<a name="API_MLPaymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MLPaymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MLPaymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MLPaymentConfig)
