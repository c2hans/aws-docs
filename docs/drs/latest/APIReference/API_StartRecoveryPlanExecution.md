---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_StartRecoveryPlanExecution.html
---

# StartRecoveryPlanExecution
<a name="API_StartRecoveryPlanExecution"></a>

Starts executing a Recovery Plan in `DRILL` or `RECOVERY` mode. A plan cannot have more than one execution in a non-terminal status at a time.

## Request Syntax
<a name="API_StartRecoveryPlanExecution_RequestSyntax"></a>

```
POST /StartRecoveryPlanExecution HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "mode": "{{string}}",
   "recoveryPlanArn": "{{string}}",
   "sourceServers": [
      {
         "recoverySnapshotID": "{{string}}",
         "sourceServerID": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartRecoveryPlanExecution_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartRecoveryPlanExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartRecoveryPlanExecution_RequestSyntax) **   <a name="drs-StartRecoveryPlanExecution-request-clientToken"></a>
A unique string provided to ensure request idempotency.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [mode](#API_StartRecoveryPlanExecution_RequestSyntax) **   <a name="drs-StartRecoveryPlanExecution-request-mode"></a>
The execution mode (`DRILL` or `RECOVERY`).
Type: String
Valid Values: `DRILL | RECOVERY`
Required: Yes

 ** [recoveryPlanArn](#API_StartRecoveryPlanExecution_RequestSyntax) **   <a name="drs-StartRecoveryPlanExecution-request-recoveryPlanArn"></a>
The ARN of the Recovery Plan to execute.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** [sourceServers](#API_StartRecoveryPlanExecution_RequestSyntax) **   <a name="drs-StartRecoveryPlanExecution-request-sourceServers"></a>
Optional list of source servers with specific recovery snapshots. If not provided, the latest snapshot is used for each server.
Type: Array of [RecoveryPlanExecutionSourceServer](API_RecoveryPlanExecutionSourceServer.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [tags](#API_StartRecoveryPlanExecution_RequestSyntax) **   <a name="drs-StartRecoveryPlanExecution-request-tags"></a>
The tags to apply to the Recovery Plan execution.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartRecoveryPlanExecution_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "recoveryPlanExecution": {
      "completedAt": "string",
      "errorDetail": {
         "code": "string",
         "message": "string"
      },
      "mode": "string",
      "recoveryPlanArn": "string",
      "recoveryPlanExecutionArn": "string",
      "startedAt": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_StartRecoveryPlanExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [recoveryPlanExecution](#API_StartRecoveryPlanExecution_ResponseSyntax) **   <a name="drs-StartRecoveryPlanExecution-response-recoveryPlanExecution"></a>
The started Recovery Plan execution.
Type: [RecoveryPlanExecution](API_RecoveryPlanExecution.md) object

## Errors
<a name="API_StartRecoveryPlanExecution_Errors"></a>

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
<a name="API_StartRecoveryPlanExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/StartRecoveryPlanExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/StartRecoveryPlanExecution)
