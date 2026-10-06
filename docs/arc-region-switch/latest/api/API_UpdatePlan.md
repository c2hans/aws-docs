---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlan.html
---

# UpdatePlan
<a name="API_UpdatePlan"></a>

Updates an existing Region switch plan. You can modify the plan's description, workflows, execution role, recovery time objective, associated alarms, and triggers.

## Request Syntax
<a name="API_UpdatePlan_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "associatedAlarms": {
      "{{string}}" : {
         "alarmType": "{{string}}",
         "crossAccountRole": "{{string}}",
         "externalId": "{{string}}",
         "resourceIdentifier": "{{string}}"
      }
   },
   "description": "{{string}}",
   "executionRole": "{{string}}",
   "recoveryTimeObjectiveMinutes": {{number}},
   "reportConfiguration": {
      "reportOutput": [
         { ... }
      ]
   },
   "triggers": [
      {
         "action": "{{string}}",
         "conditions": [
            {
               "associatedAlarmName": "{{string}}",
               "condition": "{{string}}"
            }
         ],
         "description": "{{string}}",
         "minDelayMinutesBetweenExecutions": {{number}},
         "targetRegion": "{{string}}"
      }
   ],
   "workflows": [
      {
         "steps": [
            {
               "description": "{{string}}",
               "executionBlockConfiguration": { ... },
               "executionBlockType": "{{string}}",
               "name": "{{string}}"
            }
         ],
         "workflowDescription": "{{string}}",
         "workflowTargetAction": "{{string}}",
         "workflowTargetRegion": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdatePlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_UpdatePlan_RequestSyntax) **   <a name="regionswitch-UpdatePlan-request-arn"></a>
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** [associatedAlarms](#API_UpdatePlan_RequestSyntax) **   <a name="regionswitch-UpdatePlan-request-associatedAlarms"></a>
The updated CloudWatch alarms associated with the plan.
Type: String to [AssociatedAlarm](API_AssociatedAlarm.md) object map
Required: No

 ** [description](#API_UpdatePlan_RequestSyntax) **   <a name="regionswitch-UpdatePlan-request-description"></a>
The updated description for the Region switch plan.
Type: String
Required: No

 ** [executionRole](#API_UpdatePlan_RequestSyntax) **   <a name="regionswitch-UpdatePlan-request-executionRole"></a>
The updated IAM role ARN that grants Region switch the permissions needed to execute the plan steps.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [recoveryTimeObjectiveMinutes](#API_UpdatePlan_RequestSyntax) **   <a name="regionswitch-UpdatePlan-request-recoveryTimeObjectiveMinutes"></a>
The updated target recovery time objective (RTO) in minutes for the plan.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10080.
Required: No

 ** [reportConfiguration](#API_UpdatePlan_RequestSyntax) **   <a name="regionswitch-UpdatePlan-request-reportConfiguration"></a>
The updated report configuration for the plan.
Type: [ReportConfiguration](API_ReportConfiguration.md) object
Required: No

 ** [triggers](#API_UpdatePlan_RequestSyntax) **   <a name="regionswitch-UpdatePlan-request-triggers"></a>
The updated conditions that can automatically trigger the execution of the plan.
Type: Array of [Trigger](API_Trigger.md) objects
Required: No

 ** [workflows](#API_UpdatePlan_RequestSyntax) **   <a name="regionswitch-UpdatePlan-request-workflows"></a>
The updated workflows for the Region switch plan.
Type: Array of [Workflow](API_Workflow.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdatePlan_ResponseSyntax"></a>

```
{
   "plan": {
      "arn": "string",
      "associatedAlarms": {
         "string" : {
            "alarmType": "string",
            "crossAccountRole": "string",
            "externalId": "string",
            "resourceIdentifier": "string"
         }
      },
      "description": "string",
      "executionRole": "string",
      "name": "string",
      "owner": "string",
      "primaryRegion": "string",
      "recoveryApproach": "string",
      "recoveryTimeObjectiveMinutes": number,
      "regions": [ "string" ],
      "reportConfiguration": {
         "reportOutput": [
            { ... }
         ]
      },
      "triggers": [
         {
            "action": "string",
            "conditions": [
               {
                  "associatedAlarmName": "string",
                  "condition": "string"
               }
            ],
            "description": "string",
            "minDelayMinutesBetweenExecutions": number,
            "targetRegion": "string"
         }
      ],
      "updatedAt": number,
      "version": "string",
      "workflows": [
         {
            "steps": [
               {
                  "description": "string",
                  "executionBlockConfiguration": { ... },
                  "executionBlockType": "string",
                  "name": "string"
               }
            ],
            "workflowDescription": "string",
            "workflowTargetAction": "string",
            "workflowTargetRegion": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdatePlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [plan](#API_UpdatePlan_ResponseSyntax) **   <a name="regionswitch-UpdatePlan-response-plan"></a>
The details of the updated Region switch plan.
Type: [Plan](API_Plan.md) object

## Errors
<a name="API_UpdatePlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404
HTTP Status Code: 404

## See Also
<a name="API_UpdatePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/UpdatePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/UpdatePlan)
