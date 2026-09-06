---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

Represents a user account in a Wickr network with detailed profile information, status, security settings, and authentication details.

**Note**
codeValidation, inviteCode and inviteCodeTtl are restricted to networks under preview only.

## Contents
<a name="API_User_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** cell **   <a name="wickr-Type-User-cell"></a>
The phone number minus country code, used for cloud deployments.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** challengeFailures **   <a name="wickr-Type-User-challengeFailures"></a>
The number of failed password attempts for enterprise deployments, used for account lockout policies.
Type: Integer
Required: No

 ** codeValidation **   <a name="wickr-Type-User-codeValidation"></a>
Indicates whether the user can be verified through a custom invite code.
Type: Boolean
Required: No

 ** countryCode **   <a name="wickr-Type-User-countryCode"></a>
The country code for the user's phone number, used for cloud deployments.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** firstName **   <a name="wickr-Type-User-firstName"></a>
The first name of the user.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** inviteCode **   <a name="wickr-Type-User-inviteCode"></a>
The invitation code for this user, used during registration to join the network.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** isAdmin **   <a name="wickr-Type-User-isAdmin"></a>
Indicates whether the user has administrator privileges in the network.
Type: Boolean
Required: No

 ** isInviteExpired **   <a name="wickr-Type-User-isInviteExpired"></a>
Indicates whether the user's email invitation code has expired, applicable to cloud deployments.
Type: Boolean
Required: No

 ** isUser **   <a name="wickr-Type-User-isUser"></a>
Indicates whether this account is a user (as opposed to a bot or other account type).
Type: Boolean
Required: No

 ** lastName **   <a name="wickr-Type-User-lastName"></a>
The last name of the user.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** otpEnabled **   <a name="wickr-Type-User-otpEnabled"></a>
Indicates whether one-time password (OTP) authentication is enabled for the user.
Type: Boolean
Required: No

 ** scimId **   <a name="wickr-Type-User-scimId"></a>
The SCIM (System for Cross-domain Identity Management) identifier for the user, used for identity synchronization. Currently not used.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** securityGroups **   <a name="wickr-Type-User-securityGroups"></a>
A list of security group IDs to which the user is assigned, determining their permissions and feature access.
Type: Array of strings
Pattern: `[\S]+`
Required: No

 ** status **   <a name="wickr-Type-User-status"></a>
The current status of the user (1 for pending invitation, 2 for active).
Type: Integer
Required: No

 ** suspended **   <a name="wickr-Type-User-suspended"></a>
Indicates whether the user is currently suspended and unable to access the network.
Type: Boolean
Required: No

 ** type **   <a name="wickr-Type-User-type"></a>
The descriptive type of the user account (e.g., 'user').
Type: String
Pattern: `[\S\s]*`
Required: No

 ** uname **   <a name="wickr-Type-User-uname"></a>
The unique identifier for the user.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** userId **   <a name="wickr-Type-User-userId"></a>
The unique identifier for the user within the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`
Required: No

 ** username **   <a name="wickr-Type-User-username"></a>
The email address or username of the user. For bots, this must end in 'bot'.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/User)
