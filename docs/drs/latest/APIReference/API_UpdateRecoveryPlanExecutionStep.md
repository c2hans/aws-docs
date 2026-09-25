---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateRecoveryPlanExecutionStep.html
---

# UpdateRecoveryPlanExecutionStep
<a name="API_UpdateRecoveryPlanExecutionStep"></a>

Updates an execution step. Supports two actions: (1) skip a step that is in `NOT_STARTED` or `FAILED` status; (2) update the wait duration of a `WAIT` type step that is in `NOT_STARTED` status.

## Request Syntax
<a name="API_UpdateRecoveryPlanExecutionStep_RequestSyntax"></a>

```
POST /UpdateRecoveryPlanExecutionStep HTTP/1.1
Content-type: application/json

{
   "recoveryPlanExecutionStepArn": "{{string}}",
   "servers": [
      {
         "impactLevel": "{{string}}",
         "serverArn": "{{string}}"
      }
   ],
   "status": "{{string}}",
   "waitDurationMinutes": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateRecoveryPlanExecutionStep_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateRecoveryPlanExecutionStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [recoveryPlanExecutionStepArn](#API_UpdateRecoveryPlanExecutionStep_RequestSyntax) **   <a name="drs-UpdateRecoveryPlanExecutionStep-request-recoveryPlanExecutionStepArn"></a>
The ARN of the execution step to update.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** [servers](#API_UpdateRecoveryPlanExecutionStep_RequestSyntax) **   <a name="drs-UpdateRecoveryPlanExecutionStep-request-servers"></a>
Full replacement of the server list. Only allowed when the step is in `NOT_STARTED` status for server steps.
Type: Array of [RecoveryPlanServer](API_RecoveryPlanServer.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [status](#API_UpdateRecoveryPlanExecutionStep_RequestSyntax) **   <a name="drs-UpdateRecoveryPlanExecutionStep-request-status"></a>
The status of a step within a Recovery Plan execution.
Type: String
Valid Values: `NOT_STARTED | EXECUTING | WAITING | COMPLETED | FAILED | TIMED_OUT | SKIPPED`
Required: No

 ** [waitDurationMinutes](#API_UpdateRecoveryPlanExecutionStep_RequestSyntax) **   <a name="drs-UpdateRecoveryPlanExecutionStep-request-waitDurationMinutes"></a>
Updated wait duration. Only allowed when the step is in `NOT_STARTED` status for wait steps.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 120.
Required: No

## Response Syntax
<a name="API_UpdateRecoveryPlanExecutionStep_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "recoveryPlanExecutionStep": {
      "attempt": number,
      "configuration": { ... },
      "createdAt": "string",
      "errorDetail": {
         "code": "string",
         "message": "string"
      },
      "recoveryPlanExecutionStepArn": "string",
      "status": "string",
      "stepIndex": number,
      "stepName": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_UpdateRecoveryPlanExecutionStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recoveryPlanExecutionStep](#API_UpdateRecoveryPlanExecutionStep_ResponseSyntax) **   <a name="drs-UpdateRecoveryPlanExecutionStep-response-recoveryPlanExecutionStep"></a>
The updated execution step.
Type: [RecoveryPlanExecutionStep](API_RecoveryPlanExecutionStep.md) object

## Errors
<a name="API_UpdateRecoveryPlanExecutionStep_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRecoveryPlanExecutionStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/UpdateRecoveryPlanExecutionStep)
