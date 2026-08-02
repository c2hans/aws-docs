---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionStartedEventDetails.html
---

# ExecutionStartedEventDetails
<a name="API_ExecutionStartedEventDetails"></a>

Contains details about the start of the execution.

## Contents
<a name="API_ExecutionStartedEventDetails_Contents"></a>

 ** input **   <a name="StepFunctions-Type-ExecutionStartedEventDetails-input"></a>
The JSON data input to the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** inputDetails **   <a name="StepFunctions-Type-ExecutionStartedEventDetails-inputDetails"></a>
Contains details about the input for an execution history event.
Type: [HistoryEventExecutionDataDetails](API_HistoryEventExecutionDataDetails.md) object
Required: No

 ** roleArn **   <a name="StepFunctions-Type-ExecutionStartedEventDetails-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** stateMachineAliasArn **   <a name="StepFunctions-Type-ExecutionStartedEventDetails-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) that identifies a state machine alias used for starting the state machine execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** stateMachineVersionArn **   <a name="StepFunctions-Type-ExecutionStartedEventDetails-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) that identifies a state machine version used for starting the state machine execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ExecutionStartedEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ExecutionStartedEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ExecutionStartedEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ExecutionStartedEventDetails)
