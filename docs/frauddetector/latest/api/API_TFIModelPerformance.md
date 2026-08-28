---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_TFIModelPerformance.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# TFIModelPerformance
<a name="API_TFIModelPerformance"></a>

 The Transaction Fraud Insights (TFI) model performance score.

## Contents
<a name="API_TFIModelPerformance_Contents"></a>

 ** auc **   <a name="FraudDetector-Type-TFIModelPerformance-auc"></a>
 The area under the curve (auc). This summarizes the total positive rate (tpr) and false positive rate (FPR) across all possible model score thresholds.
Type: Float
Required: No

 ** uncertaintyRange **   <a name="FraudDetector-Type-TFIModelPerformance-uncertaintyRange"></a>
 Indicates the range of area under curve (auc) expected from the TFI model. A range greater than 0.1 indicates higher model uncertainity.
Type: [UncertaintyRange](API_UncertaintyRange.md) object
Required: No

## See Also
<a name="API_TFIModelPerformance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/TFIModelPerformance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/TFIModelPerformance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/TFIModelPerformance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
