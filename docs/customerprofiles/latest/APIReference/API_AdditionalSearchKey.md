---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_AdditionalSearchKey.html
---

# AdditionalSearchKey
<a name="API_connect-customer-profiles_AdditionalSearchKey"></a>

A data type pair that consists of a `KeyName` and `Values` list that is used in conjunction with the [KeyName](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html#customerprofiles-SearchProfiles-request-KeyName) and [Values](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html#customerprofiles-SearchProfiles-request-Values) parameters to search for profiles using the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) API.

## Contents
<a name="API_connect-customer-profiles_AdditionalSearchKey_Contents"></a>

 ** KeyName **   <a name="connect-Type-connect-customer-profiles_AdditionalSearchKey-KeyName"></a>
A searchable identifier of a customer profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_AdditionalSearchKey-Values"></a>
A list of key values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_AdditionalSearchKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AdditionalSearchKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AdditionalSearchKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AdditionalSearchKey)
