---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_EventPredictionSummary.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# EventPredictionSummary
<a name="API_EventPredictionSummary"></a>

 Information about the summary of an event prediction.

## Contents
<a name="API_EventPredictionSummary_Contents"></a>

 ** detectorId **   <a name="FraudDetector-Type-EventPredictionSummary-detectorId"></a>
 The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** detectorVersionId **   <a name="FraudDetector-Type-EventPredictionSummary-detectorVersionId"></a>
 The detector version ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: No

 ** eventId **   <a name="FraudDetector-Type-EventPredictionSummary-eventId"></a>
 The event ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** eventTimestamp **   <a name="FraudDetector-Type-EventPredictionSummary-eventTimestamp"></a>
 The timestamp of the event.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** eventTypeName **   <a name="FraudDetector-Type-EventPredictionSummary-eventTypeName"></a>
 The event type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** predictionTimestamp **   <a name="FraudDetector-Type-EventPredictionSummary-predictionTimestamp"></a>
 The timestamp when the prediction was generated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

## See Also
<a name="API_EventPredictionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/EventPredictionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/EventPredictionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/EventPredictionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
