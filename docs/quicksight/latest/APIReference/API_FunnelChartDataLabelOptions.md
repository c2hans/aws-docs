---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FunnelChartDataLabelOptions.html
---

# FunnelChartDataLabelOptions
<a name="API_FunnelChartDataLabelOptions"></a>

The options that determine the presentation of the data labels.

## Contents
<a name="API_FunnelChartDataLabelOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryLabelVisibility **   <a name="QS-Type-FunnelChartDataLabelOptions-CategoryLabelVisibility"></a>
The visibility of the category labels within the data labels.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** LabelColor **   <a name="QS-Type-FunnelChartDataLabelOptions-LabelColor"></a>
The color of the data label text.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** LabelFontConfiguration **   <a name="QS-Type-FunnelChartDataLabelOptions-LabelFontConfiguration"></a>
The font configuration for the data labels.
Only the `FontSize` attribute of the font configuration is used for data labels.
Type: [FontConfiguration](API_FontConfiguration.md) object
Required: No

 ** MeasureDataLabelStyle **   <a name="QS-Type-FunnelChartDataLabelOptions-MeasureDataLabelStyle"></a>
Determines the style of the metric labels.
Type: String
Valid Values: `VALUE_ONLY | PERCENTAGE_BY_FIRST_STAGE | PERCENTAGE_BY_PREVIOUS_STAGE | VALUE_AND_PERCENTAGE_BY_FIRST_STAGE | VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE`
Required: No

 ** MeasureLabelVisibility **   <a name="QS-Type-FunnelChartDataLabelOptions-MeasureLabelVisibility"></a>
The visibility of the measure labels within the data labels.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** Position **   <a name="QS-Type-FunnelChartDataLabelOptions-Position"></a>
Determines the positioning of the data label relative to a section of the funnel.
Type: String
Valid Values: `INSIDE | OUTSIDE | LEFT | TOP | BOTTOM | RIGHT`
Required: No

 ** Visibility **   <a name="QS-Type-FunnelChartDataLabelOptions-Visibility"></a>
The visibility option that determines if data labels are displayed.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_FunnelChartDataLabelOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FunnelChartDataLabelOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FunnelChartDataLabelOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FunnelChartDataLabelOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
