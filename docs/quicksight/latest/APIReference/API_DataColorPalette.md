---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataColorPalette.html
---

# DataColorPalette
<a name="API_DataColorPalette"></a>

The theme colors that are used for data colors in charts. The colors description is a hexadecimal color code that consists of six alphanumerical characters, prefixed with `#`, for example \#37BFF5.

## Contents
<a name="API_DataColorPalette_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Colors **   <a name="QS-Type-DataColorPalette-Colors"></a>
The hexadecimal codes for the colors.
Type: Array of strings
Array Members: Maximum number of 100 items.
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** EmptyFillColor **   <a name="QS-Type-DataColorPalette-EmptyFillColor"></a>
The hexadecimal code of a color that applies to charts where a lack of data is highlighted.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** MinMaxGradient **   <a name="QS-Type-DataColorPalette-MinMaxGradient"></a>
The minimum and maximum hexadecimal codes that describe a color gradient.
Type: Array of strings
Array Members: Maximum number of 100 items.
Pattern: `^#[A-F0-9]{6}$`
Required: No

## See Also
<a name="API_DataColorPalette_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataColorPalette)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataColorPalette)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataColorPalette)
