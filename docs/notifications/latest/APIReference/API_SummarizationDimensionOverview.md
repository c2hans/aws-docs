---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_SummarizationDimensionOverview.html
---

# SummarizationDimensionOverview
<a name="API_SummarizationDimensionOverview"></a>

Provides an overview of how data is summarized across different dimensions.

## Contents
<a name="API_SummarizationDimensionOverview_Contents"></a>

 ** count **   <a name="Notifications-Type-SummarizationDimensionOverview-count"></a>
Total number of occurrences for this dimension.
Type: Integer
Required: Yes

 ** name **   <a name="Notifications-Type-SummarizationDimensionOverview-name"></a>
Name of the summarization dimension.
Type: String
Required: Yes

 ** sampleValues **   <a name="Notifications-Type-SummarizationDimensionOverview-sampleValues"></a>
Indicates the sample values found within the dimension.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_SummarizationDimensionOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/SummarizationDimensionOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/SummarizationDimensionOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/SummarizationDimensionOverview)
