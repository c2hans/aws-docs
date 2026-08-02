---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AssistantMessageBlock.html
---

# AssistantMessageBlock
<a name="API_AssistantMessageBlock"></a>

A block of content in an assistant message.

## Contents
<a name="API_AssistantMessageBlock_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="devopsagent-Type-AssistantMessageBlock-text"></a>
Text content from the assistant.
Type: String
Required: No

 ** toolUse **   <a name="devopsagent-Type-AssistantMessageBlock-toolUse"></a>
Tool use request from the assistant.
Type: JSON value
Required: No

## See Also
<a name="API_AssistantMessageBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AssistantMessageBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AssistantMessageBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AssistantMessageBlock)
