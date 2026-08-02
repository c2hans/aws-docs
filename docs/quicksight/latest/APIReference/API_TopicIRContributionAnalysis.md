---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicIRContributionAnalysis.html
---

# TopicIRContributionAnalysis
<a name="API_TopicIRContributionAnalysis"></a>

The definition for a `TopicIRContributionAnalysis`.

## Contents
<a name="API_TopicIRContributionAnalysis_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Direction **   <a name="QS-Type-TopicIRContributionAnalysis-Direction"></a>
The direction for the `TopicIRContributionAnalysis`.
Type: String
Valid Values: `INCREASE | DECREASE | NEUTRAL`
Required: No

 ** Factors **   <a name="QS-Type-TopicIRContributionAnalysis-Factors"></a>
The factors for a `TopicIRContributionAnalysis`.
Type: Array of [ContributionAnalysisFactor](API_ContributionAnalysisFactor.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** SortType **   <a name="QS-Type-TopicIRContributionAnalysis-SortType"></a>
The sort type for the `TopicIRContributionAnalysis`.
Type: String
Valid Values: `ABSOLUTE_DIFFERENCE | CONTRIBUTION_PERCENTAGE | DEVIATION_FROM_EXPECTED | PERCENTAGE_DIFFERENCE`
Required: No

 ** TimeRanges **   <a name="QS-Type-TopicIRContributionAnalysis-TimeRanges"></a>
The time ranges for the `TopicIRContributionAnalysis`.
Type: [ContributionAnalysisTimeRanges](API_ContributionAnalysisTimeRanges.md) object
Required: No

## See Also
<a name="API_TopicIRContributionAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicIRContributionAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicIRContributionAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicIRContributionAnalysis)
