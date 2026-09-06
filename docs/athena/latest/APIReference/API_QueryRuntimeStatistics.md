---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_QueryRuntimeStatistics.html
---

# QueryRuntimeStatistics
<a name="API_QueryRuntimeStatistics"></a>

The query execution timeline, statistics on input and output rows and bytes, and the different query stages that form the query execution plan.

## Contents
<a name="API_QueryRuntimeStatistics_Contents"></a>

 ** OutputStage **   <a name="athena-Type-QueryRuntimeStatistics-OutputStage"></a>
Stage statistics such as input and output rows and bytes, execution time, and stage state. This information also includes substages and the query stage plan.
Type: [QueryStage](API_QueryStage.md) object
Required: No

 ** Rows **   <a name="athena-Type-QueryRuntimeStatistics-Rows"></a>
Statistics such as input rows and bytes read by the query, rows and bytes output by the query, and the number of rows written by the query.
Type: [QueryRuntimeStatisticsRows](API_QueryRuntimeStatisticsRows.md) object
Required: No

 ** Timeline **   <a name="athena-Type-QueryRuntimeStatistics-Timeline"></a>
Timeline statistics such as query queue time, planning time, execution time, service processing time, and total execution time.
Type: [QueryRuntimeStatisticsTimeline](API_QueryRuntimeStatisticsTimeline.md) object
Required: No

## See Also
<a name="API_QueryRuntimeStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/QueryRuntimeStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/QueryRuntimeStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/QueryRuntimeStatistics)
