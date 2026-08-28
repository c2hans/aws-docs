---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ObjectAttribute.html
---

# ObjectAttribute
<a name="API_connect-customer-profiles_ObjectAttribute"></a>

The criteria that a specific object attribute must meet to trigger the destination.

## Contents
<a name="API_connect-customer-profiles_ObjectAttribute_Contents"></a>

 ** ComparisonOperator **   <a name="connect-Type-connect-customer-profiles_ObjectAttribute-ComparisonOperator"></a>
The operator used to compare an attribute against a list of values.
Type: String
Valid Values: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH | GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | EQUAL | BEFORE | AFTER | ON | BETWEEN | NOT_BETWEEN`
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_ObjectAttribute-Values"></a>
A list of attribute values used for comparison.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** FieldName **   <a name="connect-Type-connect-customer-profiles_ObjectAttribute-FieldName"></a>
A field defined within an object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_.-]+$`
Required: No

 ** Source **   <a name="connect-Type-connect-customer-profiles_ObjectAttribute-Source"></a>
An attribute contained within a source object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_connect-customer-profiles_ObjectAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ObjectAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ObjectAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ObjectAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
