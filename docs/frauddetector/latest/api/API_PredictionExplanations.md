---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_PredictionExplanations.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# PredictionExplanations
<a name="API_PredictionExplanations"></a>

 The prediction explanations that provide insight into how each event variable impacted the model version's fraud prediction score.

## Contents
<a name="API_PredictionExplanations_Contents"></a>

 ** aggregatedVariablesImpactExplanations **   <a name="FraudDetector-Type-PredictionExplanations-aggregatedVariablesImpactExplanations"></a>
 The details of the aggregated variables impact on the prediction score.
Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user`.
Type: Array of [AggregatedVariablesImpactExplanation](API_AggregatedVariablesImpactExplanation.md) objects
Required: No

 ** variableImpactExplanations **   <a name="FraudDetector-Type-PredictionExplanations-variableImpactExplanations"></a>
 The details of the event variable's impact on the prediction score.
Type: Array of [VariableImpactExplanation](API_VariableImpactExplanation.md) objects
Required: No

## See Also
<a name="API_PredictionExplanations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/PredictionExplanations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/PredictionExplanations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/PredictionExplanations)
