---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CommandParameterValueComparisonOperand.html
---

# CommandParameterValueComparisonOperand
<a name="API_CommandParameterValueComparisonOperand"></a>

The comparison operand used to compare the defined value against the value supplied in request.

## Contents
<a name="API_CommandParameterValueComparisonOperand_Contents"></a>

 ** number **   <a name="iot-Type-CommandParameterValueComparisonOperand-number"></a>
An operand of number value type, defined as a string.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** numberRange **   <a name="iot-Type-CommandParameterValueComparisonOperand-numberRange"></a>
An operand of numerical range value type.
Type: [CommandParameterValueNumberRange](API_CommandParameterValueNumberRange.md) object
Required: No

 ** numbers **   <a name="iot-Type-CommandParameterValueComparisonOperand-numbers"></a>
A List of operands of numerical value type, defined as strings.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1.
Required: No

 ** string **   <a name="iot-Type-CommandParameterValueComparisonOperand-string"></a>
An operand of string value type.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** strings **   <a name="iot-Type-CommandParameterValueComparisonOperand-strings"></a>
A List of operands of string value type.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_CommandParameterValueComparisonOperand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CommandParameterValueComparisonOperand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CommandParameterValueComparisonOperand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CommandParameterValueComparisonOperand)
