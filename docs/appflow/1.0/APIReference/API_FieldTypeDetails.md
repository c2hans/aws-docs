---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_FieldTypeDetails.html
---

# FieldTypeDetails
<a name="API_FieldTypeDetails"></a>

 Contains details regarding the supported field type and the operators that can be applied for filtering.

## Contents
<a name="API_FieldTypeDetails_Contents"></a>

 ** fieldType **   <a name="appflow-Type-FieldTypeDetails-fieldType"></a>
 The type of field, such as string, integer, date, and so on.
Type: String
Required: Yes

 ** filterOperators **   <a name="appflow-Type-FieldTypeDetails-filterOperators"></a>
 The list of operators supported by a field.
Type: Array of strings
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | CONTAINS | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: Yes

 ** fieldLengthRange **   <a name="appflow-Type-FieldTypeDetails-fieldLengthRange"></a>
This is the allowable length range for this field's value.
Type: [Range](API_Range.md) object
Required: No

 ** fieldValueRange **   <a name="appflow-Type-FieldTypeDetails-fieldValueRange"></a>
The range of values this field can hold.
Type: [Range](API_Range.md) object
Required: No

 ** supportedDateFormat **   <a name="appflow-Type-FieldTypeDetails-supportedDateFormat"></a>
The date format that the field supports.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: No

 ** supportedValues **   <a name="appflow-Type-FieldTypeDetails-supportedValues"></a>
 The list of values that a field can contain. For example, a Boolean `fieldType` can have two values: "true" and "false".
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: No

 ** valueRegexPattern **   <a name="appflow-Type-FieldTypeDetails-valueRegexPattern"></a>
The regular expression pattern for the field name.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: No

## See Also
<a name="API_FieldTypeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/FieldTypeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/FieldTypeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/FieldTypeDetails)
