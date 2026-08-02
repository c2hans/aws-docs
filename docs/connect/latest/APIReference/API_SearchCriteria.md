---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchCriteria.html
---

# SearchCriteria
<a name="API_SearchCriteria"></a>

A structure of search criteria to be used to return contacts.

## Contents
<a name="API_SearchCriteria_Contents"></a>

 ** ActiveRegions **   <a name="connect-Type-SearchCriteria-ActiveRegions"></a>
The list of active regions for contacts in ACGR instances.
Type: Array of strings
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** AdditionalTimeRange **   <a name="connect-Type-SearchCriteria-AdditionalTimeRange"></a>
Additional TimeRange used to filter contacts.
Type: [SearchContactsAdditionalTimeRange](API_SearchContactsAdditionalTimeRange.md) object
Required: No

 ** AgentHierarchyGroups **   <a name="connect-Type-SearchCriteria-AgentHierarchyGroups"></a>
The agent hierarchy groups of the agent at the time of handling the contact.
Type: [AgentHierarchyGroups](API_AgentHierarchyGroups.md) object
Required: No

 ** AgentIds **   <a name="connect-Type-SearchCriteria-AgentIds"></a>
The identifiers of agents who handled the contacts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** AiAgents **   <a name="connect-Type-SearchCriteria-AiAgents"></a>
AI Agent search criteria definitions.
Type: [AiAgentsCriteria](API_AiAgentsCriteria.md) object
Required: No

 ** Channels **   <a name="connect-Type-SearchCriteria-Channels"></a>
The list of channels associated with contacts.
Type: Array of strings
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: No

 ** ContactAnalysis **   <a name="connect-Type-SearchCriteria-ContactAnalysis"></a>
Search criteria based on analysis outputs from Connect Customer Contact Lens.
Type: [ContactAnalysis](API_ContactAnalysis.md) object
Required: No

 ** ContactTags **   <a name="connect-Type-SearchCriteria-ContactTags"></a>
An object that can be used to specify Tag conditions inside the `SearchFilter`. This accepts an `OR` of `AND` (List of List) input where:
+ Top level list specifies conditions that need to be applied with `OR` operator
+ Inner list specifies conditions that need to be applied with `AND` operator.
Type: [ControlPlaneTagFilter](API_ControlPlaneTagFilter.md) object
Required: No

 ** InitiationMethods **   <a name="connect-Type-SearchCriteria-InitiationMethods"></a>
The list of initiation methods associated with contacts.
Type: Array of strings
Valid Values: `INBOUND | OUTBOUND | TRANSFER | QUEUE_TRANSFER | CALLBACK | API | DISCONNECT | MONITOR | EXTERNAL_OUTBOUND | WEBRTC_API | AGENT_REPLY | FLOW`
Required: No

 ** Name **   <a name="connect-Type-SearchCriteria-Name"></a>
Name of the contact.
Type: [NameCriteria](API_NameCriteria.md) object
Required: No

 ** QueueIds **   <a name="connect-Type-SearchCriteria-QueueIds"></a>
The list of queue IDs associated with contacts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** RoutingCriteria **   <a name="connect-Type-SearchCriteria-RoutingCriteria"></a>
Routing criteria for the contact.
Type: [SearchableRoutingCriteria](API_SearchableRoutingCriteria.md) object
Required: No

 ** SearchableContactAttributes **   <a name="connect-Type-SearchCriteria-SearchableContactAttributes"></a>
The search criteria based on user-defined contact attributes that have been configured for contact search. For more information, see [Search by custom contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/search-custom-attributes.html) in the *Connect Customer Administrator Guide*.
To use `SearchableContactAttributes` in a search request, the `GetContactAttributes` action is required to perform an API request. For more information, see [https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-actions-as-permissions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-actions-as-permissions)Actions defined by Connect Customer.
Type: [SearchableContactAttributes](API_SearchableContactAttributes.md) object
Required: No

 ** SearchableSegmentAttributes **   <a name="connect-Type-SearchCriteria-SearchableSegmentAttributes"></a>
The search criteria based on searchable segment attributes of a contact.
Type: [SearchableSegmentAttributes](API_SearchableSegmentAttributes.md) object
Required: No

## See Also
<a name="API_SearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchCriteria)
