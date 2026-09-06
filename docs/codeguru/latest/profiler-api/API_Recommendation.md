---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

A potential improvement that was found from analyzing the profiling data.

## Contents
<a name="API_Recommendation_Contents"></a>

 ** allMatchesCount **   <a name="profiler-Type-Recommendation-allMatchesCount"></a>
How many different places in the profile graph triggered a match.
Type: Integer
Required: Yes

 ** allMatchesSum **   <a name="profiler-Type-Recommendation-allMatchesSum"></a>
How much of the total sample count is potentially affected.
Type: Double
Required: Yes

 ** endTime **   <a name="profiler-Type-Recommendation-endTime"></a>
End time of the profile that was used by this analysis. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: Yes

 ** pattern **   <a name="profiler-Type-Recommendation-pattern"></a>
The pattern that analysis recognized in the profile to make this recommendation.
Type: [Pattern](API_Pattern.md) object
Required: Yes

 ** startTime **   <a name="profiler-Type-Recommendation-startTime"></a>
The start time of the profile that was used by this analysis. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: Yes

 ** topMatches **   <a name="profiler-Type-Recommendation-topMatches"></a>
List of the matches with most impact.
Type: Array of [Match](API_Match.md) objects
Required: Yes

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/Recommendation)
