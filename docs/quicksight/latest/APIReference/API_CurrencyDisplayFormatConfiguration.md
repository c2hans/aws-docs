---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CurrencyDisplayFormatConfiguration.html
---

# CurrencyDisplayFormatConfiguration
<a name="API_CurrencyDisplayFormatConfiguration"></a>

The options that determine the currency display format configuration.

## Contents
<a name="API_CurrencyDisplayFormatConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DecimalPlacesConfiguration **   <a name="QS-Type-CurrencyDisplayFormatConfiguration-DecimalPlacesConfiguration"></a>
The option that determines the decimal places configuration.
Type: [DecimalPlacesConfiguration](API_DecimalPlacesConfiguration.md) object
Required: No

 ** NegativeValueConfiguration **   <a name="QS-Type-CurrencyDisplayFormatConfiguration-NegativeValueConfiguration"></a>
The options that determine the negative value configuration.
Type: [NegativeValueConfiguration](API_NegativeValueConfiguration.md) object
Required: No

 ** NullValueFormatConfiguration **   <a name="QS-Type-CurrencyDisplayFormatConfiguration-NullValueFormatConfiguration"></a>
The options that determine the null value format configuration.
Type: [NullValueFormatConfiguration](API_NullValueFormatConfiguration.md) object
Required: No

 ** NumberScale **   <a name="QS-Type-CurrencyDisplayFormatConfiguration-NumberScale"></a>
Determines the number scale value for the currency format.
Type: String
Valid Values: `NONE | AUTO | THOUSANDS | MILLIONS | BILLIONS | TRILLIONS | LAKHS | CRORES`
Required: No

 ** Prefix **   <a name="QS-Type-CurrencyDisplayFormatConfiguration-Prefix"></a>
Determines the prefix value of the currency format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SeparatorConfiguration **   <a name="QS-Type-CurrencyDisplayFormatConfiguration-SeparatorConfiguration"></a>
The options that determine the numeric separator configuration.
Type: [NumericSeparatorConfiguration](API_NumericSeparatorConfiguration.md) object
Required: No

 ** Suffix **   <a name="QS-Type-CurrencyDisplayFormatConfiguration-Suffix"></a>
Determines the suffix value of the currency format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Symbol **   <a name="QS-Type-CurrencyDisplayFormatConfiguration-Symbol"></a>
Determines the symbol for the currency format.
Type: String
Pattern: `[A-Z]{3}`
Required: No

## See Also
<a name="API_CurrencyDisplayFormatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CurrencyDisplayFormatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CurrencyDisplayFormatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CurrencyDisplayFormatConfiguration)
