---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_RealTimeAlertConfiguration.html
---

# RealTimeAlertConfiguration
<a name="API_media-pipelines-chime_RealTimeAlertConfiguration"></a>

A structure that contains the configuration settings for real-time alerts.

## Contents
<a name="API_media-pipelines-chime_RealTimeAlertConfiguration_Contents"></a>

 ** Disabled **   <a name="chimesdk-Type-media-pipelines-chime_RealTimeAlertConfiguration-Disabled"></a>
Turns off real-time alerts.
Type: Boolean
Required: No

 ** Rules **   <a name="chimesdk-Type-media-pipelines-chime_RealTimeAlertConfiguration-Rules"></a>
The rules in the alert. Rules specify the words or phrases that you want to be notified about.
Type: Array of [RealTimeAlertRule](API_media-pipelines-chime_RealTimeAlertRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

## See Also
<a name="API_media-pipelines-chime_RealTimeAlertConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/RealTimeAlertConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/RealTimeAlertConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/RealTimeAlertConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
