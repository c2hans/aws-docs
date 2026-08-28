---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizedBotMember.html
---

# RecognizedBotMember
<a name="API_runtime_RecognizedBotMember"></a>

The bot member that processes the request.

## Contents
<a name="API_runtime_RecognizedBotMember_Contents"></a>

 ** botId **   <a name="lexv2-Type-runtime_RecognizedBotMember-botId"></a>
The identifier of the bot member that processes the request.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** botName **   <a name="lexv2-Type-runtime_RecognizedBotMember-botName"></a>
The name of the bot member that processes the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?)+$`
Required: No

## See Also
<a name="API_runtime_RecognizedBotMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/RecognizedBotMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/RecognizedBotMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/RecognizedBotMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
