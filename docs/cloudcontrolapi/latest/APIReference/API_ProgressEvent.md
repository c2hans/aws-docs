---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ProgressEvent.html
---

# ProgressEvent
<a name="API_ProgressEvent"></a>

Represents the current status of a resource operation request. For more information, see [Managing resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html) in the * AWS Cloud Control API User Guide*.

## Contents
<a name="API_ProgressEvent_Contents"></a>

 ** ErrorCode **   <a name="ccapi-Type-ProgressEvent-ErrorCode"></a>
For requests with a status of `FAILED`, the associated error code.
For error code definitions, see [Handler error codes](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract-errors.html) in the *CloudFormation Command Line Interface User Guide for Extension Development*.
Type: String
Valid Values: `NotUpdatable | InvalidRequest | AccessDenied | UnauthorizedTaggingOperation | InvalidCredentials | AlreadyExists | NotFound | ResourceConflict | Throttling | ServiceLimitExceeded | NotStabilized | GeneralServiceException | ServiceInternalError | ServiceTimeout | NetworkFailure | InternalFailure`
Required: No

 ** EventTime **   <a name="ccapi-Type-ProgressEvent-EventTime"></a>
When the resource operation request was initiated.
Type: Timestamp
Required: No

 ** HooksRequestToken **   <a name="ccapi-Type-ProgressEvent-HooksRequestToken"></a>
The unique token representing the Hooks operation for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-A-Za-z0-9+/=]+`
Required: No

 ** Identifier **   <a name="ccapi-Type-ProgressEvent-Identifier"></a>
The primary identifier for the resource.
In some cases, the resource identifier may be available before the resource operation has reached a status of `SUCCESS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** Operation **   <a name="ccapi-Type-ProgressEvent-Operation"></a>
The resource operation type.
Type: String
Valid Values: `CREATE | DELETE | UPDATE`
Required: No

 ** OperationStatus **   <a name="ccapi-Type-ProgressEvent-OperationStatus"></a>
The current status of the resource operation request.
+  `PENDING`: The resource operation hasn't yet started.
+  `IN_PROGRESS`: The resource operation is currently in progress.
+  `SUCCESS`: The resource operation has successfully completed.
+  `FAILED`: The resource operation has failed. Refer to the error code and status message for more information.
+  `CANCEL_IN_PROGRESS`: The resource operation is in the process of being canceled.
+  `CANCEL_COMPLETE`: The resource operation has been canceled.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED | CANCEL_IN_PROGRESS | CANCEL_COMPLETE`
Required: No

 ** RequestToken **   <a name="ccapi-Type-ProgressEvent-RequestToken"></a>
The unique token representing this resource operation request.
Use the `RequestToken` with [GetResourceRequestStatus](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html) to return the current status of a resource operation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-A-Za-z0-9+/=]+`
Required: No

 ** ResourceModel **   <a name="ccapi-Type-ProgressEvent-ResourceModel"></a>
A JSON string containing the resource model, consisting of each resource property and its current value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Pattern: `[\s\S]*`
Required: No

 ** RetryAfter **   <a name="ccapi-Type-ProgressEvent-RetryAfter"></a>
When to next request the status of this resource operation request.
Type: Timestamp
Required: No

 ** StatusMessage **   <a name="ccapi-Type-ProgressEvent-StatusMessage"></a>
Any message explaining the current status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** TypeName **   <a name="ccapi-Type-ProgressEvent-TypeName"></a>
The name of the resource type used in the operation.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 196.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}`
Required: No

## See Also
<a name="API_ProgressEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/ProgressEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/ProgressEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/ProgressEvent)
