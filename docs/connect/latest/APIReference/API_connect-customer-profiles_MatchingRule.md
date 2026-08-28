---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_MatchingRule.html
---

# MatchingRule
<a name="API_connect-customer-profiles_MatchingRule"></a>

Specifies how does the rule-based matching process should match profiles. You can choose from the following attributes to build the matching Rule:
+ AccountNumber
+ Address.Address
+ Address.City
+ Address.Country
+ Address.County
+ Address.PostalCode
+ Address.State
+ Address.Province
+ BirthDate
+ BusinessName
+ EmailAddress
+ FirstName
+ Gender
+ LastName
+ MiddleName
+ PhoneNumber
+ Any customized profile attributes that start with the `Attributes`

## Contents
<a name="API_connect-customer-profiles_MatchingRule_Contents"></a>

 ** Rule **   <a name="connect-Type-connect-customer-profiles_MatchingRule-Rule"></a>
A single rule level of the `MatchRules`. Configures how the rule-based matching process should match profiles.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_MatchingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/MatchingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/MatchingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/MatchingRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
