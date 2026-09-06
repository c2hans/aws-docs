---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SendMessageContentBlockDelta.html
---

# SendMessageContentBlockDelta
<a name="API_SendMessageContentBlockDelta"></a>

Union of possible delta payloads within a content block delta event

## Contents
<a name="API_SendMessageContentBlockDelta_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** jsonDelta **   <a name="devopsagent-Type-SendMessageContentBlockDelta-jsonDelta"></a>
JSON delta for structured content blocks
Type: [SendMessageJsonDelta](API_SendMessageJsonDelta.md) object
Required: No

 ** textDelta **   <a name="devopsagent-Type-SendMessageContentBlockDelta-textDelta"></a>
Text delta for text-based content blocks
Type: [SendMessageTextDelta](API_SendMessageTextDelta.md) object
Required: No

## See Also
<a name="API_SendMessageContentBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SendMessageContentBlockDelta)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SendMessageContentBlockDelta)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SendMessageContentBlockDelta)
