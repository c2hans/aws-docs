---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_Message.html
---

# Message
<a name="API_Message"></a>

A conversation turn.

## Contents
<a name="API_Message_Contents"></a>

 ** content **   <a name="opensearchmemory-Type-Message-content"></a>
The content of the turn.
Type: [MessageContent](API_MessageContent.md) object
Required: Yes

 ** role **   <a name="opensearchmemory-Type-Message-role"></a>
The author of the turn.
Type: String
Valid Values: `USER | ASSISTANT | SYSTEM`
Required: Yes

## See Also
<a name="API_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/Message)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/Message)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/Message)
