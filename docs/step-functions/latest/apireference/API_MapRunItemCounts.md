---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunItemCounts.html
---

# MapRunItemCounts
<a name="API_MapRunItemCounts"></a>

Contains details about items that were processed in all of the child workflow executions that were started by a Map Run.

## Contents
<a name="API_MapRunItemCounts_Contents"></a>

 ** aborted **   <a name="StepFunctions-Type-MapRunItemCounts-aborted"></a>
The total number of items processed in child workflow executions that were either stopped by the user or by Step Functions, because the Map Run failed.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** failed **   <a name="StepFunctions-Type-MapRunItemCounts-failed"></a>
The total number of items processed in child workflow executions that have failed.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** pending **   <a name="StepFunctions-Type-MapRunItemCounts-pending"></a>
The total number of items to process in child workflow executions that haven't started running yet.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** resultsWritten **   <a name="StepFunctions-Type-MapRunItemCounts-resultsWritten"></a>
Returns the count of items whose results were written by `ResultWriter`. For more information, see [ResultWriter](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultwriter.html) in the * AWS Step Functions Developer Guide*.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** running **   <a name="StepFunctions-Type-MapRunItemCounts-running"></a>
The total number of items being processed in child workflow executions that are currently in-progress.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** succeeded **   <a name="StepFunctions-Type-MapRunItemCounts-succeeded"></a>
The total number of items processed in child workflow executions that have completed successfully.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** timedOut **   <a name="StepFunctions-Type-MapRunItemCounts-timedOut"></a>
The total number of items processed in child workflow executions that have timed out.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** total **   <a name="StepFunctions-Type-MapRunItemCounts-total"></a>
The total number of items processed in all the child workflow executions started by a Map Run.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** failuresNotRedrivable **   <a name="StepFunctions-Type-MapRunItemCounts-failuresNotRedrivable"></a>
The number of `FAILED`, `ABORTED`, or `TIMED_OUT` items in child workflow executions that cannot be redriven because the execution status of those child workflows is terminal. For example, child workflows with an execution status of `FAILED`, `ABORTED`, or `TIMED_OUT` and a `redriveStatus` of `NOT_REDRIVABLE`.
Type: Long
Required: No

 ** pendingRedrive **   <a name="StepFunctions-Type-MapRunItemCounts-pendingRedrive"></a>
The number of unsuccessful items in child workflow executions currently waiting to be redriven.
Type: Long
Required: No

## See Also
<a name="API_MapRunItemCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/MapRunItemCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/MapRunItemCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/MapRunItemCounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
