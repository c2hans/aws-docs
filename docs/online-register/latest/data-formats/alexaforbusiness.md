---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/alexaforbusiness.html
---

# Data retrieval APIs for Alexa for Business
<a name="alexaforbusiness"></a>

Alexa for Business provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="a4b-GetAddressBook"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetAddressBook.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetAddressBook.html) | Get the address book details by the address book ARN | Read |
| <a name="a4b-GetConferencePreference"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetConferencePreference.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetConferencePreference.html) | Retrieve the existing conference preferences | Read |
| <a name="a4b-GetConferenceProvider"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetConferenceProvider.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetConferenceProvider.html) | Get details about a specific conference provider | Read |
| <a name="a4b-GetContact"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetContact.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetContact.html) | Get the contact details by the contact ARN | Read |
| <a name="a4b-GetDevice"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetDevice.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetDevice.html) | Get device details | Read |
| <a name="a4b-GetGateway"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetGateway.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetGateway.html) | Retrieve the details of a gateway | Read |
| <a name="a4b-GetGatewayGroup"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetGatewayGroup.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetGatewayGroup.html) | Retrieve the details of a gateway group | Read |
| <a name="a4b-GetInvitationConfiguration"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetInvitationConfiguration.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetInvitationConfiguration.html) | Retrieve the configured values for the user enrollment invitation email template | Read |
| <a name="a4b-GetNetworkProfile"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetNetworkProfile.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetNetworkProfile.html) | Get the network profile details by the network profile ARN | Read |
| <a name="a4b-GetProfile"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetProfile.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetProfile.html) | Get profile when provided with Profile ARN | Read |
| <a name="a4b-GetRoom"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetRoom.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetRoom.html) | Get room details | Read |
| <a name="a4b-GetRoomSkillParameter"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetRoomSkillParameter.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetRoomSkillParameter.html) | Get an existing parameter that has been set for a skill and room | Read |
| <a name="a4b-GetSkillGroup"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetSkillGroup.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetSkillGroup.html) | Get skill group details with skill group ARN | Read |
| <a name="a4b-ListBusinessReportSchedules"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListBusinessReportSchedules.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListBusinessReportSchedules.html) | List the details of the schedules that a user configured | List |
| <a name="a4b-ListConferenceProviders"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListConferenceProviders.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListConferenceProviders.html) | List conference providers under a specific AWS account | List |
| <a name="a4b-ListDeviceEvents"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListDeviceEvents.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListDeviceEvents.html) | List the device event history, including device connection status, for up to 30 days | List |
| <a name="a4b-ListGatewayGroups"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListGatewayGroups.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListGatewayGroups.html) | List gateway group summaries | List |
| <a name="a4b-ListGateways"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListGateways.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListGateways.html) | List gateway summaries | List |
| <a name="a4b-ListSkills"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkills.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkills.html) | List skills | List |
| <a name="a4b-ListSkillsStoreCategories"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkillsStoreCategories.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkillsStoreCategories.html) | List all categories in the Alexa skill store | List |
| <a name="a4b-ListSkillsStoreSkillsByCategory"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkillsStoreSkillsByCategory.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkillsStoreSkillsByCategory.html) | List all skills in the Alexa skill store by category | List |
| <a name="a4b-ListSmartHomeAppliances"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSmartHomeAppliances.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSmartHomeAppliances.html) | List all of the smart home appliances associated with a room | List |
| <a name="a4b-ListTags"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListTags.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListTags.html) | List all tags on a resource | Read |
| <a name="a4b-ResolveRoom"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_ResolveRoom.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ResolveRoom.html) | Resolve room information | Read |
| <a name="a4b-SearchAddressBooks"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchAddressBooks.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchAddressBooks.html) | Search address books and list the ones that meet a set of filter and sort criteria | List |
| <a name="a4b-SearchContacts"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchContacts.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchContacts.html) | Search contacts and list the ones that meet a set of filter and sort criteria | List |
| <a name="a4b-SearchDevices"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchDevices.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchDevices.html) | Search for devices | List |
| <a name="a4b-SearchNetworkProfiles"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchNetworkProfiles.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchNetworkProfiles.html) | Search network profiles and list the ones that meet a set of filter and sort criteria | List |
| <a name="a4b-SearchProfiles"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchProfiles.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchProfiles.html) | Search for profiles | List |
| <a name="a4b-SearchRooms"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchRooms.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchRooms.html) | Search for rooms | List |
| <a name="a4b-SearchSkillGroups"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchSkillGroups.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchSkillGroups.html) | Search for skill groups | List |
| <a name="a4b-SearchUsers"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchUsers.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchUsers.html) | Search for users | List |
| <a name="a4b-StartSmartHomeApplianceDiscovery"></a>[https://docs.aws.amazon.com/a4b/latest/APIReference/API_StartSmartHomeApplianceDiscovery.html](https://docs.aws.amazon.com/a4b/latest/APIReference/API_StartSmartHomeApplianceDiscovery.html) | Initiate the discovery of any smart home appliances associated with the room | Read |
