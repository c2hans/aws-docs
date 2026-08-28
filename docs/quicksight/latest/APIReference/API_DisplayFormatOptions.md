---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DisplayFormatOptions.html
---

# DisplayFormatOptions
<a name="API_DisplayFormatOptions"></a>

A structure that represents additional options for display formatting.

## Contents
<a name="API_DisplayFormatOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BlankCellFormat **   <a name="QS-Type-DisplayFormatOptions-BlankCellFormat"></a>
Determines the blank cell format.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** CurrencySymbol **   <a name="QS-Type-DisplayFormatOptions-CurrencySymbol"></a>
The currency symbol, such as `USD`.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** DateFormat **   <a name="QS-Type-DisplayFormatOptions-DateFormat"></a>
Determines the `DateTime` format.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** DecimalSeparator **   <a name="QS-Type-DisplayFormatOptions-DecimalSeparator"></a>
Determines the decimal separator.
Type: String
Valid Values: `COMMA | DOT`
Required: No

 ** FractionDigits **   <a name="QS-Type-DisplayFormatOptions-FractionDigits"></a>
Determines the number of fraction digits.
Type: Integer
Required: No

 ** GroupingSeparator **   <a name="QS-Type-DisplayFormatOptions-GroupingSeparator"></a>
Determines the grouping separator.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** NegativeFormat **   <a name="QS-Type-DisplayFormatOptions-NegativeFormat"></a>
The negative format.
Type: [NegativeFormat](API_NegativeFormat.md) object
Required: No

 ** Prefix **   <a name="QS-Type-DisplayFormatOptions-Prefix"></a>
The prefix value for a display format.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Suffix **   <a name="QS-Type-DisplayFormatOptions-Suffix"></a>
The suffix value for a display format.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** UnitScaler **   <a name="QS-Type-DisplayFormatOptions-UnitScaler"></a>
The unit scaler. Valid values for this structure are: `NONE`, `AUTO`, `THOUSANDS`, `MILLIONS`, `BILLIONS`, and `TRILLIONS`.
Type: String
Valid Values: `NONE | AUTO | THOUSANDS | MILLIONS | BILLIONS | TRILLIONS | LAKHS | CRORES`
Required: No

 ** UseBlankCellFormat **   <a name="QS-Type-DisplayFormatOptions-UseBlankCellFormat"></a>
A Boolean value that indicates whether to use blank cell format.
Type: Boolean
Required: No

 ** UseGrouping **   <a name="QS-Type-DisplayFormatOptions-UseGrouping"></a>
A Boolean value that indicates whether to use grouping.
Type: Boolean
Required: No

## See Also
<a name="API_DisplayFormatOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DisplayFormatOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DisplayFormatOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DisplayFormatOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
