---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TaskTemplateField.html
---

# TaskTemplateField
<a name="API_TaskTemplateField"></a>

Describes a single task template field.

## Contents
<a name="API_TaskTemplateField_Contents"></a>

 ** Id **   <a name="connect-Type-TaskTemplateField-Id"></a>
The unique identifier for the field.
Type: [TaskTemplateFieldIdentifier](API_TaskTemplateFieldIdentifier.md) object
Required: Yes

 ** Description **   <a name="connect-Type-TaskTemplateField-Description"></a>
The description of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** SingleSelectOptions **   <a name="connect-Type-TaskTemplateField-SingleSelectOptions"></a>
A list of options for a single select field.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Type **   <a name="connect-Type-TaskTemplateField-Type"></a>
Indicates the type of field.
Type: String
Valid Values: `NAME | DESCRIPTION | SCHEDULED_TIME | QUICK_CONNECT | URL | NUMBER | TEXT | TEXT_AREA | DATE_TIME | BOOLEAN | SINGLE_SELECT | EMAIL | SELF_ASSIGN | EXPIRY_DURATION`
Required: No

## See Also
<a name="API_TaskTemplateField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TaskTemplateField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TaskTemplateField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TaskTemplateField)
