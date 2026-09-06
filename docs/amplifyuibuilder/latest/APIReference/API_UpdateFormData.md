---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateFormData.html
---

# UpdateFormData
<a name="API_UpdateFormData"></a>

Updates and saves all of the information about a form, based on form ID.

## Contents
<a name="API_UpdateFormData_Contents"></a>

 ** cta **   <a name="amplifyuibuilder-Type-UpdateFormData-cta"></a>
The `FormCTA` object that stores the call to action configuration for the form.
Type: [FormCTA](API_FormCTA.md) object
Required: No

 ** dataType **   <a name="amplifyuibuilder-Type-UpdateFormData-dataType"></a>
The type of data source to use to create the form.
Type: [FormDataTypeConfig](API_FormDataTypeConfig.md) object
Required: No

 ** fields **   <a name="amplifyuibuilder-Type-UpdateFormData-fields"></a>
The configuration information for the form's fields.
Type: String to [FieldConfig](API_FieldConfig.md) object map
Required: No

 ** formActionType **   <a name="amplifyuibuilder-Type-UpdateFormData-formActionType"></a>
Specifies whether to perform a create or update action on the form.
Type: String
Valid Values: `create | update`
Required: No

 ** labelDecorator **   <a name="amplifyuibuilder-Type-UpdateFormData-labelDecorator"></a>
Specifies an icon or decoration to display on the form.
Type: String
Valid Values: `required | optional | none`
Required: No

 ** name **   <a name="amplifyuibuilder-Type-UpdateFormData-name"></a>
The name of the form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** schemaVersion **   <a name="amplifyuibuilder-Type-UpdateFormData-schemaVersion"></a>
The schema version of the form.
Type: String
Required: No

 ** sectionalElements **   <a name="amplifyuibuilder-Type-UpdateFormData-sectionalElements"></a>
The configuration information for the visual helper elements for the form. These elements are not associated with any data.
Type: String to [SectionalElement](API_SectionalElement.md) object map
Required: No

 ** style **   <a name="amplifyuibuilder-Type-UpdateFormData-style"></a>
The configuration for the form's style.
Type: [FormStyle](API_FormStyle.md) object
Required: No

## See Also
<a name="API_UpdateFormData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/UpdateFormData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/UpdateFormData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/UpdateFormData)
