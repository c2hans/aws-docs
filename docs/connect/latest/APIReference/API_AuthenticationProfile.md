---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AuthenticationProfile.html
---

# AuthenticationProfile
<a name="API_AuthenticationProfile"></a>

This API is in preview release for Connect Customer and is subject to change. To request access to this API, contact Support.

Information about an authentication profile. An authentication profile is a resource that stores the authentication settings for users in your contact center. You use authentication profiles to set up IP address range restrictions and session timeouts. For more information, see [Set IP address restrictions or session timeouts](https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html).

## Contents
<a name="API_AuthenticationProfile_Contents"></a>

 ** AllowedIps **   <a name="connect-Type-AuthenticationProfile-AllowedIps"></a>
A list of IP address range strings that are allowed to access the Connect Customer instance. For more information about how to configure IP addresses, see [Configure IP address based access control](https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-ip-based-ac) in the *Connect Customer Administrator Guide*.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `^[A-Za-z0-9:/]*$`
Required: No

 ** Arn **   <a name="connect-Type-AuthenticationProfile-Arn"></a>
The Amazon Resource Name (ARN) for the authentication profile.
Type: String
Required: No

 ** BlockedIps **   <a name="connect-Type-AuthenticationProfile-BlockedIps"></a>
A list of IP address range strings that are blocked from accessing the Connect Customer instance. For more information about how to configure IP addresses, see [Configure IP address based access control](https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-ip-based-ac) in the *Connect Customer Administrator Guide*.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `^[A-Za-z0-9:/]*$`
Required: No

 ** CreatedTime **   <a name="connect-Type-AuthenticationProfile-CreatedTime"></a>
The timestamp when the authentication profile was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-AuthenticationProfile-Description"></a>
The description for the authentication profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** Id **   <a name="connect-Type-AuthenticationProfile-Id"></a>
A unique identifier for the authentication profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IsDefault **   <a name="connect-Type-AuthenticationProfile-IsDefault"></a>
Shows whether the authentication profile is the default authentication profile for the Connect Customer instance. The default authentication profile applies to all agents in an Connect Customer instance, unless overridden by another authentication profile.
Type: Boolean
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-AuthenticationProfile-LastModifiedRegion"></a>
The AWS Region where the authentication profile was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-AuthenticationProfile-LastModifiedTime"></a>
The timestamp when the authentication profile was last modified.
Type: Timestamp
Required: No

 ** MaxSessionDuration **   <a name="connect-Type-AuthenticationProfile-MaxSessionDuration"></a>
The long lived session duration for users logged in to Connect Customer, in minutes. After this time period, users must log in again. For more information, see [Configure the session duration](https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts) in the *Connect Customer Administrator Guide*.
Type: Integer
Valid Range: Minimum value of 360. Maximum value of 720.
Required: No

 ** Name **   <a name="connect-Type-AuthenticationProfile-Name"></a>
The name for the authentication profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** PeriodicSessionDuration **   <a name="connect-Type-AuthenticationProfile-PeriodicSessionDuration"></a>
 *This member has been deprecated.*
The short lived session duration configuration for users logged in to Connect Customer, in minutes. This value determines the maximum possible time before an agent is authenticated. For more information, see [Configure the session duration](https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts) in the *Connect Customer Administrator Guide*.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 60.
Required: No

 ** SessionInactivityDuration **   <a name="connect-Type-AuthenticationProfile-SessionInactivityDuration"></a>
The period, in minutes, before an agent is automatically signed out of the contact center when they go inactive.
Type: Integer
Valid Range: Minimum value of 15. Maximum value of 720.
Required: No

 ** SessionInactivityHandlingEnabled **   <a name="connect-Type-AuthenticationProfile-SessionInactivityHandlingEnabled"></a>
Determines if automatic logout on user inactivity is enabled.
Type: Boolean
Required: No

## See Also
<a name="API_AuthenticationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AuthenticationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AuthenticationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AuthenticationProfile)
