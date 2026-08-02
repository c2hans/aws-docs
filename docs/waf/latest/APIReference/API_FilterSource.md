---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_FilterSource.html
---

# FilterSource
<a name="API_FilterSource"></a>

Information about the bot filter that was applied to the request. This structure is populated in the response when you filter by bot category, organization, or name.

## Contents
<a name="API_FilterSource_Contents"></a>

 ** BotCategory **   <a name="WAF-Type-FilterSource-BotCategory"></a>
The bot category that was used to filter the results. For example, `ai` or `search_engine`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** BotName **   <a name="WAF-Type-FilterSource-BotName"></a>
The bot name that was used to filter the results. For example, `gptbot` or `googlebot`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** BotOrganization **   <a name="WAF-Type-FilterSource-BotOrganization"></a>
The bot organization that was used to filter the results. For example, `OpenAI` or `Google`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_FilterSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/FilterSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/FilterSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/FilterSource)
