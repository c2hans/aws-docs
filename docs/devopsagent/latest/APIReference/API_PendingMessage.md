---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_PendingMessage.html
---

# PendingMessage
<a name="API_PendingMessage"></a>

Represents a pending message in an agent execution.

## Contents
<a name="API_PendingMessage_Contents"></a>

 ** message **   <a name="devopsagent-Type-PendingMessage-message"></a>
The message content.
Type: [Message](API_Message.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** messageId **   <a name="devopsagent-Type-PendingMessage-messageId"></a>
The unique identifier for this pending message.
Type: String
Required: Yes

## See Also
<a name="API_PendingMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/PendingMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/PendingMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/PendingMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
