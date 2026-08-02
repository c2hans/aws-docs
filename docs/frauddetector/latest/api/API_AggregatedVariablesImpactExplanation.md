---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_AggregatedVariablesImpactExplanation.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# AggregatedVariablesImpactExplanation
<a name="API_AggregatedVariablesImpactExplanation"></a>

 The details of the impact of aggregated variables on the prediction score.

Account Takeover Insights (ATI) model uses the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, the model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user`.

## Contents
<a name="API_AggregatedVariablesImpactExplanation_Contents"></a>

 ** eventVariableNames **   <a name="FraudDetector-Type-AggregatedVariablesImpactExplanation-eventVariableNames"></a>
 The names of all the event variables that were used to derive the aggregated variables.
Type: Array of strings
Required: No

 ** logOddsImpact **   <a name="FraudDetector-Type-AggregatedVariablesImpactExplanation-logOddsImpact"></a>
 The raw, uninterpreted value represented as log-odds of the fraud. These values are usually between -10 to \+10, but range from -infinity to \+infinity.
+ A positive value indicates that the variables drove the risk score up.
+ A negative value indicates that the variables drove the risk score down.
Type: Float
Required: No

 ** relativeImpact **   <a name="FraudDetector-Type-AggregatedVariablesImpactExplanation-relativeImpact"></a>
 The relative impact of the aggregated variables in terms of magnitude on the prediction scores.
Type: String
Required: No

## See Also
<a name="API_AggregatedVariablesImpactExplanation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/AggregatedVariablesImpactExplanation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/AggregatedVariablesImpactExplanation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/AggregatedVariablesImpactExplanation)
