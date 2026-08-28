---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_VariableImpactExplanation.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# VariableImpactExplanation
<a name="API_VariableImpactExplanation"></a>

 The details of the event variable's impact on the prediction score.

## Contents
<a name="API_VariableImpactExplanation_Contents"></a>

 ** eventVariableName **   <a name="FraudDetector-Type-VariableImpactExplanation-eventVariableName"></a>
 The event variable name.
Type: String
Required: No

 ** logOddsImpact **   <a name="FraudDetector-Type-VariableImpactExplanation-logOddsImpact"></a>
 The raw, uninterpreted value represented as log-odds of the fraud. These values are usually between -10 to \+10, but range from - infinity to \+ infinity.
+ A positive value indicates that the variable drove the risk score up.
+ A negative value indicates that the variable drove the risk score down.
Type: Float
Required: No

 ** relativeImpact **   <a name="FraudDetector-Type-VariableImpactExplanation-relativeImpact"></a>
 The event variable's relative impact in terms of magnitude on the prediction scores. The relative impact values consist of a numerical rating (0-5, 5 being the highest) and direction (increased/decreased) impact of the fraud risk.
Type: String
Required: No

## See Also
<a name="API_VariableImpactExplanation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/VariableImpactExplanation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/VariableImpactExplanation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/VariableImpactExplanation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
