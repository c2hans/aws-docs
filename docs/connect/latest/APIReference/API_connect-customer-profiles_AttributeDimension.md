---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_AttributeDimension.html
---

# AttributeDimension
<a name="API_connect-customer-profiles_AttributeDimension"></a>

Object that segments on various Customer Profile's fields.

## Contents
<a name="API_connect-customer-profiles_AttributeDimension_Contents"></a>

 ** DimensionType **   <a name="connect-Type-connect-customer-profiles_AttributeDimension-DimensionType"></a>
The action to segment with.
Type: String
Valid Values: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH | BEFORE | AFTER | BETWEEN | NOT_BETWEEN | ON | GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | EQUAL | LIST_CONTAINS | LIST_CONTAINS_ALL`
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_AttributeDimension-Values"></a>
The values to apply the DimensionType on. To reference a calculated attribute or profile attribute as a dynamic value, use handlebar notation: `{{_profile.ProfileAttributeName}}` or `{{_calculated_attribute.CalculatedAttributeName}}`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_connect-customer-profiles_AttributeDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AttributeDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AttributeDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AttributeDimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
