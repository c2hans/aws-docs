---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_EmailOverviewAIAgentConfiguration.html
---

# EmailOverviewAIAgentConfiguration
<a name="API_amazon-q-connect_EmailOverviewAIAgentConfiguration"></a>

Configuration settings for the EMAIL\_OVERVIEW AI agent including prompt ID and locale settings.

## Contents
<a name="API_amazon-q-connect_EmailOverviewAIAgentConfiguration_Contents"></a>

 ** emailOverviewAIPromptId **   <a name="connect-Type-amazon-q-connect_EmailOverviewAIAgentConfiguration-emailOverviewAIPromptId"></a>
The ID of the System AI prompt used for generating structured email conversation summaries.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** locale **   <a name="connect-Type-amazon-q-connect_EmailOverviewAIAgentConfiguration-locale"></a>
The locale setting for language-specific email overview processing (for example, en\_US, es\_ES).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_EmailOverviewAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/EmailOverviewAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/EmailOverviewAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/EmailOverviewAIAgentConfiguration)
