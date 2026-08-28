---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Message.html
---

# Message
<a name="API_Message"></a>

A message in a conversation, either from the user or the assistant.

## Contents
<a name="API_Message_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** assistantMessage **   <a name="devopsagent-Type-Message-assistantMessage"></a>
A message from the assistant.
Type: Array of [AssistantMessageBlock](API_AssistantMessageBlock.md) objects
Required: No

 ** userMessage **   <a name="devopsagent-Type-Message-userMessage"></a>
A message from the user.
Type: Array of [UserMessageBlock](API_UserMessageBlock.md) objects
Required: No

## See Also
<a name="API_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Message)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Message)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Message)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
