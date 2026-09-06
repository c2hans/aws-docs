---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataFieldBarSeriesItem.html
---

# DataFieldBarSeriesItem
<a name="API_DataFieldBarSeriesItem"></a>

The data field series item configuration of a `BarChartVisual`.

## Contents
<a name="API_DataFieldBarSeriesItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldId **   <a name="QS-Type-DataFieldBarSeriesItem-FieldId"></a>
Field ID of the field that you are setting the series configuration for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** FieldValue **   <a name="QS-Type-DataFieldBarSeriesItem-FieldValue"></a>
Field value of the field that you are setting the series configuration for.
Type: String
Required: No

 ** Settings **   <a name="QS-Type-DataFieldBarSeriesItem-Settings"></a>
Options that determine the presentation of bar series associated to the field.
Type: [BarChartSeriesSettings](API_BarChartSeriesSettings.md) object
Required: No

## See Also
<a name="API_DataFieldBarSeriesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataFieldBarSeriesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataFieldBarSeriesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataFieldBarSeriesItem)
