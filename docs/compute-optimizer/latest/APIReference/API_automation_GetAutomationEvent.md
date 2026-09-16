---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetAutomationEvent.html
---

# GetAutomationEvent
<a name="API_automation_GetAutomationEvent"></a>

 Retrieves details about a specific automation event.

## Request Syntax
<a name="API_automation_GetAutomationEvent_RequestSyntax"></a>

```
{
   "eventId": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_GetAutomationEvent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [eventId](#API_automation_GetAutomationEvent_RequestSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-request-eventId"></a>
 The ID of the automation event to retrieve.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: Yes

## Response Syntax
<a name="API_automation_GetAutomationEvent_ResponseSyntax"></a>

```
{
   "accountId": "string",
   "completedTimestamp": number,
   "createdTimestamp": number,
   "estimatedMonthlySavings": {
      "afterDiscountSavings": number,
      "beforeDiscountSavings": number,
      "currency": "string",
      "savingsEstimationMode": "string"
   },
   "eventDescription": "string",
   "eventId": "string",
   "eventStatus": "string",
   "eventStatusReason": "string",
   "eventType": "string",
   "recommendedActionId": "string",
   "region": "string",
   "resourceArn": "string",
   "resourceId": "string",
   "resourceType": "string",
   "ruleId": "string"
}
```

## Response Elements
<a name="API_automation_GetAutomationEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-accountId"></a>
The AWS account ID associated with the automation event.
Type: String
Pattern: `[0-9]{12}`

 ** [completedTimestamp](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-completedTimestamp"></a>
The timestamp when the automation event completed.
Type: Timestamp

 ** [createdTimestamp](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-createdTimestamp"></a>
The timestamp when the automation event was created.
Type: Timestamp

 ** [estimatedMonthlySavings](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-estimatedMonthlySavings"></a>
 Contains information about estimated monthly cost savings.
Type: [EstimatedMonthlySavings](API_automation_EstimatedMonthlySavings.md) object

 ** [eventDescription](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-eventDescription"></a>
A description of the automation event.
Type: String

 ** [eventId](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-eventId"></a>
The ID of the automation event to retrieve.
Type: String
Pattern: `[0-9A-Za-z]{16}`

 ** [eventStatus](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-eventStatus"></a>
The current status of the automation event.
Type: String
Valid Values: `Ready | InProgress | Complete | Failed | Cancelled | RollbackReady | RollbackInProgress | RollbackComplete | RollbackFailed`

 ** [eventStatusReason](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-eventStatusReason"></a>
The reason for the current event status.
Type: String

 ** [eventType](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-eventType"></a>
The type of automation event.
Type: String
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`

 ** [recommendedActionId](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-recommendedActionId"></a>
The ID of the recommended action associated with this automation event.
Type: String
Pattern: `[0-9A-Za-z]{16}`

 ** [region](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-region"></a>
The AWS Region where the automation event occurred.
Type: String

 ** [resourceArn](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource affected by the automation event.
Type: String
Pattern: `arn:aws[a-z0-9-]*:[a-z0-9-]+:[a-z0-9-]*:[0-9]{0,12}:[a-zA-Z0-9/_.-]+`

 ** [resourceId](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-resourceId"></a>
The ID of the resource affected by the automation event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [resourceType](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-resourceType"></a>
The type of resource affected by the automation event.
Type: String
Valid Values: `EbsVolume`

 ** [ruleId](#API_automation_GetAutomationEvent_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationEvent-response-ruleId"></a>
The ID of the automation rule that triggered this event.
Type: String
Pattern: `[0-9A-Za-z]{16}`

## Errors
<a name="API_automation_GetAutomationEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
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

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_GetAutomationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/GetAutomationEvent)
