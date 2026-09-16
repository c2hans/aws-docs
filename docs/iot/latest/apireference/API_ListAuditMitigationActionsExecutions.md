---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditMitigationActionsExecutions.html
---

# ListAuditMitigationActionsExecutions
<a name="API_ListAuditMitigationActionsExecutions"></a>

Gets the status of audit mitigation action tasks that were executed.

Requires permission to access the [ListAuditMitigationActionsExecutions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListAuditMitigationActionsExecutions_RequestSyntax"></a>

```
GET /audit/mitigationactions/executions?actionStatus={{actionStatus}}&findingId={{findingId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&taskId={{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAuditMitigationActionsExecutions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionStatus](#API_ListAuditMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsExecutions-request-uri-actionStatus"></a>
Specify this filter to limit results to those with a specific status.
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | CANCELED | SKIPPED | PENDING`

 ** [findingId](#API_ListAuditMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsExecutions-request-uri-findingId"></a>
Specify this filter to limit results to those that were applied to a specific audit finding.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [maxResults](#API_ListAuditMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsExecutions-request-uri-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListAuditMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsExecutions-request-uri-nextToken"></a>
The token for the next set of results.

 ** [taskId](#API_ListAuditMitigationActionsExecutions_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsExecutions-request-uri-taskId"></a>
Specify this filter to limit results to actions for a specific audit mitigation actions task.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_ListAuditMitigationActionsExecutions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAuditMitigationActionsExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionsExecutions": [
      {
         "actionId": "string",
         "actionName": "string",
         "endTime": number,
         "errorCode": "string",
         "findingId": "string",
         "message": "string",
         "startTime": number,
         "status": "string",
         "taskId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAuditMitigationActionsExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionsExecutions](#API_ListAuditMitigationActionsExecutions_ResponseSyntax) **   <a name="iot-ListAuditMitigationActionsExecutions-response-actionsExecutions"></a>
A set of task execution results based on the input parameters. Details include the mitigation action applied, start time, and task status.
Type: Array of [AuditMitigationActionExecutionMetadata](API_AuditMitigationActionExecutionMetadata.md) objects

 ** [nextToken](#API_ListAuditMitigationActionsExecutions_ResponseSyntax) **   <a name="iot-ListAuditMitigationActionsExecutions-response-nextToken"></a>
The token for the next set of results.
Type: String

## Errors
<a name="API_ListAuditMitigationActionsExecutions_Errors"></a>

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
<a name="API_ListAuditMitigationActionsExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListAuditMitigationActionsExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListAuditMitigationActionsExecutions)
