---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ImportTaskDetails.html
---

# ImportTaskDetails
<a name="API_ImportTaskDetails"></a>

Contains details about an import task.

## Contents
<a name="API_ImportTaskDetails_Contents"></a>

 ** dictionaryEntryCount **   <a name="neptunegraph-Type-ImportTaskDetails-dictionaryEntryCount"></a>
The number of dictionary entries in the import task.
Type: Long
Required: Yes

 ** errorCount **   <a name="neptunegraph-Type-ImportTaskDetails-errorCount"></a>
The number of errors encountered so far.
Type: Integer
Required: Yes

 ** progressPercentage **   <a name="neptunegraph-Type-ImportTaskDetails-progressPercentage"></a>
The percentage progress so far.
Type: Integer
Required: Yes

 ** startTime **   <a name="neptunegraph-Type-ImportTaskDetails-startTime"></a>
Time at which the import task started.
Type: Timestamp
Required: Yes

 ** statementCount **   <a name="neptunegraph-Type-ImportTaskDetails-statementCount"></a>
The number of statements in the import task.
Type: Long
Required: Yes

 ** status **   <a name="neptunegraph-Type-ImportTaskDetails-status"></a>
Status of the import task.
Type: String
Required: Yes

 ** timeElapsedSeconds **   <a name="neptunegraph-Type-ImportTaskDetails-timeElapsedSeconds"></a>
Seconds elapsed since the import task started.
Type: Long
Required: Yes

 ** errorDetails **   <a name="neptunegraph-Type-ImportTaskDetails-errorDetails"></a>
Details about the errors that have been encountered.
Type: String
Required: No

## See Also
<a name="API_ImportTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ImportTaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ImportTaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ImportTaskDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
