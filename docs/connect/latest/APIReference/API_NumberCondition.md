---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_NumberCondition.html
---

# NumberCondition
<a name="API_NumberCondition"></a>

A leaf node condition which can be used to specify a numeric condition.

**Note**
The currently supported value for `FieldName` is `limit`.

## Contents
<a name="API_NumberCondition_Contents"></a>

 ** ComparisonType **   <a name="connect-Type-NumberCondition-ComparisonType"></a>
The type of comparison to be made when evaluating the number condition.
Type: String
Valid Values: `GREATER_OR_EQUAL | GREATER | LESSER_OR_EQUAL | LESSER | EQUAL | NOT_EQUAL | RANGE`
Required: No

 ** FieldName **   <a name="connect-Type-NumberCondition-FieldName"></a>
The name of the field in the number condition.
Type: String
Required: No

 ** MaxValue **   <a name="connect-Type-NumberCondition-MaxValue"></a>
The maxValue to be used while evaluating the number condition.
Type: Integer
Required: No

 ** MinValue **   <a name="connect-Type-NumberCondition-MinValue"></a>
The minValue to be used while evaluating the number condition.
Type: Integer
Required: No

## See Also
<a name="API_NumberCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/NumberCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/NumberCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/NumberCondition)
