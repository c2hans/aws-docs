---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataLabelOptions.html
---

# DataLabelOptions
<a name="API_DataLabelOptions"></a>

The options that determine the presentation of the data labels.

## Contents
<a name="API_DataLabelOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryLabelVisibility **   <a name="QS-Type-DataLabelOptions-CategoryLabelVisibility"></a>
Determines the visibility of the category field labels.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** DataLabelTypes **   <a name="QS-Type-DataLabelOptions-DataLabelTypes"></a>
The option that determines the data label type.
Type: Array of [DataLabelType](API_DataLabelType.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** LabelColor **   <a name="QS-Type-DataLabelOptions-LabelColor"></a>
Determines the color of the data labels.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** LabelContent **   <a name="QS-Type-DataLabelOptions-LabelContent"></a>
Determines the content of the data labels.
Type: String
Valid Values: `VALUE | PERCENT | VALUE_AND_PERCENT`
Required: No

 ** LabelFontConfiguration **   <a name="QS-Type-DataLabelOptions-LabelFontConfiguration"></a>
Determines the font configuration of the data labels.
Type: [FontConfiguration](API_FontConfiguration.md) object
Required: No

 ** MeasureLabelVisibility **   <a name="QS-Type-DataLabelOptions-MeasureLabelVisibility"></a>
Determines the visibility of the measure field labels.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** Overlap **   <a name="QS-Type-DataLabelOptions-Overlap"></a>
Determines whether overlap is enabled or disabled for the data labels.
Type: String
Valid Values: `DISABLE_OVERLAP | ENABLE_OVERLAP`
Required: No

 ** Position **   <a name="QS-Type-DataLabelOptions-Position"></a>
Determines the position of the data labels.
Type: String
Valid Values: `INSIDE | OUTSIDE | LEFT | TOP | BOTTOM | RIGHT`
Required: No

 ** TotalsVisibility **   <a name="QS-Type-DataLabelOptions-TotalsVisibility"></a>
Determines the visibility of the total.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** Visibility **   <a name="QS-Type-DataLabelOptions-Visibility"></a>
Determines the visibility of the data labels.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_DataLabelOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataLabelOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataLabelOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataLabelOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
