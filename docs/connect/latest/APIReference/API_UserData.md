---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserData.html
---

# UserData
<a name="API_UserData"></a>

Data for a user.

## Contents
<a name="API_UserData_Contents"></a>

 ** ActiveSlotsByChannel **   <a name="connect-Type-UserData-ActiveSlotsByChannel"></a>
 A map of active slots by channel. The key is a channel name. The value is an integer: the number of active slots.
Type: String to integer map
Valid Keys: `VOICE | CHAT | TASK | EMAIL`
Valid Range: Minimum value of 0.
Required: No

 ** AvailableSlotsByChannel **   <a name="connect-Type-UserData-AvailableSlotsByChannel"></a>
A map of available slots by channel. The key is a channel name. The value is an integer: the available number of slots.
Type: String to integer map
Valid Keys: `VOICE | CHAT | TASK | EMAIL`
Valid Range: Minimum value of 0.
Required: No

 ** Contacts **   <a name="connect-Type-UserData-Contacts"></a>
A list of contact reference information.
Type: Array of [AgentContactReference](API_AgentContactReference.md) objects
Required: No

 ** HierarchyPath **   <a name="connect-Type-UserData-HierarchyPath"></a>
Contains information about the levels of a hierarchy group assigned to a user.
Type: [HierarchyPathReference](API_HierarchyPathReference.md) object
Required: No

 ** MaxSlotsByChannel **   <a name="connect-Type-UserData-MaxSlotsByChannel"></a>
A map of maximum slots by channel. The key is a channel name. The value is an integer: the maximum number of slots. This is calculated from [MediaConcurrency](https://docs.aws.amazon.com/connect/latest/APIReference/API_MediaConcurrency.html) of the `RoutingProfile` assigned to the agent.
Type: String to integer map
Valid Keys: `VOICE | CHAT | TASK | EMAIL`
Valid Range: Minimum value of 0.
Required: No

 ** NextStatus **   <a name="connect-Type-UserData-NextStatus"></a>
The Next status of the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** RoutingProfile **   <a name="connect-Type-UserData-RoutingProfile"></a>
Information about the routing profile that is assigned to the user.
Type: [RoutingProfileReference](API_RoutingProfileReference.md) object
Required: No

 ** Status **   <a name="connect-Type-UserData-Status"></a>
The status of the agent that they manually set in their Contact Control Panel (CCP), or that the supervisor manually changes in the real-time metrics report.
Type: [AgentStatusReference](API_AgentStatusReference.md) object
Required: No

 ** User **   <a name="connect-Type-UserData-User"></a>
Information about the user for the data that is returned. It contains the `resourceId` and ARN of the user.
Type: [UserReference](API_UserReference.md) object
Required: No

## See Also
<a name="API_UserData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
