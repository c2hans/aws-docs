---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationFieldDefinition.html
---

# RegistrationFieldDefinition
<a name="API_RegistrationFieldDefinition"></a>

Provides a description of the specified field.

## Contents
<a name="API_RegistrationFieldDefinition_Contents"></a>

 ** DisplayHints **   <a name="pinpoint-Type-RegistrationFieldDefinition-DisplayHints"></a>
An array of RegistrationFieldDisplayHints objects for the field.
Type: [RegistrationFieldDisplayHints](API_RegistrationFieldDisplayHints.md) object
Required: Yes

 ** FieldPath **   <a name="pinpoint-Type-RegistrationFieldDefinition-FieldPath"></a>
The path to the registration form field. You can use [DescribeRegistrationFieldDefinitions](API_DescribeRegistrationFieldDefinitions.md) for a list of **FieldPaths**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`
Required: Yes

 ** FieldRequirement **   <a name="pinpoint-Type-RegistrationFieldDefinition-FieldRequirement"></a>
Specifies if the field for the registration form is required, conditional or optional.
Type: String
Valid Values: `REQUIRED | CONDITIONAL | OPTIONAL`
Required: Yes

 ** FieldType **   <a name="pinpoint-Type-RegistrationFieldDefinition-FieldType"></a>
The type of field.
Type: String
Valid Values: `SELECT | TEXT | ATTACHMENT`
Required: Yes

 ** SectionPath **   <a name="pinpoint-Type-RegistrationFieldDefinition-SectionPath"></a>
The section path of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** SelectValidation **   <a name="pinpoint-Type-RegistrationFieldDefinition-SelectValidation"></a>
The validation rules for a select field.
Type: [SelectValidation](API_SelectValidation.md) object
Required: No

 ** TextValidation **   <a name="pinpoint-Type-RegistrationFieldDefinition-TextValidation"></a>
The validation rules for a text field.
Type: [TextValidation](API_TextValidation.md) object
Required: No

## See Also
<a name="API_RegistrationFieldDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationFieldDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationFieldDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationFieldDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
