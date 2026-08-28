---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Profile.html
---

# Profile
<a name="API_connect-customer-profiles_Profile"></a>

The standard profile of a customer.

## Contents
<a name="API_connect-customer-profiles_Profile_Contents"></a>

 ** AccountNumber **   <a name="connect-Type-connect-customer-profiles_Profile-AccountNumber"></a>
An account number that you have assigned to the customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** AdditionalInformation **   <a name="connect-Type-connect-customer-profiles_Profile-AdditionalInformation"></a>
Any additional information relevant to the customer’s profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** Address **   <a name="connect-Type-connect-customer-profiles_Profile-Address"></a>
A generic address associated with the customer that is not mailing, shipping, or billing.
Type: [Address](API_connect-customer-profiles_Address.md) object
Required: No

 ** Attributes **   <a name="connect-Type-connect-customer-profiles_Profile-Attributes"></a>
A key value pair of attributes of a customer profile.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** BillingAddress **   <a name="connect-Type-connect-customer-profiles_Profile-BillingAddress"></a>
The customer’s billing address.
Type: [Address](API_connect-customer-profiles_Address.md) object
Required: No

 ** BirthDate **   <a name="connect-Type-connect-customer-profiles_Profile-BirthDate"></a>
The customer’s birth date.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** BusinessEmailAddress **   <a name="connect-Type-connect-customer-profiles_Profile-BusinessEmailAddress"></a>
The customer’s business email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** BusinessName **   <a name="connect-Type-connect-customer-profiles_Profile-BusinessName"></a>
The name of the customer’s business.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** BusinessPhoneNumber **   <a name="connect-Type-connect-customer-profiles_Profile-BusinessPhoneNumber"></a>
The customer’s home phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** EmailAddress **   <a name="connect-Type-connect-customer-profiles_Profile-EmailAddress"></a>
The customer’s email address, which has not been specified as a personal or business address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** EngagementPreferences **   <a name="connect-Type-connect-customer-profiles_Profile-EngagementPreferences"></a>
The customer or account’s engagement preferences.
Type: [EngagementPreferences](API_connect-customer-profiles_EngagementPreferences.md) object
Required: No

 ** FirstName **   <a name="connect-Type-connect-customer-profiles_Profile-FirstName"></a>
The customer’s first name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** FoundByItems **   <a name="connect-Type-connect-customer-profiles_Profile-FoundByItems"></a>
A list of items used to find a profile returned in a [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) response. An item is a key-value(s) pair that matches an attribute in the profile.
If the optional `AdditionalSearchKeys` parameter was included in the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) request, the `FoundByItems` list should be interpreted based on the `LogicalOperator` used in the request:
+  `AND` - The profile included in the response matched all of the search keys specified in the request. The `FoundByItems` will include all of the key-value(s) pairs that were specified in the request (as this is a requirement of `AND` search logic).
+  `OR` - The profile included in the response matched at least one of the search keys specified in the request. The `FoundByItems` will include each of the key-value(s) pairs that the profile was found by.
The `OR` relationship is the default behavior if the `LogicalOperator` parameter is not included in the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) request.
Type: Array of [FoundByKeyValue](API_connect-customer-profiles_FoundByKeyValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** Gender **   <a name="connect-Type-connect-customer-profiles_Profile-Gender"></a>
 *This member has been deprecated.*
The gender with which the customer identifies.
Type: String
Valid Values: `MALE | FEMALE | UNSPECIFIED`
Required: No

 ** GenderString **   <a name="connect-Type-connect-customer-profiles_Profile-GenderString"></a>
An alternative to Gender which accepts any string as input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** HomePhoneNumber **   <a name="connect-Type-connect-customer-profiles_Profile-HomePhoneNumber"></a>
The customer’s home phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** LastName **   <a name="connect-Type-connect-customer-profiles_Profile-LastName"></a>
The customer’s last name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** MailingAddress **   <a name="connect-Type-connect-customer-profiles_Profile-MailingAddress"></a>
The customer’s mailing address.
Type: [Address](API_connect-customer-profiles_Address.md) object
Required: No

 ** MiddleName **   <a name="connect-Type-connect-customer-profiles_Profile-MiddleName"></a>
The customer’s middle name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** MobilePhoneNumber **   <a name="connect-Type-connect-customer-profiles_Profile-MobilePhoneNumber"></a>
The customer’s mobile phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PartyType **   <a name="connect-Type-connect-customer-profiles_Profile-PartyType"></a>
 *This member has been deprecated.*
The type of profile used to describe the customer.
Type: String
Valid Values: `INDIVIDUAL | BUSINESS | OTHER`
Required: No

 ** PartyTypeString **   <a name="connect-Type-connect-customer-profiles_Profile-PartyTypeString"></a>
An alternative to PartyType which accepts any string as input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PersonalEmailAddress **   <a name="connect-Type-connect-customer-profiles_Profile-PersonalEmailAddress"></a>
The customer’s personal email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PhoneNumber **   <a name="connect-Type-connect-customer-profiles_Profile-PhoneNumber"></a>
The customer's phone number, which has not been specified as a mobile, home, or business number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ProfileId **   <a name="connect-Type-connect-customer-profiles_Profile-ProfileId"></a>
The unique identifier of a customer profile.
Type: String
Pattern: `[a-f0-9]{32}`
Required: No

 ** ProfileType **   <a name="connect-Type-connect-customer-profiles_Profile-ProfileType"></a>
The type of the profile.
Type: String
Valid Values: `ACCOUNT_PROFILE | PROFILE`
Required: No

 ** ShippingAddress **   <a name="connect-Type-connect-customer-profiles_Profile-ShippingAddress"></a>
The customer’s shipping address.
Type: [Address](API_connect-customer-profiles_Address.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_Profile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Profile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Profile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Profile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
