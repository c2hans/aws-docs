---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_AgentOutputMessage.html
---

# AgentOutputMessage
<a name="API_AgentOutputMessage"></a>

Represents a response message from the agent during chat-based profile customization.

## Contents
<a name="API_AgentOutputMessage_Contents"></a>

 ** Body **   <a name="HealthLake-Type-AgentOutputMessage-Body"></a>
The text of the agent's response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40960.
Required: Yes

 ** Type **   <a name="HealthLake-Type-AgentOutputMessage-Type"></a>
The type of output message, which indicates how to interpret the agent's response.
Type: String
Valid Values: `INITIAL_GREETING | normal | confirmation | complete | error | options | choices`
Required: Yes

 ** OptionsList **   <a name="HealthLake-Type-AgentOutputMessage-OptionsList"></a>
A list of selectable options presented when the response type is `options`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_AgentOutputMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/AgentOutputMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/AgentOutputMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/AgentOutputMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
