---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_IngestedEventStatistics.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# IngestedEventStatistics
<a name="API_IngestedEventStatistics"></a>

Data about the stored events.

## Contents
<a name="API_IngestedEventStatistics_Contents"></a>

 ** eventDataSizeInBytes **   <a name="FraudDetector-Type-IngestedEventStatistics-eventDataSizeInBytes"></a>
The total size of the stored events.
Type: Long
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-IngestedEventStatistics-lastUpdatedTime"></a>
Timestamp of when the stored event was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** leastRecentEvent **   <a name="FraudDetector-Type-IngestedEventStatistics-leastRecentEvent"></a>
The oldest stored event.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** mostRecentEvent **   <a name="FraudDetector-Type-IngestedEventStatistics-mostRecentEvent"></a>
The newest stored event.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** numberOfEvents **   <a name="FraudDetector-Type-IngestedEventStatistics-numberOfEvents"></a>
The number of stored events.
Type: Long
Required: No

## See Also
<a name="API_IngestedEventStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/IngestedEventStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/IngestedEventStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/IngestedEventStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
