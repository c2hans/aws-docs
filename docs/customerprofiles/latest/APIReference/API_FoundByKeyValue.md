---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_FoundByKeyValue.html
---

# FoundByKeyValue
<a name="API_connect-customer-profiles_FoundByKeyValue"></a>

A data type pair that consists of a `KeyName` and `Values` list that were used to find a profile returned in response to a [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) request.

## Contents
<a name="API_connect-customer-profiles_FoundByKeyValue_Contents"></a>

 ** KeyName **   <a name="connect-Type-connect-customer-profiles_FoundByKeyValue-KeyName"></a>
A searchable identifier of a customer profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** Values **   <a name="connect-Type-connect-customer-profiles_FoundByKeyValue-Values"></a>
A list of key values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_connect-customer-profiles_FoundByKeyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/FoundByKeyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/FoundByKeyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/FoundByKeyValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
