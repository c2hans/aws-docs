---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ContactPreference.html
---

# ContactPreference
<a name="API_connect-customer-profiles_ContactPreference"></a>

Object that defines users contact preference.

## Contents
<a name="API_connect-customer-profiles_ContactPreference_Contents"></a>

 ** ContactType **   <a name="connect-Type-connect-customer-profiles_ContactPreference-ContactType"></a>
The contact type used for engagement. For example: HomePhoneNumber, PersonalEmailAddress.
Type: String
Valid Values: `PhoneNumber | MobilePhoneNumber | HomePhoneNumber | BusinessPhoneNumber | EmailAddress | PersonalEmailAddress | BusinessEmailAddress`
Required: No

 ** KeyName **   <a name="connect-Type-connect-customer-profiles_ContactPreference-KeyName"></a>
A searchable, unique identifier of a customer profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** KeyValue **   <a name="connect-Type-connect-customer-profiles_ContactPreference-KeyValue"></a>
The key value used to look up profile based off the keyName.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ProfileId **   <a name="connect-Type-connect-customer-profiles_ContactPreference-ProfileId"></a>
The unique identifier of a customer profile.
Type: String
Pattern: `[a-f0-9]{32}`
Required: No

## See Also
<a name="API_connect-customer-profiles_ContactPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ContactPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ContactPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ContactPreference)
