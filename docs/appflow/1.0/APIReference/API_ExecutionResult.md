---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ExecutionResult.html
---

# ExecutionResult
<a name="API_ExecutionResult"></a>

 Specifies the end result of the flow run.

## Contents
<a name="API_ExecutionResult_Contents"></a>

 ** bytesProcessed **   <a name="appflow-Type-ExecutionResult-bytesProcessed"></a>
 The total number of bytes processed by the flow run.
Type: Long
Required: No

 ** bytesWritten **   <a name="appflow-Type-ExecutionResult-bytesWritten"></a>
 The total number of bytes written as a result of the flow run.
Type: Long
Required: No

 ** errorInfo **   <a name="appflow-Type-ExecutionResult-errorInfo"></a>
 Provides any error message information related to the flow run.
Type: [ErrorInfo](API_ErrorInfo.md) object
Required: No

 ** maxPageSize **   <a name="appflow-Type-ExecutionResult-maxPageSize"></a>
The maximum number of records that Amazon AppFlow receives in each page of the response from your SAP application.
Type: Long
Required: No

 ** numParallelProcesses **   <a name="appflow-Type-ExecutionResult-numParallelProcesses"></a>
The number of processes that Amazon AppFlow ran at the same time when it retrieved your data.
Type: Long
Required: No

 ** recordsProcessed **   <a name="appflow-Type-ExecutionResult-recordsProcessed"></a>
 The number of records processed in the flow run.
Type: Long
Required: No

## See Also
<a name="API_ExecutionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ExecutionResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ExecutionResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ExecutionResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
