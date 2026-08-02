---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColorScale.html
---

# ColorScale
<a name="API_ColorScale"></a>

Determines the color scale that is applied to the visual.

## Contents
<a name="API_ColorScale_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColorFillType **   <a name="QS-Type-ColorScale-ColorFillType"></a>
Determines the color fill type.
Type: String
Valid Values: `DISCRETE | GRADIENT`
Required: Yes

 ** Colors **   <a name="QS-Type-ColorScale-Colors"></a>
Determines the list of colors that are applied to the visual.
Type: Array of [DataColor](API_DataColor.md) objects
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: Yes

 ** NullValueColor **   <a name="QS-Type-ColorScale-NullValueColor"></a>
Determines the color that is applied to null values.
Type: [DataColor](API_DataColor.md) object
Required: No

## See Also
<a name="API_ColorScale_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ColorScale)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ColorScale)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ColorScale)
