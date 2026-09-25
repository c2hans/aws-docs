---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateRecoveryPlanStep.html
---

# CreateRecoveryPlanStep
<a name="API_CreateRecoveryPlanStep"></a>

Creates a step in a Recovery Plan. A step is either `SERVER` type (servers to recover in parallel) or `WAIT` type (timed pause between steps).

## Request Syntax
<a name="API_CreateRecoveryPlanStep_RequestSyntax"></a>

```
POST /CreateRecoveryPlanStep HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "recoveryPlanArn": "{{string}}",
   "stepName": "{{string}}",
   "stepOrder": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateRecoveryPlanStep_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRecoveryPlanStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateRecoveryPlanStep_RequestSyntax) **   <a name="drs-CreateRecoveryPlanStep-request-clientToken"></a>
A unique string provided to ensure request idempotency.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [configuration](#API_CreateRecoveryPlanStep_RequestSyntax) **   <a name="drs-CreateRecoveryPlanStep-request-configuration"></a>
The type-specific configuration of the step. Exactly one of `serverStepConfiguration` or `waitStepConfiguration` must be set.
Type: [RecoveryPlanStepConfiguration](API_RecoveryPlanStepConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [recoveryPlanArn](#API_CreateRecoveryPlanStep_RequestSyntax) **   <a name="drs-CreateRecoveryPlanStep-request-recoveryPlanArn"></a>
The ARN of the Recovery Plan to add the step to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** [stepName](#API_CreateRecoveryPlanStep_RequestSyntax) **   <a name="drs-CreateRecoveryPlanStep-request-stepName"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _-]*`
Required: Yes

 ** [stepOrder](#API_CreateRecoveryPlanStep_RequestSyntax) **   <a name="drs-CreateRecoveryPlanStep-request-stepOrder"></a>
The 1-based position of the step within the Recovery Plan.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

## Response Syntax
<a name="API_CreateRecoveryPlanStep_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "recoveryPlanStep": {
      "configuration": { ... },
      "createdAt": "string",
      "recoveryPlanStepArn": "string",
      "stepName": "string",
      "stepOrder": number,
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_CreateRecoveryPlanStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [recoveryPlanStep](#API_CreateRecoveryPlanStep_ResponseSyntax) **   <a name="drs-CreateRecoveryPlanStep-response-recoveryPlanStep"></a>
The created Recovery Plan step.
Type: [RecoveryPlanStep](API_RecoveryPlanStep.md) object

## Errors
<a name="API_CreateRecoveryPlanStep_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request could not be completed because its exceeded the service quota.
 ** quotaCode **
Quota code.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
 ** serviceCode **
Service code.
HTTP Status Code: 402

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
<a name="API_CreateRecoveryPlanStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/CreateRecoveryPlanStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/CreateRecoveryPlanStep)
