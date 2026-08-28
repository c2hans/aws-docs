---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CheckpointUpdatedExecutionState.html
---

# CheckpointUpdatedExecutionState
<a name="API_CheckpointUpdatedExecutionState"></a>

Contains operations that have been updated since the last checkpoint, such as completed asynchronous work like timers or callbacks.

## Contents
<a name="API_CheckpointUpdatedExecutionState_Contents"></a>

 ** NextMarker **   <a name="lambda-Type-CheckpointUpdatedExecutionState-NextMarker"></a>
Indicates that more results are available. Use this value in a subsequent call to retrieve the next page of results.
Type: String
Required: No

 ** Operations **   <a name="lambda-Type-CheckpointUpdatedExecutionState-Operations"></a>
A list of operations that have been updated since the last checkpoint.
Type: Array of [Operation](API_Operation.md) objects
Required: No

## See Also
<a name="API_CheckpointUpdatedExecutionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CheckpointUpdatedExecutionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CheckpointUpdatedExecutionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CheckpointUpdatedExecutionState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
