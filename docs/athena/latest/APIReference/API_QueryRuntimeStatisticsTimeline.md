---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_QueryRuntimeStatisticsTimeline.html
---

# QueryRuntimeStatisticsTimeline
<a name="API_QueryRuntimeStatisticsTimeline"></a>

Timeline statistics such as query queue time, planning time, execution time, service processing time, and total execution time.

## Contents
<a name="API_QueryRuntimeStatisticsTimeline_Contents"></a>

 ** EngineExecutionTimeInMillis **   <a name="athena-Type-QueryRuntimeStatisticsTimeline-EngineExecutionTimeInMillis"></a>
The number of milliseconds that the query took to execute.
Type: Long
Required: No

 ** QueryPlanningTimeInMillis **   <a name="athena-Type-QueryRuntimeStatisticsTimeline-QueryPlanningTimeInMillis"></a>
The number of milliseconds that Athena took to plan the query processing flow. This includes the time spent retrieving table partitions from the data source. Note that because the query engine performs the query planning, query planning time is a subset of engine processing time.
Type: Long
Required: No

 ** QueryQueueTimeInMillis **   <a name="athena-Type-QueryRuntimeStatisticsTimeline-QueryQueueTimeInMillis"></a>
The number of milliseconds that the query was in your query queue waiting for resources. Note that if transient errors occur, Athena might automatically add the query back to the queue.
Type: Long
Required: No

 ** ServicePreProcessingTimeInMillis **   <a name="athena-Type-QueryRuntimeStatisticsTimeline-ServicePreProcessingTimeInMillis"></a>
 The number of milliseconds that Athena spends on preprocessing before it submits the query to the engine.
Type: Long
Required: No

 ** ServiceProcessingTimeInMillis **   <a name="athena-Type-QueryRuntimeStatisticsTimeline-ServiceProcessingTimeInMillis"></a>
The number of milliseconds that Athena took to finalize and publish the query results after the query engine finished running the query.
Type: Long
Required: No

 ** TotalExecutionTimeInMillis **   <a name="athena-Type-QueryRuntimeStatisticsTimeline-TotalExecutionTimeInMillis"></a>
The number of milliseconds that Athena took to run the query.
Type: Long
Required: No

## See Also
<a name="API_QueryRuntimeStatisticsTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/QueryRuntimeStatisticsTimeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/QueryRuntimeStatisticsTimeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/QueryRuntimeStatisticsTimeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
