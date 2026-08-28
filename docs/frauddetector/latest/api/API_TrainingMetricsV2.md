---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_TrainingMetricsV2.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# TrainingMetricsV2
<a name="API_TrainingMetricsV2"></a>

 The training metrics details.

## Contents
<a name="API_TrainingMetricsV2_Contents"></a>

 ** ati **   <a name="FraudDetector-Type-TrainingMetricsV2-ati"></a>
 The Account Takeover Insights (ATI) model training metric details.
Type: [ATITrainingMetricsValue](API_ATITrainingMetricsValue.md) object
Required: No

 ** ofi **   <a name="FraudDetector-Type-TrainingMetricsV2-ofi"></a>
 The Online Fraud Insights (OFI) model training metric details.
Type: [OFITrainingMetricsValue](API_OFITrainingMetricsValue.md) object
Required: No

 ** tfi **   <a name="FraudDetector-Type-TrainingMetricsV2-tfi"></a>
 The Transaction Fraud Insights (TFI) model training metric details.
Type: [TFITrainingMetricsValue](API_TFITrainingMetricsValue.md) object
Required: No

## See Also
<a name="API_TrainingMetricsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/TrainingMetricsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/TrainingMetricsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/TrainingMetricsV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
