---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaFlowHealthStatus.html
---

# MetaFlowHealthStatus
<a name="API_MetaFlowHealthStatus"></a>

Contains the overall health status and per-entity breakdown for a WhatsApp Flow.

## Contents
<a name="API_MetaFlowHealthStatus_Contents"></a>

 ** canSendMessage **   <a name="Social-Type-MetaFlowHealthStatus-canSendMessage"></a>
The overall messaging availability status (for example, AVAILABLE, LIMITED, or BLOCKED).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** entities **   <a name="Social-Type-MetaFlowHealthStatus-entities"></a>
A list of health status entities with per-entity availability information.
Type: Array of [MetaFlowHealthEntity](API_MetaFlowHealthEntity.md) objects
Required: No

## See Also
<a name="API_MetaFlowHealthStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/MetaFlowHealthStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/MetaFlowHealthStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/MetaFlowHealthStatus)
