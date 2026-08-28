---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_KeywordFilter.html
---

# KeywordFilter
<a name="API_KeywordFilter"></a>

The information for keywords that meet a specified criteria.

## Contents
<a name="API_KeywordFilter_Contents"></a>

 ** Name **   <a name="pinpoint-Type-KeywordFilter-Name"></a>
The name of the attribute to filter on.
Type: String
Valid Values: `keyword-action`
Required: Yes

 ** Values **   <a name="pinpoint-Type-KeywordFilter-Values"></a>
An array values to filter for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/\.:A-Za-z0-9+_-]+`
Required: Yes

## See Also
<a name="API_KeywordFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/KeywordFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/KeywordFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/KeywordFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
