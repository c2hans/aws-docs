---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_AgentInputMessage.html
---

# AgentInputMessage
<a name="API_AgentInputMessage"></a>

Represents a message sent to the agent during chat-based profile customization.

## Contents
<a name="API_AgentInputMessage_Contents"></a>

 ** Body **   <a name="HealthLake-Type-AgentInputMessage-Body"></a>
The text of your message to the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40960.
Required: Yes

 ** Type **   <a name="HealthLake-Type-AgentInputMessage-Type"></a>
The type of input message, which determines how the agent processes your request. Valid values:
+  `normal`: A regular message to the agent.
+  `confirmation_response`: A response to a confirmation request from the agent.
Type: String
Valid Values: `normal | confirmation_response`
Required: Yes

## See Also
<a name="API_AgentInputMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/AgentInputMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/AgentInputMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/AgentInputMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
