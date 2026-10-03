---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_RegistrationAssociationSummary.html
---

# RegistrationAssociationSummary
<a name="API_RegistrationAssociationSummary"></a>

Contains summary information about a registration that is associated with a brand profile.

## Contents
<a name="API_RegistrationAssociationSummary_Contents"></a>

 ** createdAt **   <a name="endusermessaging-Type-RegistrationAssociationSummary-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** registrationId **   <a name="endusermessaging-Type-RegistrationAssociationSummary-registrationId"></a>
The identifier of the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** registrationType **   <a name="endusermessaging-Type-RegistrationAssociationSummary-registrationType"></a>
The type of the registration, for example US\_TOLL\_FREE\_REGISTRATION or SENDER\_ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** smartMatchUsed **   <a name="endusermessaging-Type-RegistrationAssociationSummary-smartMatchUsed"></a>
Specifies whether smart matching was used to create the association.
Type: Boolean
Required: Yes

## See Also
<a name="API_RegistrationAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/RegistrationAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/RegistrationAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/RegistrationAssociationSummary)
