---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateFormData.html
---

# CreateFormData
<a name="API_CreateFormData"></a>

Represents all of the information that is required to create a form.

## Contents
<a name="API_CreateFormData_Contents"></a>

 ** dataType **   <a name="amplifyuibuilder-Type-CreateFormData-dataType"></a>
The type of data source to use to create the form.
Type: [FormDataTypeConfig](API_FormDataTypeConfig.md) object
Required: Yes

 ** fields **   <a name="amplifyuibuilder-Type-CreateFormData-fields"></a>
The configuration information for the form's fields.
Type: String to [FieldConfig](API_FieldConfig.md) object map
Required: Yes

 ** formActionType **   <a name="amplifyuibuilder-Type-CreateFormData-formActionType"></a>
Specifies whether to perform a create or update action on the form.
Type: String
Valid Values: `create | update`
Required: Yes

 ** name **   <a name="amplifyuibuilder-Type-CreateFormData-name"></a>
The name of the form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** schemaVersion **   <a name="amplifyuibuilder-Type-CreateFormData-schemaVersion"></a>
The schema version of the form.
Type: String
Required: Yes

 ** sectionalElements **   <a name="amplifyuibuilder-Type-CreateFormData-sectionalElements"></a>
The configuration information for the visual helper elements for the form. These elements are not associated with any data.
Type: String to [SectionalElement](API_SectionalElement.md) object map
Required: Yes

 ** style **   <a name="amplifyuibuilder-Type-CreateFormData-style"></a>
The configuration for the form's style.
Type: [FormStyle](API_FormStyle.md) object
Required: Yes

 ** cta **   <a name="amplifyuibuilder-Type-CreateFormData-cta"></a>
The `FormCTA` object that stores the call to action configuration for the form.
Type: [FormCTA](API_FormCTA.md) object
Required: No

 ** labelDecorator **   <a name="amplifyuibuilder-Type-CreateFormData-labelDecorator"></a>
Specifies an icon or decoration to display on the form.
Type: String
Valid Values: `required | optional | none`
Required: No

 ** tags **   <a name="amplifyuibuilder-Type-CreateFormData-tags"></a>
One or more key-value pairs to use when tagging the form data.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_CreateFormData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CreateFormData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CreateFormData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CreateFormData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
