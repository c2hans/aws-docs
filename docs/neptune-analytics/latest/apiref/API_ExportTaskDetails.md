---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportTaskDetails.html
---

# ExportTaskDetails
<a name="API_ExportTaskDetails"></a>

Contains details about the specified export task.

## Contents
<a name="API_ExportTaskDetails_Contents"></a>

 ** progressPercentage **   <a name="neptunegraph-Type-ExportTaskDetails-progressPercentage"></a>
The number of progress percentage of the export task.
Type: Integer
Required: Yes

 ** startTime **   <a name="neptunegraph-Type-ExportTaskDetails-startTime"></a>
The start time of the export task.
Type: Timestamp
Required: Yes

 ** timeElapsedSeconds **   <a name="neptunegraph-Type-ExportTaskDetails-timeElapsedSeconds"></a>
The time elapsed, in seconds, since the start time of the export task.
Type: Long
Required: Yes

 ** numEdgesWritten **   <a name="neptunegraph-Type-ExportTaskDetails-numEdgesWritten"></a>
The number of exported edges.
Type: Long
Required: No

 ** numVerticesWritten **   <a name="neptunegraph-Type-ExportTaskDetails-numVerticesWritten"></a>
The number of exported vertices.
Type: Long
Required: No

## See Also
<a name="API_ExportTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ExportTaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ExportTaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ExportTaskDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
