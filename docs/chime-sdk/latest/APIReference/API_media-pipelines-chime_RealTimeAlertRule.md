---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_RealTimeAlertRule.html
---

# RealTimeAlertRule
<a name="API_media-pipelines-chime_RealTimeAlertRule"></a>

Specifies the words or phrases that trigger an alert.

## Contents
<a name="API_media-pipelines-chime_RealTimeAlertRule_Contents"></a>

 ** Type **   <a name="chimesdk-Type-media-pipelines-chime_RealTimeAlertRule-Type"></a>
The type of alert rule.
Type: String
Valid Values: `KeywordMatch | Sentiment | IssueDetection`
Required: Yes

 ** IssueDetectionConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_RealTimeAlertRule-IssueDetectionConfiguration"></a>
Specifies the issue detection settings for a real-time alert rule.
Type: [IssueDetectionConfiguration](API_media-pipelines-chime_IssueDetectionConfiguration.md) object
Required: No

 ** KeywordMatchConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_RealTimeAlertRule-KeywordMatchConfiguration"></a>
Specifies the settings for matching the keywords in a real-time alert rule.
Type: [KeywordMatchConfiguration](API_media-pipelines-chime_KeywordMatchConfiguration.md) object
Required: No

 ** SentimentConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_RealTimeAlertRule-SentimentConfiguration"></a>
Specifies the settings for predicting sentiment in a real-time alert rule.
Type: [SentimentConfiguration](API_media-pipelines-chime_SentimentConfiguration.md) object
Required: No

## See Also
<a name="API_media-pipelines-chime_RealTimeAlertRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/RealTimeAlertRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/RealTimeAlertRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/RealTimeAlertRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
