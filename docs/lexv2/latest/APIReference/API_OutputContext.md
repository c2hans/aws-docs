---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_OutputContext.html
---

# OutputContext
<a name="API_OutputContext"></a>

Describes a session context that is activated when an intent is fulfilled.

## Contents
<a name="API_OutputContext_Contents"></a>

 ** name **   <a name="lexv2-Type-OutputContext-name"></a>
The name of the output context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** timeToLiveInSeconds **   <a name="lexv2-Type-OutputContext-timeToLiveInSeconds"></a>
The amount of time, in seconds, that the output context should remain active. The time is figured from the first time the context is sent to the user.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 86400.
Required: Yes

 ** turnsToLive **   <a name="lexv2-Type-OutputContext-turnsToLive"></a>
The number of conversation turns that the output context should remain active. The number of turns is counted from the first time that the context is sent to the user.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: Yes

## See Also
<a name="API_OutputContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/OutputContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/OutputContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/OutputContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
