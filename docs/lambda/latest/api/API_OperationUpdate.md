---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_OperationUpdate.html
---

# OperationUpdate
<a name="API_OperationUpdate"></a>

An update to be applied to an operation during checkpointing.

## Contents
<a name="API_OperationUpdate_Contents"></a>

 ** Action **   <a name="lambda-Type-OperationUpdate-Action"></a>
The action to take on the operation.
Type: String
Valid Values: `START | SUCCEED | FAIL | RETRY | CANCEL`
Required: Yes

 ** Id **   <a name="lambda-Type-OperationUpdate-Id"></a>
The unique identifier for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** Type **   <a name="lambda-Type-OperationUpdate-Type"></a>
The type of operation to update.
Type: String
Valid Values: `EXECUTION | CONTEXT | STEP | WAIT | CALLBACK | CHAINED_INVOKE`
Required: Yes

 ** CallbackOptions **   <a name="lambda-Type-OperationUpdate-CallbackOptions"></a>
Configuration options for callback operations in durable executions, including timeout settings and retry behavior.
Type: [CallbackOptions](API_CallbackOptions.md) object
Required: No

 ** ChainedInvokeOptions **   <a name="lambda-Type-OperationUpdate-ChainedInvokeOptions"></a>
Configuration options for chained function invocations in durable executions, including retry settings and timeout configuration.
Type: [ChainedInvokeOptions](API_ChainedInvokeOptions.md) object
Required: No

 ** ContextOptions **   <a name="lambda-Type-OperationUpdate-ContextOptions"></a>
Options for context operations.
Type: [ContextOptions](API_ContextOptions.md) object
Required: No

 ** Error **   <a name="lambda-Type-OperationUpdate-Error"></a>
The error information for failed operations.
Type: [ErrorObject](API_ErrorObject.md) object
Required: No

 ** Name **   <a name="lambda-Type-OperationUpdate-Name"></a>
The customer-provided name for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x20-\x7E]+`
Required: No

 ** ParentId **   <a name="lambda-Type-OperationUpdate-ParentId"></a>
The unique identifier of the parent operation, if this operation is running within a child context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** Payload **   <a name="lambda-Type-OperationUpdate-Payload"></a>
The payload for successful operations. The maximum payload size is 6 MB for synchronous `EXECUTION` operations (RequestResponse invocationType), 1 MB for asynchronous `EXECUTION` (Event invocationType) and `CHAINED_INVOKE` operations, and 256 KB for `CONTEXT`, `STEP`, `WAIT`, and `CALLBACK` operations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6291456.
Required: No

 ** StepOptions **   <a name="lambda-Type-OperationUpdate-StepOptions"></a>
Options for step operations.
Type: [StepOptions](API_StepOptions.md) object
Required: No

 ** SubType **   <a name="lambda-Type-OperationUpdate-SubType"></a>
The subtype of the operation, providing additional categorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** WaitOptions **   <a name="lambda-Type-OperationUpdate-WaitOptions"></a>
Options for wait operations.
Type: [WaitOptions](API_WaitOptions.md) object
Required: No

## See Also
<a name="API_OperationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/OperationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/OperationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/OperationUpdate)
