---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListDetectMitigationActionsExecutions.html
---

# ListDetectMitigationActionsExecutions
<a name="API_ListDetectMitigationActionsExecutions"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

 Lists mitigation actions executions for a Device Defender ML Detect Security Profile.

Requires permission to access the [ListDetectMitigationActionsExecutions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListDetectMitigationActionsExecutions_RequestSyntax"></a>

```
GET /detect/mitigationactions/executions?endTime={{endTime}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startTime={{startTime}}&taskId={{taskId}}&thingName={{thingName}}&violationId={{violationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDetectMitigationActionsExecutions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_ListDetectMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-request-uri-endTime"></a>
 The end of the time period for which ML Detect mitigation actions executions are returned.

 ** [maxResults](#API_ListDetectMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-request-uri-maxResults"></a>
 The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListDetectMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-request-uri-nextToken"></a>
 The token for the next set of results.

 ** [startTime](#API_ListDetectMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-request-uri-startTime"></a>
 A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.

 ** [taskId](#API_ListDetectMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-request-uri-taskId"></a>
 The unique identifier of the task.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [thingName](#API_ListDetectMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-request-uri-thingName"></a>
 The name of the thing whose mitigation actions are listed.
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [violationId](#API_ListDetectMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-request-uri-violationId"></a>
 The unique identifier of the violation.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`

## Request Body
<a name="API_ListDetectMitigationActionsExecutions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDetectMitigationActionsExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionsExecutions": [
      {
         "actionName": "string",
         "errorCode": "string",
         "executionEndDate": number,
         "executionStartDate": number,
         "message": "string",
         "status": "string",
         "taskId": "string",
         "thingName": "string",
         "violationId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDetectMitigationActionsExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionsExecutions](#API_ListDetectMitigationActionsExecutions_ResponseSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-response-actionsExecutions"></a>
 List of actions executions.
Type: Array of [DetectMitigationActionExecution](API_DetectMitigationActionExecution.md) objects

 ** [nextToken](#API_ListDetectMitigationActionsExecutions_ResponseSyntax) **   <a name="iot-ListDetectMitigationActionsExecutions-response-nextToken"></a>
 A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

## Errors
<a name="API_ListDetectMitigationActionsExecutions_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListDetectMitigationActionsExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListDetectMitigationActionsExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListDetectMitigationActionsExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
