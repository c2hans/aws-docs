---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionSucceededEventDetails.html
---

# ExecutionSucceededEventDetails
<a name="API_ExecutionSucceededEventDetails"></a>

Contains details about the successful termination of the execution.

## Contents
<a name="API_ExecutionSucceededEventDetails_Contents"></a>

 ** output **   <a name="StepFunctions-Type-ExecutionSucceededEventDetails-output"></a>
The JSON data output by the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** outputDetails **   <a name="StepFunctions-Type-ExecutionSucceededEventDetails-outputDetails"></a>
Contains details about the output of an execution history event.
Type: [HistoryEventExecutionDataDetails](API_HistoryEventExecutionDataDetails.md) object
Required: No

## See Also
<a name="API_ExecutionSucceededEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ExecutionSucceededEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ExecutionSucceededEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ExecutionSucceededEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
