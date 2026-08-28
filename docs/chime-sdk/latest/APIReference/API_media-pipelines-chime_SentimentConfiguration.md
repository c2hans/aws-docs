---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SentimentConfiguration.html
---

# SentimentConfiguration
<a name="API_media-pipelines-chime_SentimentConfiguration"></a>

A structure that contains the configuration settings for a sentiment analysis task.

## Contents
<a name="API_media-pipelines-chime_SentimentConfiguration_Contents"></a>

 ** RuleName **   <a name="chimesdk-Type-media-pipelines-chime_SentimentConfiguration-RuleName"></a>
The name of the rule in the sentiment configuration.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** SentimentType **   <a name="chimesdk-Type-media-pipelines-chime_SentimentConfiguration-SentimentType"></a>
The type of sentiment, `POSITIVE`, `NEGATIVE`, or `NEUTRAL`.
Type: String
Valid Values: `NEGATIVE`
Required: Yes

 ** TimePeriod **   <a name="chimesdk-Type-media-pipelines-chime_SentimentConfiguration-TimePeriod"></a>
Specifies the analysis interval.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 1800.
Required: Yes

## See Also
<a name="API_media-pipelines-chime_SentimentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/SentimentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/SentimentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/SentimentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
