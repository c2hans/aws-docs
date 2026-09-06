---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Pattern.html
---

# Pattern
<a name="API_Pattern"></a>

 A set of rules used to make a recommendation during an analysis.

## Contents
<a name="API_Pattern_Contents"></a>

 ** countersToAggregate **   <a name="profiler-Type-Pattern-countersToAggregate"></a>
 A list of the different counters used to determine if there is a match.
Type: Array of strings
Required: No

 ** description **   <a name="profiler-Type-Pattern-description"></a>
The description of the recommendation. This explains a potential inefficiency in a profiled application.
Type: String
Required: No

 ** id **   <a name="profiler-Type-Pattern-id"></a>
The universally unique identifier (UUID) of this pattern.
Type: String
Required: No

 ** name **   <a name="profiler-Type-Pattern-name"></a>
The name for this pattern.
Type: String
Required: No

 ** resolutionSteps **   <a name="profiler-Type-Pattern-resolutionSteps"></a>
 A string that contains the steps recommended to address the potential inefficiency.
Type: String
Required: No

 ** targetFrames **   <a name="profiler-Type-Pattern-targetFrames"></a>
A list of frame names that were searched during the analysis that generated a recommendation.
Type: Array of arrays of strings
Required: No

 ** thresholdPercent **   <a name="profiler-Type-Pattern-thresholdPercent"></a>
 The percentage of time an application spends in one method that triggers a recommendation. The percentage of time is the same as the percentage of the total gathered sample counts during analysis.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_Pattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/Pattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/Pattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/Pattern)
