---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExpressionVariable.html
---

# ExpressionVariable
<a name="API_ExpressionVariable"></a>

Contains expression variable information.

## Contents
<a name="API_ExpressionVariable_Contents"></a>

 ** name **   <a name="iotsitewise-Type-ExpressionVariable-name"></a>
The friendly name of the variable to be used in the expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z][a-z0-9_]*$`
Required: Yes

 ** value **   <a name="iotsitewise-Type-ExpressionVariable-value"></a>
The variable that identifies an asset property from which to use values.
Type: [VariableValue](API_VariableValue.md) object
Required: Yes

## See Also
<a name="API_ExpressionVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ExpressionVariable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ExpressionVariable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ExpressionVariable)
