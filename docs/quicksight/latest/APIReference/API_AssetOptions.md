---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetOptions.html
---

# AssetOptions
<a name="API_AssetOptions"></a>

An array of analysis level configurations.

## Contents
<a name="API_AssetOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomActionDefaults **   <a name="QS-Type-AssetOptions-CustomActionDefaults"></a>
A list of visual custom actions for the analysis.
Type: [VisualCustomActionDefaults](API_VisualCustomActionDefaults.md) object
Required: No

 ** ExcludedDataSetArns **   <a name="QS-Type-AssetOptions-ExcludedDataSetArns"></a>
A list of dataset ARNS to exclude from Dashboard Q&A.
Type: Array of strings
Array Members: Maximum number of 100 items.
Required: No

 ** QBusinessInsightsStatus **   <a name="QS-Type-AssetOptions-QBusinessInsightsStatus"></a>
Determines whether insight summaries from Amazon Q Business are allowed in Dashboard Q&A.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Timezone **   <a name="QS-Type-AssetOptions-Timezone"></a>
Determines the timezone for the analysis.
Type: String
Required: No

 ** WeekStart **   <a name="QS-Type-AssetOptions-WeekStart"></a>
Determines the week start day for an analysis.
Type: String
Valid Values: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
Required: No

## See Also
<a name="API_AssetOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetOptions)
