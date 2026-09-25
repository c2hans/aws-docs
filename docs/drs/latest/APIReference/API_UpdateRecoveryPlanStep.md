---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateRecoveryPlanStep.html
---

# UpdateRecoveryPlanStep
<a name="API_UpdateRecoveryPlanStep"></a>

Updates a Recovery Plan step's name or configuration. Step type is immutable.

## Request Syntax
<a name="API_UpdateRecoveryPlanStep_RequestSyntax"></a>

```
POST /UpdateRecoveryPlanStep HTTP/1.1
Content-type: application/json

{
   "configuration": { ... },
   "recoveryPlanStepArn": "{{string}}",
   "stepName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRecoveryPlanStep_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateRecoveryPlanStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateRecoveryPlanStep_RequestSyntax) **   <a name="drs-UpdateRecoveryPlanStep-request-configuration"></a>
The new type-specific configuration of the step. The step type cannot be changed.
Type: [RecoveryPlanStepConfiguration](API_RecoveryPlanStepConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [recoveryPlanStepArn](#API_UpdateRecoveryPlanStep_RequestSyntax) **   <a name="drs-UpdateRecoveryPlanStep-request-recoveryPlanStepArn"></a>
The ARN of the Recovery Plan step to update.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** [stepName](#API_UpdateRecoveryPlanStep_RequestSyntax) **   <a name="drs-UpdateRecoveryPlanStep-request-stepName"></a>
The new name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _-]*`
Required: No

## Response Syntax
<a name="API_UpdateRecoveryPlanStep_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateRecoveryPlanStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recoveryPlanStep](#API_UpdateRecoveryPlanStep_ResponseSyntax) **   <a name="drs-UpdateRecoveryPlanStep-response-recoveryPlanStep"></a>
The updated Recovery Plan step.
Type: [RecoveryPlanStep](API_RecoveryPlanStep.md) object

## Errors
<a name="API_UpdateRecoveryPlanStep_Errors"></a>

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
<a name="API_UpdateRecoveryPlanStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/UpdateRecoveryPlanStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/UpdateRecoveryPlanStep)
