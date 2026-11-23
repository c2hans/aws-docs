---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormItemEnablementSourceValue.html
---

# EvaluationFormItemEnablementSourceValue

An enablement expression source value. Provide only the value member that matches the specified `Type`.

## Contents
<a name="API_EvaluationFormItemEnablementSourceValue_Contents"></a>

 ** Type **   <a name="connect-Type-EvaluationFormItemEnablementSourceValue-Type"></a>
A type of source item value. Valid values: `OPTION_REF_ID` \| `STRING_VALUE` \| `NUMERIC_VALUE` \| `BOOLEAN_VALUE` \| `DATETIME_VALUE`.
Type: String
Valid Values: `OPTION_REF_ID | STRING_VALUE | NUMERIC_VALUE | BOOLEAN_VALUE | DATETIME_VALUE`
Required: Yes

 ** BooleanValue **   <a name="connect-Type-EvaluationFormItemEnablementSourceValue-BooleanValue"></a>
A Boolean value to compare against the source. Use when `Type` is `BOOLEAN_VALUE`.
Type: Boolean
Required: No

 ** DateTimeValue **   <a name="connect-Type-EvaluationFormItemEnablementSourceValue-DateTimeValue"></a>
A date and time value to compare against the source. Use when `Type` is `DATETIME_VALUE`.
Type: Timestamp
Required: No

 ** NumericValue **   <a name="connect-Type-EvaluationFormItemEnablementSourceValue-NumericValue"></a>
A numeric value to compare against the source. Use when `Type` is `NUMERIC_VALUE`.
Type: Double
Required: No

 ** RefId **   <a name="connect-Type-EvaluationFormItemEnablementSourceValue-RefId"></a>
A referenceId of the source value. Use when `Type` is `OPTION_REF_ID`.
Type: String
Required: No

 ** StringValue **   <a name="connect-Type-EvaluationFormItemEnablementSourceValue-StringValue"></a>
A string value to compare against the source. Use when `Type` is `STRING_VALUE`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

## See Also
<a name="API_EvaluationFormItemEnablementSourceValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormItemEnablementSourceValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormItemEnablementSourceValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormItemEnablementSourceValue)
