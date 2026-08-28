---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ExecutionStats.html
---

# ExecutionStats
<a name="API_query_ExecutionStats"></a>

Statistics for a single scheduled query run.

## Contents
<a name="API_query_ExecutionStats_Contents"></a>

 ** BytesMetered **   <a name="timestream-Type-query_ExecutionStats-BytesMetered"></a>
Bytes metered for a single scheduled query run.
Type: Long
Required: No

 ** CumulativeBytesScanned **   <a name="timestream-Type-query_ExecutionStats-CumulativeBytesScanned"></a>
Bytes scanned for a single scheduled query run.
Type: Long
Required: No

 ** DataWrites **   <a name="timestream-Type-query_ExecutionStats-DataWrites"></a>
Data writes metered for records ingested in a single scheduled query run.
Type: Long
Required: No

 ** ExecutionTimeInMillis **   <a name="timestream-Type-query_ExecutionStats-ExecutionTimeInMillis"></a>
Total time, measured in milliseconds, that was needed for the scheduled query run to complete.
Type: Long
Required: No

 ** QueryResultRows **   <a name="timestream-Type-query_ExecutionStats-QueryResultRows"></a>
Number of rows present in the output from running a query before ingestion to destination data source.
Type: Long
Required: No

 ** RecordsIngested **   <a name="timestream-Type-query_ExecutionStats-RecordsIngested"></a>
The number of records ingested for a single scheduled query run.
Type: Long
Required: No

## See Also
<a name="API_query_ExecutionStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ExecutionStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ExecutionStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ExecutionStats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
