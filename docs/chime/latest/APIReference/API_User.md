---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_User.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# User
<a name="API_User"></a>

The user on the Amazon Chime account.

## Contents
<a name="API_User_Contents"></a>

 ** UserId **   <a name="chime-Type-User-UserId"></a>
The user ID.
Type: String
Required: Yes

 ** AccountId **   <a name="chime-Type-User-AccountId"></a>
The Amazon Chime account ID.
Type: String
Required: No

 ** AlexaForBusinessMetadata **   <a name="chime-Type-User-AlexaForBusinessMetadata"></a>
The Alexa for Business metadata.
Type: [AlexaForBusinessMetadata](API_AlexaForBusinessMetadata.md) object
Required: No

 ** DisplayName **   <a name="chime-Type-User-DisplayName"></a>
The display name of the user.
Type: String
Required: No

 ** InvitedOn **   <a name="chime-Type-User-InvitedOn"></a>
Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.
Type: Timestamp
Required: No

 ** LicenseType **   <a name="chime-Type-User-LicenseType"></a>
The license type for the user.
Type: String
Valid Values: `Basic | Plus | Pro | ProTrial`
Required: No

 ** PersonalPIN **   <a name="chime-Type-User-PersonalPIN"></a>
The user's personal meeting PIN.
Type: String
Required: No

 ** PrimaryEmail **   <a name="chime-Type-User-PrimaryEmail"></a>
The primary email address of the user.
Type: String
Pattern: `.+@.+\..+`
Required: No

 ** PrimaryProvisionedNumber **   <a name="chime-Type-User-PrimaryProvisionedNumber"></a>
The primary phone number associated with the user.
Type: String
Required: No

 ** RegisteredOn **   <a name="chime-Type-User-RegisteredOn"></a>
Date and time when the user is registered, in ISO 8601 format.
Type: Timestamp
Required: No

 ** UserInvitationStatus **   <a name="chime-Type-User-UserInvitationStatus"></a>
The user invite status.
Type: String
Valid Values: `Pending | Accepted | Failed`
Required: No

 ** UserRegistrationStatus **   <a name="chime-Type-User-UserRegistrationStatus"></a>
The user registration status.
Type: String
Valid Values: `Unregistered | Registered | Suspended`
Required: No

 ** UserType **   <a name="chime-Type-User-UserType"></a>
The user type.
Type: String
Valid Values: `PrivateUser | SharedDevice`
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/User)
