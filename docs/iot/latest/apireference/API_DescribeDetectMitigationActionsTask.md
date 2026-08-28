---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDetectMitigationActionsTask.html
---

# DescribeDetectMitigationActionsTask
<a name="API_DescribeDetectMitigationActionsTask"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

 Gets information about a Device Defender ML Detect mitigation action.

Requires permission to access the [DescribeDetectMitigationActionsTask](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeDetectMitigationActionsTask_RequestSyntax"></a>

```
GET /detect/mitigationactions/tasks/{{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDetectMitigationActionsTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskId](#API_DescribeDetectMitigationActionsTask_RequestSyntax) **   <a name="iot-DescribeDetectMitigationActionsTask-request-uri-taskId"></a>
 The unique identifier of the task.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeDetectMitigationActionsTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDetectMitigationActionsTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "taskSummary": {
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
      "onlyActiveViolationsIncluded": boolean,
      "suppressedAlertsIncluded": boolean,
      "target": {
         "behaviorName": "string",
         "securityProfileName": "string",
         "violationIds": [ "string" ]
      },
      "taskEndTime": number,
      "taskId": "string",
      "taskStartTime": number,
      "taskStatistics": {
         "actionsExecuted": number,
         "actionsFailed": number,
         "actionsSkipped": number
      },
      "taskStatus": "string",
      "violationEventOccurrenceRange": {
         "endTime": number,
         "startTime": number
      }
   }
}
```

## Response Elements
<a name="API_DescribeDetectMitigationActionsTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskSummary](#API_DescribeDetectMitigationActionsTask_ResponseSyntax) **   <a name="iot-DescribeDetectMitigationActionsTask-response-taskSummary"></a>
 The description of a task.
Type: [DetectMitigationActionsTaskSummary](API_DetectMitigationActionsTaskSummary.md) object

## Errors
<a name="API_DescribeDetectMitigationActionsTask_Errors"></a>

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
<a name="API_DescribeDetectMitigationActionsTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeDetectMitigationActionsTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeDetectMitigationActionsTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
