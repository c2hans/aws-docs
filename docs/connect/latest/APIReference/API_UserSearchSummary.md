---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserSearchSummary.html
---

# UserSearchSummary
<a name="API_UserSearchSummary"></a>

Information about the returned users.

## Contents
<a name="API_UserSearchSummary_Contents"></a>

 ** AfterContactWorkConfigs **   <a name="connect-Type-UserSearchSummary-AfterContactWorkConfigs"></a>
The list of after contact work (ACW) timeout configuration settings for each channel.
Type: Array of [AfterContactWorkConfigPerChannel](API_AfterContactWorkConfigPerChannel.md) objects
Required: No

 ** Arn **   <a name="connect-Type-UserSearchSummary-Arn"></a>
The Amazon Resource Name (ARN) of the user.
Type: String
Required: No

 ** AutoAcceptConfigs **   <a name="connect-Type-UserSearchSummary-AutoAcceptConfigs"></a>
The list of auto-accept configuration settings for each channel.
Type: Array of [AutoAcceptConfig](API_AutoAcceptConfig.md) objects
Required: No

 ** DirectoryUserId **   <a name="connect-Type-UserSearchSummary-DirectoryUserId"></a>
The directory identifier of the user.
Type: String
Required: No

 ** HierarchyGroupId **   <a name="connect-Type-UserSearchSummary-HierarchyGroupId"></a>
The identifier of the user's hierarchy group.
Type: String
Required: No

 ** Id **   <a name="connect-Type-UserSearchSummary-Id"></a>
The identifier of the user's summary.
Type: String
Required: No

 ** IdentityInfo **   <a name="connect-Type-UserSearchSummary-IdentityInfo"></a>
The user's first name and last name.
Type: [UserIdentityInfoLite](API_UserIdentityInfoLite.md) object
Required: No

 ** PersistentConnectionConfigs **   <a name="connect-Type-UserSearchSummary-PersistentConnectionConfigs"></a>
The list of persistent connection configuration settings for each channel.
Type: Array of [PersistentConnectionConfig](API_PersistentConnectionConfig.md) objects
Required: No

 ** PhoneConfig **   <a name="connect-Type-UserSearchSummary-PhoneConfig"></a>
Contains information about the phone configuration settings for a user.
Type: [UserPhoneConfig](API_UserPhoneConfig.md) object
Required: No

 ** PhoneNumberConfigs **   <a name="connect-Type-UserSearchSummary-PhoneNumberConfigs"></a>
The list of phone number configuration settings for each channel.
Type: Array of [PhoneNumberConfig](API_PhoneNumberConfig.md) objects
Required: No

 ** RoutingProfileId **   <a name="connect-Type-UserSearchSummary-RoutingProfileId"></a>
The identifier of the user's routing profile.
Type: String
Required: No

 ** SecurityProfileIds **   <a name="connect-Type-UserSearchSummary-SecurityProfileIds"></a>
The identifiers of the user's security profiles.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** Tags **   <a name="connect-Type-UserSearchSummary-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Username **   <a name="connect-Type-UserSearchSummary-Username"></a>
The name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** VoiceEnhancementConfigs **   <a name="connect-Type-UserSearchSummary-VoiceEnhancementConfigs"></a>
The list of voice enhancement configuration settings for each channel.
Type: Array of [VoiceEnhancementConfig](API_VoiceEnhancementConfig.md) objects
Required: No

## See Also
<a name="API_UserSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserSearchSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
