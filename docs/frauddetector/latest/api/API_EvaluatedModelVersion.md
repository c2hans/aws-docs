---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_EvaluatedModelVersion.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# EvaluatedModelVersion
<a name="API_EvaluatedModelVersion"></a>

 The model version evaluated for generating prediction.

## Contents
<a name="API_EvaluatedModelVersion_Contents"></a>

 ** evaluations **   <a name="FraudDetector-Type-EvaluatedModelVersion-evaluations"></a>
 Evaluations generated for the model version.
Type: Array of [ModelVersionEvaluation](API_ModelVersionEvaluation.md) objects
Required: No

 ** modelId **   <a name="FraudDetector-Type-EvaluatedModelVersion-modelId"></a>
 The model ID.
Type: String
Required: No

 ** modelType **   <a name="FraudDetector-Type-EvaluatedModelVersion-modelType"></a>
The model type.
Valid values: `ONLINE_FRAUD_INSIGHTS` \| `TRANSACTION_FRAUD_INSIGHTS`
Type: String
Required: No

 ** modelVersion **   <a name="FraudDetector-Type-EvaluatedModelVersion-modelVersion"></a>
 The model version.
Type: String
Required: No

## See Also
<a name="API_EvaluatedModelVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/EvaluatedModelVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/EvaluatedModelVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/EvaluatedModelVersion)
