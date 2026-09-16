---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditMitigationActionsTask.html
---

# DescribeAuditMitigationActionsTask
<a name="API_DescribeAuditMitigationActionsTask"></a>

Gets information about an audit mitigation task that is used to apply mitigation actions to a set of audit findings. Properties include the actions being applied, the audit checks to which they're being applied, the task status, and aggregated task statistics.

## Request Syntax
<a name="API_DescribeAuditMitigationActionsTask_RequestSyntax"></a>

```
GET /audit/mitigationactions/tasks/{{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAuditMitigationActionsTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskId](#API_DescribeAuditMitigationActionsTask_RequestSyntax) **   <a name="iot-DescribeAuditMitigationActionsTask-request-uri-taskId"></a>
The unique identifier for the audit mitigation task.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeAuditMitigationActionsTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAuditMitigationActionsTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionsDefinition": [
      {
         "actionParams": {
            "addThingsToThingGroupParams": {
               "overrideDynamicGroups": boolean,
               "thingGroupNames": [ "string" ]
            },
            "enableIoTLoggingParams": {
               "logLevel": "string",
               "roleArnForLogging": "string"
            },
            "publishFindingToSnsParams": {
               "topicArn": "string"
            },
            "replaceDefaultPolicyVersionParams": {
               "templateName": "string"
            },
            "updateCACertificateParams": {
               "action": "string"
            },
            "updateDeviceCertificateParams": {
               "action": "string"
            }
         },
         "id": "string",
         "name": "string",
         "roleArn": "string"
      }
   ],
   "auditCheckToActionsMapping": {
      "string" : [ "string" ]
   },
   "endTime": number,
   "startTime": number,
   "target": {
      "auditCheckToReasonCodeFilter": {
         "string" : [ "string" ]
      },
      "auditTaskId": "string",
      "findingIds": [ "string" ]
   },
   "taskStatistics": {
      "string" : {
         "canceledFindingsCount": number,
         "failedFindingsCount": number,
         "skippedFindingsCount": number,
         "succeededFindingsCount": number,
         "totalFindingsCount": number
      }
   },
   "taskStatus": "string"
}
```

## Response Elements
<a name="API_DescribeAuditMitigationActionsTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionsDefinition](#API_DescribeAuditMitigationActionsTask_ResponseSyntax) **   <a name="iot-DescribeAuditMitigationActionsTask-response-actionsDefinition"></a>
Specifies the mitigation actions and their parameters that are applied as part of this task.
Type: Array of [MitigationAction](API_MitigationAction.md) objects

 ** [auditCheckToActionsMapping](#API_DescribeAuditMitigationActionsTask_ResponseSyntax) **   <a name="iot-DescribeAuditMitigationActionsTask-response-auditCheckToActionsMapping"></a>
Specifies the mitigation actions that should be applied to specific audit checks.
Type: String to array of strings map
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [endTime](#API_DescribeAuditMitigationActionsTask_ResponseSyntax) **   <a name="iot-DescribeAuditMitigationActionsTask-response-endTime"></a>
The date and time when the task was completed or canceled.
Type: Timestamp

 ** [startTime](#API_DescribeAuditMitigationActionsTask_ResponseSyntax) **   <a name="iot-DescribeAuditMitigationActionsTask-response-startTime"></a>
The date and time when the task was started.
Type: Timestamp

 ** [target](#API_DescribeAuditMitigationActionsTask_ResponseSyntax) **   <a name="iot-DescribeAuditMitigationActionsTask-response-target"></a>
Identifies the findings to which the mitigation actions are applied. This can be by audit checks, by audit task, or a set of findings.
Type: [AuditMitigationActionsTaskTarget](API_AuditMitigationActionsTaskTarget.md) object

 ** [taskStatistics](#API_DescribeAuditMitigationActionsTask_ResponseSyntax) **   <a name="iot-DescribeAuditMitigationActionsTask-response-taskStatistics"></a>
Aggregate counts of the results when the mitigation tasks were applied to the findings for this audit mitigation actions task.
Type: String to [TaskStatisticsForAuditCheck](API_TaskStatisticsForAuditCheck.md) object map

 ** [taskStatus](#API_DescribeAuditMitigationActionsTask_ResponseSyntax) **   <a name="iot-DescribeAuditMitigationActionsTask-response-taskStatus"></a>
The current status of the task.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | CANCELED`

## Errors
<a name="API_DescribeAuditMitigationActionsTask_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAuditMitigationActionsTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeAuditMitigationActionsTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeAuditMitigationActionsTask)
