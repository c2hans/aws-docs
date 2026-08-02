---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ParameterDeclaration.html
---

# ParameterDeclaration
<a name="API_ParameterDeclaration"></a>

The declaration definition of a parameter.

For more information, see [Parameters in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) in the *Amazon Quick Suite User Guide*.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_ParameterDeclaration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DateTimeParameterDeclaration **   <a name="QS-Type-ParameterDeclaration-DateTimeParameterDeclaration"></a>
A parameter declaration for the `DateTime` data type.
Type: [DateTimeParameterDeclaration](API_DateTimeParameterDeclaration.md) object
Required: No

 ** DecimalParameterDeclaration **   <a name="QS-Type-ParameterDeclaration-DecimalParameterDeclaration"></a>
A parameter declaration for the `Decimal` data type.
Type: [DecimalParameterDeclaration](API_DecimalParameterDeclaration.md) object
Required: No

 ** IntegerParameterDeclaration **   <a name="QS-Type-ParameterDeclaration-IntegerParameterDeclaration"></a>
A parameter declaration for the `Integer` data type.
Type: [IntegerParameterDeclaration](API_IntegerParameterDeclaration.md) object
Required: No

 ** StringParameterDeclaration **   <a name="QS-Type-ParameterDeclaration-StringParameterDeclaration"></a>
A parameter declaration for the `String` data type.
Type: [StringParameterDeclaration](API_StringParameterDeclaration.md) object
Required: No

## See Also
<a name="API_ParameterDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ParameterDeclaration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ParameterDeclaration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ParameterDeclaration)
