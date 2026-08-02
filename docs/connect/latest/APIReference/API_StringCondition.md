---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StringCondition.html
---

# StringCondition
<a name="API_StringCondition"></a>

A leaf node condition which can be used to specify a string condition.

## Contents
<a name="API_StringCondition_Contents"></a>

 ** ComparisonType **   <a name="connect-Type-StringCondition-ComparisonType"></a>
The type of comparison to be made when evaluating the string condition.
Type: String
Valid Values: `STARTS_WITH | CONTAINS | EXACT`
Required: No

 ** FieldName **   <a name="connect-Type-StringCondition-FieldName"></a>
The name of the field in the string condition.
Type: String
Required: No

 ** Value **   <a name="connect-Type-StringCondition-Value"></a>
The value of the string.
Type: String
Required: No

## See Also
<a name="API_StringCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StringCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StringCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StringCondition)
