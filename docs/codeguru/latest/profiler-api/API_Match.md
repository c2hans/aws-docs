---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Match.html
---

# Match
<a name="API_Match"></a>

The part of a profile that contains a recommendation found during analysis.

## Contents
<a name="API_Match_Contents"></a>

 ** frameAddress **   <a name="profiler-Type-Match-frameAddress"></a>
The location in the profiling graph that contains a recommendation found during analysis.
Type: String
Required: No

 ** targetFramesIndex **   <a name="profiler-Type-Match-targetFramesIndex"></a>
The target frame that triggered a match.
Type: Integer
Required: No

 ** thresholdBreachValue **   <a name="profiler-Type-Match-thresholdBreachValue"></a>
The value in the profile data that exceeded the recommendation threshold.
Type: Double
Required: No

## See Also
<a name="API_Match_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/Match)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/Match)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/Match)
