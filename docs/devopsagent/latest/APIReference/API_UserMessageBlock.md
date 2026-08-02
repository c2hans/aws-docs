---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UserMessageBlock.html
---

# UserMessageBlock
<a name="API_UserMessageBlock"></a>

A block of content in a user message.

## Contents
<a name="API_UserMessageBlock_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="devopsagent-Type-UserMessageBlock-text"></a>
Text content from the user.
Type: String
Required: No

 ** toolResult **   <a name="devopsagent-Type-UserMessageBlock-toolResult"></a>
Tool execution result provided by the user.
Type: JSON value
Required: No

## See Also
<a name="API_UserMessageBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/UserMessageBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/UserMessageBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/UserMessageBlock)
