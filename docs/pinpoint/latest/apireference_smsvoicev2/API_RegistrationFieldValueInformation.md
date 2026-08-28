---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationFieldValueInformation.html
---

# RegistrationFieldValueInformation
<a name="API_RegistrationFieldValueInformation"></a>

Provides the values of the specified field.

## Contents
<a name="API_RegistrationFieldValueInformation_Contents"></a>

 ** FieldPath **   <a name="pinpoint-Type-RegistrationFieldValueInformation-FieldPath"></a>
The path to the registration form field. You can use [DescribeRegistrationFieldDefinitions](API_DescribeRegistrationFieldDefinitions.md) for a list of **FieldPaths**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`
Required: Yes

 ** DeniedReason **   <a name="pinpoint-Type-RegistrationFieldValueInformation-DeniedReason"></a>
A description of why the registration was denied.
Type: String
Required: No

 ** Feedback **   <a name="pinpoint-Type-RegistrationFieldValueInformation-Feedback"></a>
Generative AI feedback information provided for this specific field during the registration review process. This may include validation errors, suggestions for improvement, or additional requirements.
Type: String
Required: No

 ** RegistrationAttachmentId **   <a name="pinpoint-Type-RegistrationFieldValueInformation-RegistrationAttachmentId"></a>
The unique identifier for the registration attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** SelectChoices **   <a name="pinpoint-Type-RegistrationFieldValueInformation-SelectChoices"></a>
An array of values for the form field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** TextValue **   <a name="pinpoint-Type-RegistrationFieldValueInformation-TextValue"></a>
The text data for a free form field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_RegistrationFieldValueInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationFieldValueInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationFieldValueInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationFieldValueInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
