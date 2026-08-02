---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KPIOptions.html
---

# KPIOptions
<a name="API_KPIOptions"></a>

The options that determine the presentation of a KPI visual.

## Contents
<a name="API_KPIOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Comparison **   <a name="QS-Type-KPIOptions-Comparison"></a>
The comparison configuration of a KPI visual.
Type: [ComparisonConfiguration](API_ComparisonConfiguration.md) object
Required: No

 ** PrimaryValueDisplayType **   <a name="QS-Type-KPIOptions-PrimaryValueDisplayType"></a>
The options that determine the primary value display type.
Type: String
Valid Values: `HIDDEN | COMPARISON | ACTUAL`
Required: No

 ** PrimaryValueFontConfiguration **   <a name="QS-Type-KPIOptions-PrimaryValueFontConfiguration"></a>
The options that determine the primary value font configuration.
Type: [FontConfiguration](API_FontConfiguration.md) object
Required: No

 ** ProgressBar **   <a name="QS-Type-KPIOptions-ProgressBar"></a>
The options that determine the presentation of the progress bar of a KPI visual.
Type: [ProgressBarOptions](API_ProgressBarOptions.md) object
Required: No

 ** SecondaryValue **   <a name="QS-Type-KPIOptions-SecondaryValue"></a>
The options that determine the presentation of the secondary value of a KPI visual.
Type: [SecondaryValueOptions](API_SecondaryValueOptions.md) object
Required: No

 ** SecondaryValueFontConfiguration **   <a name="QS-Type-KPIOptions-SecondaryValueFontConfiguration"></a>
The options that determine the secondary value font configuration.
Type: [FontConfiguration](API_FontConfiguration.md) object
Required: No

 ** Sparkline **   <a name="QS-Type-KPIOptions-Sparkline"></a>
The options that determine the visibility, color, type, and tooltip visibility of the sparkline of a KPI visual.
Type: [KPISparklineOptions](API_KPISparklineOptions.md) object
Required: No

 ** TrendArrows **   <a name="QS-Type-KPIOptions-TrendArrows"></a>
The options that determine the presentation of trend arrows in a KPI visual.
Type: [TrendArrowOptions](API_TrendArrowOptions.md) object
Required: No

 ** VisualLayoutOptions **   <a name="QS-Type-KPIOptions-VisualLayoutOptions"></a>
The options that determine the layout a KPI visual.
Type: [KPIVisualLayoutOptions](API_KPIVisualLayoutOptions.md) object
Required: No

## See Also
<a name="API_KPIOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KPIOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KPIOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KPIOptions)
