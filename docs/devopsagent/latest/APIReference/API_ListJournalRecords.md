---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListJournalRecords.html
---

# ListJournalRecords
<a name="API_ListJournalRecords"></a>

List journal records for a specific execution

## Request Syntax
<a name="API_ListJournalRecords_RequestSyntax"></a>

```
POST /journal/agent-space/{{agentSpaceId}}/journalRecords HTTP/1.1
Content-type: application/json

{
   "executionId": "{{string}}",
   "limit": {{number}},
   "nextToken": "{{string}}",
   "order": "{{string}}",
   "recordType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListJournalRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_ListJournalRecords_RequestSyntax) **   <a name="devopsagent-ListJournalRecords-request-uri-agentSpaceId"></a>
The unique identifier for the agent space containing the execution
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_ListJournalRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [executionId](#API_ListJournalRecords_RequestSyntax) **   <a name="devopsagent-ListJournalRecords-request-executionId"></a>
The unique identifier of the execution whose journal records to retrieve
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [limit](#API_ListJournalRecords_RequestSyntax) **   <a name="devopsagent-ListJournalRecords-request-limit"></a>
Maximum number of records to return in a single response (1-100, default: 100)
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListJournalRecords_RequestSyntax) **   <a name="devopsagent-ListJournalRecords-request-nextToken"></a>
Token for retrieving the next page of results
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [order](#API_ListJournalRecords_RequestSyntax) **   <a name="devopsagent-ListJournalRecords-request-order"></a>
Sort order for the records based on timestamp (default: DESC)
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** [recordType](#API_ListJournalRecords_RequestSyntax) **   <a name="devopsagent-ListJournalRecords-request-recordType"></a>
Filter records by type (empty string returns all types)
Type: String
Required: No

## Response Syntax
<a name="API_ListJournalRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "records": [
      {
         "agentSpaceId": "string",
         "content": JSON value,
         "createdAt": number,
         "executionId": "string",
         "recordId": "string",
         "recordType": "string",
         "userReference": {
            "userId": "string",
            "userType": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListJournalRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListJournalRecords_ResponseSyntax) **   <a name="devopsagent-ListJournalRecords-response-nextToken"></a>
Token for retrieving the next page of results, if more results are available
Type: String

 ** [records](#API_ListJournalRecords_ResponseSyntax) **   <a name="devopsagent-ListJournalRecords-response-records"></a>
List of journal records matching the request criteria
Type: Array of [JournalRecord](API_JournalRecord.md) objects

## Errors
<a name="API_ListJournalRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListJournalRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/ListJournalRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ListJournalRecords)
