---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_AttributeTypesSelector.html
---

# AttributeTypesSelector
<a name="API_connect-customer-profiles_AttributeTypesSelector"></a>

Configuration information about the `AttributeTypesSelector `where the rule-based identity resolution uses to match profiles. You can choose how profiles are compared across attribute types and which attribute to use for matching from each type. There are three attribute types you can configure:
+ Email type
  + You can choose from `Email`, `BusinessEmail`, and `PersonalEmail`
+ Phone number type
  + You can choose from `Phone`, `HomePhone`, and `MobilePhone`
+ Address type
  + You can choose from `Address`, `BusinessAddress`, `MaillingAddress`, and `ShippingAddress`

You can either choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `AttributeMatchingModel`. When choosing `MANY_TO_MANY`, the system can match attribute across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A and the value of `BusinessEmail` field of Profile B matches, the two profiles are matched on the Email type. When choosing `ONE_TO_ONE` the system can only match if the sub-types are exact matches. For example, only when the value of the `Email` field of Profile A and the value of the `Email` field of Profile B matches, the two profiles are matched on the Email type.

## Contents
<a name="API_connect-customer-profiles_AttributeTypesSelector_Contents"></a>

 ** AttributeMatchingModel **   <a name="connect-Type-connect-customer-profiles_AttributeTypesSelector-AttributeMatchingModel"></a>
Configures the `AttributeMatchingModel`, you can either choose `ONE_TO_ONE` or `MANY_TO_MANY`.
Type: String
Valid Values: `ONE_TO_ONE | MANY_TO_MANY`
Required: Yes

 ** Address **   <a name="connect-Type-connect-customer-profiles_AttributeTypesSelector-Address"></a>
The `Address` type. You can choose from `Address`, `BusinessAddress`, `MaillingAddress`, and `ShippingAddress`.
You only can use the Address type in the `MatchingRule`. For example, if you want to match profile based on `BusinessAddress.City` or `MaillingAddress.City`, you need to choose the `BusinessAddress` and the `MaillingAddress` to represent the Address type and specify the `Address.City` on the matching rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** EmailAddress **   <a name="connect-Type-connect-customer-profiles_AttributeTypesSelector-EmailAddress"></a>
The `Email` type. You can choose from `EmailAddress`, `BusinessEmailAddress` and `PersonalEmailAddress`.
You only can use the `EmailAddress` type in the `MatchingRule`. For example, if you want to match profile based on `PersonalEmailAddress` or `BusinessEmailAddress`, you need to choose the `PersonalEmailAddress` and the `BusinessEmailAddress` to represent the `EmailAddress` type and only specify the `EmailAddress` on the matching rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PhoneNumber **   <a name="connect-Type-connect-customer-profiles_AttributeTypesSelector-PhoneNumber"></a>
The `PhoneNumber` type. You can choose from `PhoneNumber`, `HomePhoneNumber`, and `MobilePhoneNumber`.
You only can use the `PhoneNumber` type in the `MatchingRule`. For example, if you want to match a profile based on `Phone` or `HomePhone`, you need to choose the `Phone` and the `HomePhone` to represent the `PhoneNumber` type and only specify the `PhoneNumber` on the matching rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_connect-customer-profiles_AttributeTypesSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AttributeTypesSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AttributeTypesSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AttributeTypesSelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
