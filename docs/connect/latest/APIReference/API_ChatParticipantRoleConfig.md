---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ChatParticipantRoleConfig.html
---

# ChatParticipantRoleConfig
<a name="API_ChatParticipantRoleConfig"></a>

Configuration information for the chat participant role.

## Contents
<a name="API_ChatParticipantRoleConfig_Contents"></a>

 ** ParticipantTimerConfigList **   <a name="connect-Type-ChatParticipantRoleConfig-ParticipantTimerConfigList"></a>
A list of participant timers. You can specify any unique combination of role and timer type. Duplicate entries error out the request with a 400.
Type: Array of [ParticipantTimerConfiguration](API_ParticipantTimerConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Required: Yes

## See Also
<a name="API_ChatParticipantRoleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ChatParticipantRoleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ChatParticipantRoleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ChatParticipantRoleConfig)
