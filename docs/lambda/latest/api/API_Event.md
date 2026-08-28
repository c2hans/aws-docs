---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_Event.html
---

# Event
<a name="API_Event"></a>

An event that occurred during the execution of a durable function.

## Contents
<a name="API_Event_Contents"></a>

 ** CallbackFailedDetails **   <a name="lambda-Type-Event-CallbackFailedDetails"></a>
Contains details about a failed callback operation, including error information and the reason for failure.
Type: [CallbackFailedDetails](API_CallbackFailedDetails.md) object
Required: No

 ** CallbackStartedDetails **   <a name="lambda-Type-Event-CallbackStartedDetails"></a>
Contains details about a callback operation that has started, including timing information and callback metadata.
Type: [CallbackStartedDetails](API_CallbackStartedDetails.md) object
Required: No

 ** CallbackSucceededDetails **   <a name="lambda-Type-Event-CallbackSucceededDetails"></a>
Contains details about a successfully completed callback operation, including the result data and completion timestamp.
Type: [CallbackSucceededDetails](API_CallbackSucceededDetails.md) object
Required: No

 ** CallbackTimedOutDetails **   <a name="lambda-Type-Event-CallbackTimedOutDetails"></a>
Contains details about a callback operation that timed out, including timeout duration and any partial results.
Type: [CallbackTimedOutDetails](API_CallbackTimedOutDetails.md) object
Required: No

 ** ChainedInvokeFailedDetails **   <a name="lambda-Type-Event-ChainedInvokeFailedDetails"></a>
Contains details about a failed chained function invocation, including error information and failure reason.
Type: [ChainedInvokeFailedDetails](API_ChainedInvokeFailedDetails.md) object
Required: No

 ** ChainedInvokeStartedDetails **   <a name="lambda-Type-Event-ChainedInvokeStartedDetails"></a>
Contains details about a chained function invocation that has started execution, including start time and execution context.
Type: [ChainedInvokeStartedDetails](API_ChainedInvokeStartedDetails.md) object
Required: No

 ** ChainedInvokeStoppedDetails **   <a name="lambda-Type-Event-ChainedInvokeStoppedDetails"></a>
Details about a chained invocation that was stopped.
Type: [ChainedInvokeStoppedDetails](API_ChainedInvokeStoppedDetails.md) object
Required: No

 ** ChainedInvokeSucceededDetails **   <a name="lambda-Type-Event-ChainedInvokeSucceededDetails"></a>
Details about a chained invocation that succeeded.
Type: [ChainedInvokeSucceededDetails](API_ChainedInvokeSucceededDetails.md) object
Required: No

 ** ChainedInvokeTimedOutDetails **   <a name="lambda-Type-Event-ChainedInvokeTimedOutDetails"></a>
Details about a chained invocation that timed out.
Type: [ChainedInvokeTimedOutDetails](API_ChainedInvokeTimedOutDetails.md) object
Required: No

 ** ContextFailedDetails **   <a name="lambda-Type-Event-ContextFailedDetails"></a>
Details about a context that failed.
Type: [ContextFailedDetails](API_ContextFailedDetails.md) object
Required: No

 ** ContextStartedDetails **   <a name="lambda-Type-Event-ContextStartedDetails"></a>
Details about a context that started.
Type: [ContextStartedDetails](API_ContextStartedDetails.md) object
Required: No

 ** ContextSucceededDetails **   <a name="lambda-Type-Event-ContextSucceededDetails"></a>
Details about a context that succeeded.
Type: [ContextSucceededDetails](API_ContextSucceededDetails.md) object
Required: No

 ** EventId **   <a name="lambda-Type-Event-EventId"></a>
The unique identifier for this event. Event IDs increment sequentially.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** EventTimestamp **   <a name="lambda-Type-Event-EventTimestamp"></a>
The date and time when this event occurred, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: No

 ** EventType **   <a name="lambda-Type-Event-EventType"></a>
The type of event that occurred.
Type: String
Valid Values: `ExecutionStarted | ExecutionSucceeded | ExecutionFailed | ExecutionTimedOut | ExecutionStopped | ContextStarted | ContextSucceeded | ContextFailed | WaitStarted | WaitSucceeded | WaitCancelled | StepStarted | StepSucceeded | StepFailed | ChainedInvokeStarted | ChainedInvokeSucceeded | ChainedInvokeFailed | ChainedInvokeTimedOut | ChainedInvokeStopped | CallbackStarted | CallbackSucceeded | CallbackFailed | CallbackTimedOut | InvocationCompleted`
Required: No

 ** ExecutionFailedDetails **   <a name="lambda-Type-Event-ExecutionFailedDetails"></a>
Details about an execution that failed.
Type: [ExecutionFailedDetails](API_ExecutionFailedDetails.md) object
Required: No

 ** ExecutionStartedDetails **   <a name="lambda-Type-Event-ExecutionStartedDetails"></a>
Details about an execution that started.
Type: [ExecutionStartedDetails](API_ExecutionStartedDetails.md) object
Required: No

 ** ExecutionStoppedDetails **   <a name="lambda-Type-Event-ExecutionStoppedDetails"></a>
Details about an execution that was stopped.
Type: [ExecutionStoppedDetails](API_ExecutionStoppedDetails.md) object
Required: No

 ** ExecutionSucceededDetails **   <a name="lambda-Type-Event-ExecutionSucceededDetails"></a>
Details about an execution that succeeded.
Type: [ExecutionSucceededDetails](API_ExecutionSucceededDetails.md) object
Required: No

 ** ExecutionTimedOutDetails **   <a name="lambda-Type-Event-ExecutionTimedOutDetails"></a>
Details about an execution that timed out.
Type: [ExecutionTimedOutDetails](API_ExecutionTimedOutDetails.md) object
Required: No

 ** Id **   <a name="lambda-Type-Event-Id"></a>
The unique identifier for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** InvocationCompletedDetails **   <a name="lambda-Type-Event-InvocationCompletedDetails"></a>
Details about a function invocation that completed.
Type: [InvocationCompletedDetails](API_InvocationCompletedDetails.md) object
Required: No

 ** Name **   <a name="lambda-Type-Event-Name"></a>
The customer-provided name for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x20-\x7E]+`
Required: No

 ** ParentId **   <a name="lambda-Type-Event-ParentId"></a>
The unique identifier of the parent operation, if this operation is running within a child context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** StepFailedDetails **   <a name="lambda-Type-Event-StepFailedDetails"></a>
Details about a step that failed.
Type: [StepFailedDetails](API_StepFailedDetails.md) object
Required: No

 ** StepStartedDetails **   <a name="lambda-Type-Event-StepStartedDetails"></a>
Details about a step that started.
Type: [StepStartedDetails](API_StepStartedDetails.md) object
Required: No

 ** StepSucceededDetails **   <a name="lambda-Type-Event-StepSucceededDetails"></a>
Details about a step that succeeded.
Type: [StepSucceededDetails](API_StepSucceededDetails.md) object
Required: No

 ** SubType **   <a name="lambda-Type-Event-SubType"></a>
The subtype of the event, providing additional categorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** WaitCancelledDetails **   <a name="lambda-Type-Event-WaitCancelledDetails"></a>
Details about a wait operation that was cancelled.
Type: [WaitCancelledDetails](API_WaitCancelledDetails.md) object
Required: No

 ** WaitStartedDetails **   <a name="lambda-Type-Event-WaitStartedDetails"></a>
Details about a wait operation that started.
Type: [WaitStartedDetails](API_WaitStartedDetails.md) object
Required: No

 ** WaitSucceededDetails **   <a name="lambda-Type-Event-WaitSucceededDetails"></a>
Details about a wait operation that succeeded.
Type: [WaitSucceededDetails](API_WaitSucceededDetails.md) object
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
