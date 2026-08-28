---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AuthChallengeRequestEvent.html
---

# AuthChallengeRequestEvent
<a name="API_AuthChallengeRequestEvent"></a>

An authentication verification event activated by an end user request to use a custom plugin.

## Contents
<a name="API_AuthChallengeRequestEvent_Contents"></a>

 ** authorizationUrl **   <a name="qbusiness-Type-AuthChallengeRequestEvent-authorizationUrl"></a>
The URL sent by Amazon Q Business to a third party authentication server in response to an authentication verification event activated by an end user request to use a custom plugin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`
Required: Yes

## See Also
<a name="API_AuthChallengeRequestEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AuthChallengeRequestEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AuthChallengeRequestEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AuthChallengeRequestEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
