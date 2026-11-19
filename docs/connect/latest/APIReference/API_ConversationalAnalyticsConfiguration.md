---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ConversationalAnalyticsConfiguration.html
---

# ConversationalAnalyticsConfiguration

The conversational analytics configuration settings for a contact.

## Contents
<a name="API_ConversationalAnalyticsConfiguration_Contents"></a>

 ** ChannelConfiguration **   <a name="connect-Type-ConversationalAnalyticsConfiguration-ChannelConfiguration"></a>
The per-channel conversational analytics settings for the contact.
Type: [ContactLensChannelConfiguration](API_ContactLensChannelConfiguration.md) object
Required: No

 ** Enabled **   <a name="connect-Type-ConversationalAnalyticsConfiguration-Enabled"></a>
Specifies whether conversational analytics is enabled for the contact.
Type: Boolean
Required: No

 ** LanguageLocale **   <a name="connect-Type-ConversationalAnalyticsConfiguration-LanguageLocale"></a>
The language locale that conversational analytics uses to analyze the contact (for example, `en-US`).
Type: String
Required: No

 ** LanguageLocales **   <a name="connect-Type-ConversationalAnalyticsConfiguration-LanguageLocales"></a>
The language locales that conversational analytics uses to analyze the contact (for example, `en-US` and `es-ES`).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** RedactionConfiguration **   <a name="connect-Type-ConversationalAnalyticsConfiguration-RedactionConfiguration"></a>
The redaction configuration for the contact transcript.
Type: [ContactLensRedactionConfiguration](API_ContactLensRedactionConfiguration.md) object
Required: No

 ** SentimentConfiguration **   <a name="connect-Type-ConversationalAnalyticsConfiguration-SentimentConfiguration"></a>
The sentiment analysis configuration for the contact.
Type: [ContactLensSentimentConfiguration](API_ContactLensSentimentConfiguration.md) object
Required: No

 ** SummaryConfiguration **   <a name="connect-Type-ConversationalAnalyticsConfiguration-SummaryConfiguration"></a>
The summary configuration for the contact.
Type: [ContactLensSummaryConfiguration](API_ContactLensSummaryConfiguration.md) object
Required: No

## See Also
<a name="API_ConversationalAnalyticsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ConversationalAnalyticsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ConversationalAnalyticsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ConversationalAnalyticsConfiguration)
