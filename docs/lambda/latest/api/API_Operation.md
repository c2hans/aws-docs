---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_Operation.html
---

# Operation
<a name="API_Operation"></a>

Information about an operation within a durable execution.

## Contents
<a name="API_Operation_Contents"></a>

 ** Id **   <a name="lambda-Type-Operation-Id"></a>
The unique identifier for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** StartTimestamp **   <a name="lambda-Type-Operation-StartTimestamp"></a>
The date and time when the operation started, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: Yes

 ** Status **   <a name="lambda-Type-Operation-Status"></a>
The current status of the operation.
Type: String
Valid Values: `STARTED | PENDING | READY | SUCCEEDED | FAILED | CANCELLED | TIMED_OUT | STOPPED`
Required: Yes

 ** Type **   <a name="lambda-Type-Operation-Type"></a>
The type of operation.
Type: String
Valid Values: `EXECUTION | CONTEXT | STEP | WAIT | CALLBACK | CHAINED_INVOKE`
Required: Yes

 ** CallbackDetails **   <a name="lambda-Type-Operation-CallbackDetails"></a>
Contains details about a callback operation in a durable execution, including the callback token and timeout configuration.
Type: [CallbackDetails](API_CallbackDetails.md) object
Required: No

 ** ChainedInvokeDetails **   <a name="lambda-Type-Operation-ChainedInvokeDetails"></a>
Contains details about a chained function invocation in a durable execution, including the target function and invocation parameters.
Type: [ChainedInvokeDetails](API_ChainedInvokeDetails.md) object
Required: No

 ** ContextDetails **   <a name="lambda-Type-Operation-ContextDetails"></a>
Details about the context, if this operation represents a context.
Type: [ContextDetails](API_ContextDetails.md) object
Required: No

 ** EndTimestamp **   <a name="lambda-Type-Operation-EndTimestamp"></a>
The date and time when the operation ended, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: No

 ** ExecutionDetails **   <a name="lambda-Type-Operation-ExecutionDetails"></a>
Details about the execution, if this operation represents an execution.
Type: [ExecutionDetails](API_ExecutionDetails.md) object
Required: No

 ** Name **   <a name="lambda-Type-Operation-Name"></a>
The customer-provided name for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x20-\x7E]+`
Required: No

 ** ParentId **   <a name="lambda-Type-Operation-ParentId"></a>
The unique identifier of the parent operation, if this operation is running within a child context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** StepDetails **   <a name="lambda-Type-Operation-StepDetails"></a>
Details about the step, if this operation represents a step.
Type: [StepDetails](API_StepDetails.md) object
Required: No

 ** SubType **   <a name="lambda-Type-Operation-SubType"></a>
The subtype of the operation, providing additional categorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** WaitDetails **   <a name="lambda-Type-Operation-WaitDetails"></a>
Details about the wait operation, if this operation represents a wait.
Type: [WaitDetails](API_WaitDetails.md) object
Required: No

## See Also
<a name="API_Operation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/Operation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/Operation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/Operation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
