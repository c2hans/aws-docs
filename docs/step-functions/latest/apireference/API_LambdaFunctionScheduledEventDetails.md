---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_LambdaFunctionScheduledEventDetails.html
---

# LambdaFunctionScheduledEventDetails
<a name="API_LambdaFunctionScheduledEventDetails"></a>

Contains details about a Lambda function scheduled during an execution.

## Contents
<a name="API_LambdaFunctionScheduledEventDetails_Contents"></a>

 ** resource **   <a name="StepFunctions-Type-LambdaFunctionScheduledEventDetails-resource"></a>
The Amazon Resource Name (ARN) of the scheduled Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** input **   <a name="StepFunctions-Type-LambdaFunctionScheduledEventDetails-input"></a>
The JSON data input to the Lambda function. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** inputDetails **   <a name="StepFunctions-Type-LambdaFunctionScheduledEventDetails-inputDetails"></a>
Contains details about input for an execution history event.
Type: [HistoryEventExecutionDataDetails](API_HistoryEventExecutionDataDetails.md) object
Required: No

 ** taskCredentials **   <a name="StepFunctions-Type-LambdaFunctionScheduledEventDetails-taskCredentials"></a>
The credentials that Step Functions uses for the task.
Type: [TaskCredentials](API_TaskCredentials.md) object
Required: No

 ** timeoutInSeconds **   <a name="StepFunctions-Type-LambdaFunctionScheduledEventDetails-timeoutInSeconds"></a>
The maximum allowed duration of the Lambda function.
Type: Long
Required: No

## See Also
<a name="API_LambdaFunctionScheduledEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/LambdaFunctionScheduledEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/LambdaFunctionScheduledEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/LambdaFunctionScheduledEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
