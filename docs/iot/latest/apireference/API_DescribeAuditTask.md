---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditTask.html
---

# DescribeAuditTask
<a name="API_DescribeAuditTask"></a>

Gets information about a Device Defender audit.

Requires permission to access the [DescribeAuditTask](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeAuditTask_RequestSyntax"></a>

```
GET /audit/tasks/{{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAuditTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskId](#API_DescribeAuditTask_RequestSyntax) **   <a name="iot-DescribeAuditTask-request-uri-taskId"></a>
The ID of the audit whose information you want to get.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DescribeAuditTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAuditTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "auditDetails": {
      "string" : {
         "checkCompliant": boolean,
         "checkRunStatus": "string",
         "errorCode": "string",
         "message": "string",
         "nonCompliantResourcesCount": number,
         "suppressedNonCompliantResourcesCount": number,
         "totalResourcesCount": number
      }
   },
   "scheduledAuditName": "string",
   "taskStartTime": number,
   "taskStatistics": {
      "canceledChecks": number,
      "compliantChecks": number,
      "failedChecks": number,
      "inProgressChecks": number,
      "nonCompliantChecks": number,
      "totalChecks": number,
      "waitingForDataCollectionChecks": number
   },
   "taskStatus": "string",
   "taskType": "string"
}
```

## Response Elements
<a name="API_DescribeAuditTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [auditDetails](#API_DescribeAuditTask_ResponseSyntax) **   <a name="iot-DescribeAuditTask-response-auditDetails"></a>
Detailed information about each check performed during this audit.
Type: String to [AuditCheckDetails](API_AuditCheckDetails.md) object map

 ** [scheduledAuditName](#API_DescribeAuditTask_ResponseSyntax) **   <a name="iot-DescribeAuditTask-response-scheduledAuditName"></a>
The name of the scheduled audit (only if the audit was a scheduled audit).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [taskStartTime](#API_DescribeAuditTask_ResponseSyntax) **   <a name="iot-DescribeAuditTask-response-taskStartTime"></a>
The time the audit started.
Type: Timestamp

 ** [taskStatistics](#API_DescribeAuditTask_ResponseSyntax) **   <a name="iot-DescribeAuditTask-response-taskStatistics"></a>
Statistical information about the audit.
Type: [TaskStatistics](API_TaskStatistics.md) object

 ** [taskStatus](#API_DescribeAuditTask_ResponseSyntax) **   <a name="iot-DescribeAuditTask-response-taskStatus"></a>
The status of the audit: one of "IN\_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | CANCELED`

 ** [taskType](#API_DescribeAuditTask_ResponseSyntax) **   <a name="iot-DescribeAuditTask-response-taskType"></a>
The type of audit: "ON\_DEMAND\_AUDIT\_TASK" or "SCHEDULED\_AUDIT\_TASK".
Type: String
Valid Values: `ON_DEMAND_AUDIT_TASK | SCHEDULED_AUDIT_TASK`

## Errors
<a name="API_DescribeAuditTask_Errors"></a>

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
<a name="API_DescribeAuditTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeAuditTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeAuditTask)
