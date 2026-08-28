---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Computation.html
---

# Computation
<a name="API_Computation"></a>

The computation union that is used in an insight visual.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_Computation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Forecast **   <a name="QS-Type-Computation-Forecast"></a>
The forecast computation configuration.
Type: [ForecastComputation](API_ForecastComputation.md) object
Required: No

 ** GrowthRate **   <a name="QS-Type-Computation-GrowthRate"></a>
The growth rate computation configuration.
Type: [GrowthRateComputation](API_GrowthRateComputation.md) object
Required: No

 ** MaximumMinimum **   <a name="QS-Type-Computation-MaximumMinimum"></a>
The maximum and minimum computation configuration.
Type: [MaximumMinimumComputation](API_MaximumMinimumComputation.md) object
Required: No

 ** MetricComparison **   <a name="QS-Type-Computation-MetricComparison"></a>
The metric comparison computation configuration.
Type: [MetricComparisonComputation](API_MetricComparisonComputation.md) object
Required: No

 ** PeriodOverPeriod **   <a name="QS-Type-Computation-PeriodOverPeriod"></a>
The period over period computation configuration.
Type: [PeriodOverPeriodComputation](API_PeriodOverPeriodComputation.md) object
Required: No

 ** PeriodToDate **   <a name="QS-Type-Computation-PeriodToDate"></a>
The period to `DataSetIdentifier` computation configuration.
Type: [PeriodToDateComputation](API_PeriodToDateComputation.md) object
Required: No

 ** TopBottomMovers **   <a name="QS-Type-Computation-TopBottomMovers"></a>
The top movers and bottom movers computation configuration.
Type: [TopBottomMoversComputation](API_TopBottomMoversComputation.md) object
Required: No

 ** TopBottomRanked **   <a name="QS-Type-Computation-TopBottomRanked"></a>
The top ranked and bottom ranked computation configuration.
Type: [TopBottomRankedComputation](API_TopBottomRankedComputation.md) object
Required: No

 ** TotalAggregation **   <a name="QS-Type-Computation-TotalAggregation"></a>
The total aggregation computation configuration.
Type: [TotalAggregationComputation](API_TotalAggregationComputation.md) object
Required: No

 ** UniqueValues **   <a name="QS-Type-Computation-UniqueValues"></a>
The unique values computation configuration.
Type: [UniqueValuesComputation](API_UniqueValuesComputation.md) object
Required: No

## See Also
<a name="API_Computation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Computation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Computation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Computation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
