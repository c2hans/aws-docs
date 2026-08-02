---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AiAgentInfo.html
---

# AiAgentInfo
<a name="API_AiAgentInfo"></a>

 Information of the AI agent involved in the contact.

## Contents
<a name="API_AiAgentInfo_Contents"></a>

 ** AiAgentEscalated **   <a name="connect-Type-AiAgentInfo-AiAgentEscalated"></a>
 A boolean flag indicating whether the contact initially handled by this AI agent was escalated to a human agent.
Type: Boolean
Required: No

 ** AiAgentVersionId **   <a name="connect-Type-AiAgentInfo-AiAgentVersionId"></a>
 The unique identifier that specifies both the AI agent ID and its version number that was involved in the contact
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** AiUseCase **   <a name="connect-Type-AiAgentInfo-AiUseCase"></a>
 The use case or scenario for which the AI agent is involved in the contact
Type: String
Valid Values: `AgentAssistance | SelfService`
Required: No

## See Also
<a name="API_AiAgentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AiAgentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AiAgentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AiAgentInfo)
