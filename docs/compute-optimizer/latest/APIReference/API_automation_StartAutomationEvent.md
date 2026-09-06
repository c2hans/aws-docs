---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_StartAutomationEvent.html
---

# StartAutomationEvent
<a name="API_automation_StartAutomationEvent"></a>

 Initiates a one-time, on-demand automation for the specified recommended action.

**Note**
Management accounts and delegated administrators can only initiate recommended actions for associated member accounts. You can associate a member account using `AssociateAccounts`.

## Request Syntax
<a name="API_automation_StartAutomationEvent_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "recommendedActionId": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_StartAutomationEvent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_automation_StartAutomationEvent_RequestSyntax) **   <a name="computeoptimizer-automation_StartAutomationEvent-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

 ** [recommendedActionId](#API_automation_StartAutomationEvent_RequestSyntax) **   <a name="computeoptimizer-automation_StartAutomationEvent-request-recommendedActionId"></a>
 The ID of the recommended action to automate.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: Yes

## Response Syntax
<a name="API_automation_StartAutomationEvent_ResponseSyntax"></a>

```
{
   "eventId": "string",
   "eventStatus": "string",
   "recommendedActionId": "string"
}
```

## Response Elements
<a name="API_automation_StartAutomationEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventId](#API_automation_StartAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_StartAutomationEvent-response-eventId"></a>
The ID of the automation event.
Type: String
Pattern: `[0-9A-Za-z]{16}`

 ** [eventStatus](#API_automation_StartAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_StartAutomationEvent-response-eventStatus"></a>
The current status of the automation event.
Type: String
Valid Values: `Ready | InProgress | Complete | Failed | Cancelled | RollbackReady | RollbackInProgress | RollbackComplete | RollbackFailed`

 ** [recommendedActionId](#API_automation_StartAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_StartAutomationEvent-response-recommendedActionId"></a>
The ID of the recommended action being automated.
Type: String
Pattern: `[0-9A-Za-z]{16}`

## Errors
<a name="API_automation_StartAutomationEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 400

 ** IdempotencyTokenInUseException **
 The specified client token is already in use.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
Exception thrown when the same client token is used with different parameters, indicating a mismatch in idempotent request parameters.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
 One or more parameter values are not valid.
HTTP Status Code: 400

 ** OptInRequiredException **
 The account must be opted in to Compute Optimizer Automation before performing this action.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified resource was not found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
 The request would exceed service quotas.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_StartAutomationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/StartAutomationEvent)
