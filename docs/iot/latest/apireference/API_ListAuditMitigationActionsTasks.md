---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditMitigationActionsTasks.html
---

# ListAuditMitigationActionsTasks
<a name="API_ListAuditMitigationActionsTasks"></a>

Gets a list of audit mitigation action tasks that match the specified filters.

Requires permission to access the [ListAuditMitigationActionsTasks](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListAuditMitigationActionsTasks_RequestSyntax"></a>

```
GET /audit/mitigationactions/tasks?auditTaskId={{auditTaskId}}&endTime={{endTime}}&findingId={{findingId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startTime={{startTime}}&taskStatus={{taskStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAuditMitigationActionsTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [auditTaskId](#API_ListAuditMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-request-uri-auditTaskId"></a>
Specify this filter to limit results to tasks that were applied to results for a specific audit.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9\-]+`

 ** [endTime](#API_ListAuditMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-request-uri-endTime"></a>
Specify this filter to limit results to tasks that were completed or canceled on or before a specific date and time.
Required: Yes

 ** [findingId](#API_ListAuditMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-request-uri-findingId"></a>
Specify this filter to limit results to tasks that were applied to a specific audit finding.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [maxResults](#API_ListAuditMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-request-uri-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListAuditMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-request-uri-nextToken"></a>
The token for the next set of results.

 ** [startTime](#API_ListAuditMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-request-uri-startTime"></a>
Specify this filter to limit results to tasks that began on or after a specific date and time.
Required: Yes

 ** [taskStatus](#API_ListAuditMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-request-uri-taskStatus"></a>
Specify this filter to limit results to tasks that are in a specific state.
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | CANCELED`

## Request Body
<a name="API_ListAuditMitigationActionsTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAuditMitigationActionsTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "tasks": [
      {
         "startTime": number,
         "taskId": "string",
         "taskStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAuditMitigationActionsTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAuditMitigationActionsTasks_ResponseSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-response-nextToken"></a>
The token for the next set of results.
Type: String

 ** [tasks](#API_ListAuditMitigationActionsTasks_ResponseSyntax) **   <a name="iot-ListAuditMitigationActionsTasks-response-tasks"></a>
The collection of audit mitigation tasks that matched the filter criteria.
Type: Array of [AuditMitigationActionsTaskMetadata](API_AuditMitigationActionsTaskMetadata.md) objects

## Errors
<a name="API_ListAuditMitigationActionsTasks_Errors"></a>

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
<a name="API_ListAuditMitigationActionsTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListAuditMitigationActionsTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListAuditMitigationActionsTasks)
