---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Form.html
---

# Form
<a name="API_Form"></a>

Contains the configuration settings for a `Form` user interface (UI) element for an Amplify app. A form is a component you can add to your project by specifying a data source as the default configuration for the form.

## Contents
<a name="API_Form_Contents"></a>

 ** appId **   <a name="amplifyuibuilder-Type-Form-appId"></a>
The unique ID of the Amplify app associated with the form.
Type: String
Required: Yes

 ** dataType **   <a name="amplifyuibuilder-Type-Form-dataType"></a>
The type of data source to use to create the form.
Type: [FormDataTypeConfig](API_FormDataTypeConfig.md) object
Required: Yes

 ** environmentName **   <a name="amplifyuibuilder-Type-Form-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Type: String
Required: Yes

 ** fields **   <a name="amplifyuibuilder-Type-Form-fields"></a>
Stores the information about the form's fields.
Type: String to [FieldConfig](API_FieldConfig.md) object map
Required: Yes

 ** formActionType **   <a name="amplifyuibuilder-Type-Form-formActionType"></a>
The operation to perform on the specified form.
Type: String
Valid Values: `create | update`
Required: Yes

 ** id **   <a name="amplifyuibuilder-Type-Form-id"></a>
The unique ID of the form.
Type: String
Required: Yes

 ** name **   <a name="amplifyuibuilder-Type-Form-name"></a>
The name of the form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** schemaVersion **   <a name="amplifyuibuilder-Type-Form-schemaVersion"></a>
The schema version of the form when it was imported.
Type: String
Required: Yes

 ** sectionalElements **   <a name="amplifyuibuilder-Type-Form-sectionalElements"></a>
Stores the visual helper elements for the form that are not associated with any data.
Type: String to [SectionalElement](API_SectionalElement.md) object map
Required: Yes

 ** style **   <a name="amplifyuibuilder-Type-Form-style"></a>
Stores the configuration for the form's style.
Type: [FormStyle](API_FormStyle.md) object
Required: Yes

 ** cta **   <a name="amplifyuibuilder-Type-Form-cta"></a>
Stores the call to action configuration for the form.
Type: [FormCTA](API_FormCTA.md) object
Required: No

 ** labelDecorator **   <a name="amplifyuibuilder-Type-Form-labelDecorator"></a>
Specifies an icon or decoration to display on the form.
Type: String
Valid Values: `required | optional | none`
Required: No

 ** tags **   <a name="amplifyuibuilder-Type-Form-tags"></a>
One or more key-value pairs to use when tagging the form.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Form_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/Form)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/Form)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/Form)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
