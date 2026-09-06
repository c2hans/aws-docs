---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BlockedPhrasesConfiguration.html
---

# BlockedPhrasesConfiguration
<a name="API_BlockedPhrasesConfiguration"></a>

Provides information about the phrases blocked from chat by your chat control configuration.

## Contents
<a name="API_BlockedPhrasesConfiguration_Contents"></a>

 ** blockedPhrases **   <a name="qbusiness-Type-BlockedPhrasesConfiguration-blockedPhrases"></a>
A list of phrases blocked from a Amazon Q Business web experience chat.
Each phrase can contain a maximum of 36 characters. The list can contain a maximum of 20 phrases.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 36.
Pattern: `\P{C}*`
Required: No

 ** systemMessageOverride **   <a name="qbusiness-Type-BlockedPhrasesConfiguration-systemMessageOverride"></a>
The configured custom message displayed to an end user informing them that they've used a blocked phrase during chat.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350.
Pattern: `\P{C}*`
Required: No

## See Also
<a name="API_BlockedPhrasesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/BlockedPhrasesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/BlockedPhrasesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/BlockedPhrasesConfiguration)
