---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ProfileAttributes.html
---

# ProfileAttributes
<a name="API_connect-customer-profiles_ProfileAttributes"></a>

The object used to segment on attributes within the customer profile.

## Contents
<a name="API_connect-customer-profiles_ProfileAttributes_Contents"></a>

 ** AccountNumber **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-AccountNumber"></a>
A field to describe values to segment on within account number.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** AdditionalInformation **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-AdditionalInformation"></a>
A field to describe values to segment on within additional information.
Type: [ExtraLengthValueProfileDimension](API_connect-customer-profiles_ExtraLengthValueProfileDimension.md) object
Required: No

 ** Address **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-Address"></a>
A field to describe values to segment on within address.
Type: [AddressDimension](API_connect-customer-profiles_AddressDimension.md) object
Required: No

 ** Attributes **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-Attributes"></a>
A field to describe values to segment on within attributes.
Type: String to [AttributeDimension](API_connect-customer-profiles_AttributeDimension.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** BillingAddress **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-BillingAddress"></a>
A field to describe values to segment on within billing address.
Type: [AddressDimension](API_connect-customer-profiles_AddressDimension.md) object
Required: No

 ** BirthDate **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-BirthDate"></a>
A field to describe values to segment on within birthDate.
Type: [DateDimension](API_connect-customer-profiles_DateDimension.md) object
Required: No

 ** BusinessEmailAddress **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-BusinessEmailAddress"></a>
A field to describe values to segment on within business email address.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** BusinessName **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-BusinessName"></a>
A field to describe values to segment on within business name.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** BusinessPhoneNumber **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-BusinessPhoneNumber"></a>
A field to describe values to segment on within business phone number.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** EmailAddress **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-EmailAddress"></a>
A field to describe values to segment on within email address.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** FirstName **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-FirstName"></a>
A field to describe values to segment on within first name.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** GenderString **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-GenderString"></a>
A field to describe values to segment on within genderString.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** HomePhoneNumber **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-HomePhoneNumber"></a>
A field to describe values to segment on within home phone number.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** LastName **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-LastName"></a>
A field to describe values to segment on within last name.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** MailingAddress **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-MailingAddress"></a>
A field to describe values to segment on within mailing address.
Type: [AddressDimension](API_connect-customer-profiles_AddressDimension.md) object
Required: No

 ** MiddleName **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-MiddleName"></a>
A field to describe values to segment on within middle name.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** MobilePhoneNumber **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-MobilePhoneNumber"></a>
A field to describe values to segment on within mobile phone number.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** PartyTypeString **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-PartyTypeString"></a>
A field to describe values to segment on within partyTypeString.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** PersonalEmailAddress **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-PersonalEmailAddress"></a>
A field to describe values to segment on within personal email address.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** PhoneNumber **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-PhoneNumber"></a>
A field to describe values to segment on within phone number.
Type: [ProfileDimension](API_connect-customer-profiles_ProfileDimension.md) object
Required: No

 ** ProfileType **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-ProfileType"></a>
A field to describe values to segment on within profile type.
Type: [ProfileTypeDimension](API_connect-customer-profiles_ProfileTypeDimension.md) object
Required: No

 ** ShippingAddress **   <a name="connect-Type-connect-customer-profiles_ProfileAttributes-ShippingAddress"></a>
A field to describe values to segment on within shipping address.
Type: [AddressDimension](API_connect-customer-profiles_AddressDimension.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_ProfileAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ProfileAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ProfileAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ProfileAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
