---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ChatChannel.html
---

# ChatChannel
<a name="API_ChatChannel"></a>

The Amazon Q Developer in chat applications chat channel used for collaboration during an incident.

## Contents
<a name="API_ChatChannel_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** chatbotSns **   <a name="IncidentManager-Type-ChatChannel-chatbotSns"></a>
The Amazon SNS targets that Amazon Q Developer in chat applications uses to notify the chat channel of updates to an incident. You can also make updates to the incident through the chat channel by using the Amazon SNS topics.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** empty **   <a name="IncidentManager-Type-ChatChannel-empty"></a>
Used to remove the chat channel from an incident record or response plan.
Type: [EmptyChatChannel](API_EmptyChatChannel.md) object
Required: No

## See Also
<a name="API_ChatChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ChatChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ChatChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ChatChannel)
