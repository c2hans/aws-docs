---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_TemplateVariableMetadata.html
---

# TemplateVariableMetadata
<a name="API_TemplateVariableMetadata"></a>

Contains metadata about a template variable.

## Contents
<a name="API_TemplateVariableMetadata_Contents"></a>

 ** Required **   <a name="pinpoint-Type-TemplateVariableMetadata-Required"></a>
Whether the variable is required.
Type: Boolean
Required: Yes

 ** Type **   <a name="pinpoint-Type-TemplateVariableMetadata-Type"></a>
The type of the variable.
Type: String
Valid Values: `STRING | INTEGER | BOOLEAN`
Required: Yes

 ** DefaultValue **   <a name="pinpoint-Type-TemplateVariableMetadata-DefaultValue"></a>
The default value for the variable.
Type: String
Required: No

 ** Description **   <a name="pinpoint-Type-TemplateVariableMetadata-Description"></a>
A description of the variable.
Type: String
Required: No

 ** MaxLength **   <a name="pinpoint-Type-TemplateVariableMetadata-MaxLength"></a>
The maximum length for string variables.
Type: Integer
Required: No

 ** MaxValue **   <a name="pinpoint-Type-TemplateVariableMetadata-MaxValue"></a>
The maximum value for numeric variables.
Type: Integer
Required: No

 ** MinValue **   <a name="pinpoint-Type-TemplateVariableMetadata-MinValue"></a>
The minimum value for numeric variables.
Type: Integer
Required: No

 ** Pattern **   <a name="pinpoint-Type-TemplateVariableMetadata-Pattern"></a>
The regex pattern the variable value must match.
Type: String
Required: No

 ** Sample **   <a name="pinpoint-Type-TemplateVariableMetadata-Sample"></a>
A sample value for the variable.
Type: String
Required: No

 ** Source **   <a name="pinpoint-Type-TemplateVariableMetadata-Source"></a>
The source of the variable, either `CUSTOMER` or `SYSTEM`.
Type: String
Valid Values: `CUSTOMER | SYSTEM`
Required: No

## See Also
<a name="API_TemplateVariableMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/TemplateVariableMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/TemplateVariableMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/TemplateVariableMetadata)
