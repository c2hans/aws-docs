---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_KeywordInformation.html
---

# KeywordInformation
<a name="API_KeywordInformation"></a>

The information for all keywords in a pool.

## Contents
<a name="API_KeywordInformation_Contents"></a>

 ** Keyword **   <a name="pinpoint-Type-KeywordInformation-Keyword"></a>
The keyword as a string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[ \S]+`
Required: Yes

 ** KeywordAction **   <a name="pinpoint-Type-KeywordInformation-KeywordAction"></a>
The action to perform for the keyword.
Type: String
Valid Values: `AUTOMATIC_RESPONSE | OPT_OUT | OPT_IN`
Required: Yes

 ** KeywordMessage **   <a name="pinpoint-Type-KeywordInformation-KeywordMessage"></a>
A custom message that can be used with the keyword.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(?!\s*$)[\s\S]+`
Required: Yes

## See Also
<a name="API_KeywordInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/KeywordInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/KeywordInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/KeywordInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
