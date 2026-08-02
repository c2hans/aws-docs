---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaFlowHealthEntity.html
---

# MetaFlowHealthEntity
<a name="API_MetaFlowHealthEntity"></a>

Represents a single entity in the health status check for a WhatsApp Flow.

## Contents
<a name="API_MetaFlowHealthEntity_Contents"></a>

 ** canSendMessage **   <a name="Social-Type-MetaFlowHealthEntity-canSendMessage"></a>
The messaging availability status for this entity (for example, AVAILABLE, LIMITED, or BLOCKED).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** entityType **   <a name="Social-Type-MetaFlowHealthEntity-entityType"></a>
The type of entity (for example, FLOW, WABA, BUSINESS, or APP).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** id **   <a name="Social-Type-MetaFlowHealthEntity-id"></a>
The unique identifier of the entity.
Type: String
Required: Yes

## See Also
<a name="API_MetaFlowHealthEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/MetaFlowHealthEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/MetaFlowHealthEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/MetaFlowHealthEntity)
