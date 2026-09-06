---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListActs.html
---

# ListActs
<a name="API_ListActs"></a>

Lists all acts within a specific session with their current status and execution details.

## Request Syntax
<a name="API_ListActs_RequestSyntax"></a>

```
POST /workflow-definitions/{{workflowDefinitionName}}/acts?maxResults={{maxResults}}&nextToken={{nextToken}}&sessionId={{sessionId}}&workflowRunId={{workflowRunId}} HTTP/1.1
Content-type: application/json

{
   "sortOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListActs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListActs_RequestSyntax) **   <a name="novaact-ListActs-request-uri-maxResults"></a>
The maximum number of acts to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListActs_RequestSyntax) **   <a name="novaact-ListActs-request-uri-nextToken"></a>
The token for retrieving the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [sessionId](#API_ListActs_RequestSyntax) **   <a name="novaact-ListActs-request-uri-sessionId"></a>
The unique identifier of the session to list acts for.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [workflowDefinitionName](#API_ListActs_RequestSyntax) **   <a name="novaact-ListActs-request-uri-workflowDefinitionName"></a>
The name of the workflow definition containing the session.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]{1,40}`
Required: Yes

 ** [workflowRunId](#API_ListActs_RequestSyntax) **   <a name="novaact-ListActs-request-uri-workflowRunId"></a>
The unique identifier of the workflow run containing the session.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Request Body
<a name="API_ListActs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sortOrder](#API_ListActs_RequestSyntax) **   <a name="novaact-ListActs-request-sortOrder"></a>
The sort order for the returned acts (ascending or descending).
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListActs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actSummaries": [
      {
         "actId": "string",
         "endedAt": "string",
         "sessionId": "string",
         "startedAt": "string",
         "status": "string",
         "traceLocation": {
            "location": "string",
            "locationType": "string"
         },
         "workflowRunId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListActs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actSummaries](#API_ListActs_ResponseSyntax) **   <a name="novaact-ListActs-response-actSummaries"></a>
A list of summary information for acts in the session.
Type: Array of [ActSummary](API_ActSummary.md) objects

 ** [nextToken](#API_ListActs_ResponseSyntax) **   <a name="novaact-ListActs-response-nextToken"></a>
The token for retrieving the next page of results, if available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

## Errors
<a name="API_ListActs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient permissions to perform this action.
 ** message **
You don't have sufficient permissions to perform this action. Verify your IAM permissions and try again.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
The requested operation conflicts with the current state of the resource.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 409

 [InternalServerException](API_InternalServerException.md)
An internal server error occurred. Please try again later.
 ** message **
The service encountered an internal error. Try again later.
 ** reason **
The reason for the internal server error.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The requested resource was not found.
 ** message **
The specified resource was not found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was throttled due to too many requests. Please try again later.
 ** message **
The request was denied due to request throttling.
 ** quotaCode **
The quota code related to the throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the throttled request.
 ** serviceCode **
The service code where throttling occurred.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input parameters for the request are invalid.
 ** fieldList **
The list of fields that failed validation.
 ** message **
The input fails to satisfy the constraints specified by the service.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListActs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/nova-act-2025-08-22/ListActs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/nova-act-2025-08-22/ListActs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/ListActs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/nova-act-2025-08-22/ListActs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/ListActs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/nova-act-2025-08-22/ListActs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/nova-act-2025-08-22/ListActs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/nova-act-2025-08-22/ListActs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/nova-act-2025-08-22/ListActs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ListActs)
