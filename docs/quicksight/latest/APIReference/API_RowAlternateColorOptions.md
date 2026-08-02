---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RowAlternateColorOptions.html
---

# RowAlternateColorOptions
<a name="API_RowAlternateColorOptions"></a>

Determines the row alternate color options.

## Contents
<a name="API_RowAlternateColorOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RowAlternateColors **   <a name="QS-Type-RowAlternateColorOptions-RowAlternateColors"></a>
Determines the list of row alternate colors.
Type: Array of strings
Array Members: Maximum number of 1 item.
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** Status **   <a name="QS-Type-RowAlternateColorOptions-Status"></a>
Determines the widget status.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** UsePrimaryBackgroundColor **   <a name="QS-Type-RowAlternateColorOptions-UsePrimaryBackgroundColor"></a>
The primary background color options for alternate rows.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_RowAlternateColorOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RowAlternateColorOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RowAlternateColorOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RowAlternateColorOptions)
