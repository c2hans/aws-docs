---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataFieldSeriesItem.html
---

# DataFieldSeriesItem
<a name="API_DataFieldSeriesItem"></a>

The data field series item configuration of a line chart.

## Contents
<a name="API_DataFieldSeriesItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AxisBinding **   <a name="QS-Type-DataFieldSeriesItem-AxisBinding"></a>
The axis that you are binding the field to.
Type: String
Valid Values: `PRIMARY_YAXIS | SECONDARY_YAXIS`
Required: Yes

 ** FieldId **   <a name="QS-Type-DataFieldSeriesItem-FieldId"></a>
The field ID of the field that you are setting the axis binding to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** FieldValue **   <a name="QS-Type-DataFieldSeriesItem-FieldValue"></a>
The field value of the field that you are setting the axis binding to.
Type: String
Required: No

 ** Settings **   <a name="QS-Type-DataFieldSeriesItem-Settings"></a>
The options that determine the presentation of line series associated to the field.
Type: [LineChartSeriesSettings](API_LineChartSeriesSettings.md) object
Required: No

## See Also
<a name="API_DataFieldSeriesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataFieldSeriesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataFieldSeriesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataFieldSeriesItem)
