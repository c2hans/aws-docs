---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditTasks.html
---

# ListAuditTasks
<a name="API_ListAuditTasks"></a>

Lists the Device Defender audits that have been performed during a given time period.

Requires permission to access the [ListAuditTasks](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListAuditTasks_RequestSyntax"></a>

```
GET /audit/tasks?endTime={{endTime}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startTime={{startTime}}&taskStatus={{taskStatus}}&taskType={{taskType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAuditTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_ListAuditTasks_RequestSyntax) **   <a name="iot-ListAuditTasks-request-uri-endTime"></a>
The end of the time period.
Required: Yes

 ** [maxResults](#API_ListAuditTasks_RequestSyntax) **   <a name="iot-ListAuditTasks-request-uri-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListAuditTasks_RequestSyntax) **   <a name="iot-ListAuditTasks-request-uri-nextToken"></a>
The token for the next set of results.

 ** [startTime](#API_ListAuditTasks_RequestSyntax) **   <a name="iot-ListAuditTasks-request-uri-startTime"></a>
The beginning of the time period. Audit information is retained for a limited time (90 days). Requesting a start time prior to what is retained results in an "InvalidRequestException".
Required: Yes

 ** [taskStatus](#API_ListAuditTasks_RequestSyntax) **   <a name="iot-ListAuditTasks-request-uri-taskStatus"></a>
A filter to limit the output to audits with the specified completion status: can be one of "IN\_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | CANCELED`

 ** [taskType](#API_ListAuditTasks_RequestSyntax) **   <a name="iot-ListAuditTasks-request-uri-taskType"></a>
A filter to limit the output to the specified type of audit: can be one of "ON\_DEMAND\_AUDIT\_TASK" or "SCHEDULED\_\_AUDIT\_TASK".
Valid Values: `ON_DEMAND_AUDIT_TASK | SCHEDULED_AUDIT_TASK`

## Request Body
<a name="API_ListAuditTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAuditTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "tasks": [
      {
         "taskId": "string",
         "taskStatus": "string",
         "taskType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAuditTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAuditTasks_ResponseSyntax) **   <a name="iot-ListAuditTasks-response-nextToken"></a>
A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

 ** [tasks](#API_ListAuditTasks_ResponseSyntax) **   <a name="iot-ListAuditTasks-response-tasks"></a>
The audits that were performed during the specified time period.
Type: Array of [AuditTaskMetadata](API_AuditTaskMetadata.md) objects

## Errors
<a name="API_ListAuditTasks_Errors"></a>

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
<a name="API_ListAuditTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListAuditTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListAuditTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
