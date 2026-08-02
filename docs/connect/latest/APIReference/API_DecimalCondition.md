---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DecimalCondition.html
---

# DecimalCondition
<a name="API_DecimalCondition"></a>

A decimal search condition for Search APIs.

## Contents
<a name="API_DecimalCondition_Contents"></a>

 ** ComparisonType **   <a name="connect-Type-DecimalCondition-ComparisonType"></a>
The type of comparison to be made when evaluating the decimal condition.
Type: String
Valid Values: `GREATER_OR_EQUAL | GREATER | LESSER_OR_EQUAL | LESSER | EQUAL | NOT_EQUAL | RANGE`
Required: No

 ** FieldName **   <a name="connect-Type-DecimalCondition-FieldName"></a>
A name of the decimal property to be searched.
Type: String
Required: No

 ** MaxValue **   <a name="connect-Type-DecimalCondition-MaxValue"></a>
A maximum value of the decimal property.
Type: Double
Required: No

 ** MinValue **   <a name="connect-Type-DecimalCondition-MinValue"></a>
A minimum value of the decimal property.
Type: Double
Required: No

## See Also
<a name="API_DecimalCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DecimalCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DecimalCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DecimalCondition)
