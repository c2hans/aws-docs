---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

Contains information about a user account for an Connect Customer instance.

## Contents
<a name="API_User_Contents"></a>

 ** AfterContactWorkConfigs **   <a name="connect-Type-User-AfterContactWorkConfigs"></a>
The list of after contact work (ACW) timeout configuration settings for each channel.
Type: Array of [AfterContactWorkConfigPerChannel](API_AfterContactWorkConfigPerChannel.md) objects
Required: No

 ** Arn **   <a name="connect-Type-User-Arn"></a>
The Amazon Resource Name (ARN) of the user account.
Type: String
Required: No

 ** AutoAcceptConfigs **   <a name="connect-Type-User-AutoAcceptConfigs"></a>
The list of auto-accept configuration settings for each channel.
Type: Array of [AutoAcceptConfig](API_AutoAcceptConfig.md) objects
Required: No

 ** DirectoryUserId **   <a name="connect-Type-User-DirectoryUserId"></a>
The identifier of the user account in the directory used for identity management.
Type: String
Required: No

 ** HierarchyGroupId **   <a name="connect-Type-User-HierarchyGroupId"></a>
The identifier of the hierarchy group for the user.
Type: String
Required: No

 ** Id **   <a name="connect-Type-User-Id"></a>
The identifier of the user account.
Type: String
Required: No

 ** IdentityInfo **   <a name="connect-Type-User-IdentityInfo"></a>
Information about the user identity.
Type: [UserIdentityInfo](API_UserIdentityInfo.md) object
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-User-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-User-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** PersistentConnectionConfigs **   <a name="connect-Type-User-PersistentConnectionConfigs"></a>
The list of persistent connection configuration settings for each channel.
Type: Array of [PersistentConnectionConfig](API_PersistentConnectionConfig.md) objects
Required: No

 ** PhoneConfig **   <a name="connect-Type-User-PhoneConfig"></a>
Information about the phone configuration for the user.
Type: [UserPhoneConfig](API_UserPhoneConfig.md) object
Required: No

 ** PhoneNumberConfigs **   <a name="connect-Type-User-PhoneNumberConfigs"></a>
The list of phone number configuration settings for each channel.
Type: Array of [PhoneNumberConfig](API_PhoneNumberConfig.md) objects
Required: No

 ** RoutingProfileId **   <a name="connect-Type-User-RoutingProfileId"></a>
The identifier of the routing profile for the user.
Type: String
Required: No

 ** SecurityProfileIds **   <a name="connect-Type-User-SecurityProfileIds"></a>
The identifiers of the security profiles for the user.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** Tags **   <a name="connect-Type-User-Tags"></a>
The tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Username **   <a name="connect-Type-User-Username"></a>
The user name assigned to the user account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** VoiceEnhancementConfigs **   <a name="connect-Type-User-VoiceEnhancementConfigs"></a>
The list of voice enhancement configuration settings for each channel.
Type: Array of [VoiceEnhancementConfig](API_VoiceEnhancementConfig.md) objects
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/User)
