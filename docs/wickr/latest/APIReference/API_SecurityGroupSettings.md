---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_SecurityGroupSettings.html
---

# SecurityGroupSettings
<a name="API_SecurityGroupSettings"></a>

Comprehensive configuration settings that define all user capabilities, restrictions, and features for members of a security group. These settings control everything from calling permissions to federation settings to security policies.

## Contents
<a name="API_SecurityGroupSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** alwaysReauthenticate **   <a name="wickr-Type-SecurityGroupSettings-alwaysReauthenticate"></a>
Requires users to reauthenticate every time they return to the application, providing an additional layer of security.
Type: Boolean
Required: No

 ** atakPackageValues **   <a name="wickr-Type-SecurityGroupSettings-atakPackageValues"></a>
Configuration values for ATAK (Android Team Awareness Kit) package integration, when ATAK is enabled.
Type: Array of strings
Pattern: `[\S\s]*`
Required: No

 ** calling **   <a name="wickr-Type-SecurityGroupSettings-calling"></a>
The calling feature permissions and settings that control what types of calls users can initiate and participate in.
Type: [CallingSettings](API_CallingSettings.md) object
Required: No

 ** checkForUpdates **   <a name="wickr-Type-SecurityGroupSettings-checkForUpdates"></a>
Enables automatic checking for Wickr client updates to ensure users stay current with the latest version.
Type: Boolean
Required: No

 ** enableAtak **   <a name="wickr-Type-SecurityGroupSettings-enableAtak"></a>
Enables ATAK (Android Team Awareness Kit) integration for tactical communication and situational awareness.
Type: Boolean
Required: No

 ** enableCrashReports **   <a name="wickr-Type-SecurityGroupSettings-enableCrashReports"></a>
Allow users to report crashes.
Type: Boolean
Required: No

 ** enableFileDownload **   <a name="wickr-Type-SecurityGroupSettings-enableFileDownload"></a>
Specifies whether users can download files from messages to their devices.
Type: Boolean
Required: No

 ** enableGuestFederation **   <a name="wickr-Type-SecurityGroupSettings-enableGuestFederation"></a>
Allows users to communicate with guest users from other Wickr networks and federated external networks.
Type: Boolean
Required: No

 ** enableNotificationPreview **   <a name="wickr-Type-SecurityGroupSettings-enableNotificationPreview"></a>
Enables message preview text in push notifications, allowing users to see message content before opening the app.
Type: Boolean
Required: No

 ** enableOpenAccessOption **   <a name="wickr-Type-SecurityGroupSettings-enableOpenAccessOption"></a>
 Allow users to avoid censorship when they are geo-blocked or have network limitations.
Type: Boolean
Required: No

 ** enableRestrictedGlobalFederation **   <a name="wickr-Type-SecurityGroupSettings-enableRestrictedGlobalFederation"></a>
Enables restricted global federation, limiting external communication to only specified permitted networks.
Type: Boolean
Required: No

 ** federationMode **   <a name="wickr-Type-SecurityGroupSettings-federationMode"></a>
The local federation mode controlling how users can communicate with other networks. Values: 0 (none), 1 (federated), 2 (restricted).
Type: Integer
Required: No

 ** filesEnabled **   <a name="wickr-Type-SecurityGroupSettings-filesEnabled"></a>
Enables file sharing capabilities, allowing users to send and receive files in conversations.
Type: Boolean
Required: No

 ** forceDeviceLockout **   <a name="wickr-Type-SecurityGroupSettings-forceDeviceLockout"></a>
 Defines the number of failed login attempts before data stored on the device is reset. Should be less than lockoutThreshold.
Type: Integer
Required: No

 ** forceOpenAccess **   <a name="wickr-Type-SecurityGroupSettings-forceOpenAccess"></a>
Automatically enable and enforce Wickr open access on all devices. Valid only if enableOpenAccessOption settings is enabled.
Type: Boolean
Required: No

 ** forceReadReceipts **   <a name="wickr-Type-SecurityGroupSettings-forceReadReceipts"></a>
Allow user approved bots to read messages in rooms without using a slash command.
Type: Boolean
Required: No

 ** globalFederation **   <a name="wickr-Type-SecurityGroupSettings-globalFederation"></a>
Allows users to communicate with users on other Wickr instances (Wickr Enterprise) outside the current network.
Type: Boolean
Required: No

 ** isAtoEnabled **   <a name="wickr-Type-SecurityGroupSettings-isAtoEnabled"></a>
Enforces a two-factor authentication when a user adds a new device to their account.
Type: Boolean
Required: No

 ** isLinkPreviewEnabled **   <a name="wickr-Type-SecurityGroupSettings-isLinkPreviewEnabled"></a>
Enables automatic preview of links shared in messages, showing webpage thumbnails and descriptions.
Type: Boolean
Required: No

 ** locationAllowMaps **   <a name="wickr-Type-SecurityGroupSettings-locationAllowMaps"></a>
Allows map integration in location sharing, enabling users to view shared locations on interactive maps. Only allowed when location setting is enabled.
Type: Boolean
Required: No

 ** locationEnabled **   <a name="wickr-Type-SecurityGroupSettings-locationEnabled"></a>
Enables location sharing features, allowing users to share their current location with others.
Type: Boolean
Required: No

 ** lockoutThreshold **   <a name="wickr-Type-SecurityGroupSettings-lockoutThreshold"></a>
The number of failed password attempts before a user account is locked out.
Type: Integer
Required: No

 ** maxAutoDownloadSize **   <a name="wickr-Type-SecurityGroupSettings-maxAutoDownloadSize"></a>
The maximum file size in bytes that will be automatically downloaded without user confirmation. Only allowed if fileDownload is enabled. Valid Values [512000 (low\_quality), 7340032 (high\_quality) ]
Type: Long
Required: No

 ** maxBor **   <a name="wickr-Type-SecurityGroupSettings-maxBor"></a>
The maximum burn-on-read (BOR) time in seconds, which determines how long messages remain visible before auto-deletion after being read.
Type: Integer
Required: No

 ** maxNonSsoSessionMinutes **   <a name="wickr-Type-SecurityGroupSettings-maxNonSsoSessionMinutes"></a>
Maximum session duration in minutes for non-SSO users. Set to 0 to disable. Valid range is 60 to 525600 (1 hour to 365 days).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 525600.
Required: No

 ** maxTtl **   <a name="wickr-Type-SecurityGroupSettings-maxTtl"></a>
The maximum time-to-live (TTL) in seconds for messages, after which they will be automatically deleted from all devices.
Type: Long
Required: No

 ** messageForwardingEnabled **   <a name="wickr-Type-SecurityGroupSettings-messageForwardingEnabled"></a>
Enables message forwarding, allowing users to forward messages from one conversation to another.
Type: Boolean
Required: No

 ** passwordRequirements **   <a name="wickr-Type-SecurityGroupSettings-passwordRequirements"></a>
The password complexity requirements that users must follow when creating or changing passwords.
Type: [PasswordRequirements](API_PasswordRequirements.md) object
Required: No

 ** permittedNetworks **   <a name="wickr-Type-SecurityGroupSettings-permittedNetworks"></a>
A list of network IDs that are permitted for local federation when federation mode is set to restricted.
Type: Array of strings
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: No

 ** permittedWickrAwsNetworks **   <a name="wickr-Type-SecurityGroupSettings-permittedWickrAwsNetworks"></a>
A list of permitted Wickr networks for global federation, restricting communication to specific approved networks.
Type: Array of [WickrAwsNetworks](API_WickrAwsNetworks.md) objects
Required: No

 ** permittedWickrEnterpriseNetworks **   <a name="wickr-Type-SecurityGroupSettings-permittedWickrEnterpriseNetworks"></a>
A list of permitted Wickr Enterprise networks for global federation, restricting communication to specific approved networks.
Type: Array of [PermittedWickrEnterpriseNetwork](API_PermittedWickrEnterpriseNetwork.md) objects
Required: No

 ** presenceEnabled **   <a name="wickr-Type-SecurityGroupSettings-presenceEnabled"></a>
Enables presence indicators that show whether users are online, away, or offline.
Type: Boolean
Required: No

 ** quickResponses **   <a name="wickr-Type-SecurityGroupSettings-quickResponses"></a>
A list of pre-defined quick response message templates that users can send with a single tap.
Type: Array of strings
Pattern: `[\S\s]*`
Required: No

 ** showMasterRecoveryKey **   <a name="wickr-Type-SecurityGroupSettings-showMasterRecoveryKey"></a>
Users will get a master recovery key that can be used to securely sign in to their Wickr account without having access to their primary device for authentication. Available in SSO enabled network.
Type: Boolean
Required: No

 ** shredder **   <a name="wickr-Type-SecurityGroupSettings-shredder"></a>
The message shredder configuration that controls secure deletion of messages and files from devices.
Type: [ShredderSettings](API_ShredderSettings.md) object
Required: No

 ** ssoMaxIdleMinutes **   <a name="wickr-Type-SecurityGroupSettings-ssoMaxIdleMinutes"></a>
The duration for which users SSO session remains inactive before automatically logging them out for security. Available in SSO enabled network.
Type: Integer
Required: No

## See Also
<a name="API_SecurityGroupSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/SecurityGroupSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/SecurityGroupSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/SecurityGroupSettings)
