---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NumberDisplayFormatConfiguration.html
---

# NumberDisplayFormatConfiguration
<a name="API_NumberDisplayFormatConfiguration"></a>

The options that determine the number display format configuration.

## Contents
<a name="API_NumberDisplayFormatConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DecimalPlacesConfiguration **   <a name="QS-Type-NumberDisplayFormatConfiguration-DecimalPlacesConfiguration"></a>
The option that determines the decimal places configuration.
Type: [DecimalPlacesConfiguration](API_DecimalPlacesConfiguration.md) object
Required: No

 ** NegativeValueConfiguration **   <a name="QS-Type-NumberDisplayFormatConfiguration-NegativeValueConfiguration"></a>
The options that determine the negative value configuration.
Type: [NegativeValueConfiguration](API_NegativeValueConfiguration.md) object
Required: No

 ** NullValueFormatConfiguration **   <a name="QS-Type-NumberDisplayFormatConfiguration-NullValueFormatConfiguration"></a>
The options that determine the null value format configuration.
Type: [NullValueFormatConfiguration](API_NullValueFormatConfiguration.md) object
Required: No

 ** NumberScale **   <a name="QS-Type-NumberDisplayFormatConfiguration-NumberScale"></a>
Determines the number scale value of the number format.
Type: String
Valid Values: `NONE | AUTO | THOUSANDS | MILLIONS | BILLIONS | TRILLIONS | LAKHS | CRORES`
Required: No

 ** Prefix **   <a name="QS-Type-NumberDisplayFormatConfiguration-Prefix"></a>
Determines the prefix value of the number format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SeparatorConfiguration **   <a name="QS-Type-NumberDisplayFormatConfiguration-SeparatorConfiguration"></a>
The options that determine the numeric separator configuration.
Type: [NumericSeparatorConfiguration](API_NumericSeparatorConfiguration.md) object
Required: No

 ** Suffix **   <a name="QS-Type-NumberDisplayFormatConfiguration-Suffix"></a>
Determines the suffix value of the number format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_NumberDisplayFormatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NumberDisplayFormatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NumberDisplayFormatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NumberDisplayFormatConfiguration)
