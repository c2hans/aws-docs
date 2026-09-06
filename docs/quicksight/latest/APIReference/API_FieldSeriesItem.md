---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FieldSeriesItem.html
---

# FieldSeriesItem
<a name="API_FieldSeriesItem"></a>

The field series item configuration of a line chart.

## Contents
<a name="API_FieldSeriesItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AxisBinding **   <a name="QS-Type-FieldSeriesItem-AxisBinding"></a>
The axis that you are binding the field to.
Type: String
Valid Values: `PRIMARY_YAXIS | SECONDARY_YAXIS`
Required: Yes

 ** FieldId **   <a name="QS-Type-FieldSeriesItem-FieldId"></a>
The field ID of the field for which you are setting the axis binding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Settings **   <a name="QS-Type-FieldSeriesItem-Settings"></a>
The options that determine the presentation of line series associated to the field.
Type: [LineChartSeriesSettings](API_LineChartSeriesSettings.md) object
Required: No

## See Also
<a name="API_FieldSeriesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FieldSeriesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FieldSeriesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FieldSeriesItem)
