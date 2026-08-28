---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ObjectTypeField.html
---

# ObjectTypeField
<a name="API_connect-customer-profiles_ObjectTypeField"></a>

Represents a field in a ProfileObjectType.

## Contents
<a name="API_connect-customer-profiles_ObjectTypeField_Contents"></a>

 ** ContentType **   <a name="connect-Type-connect-customer-profiles_ObjectTypeField-ContentType"></a>
The content type of the field. Used for determining equality when searching.
Type: String
Valid Values: `STRING | NUMBER | PHONE_NUMBER | EMAIL_ADDRESS | NAME`
Required: No

 ** Source **   <a name="connect-Type-connect-customer-profiles_ObjectTypeField-Source"></a>
A field of a ProfileObject. For example: \_source.FirstName, where “\_source” is a ProfileObjectType of a Zendesk user and “FirstName” is a field in that ObjectType.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** Target **   <a name="connect-Type-connect-customer-profiles_ObjectTypeField-Target"></a>
The location of the data in the standard ProfileObject model. For example: \_profile.Address.PostalCode. Do not include sensitive or personally identifiable information (PII) in the target field name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_connect-customer-profiles_ObjectTypeField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ObjectTypeField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ObjectTypeField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ObjectTypeField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
