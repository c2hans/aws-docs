---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FieldConfig.html
---

# FieldConfig
<a name="API_FieldConfig"></a>

Describes the configuration information for a field in a table.

## Contents
<a name="API_FieldConfig_Contents"></a>

 ** excluded **   <a name="amplifyuibuilder-Type-FieldConfig-excluded"></a>
Specifies whether to hide a field.
Type: Boolean
Required: No

 ** inputType **   <a name="amplifyuibuilder-Type-FieldConfig-inputType"></a>
Describes the configuration for the default input value to display for a field.
Type: [FieldInputConfig](API_FieldInputConfig.md) object
Required: No

 ** label **   <a name="amplifyuibuilder-Type-FieldConfig-label"></a>
The label for the field.
Type: String
Required: No

 ** position **   <a name="amplifyuibuilder-Type-FieldConfig-position"></a>
Specifies the field position.
Type: [FieldPosition](API_FieldPosition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** validations **   <a name="amplifyuibuilder-Type-FieldConfig-validations"></a>
The validations to perform on the value in the field.
Type: Array of [FieldValidationConfiguration](API_FieldValidationConfiguration.md) objects
Required: No

## See Also
<a name="API_FieldConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/FieldConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/FieldConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/FieldConfig)
