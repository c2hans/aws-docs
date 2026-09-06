---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FieldInputConfig.html
---

# FieldInputConfig
<a name="API_FieldInputConfig"></a>

Describes the configuration for the default input values to display for a field.

## Contents
<a name="API_FieldInputConfig_Contents"></a>

 ** type **   <a name="amplifyuibuilder-Type-FieldInputConfig-type"></a>
The input type for the field.
Type: String
Required: Yes

 ** defaultChecked **   <a name="amplifyuibuilder-Type-FieldInputConfig-defaultChecked"></a>
Specifies whether a field has a default value.
Type: Boolean
Required: No

 ** defaultCountryCode **   <a name="amplifyuibuilder-Type-FieldInputConfig-defaultCountryCode"></a>
The default country code for a phone number.
Type: String
Required: No

 ** defaultValue **   <a name="amplifyuibuilder-Type-FieldInputConfig-defaultValue"></a>
The default value for the field.
Type: String
Required: No

 ** descriptiveText **   <a name="amplifyuibuilder-Type-FieldInputConfig-descriptiveText"></a>
The text to display to describe the field.
Type: String
Required: No

 ** fileUploaderConfig **   <a name="amplifyuibuilder-Type-FieldInputConfig-fileUploaderConfig"></a>
The configuration for the file uploader field.
Type: [FileUploaderFieldConfig](API_FileUploaderFieldConfig.md) object
Required: No

 ** isArray **   <a name="amplifyuibuilder-Type-FieldInputConfig-isArray"></a>
Specifies whether to render the field as an array. This property is ignored if the `dataSourceType` for the form is a Data Store.
Type: Boolean
Required: No

 ** maxValue **   <a name="amplifyuibuilder-Type-FieldInputConfig-maxValue"></a>
The maximum value to display for the field.
Type: Float
Required: No

 ** minValue **   <a name="amplifyuibuilder-Type-FieldInputConfig-minValue"></a>
The minimum value to display for the field.
Type: Float
Required: No

 ** name **   <a name="amplifyuibuilder-Type-FieldInputConfig-name"></a>
The name of the field.
Type: String
Required: No

 ** placeholder **   <a name="amplifyuibuilder-Type-FieldInputConfig-placeholder"></a>
The text to display as a placeholder for the field.
Type: String
Required: No

 ** readOnly **   <a name="amplifyuibuilder-Type-FieldInputConfig-readOnly"></a>
Specifies a read only field.
Type: Boolean
Required: No

 ** required **   <a name="amplifyuibuilder-Type-FieldInputConfig-required"></a>
Specifies a field that requires input.
Type: Boolean
Required: No

 ** step **   <a name="amplifyuibuilder-Type-FieldInputConfig-step"></a>
The stepping increment for a numeric value in a field.
Type: Float
Required: No

 ** value **   <a name="amplifyuibuilder-Type-FieldInputConfig-value"></a>
The value for the field.
Type: String
Required: No

 ** valueMappings **   <a name="amplifyuibuilder-Type-FieldInputConfig-valueMappings"></a>
The information to use to customize the input fields with data at runtime.
Type: [ValueMappings](API_ValueMappings.md) object
Required: No

## See Also
<a name="API_FieldInputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/FieldInputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/FieldInputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/FieldInputConfig)
