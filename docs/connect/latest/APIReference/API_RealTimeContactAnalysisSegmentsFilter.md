---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentsFilter.html
---

# RealTimeContactAnalysisSegmentsFilter
<a name="API_RealTimeContactAnalysisSegmentsFilter"></a>

A filter that restricts the segments returned by `ListRealtimeContactAnalysisSegmentsV2`. It currently supports filtering category segments by the tags on the rules that create them, which enforces tag-based access control on the categories a caller can view.

## Contents
<a name="API_RealTimeContactAnalysisSegmentsFilter_Contents"></a>

 ** CategoriesAttributeFilter **   <a name="connect-Type-RealTimeContactAnalysisSegmentsFilter-CategoriesAttributeFilter"></a>
A filter applied to category segments based on the tags of the rules that create the matched categories. This filter applies only when `SegmentTypes` includes `Categories`.
Type: [CategoriesAttributeFilter](API_CategoriesAttributeFilter.md) object
Required: No

## See Also
<a name="API_RealTimeContactAnalysisSegmentsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisSegmentsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisSegmentsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisSegmentsFilter)
