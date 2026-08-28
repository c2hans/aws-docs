---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListAnalysisLogExports.html
---

# ListAnalysisLogExports
<a name="API_ListAnalysisLogExports"></a>

Lists analysis log exports, sorted by the most recent export. Results are paginated. Use the `nextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_ListAnalysisLogExports_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/analysislogexports?analysisIdentifier={{analysisIdentifier}}&maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAnalysisLogExports_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analysisIdentifier](#API_ListAnalysisLogExports_RequestSyntax) **   <a name="API-ListAnalysisLogExports-request-uri-analysisIdentifier"></a>
A filter on the unique identifier of the protected query that the analysis logs were exported for.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [maxResults](#API_ListAnalysisLogExports_RequestSyntax) **   <a name="API-ListAnalysisLogExports-request-uri-maxResults"></a>
The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [membershipIdentifier](#API_ListAnalysisLogExports_RequestSyntax) **   <a name="API-ListAnalysisLogExports-request-uri-membershipIdentifier"></a>
A unique identifier for the membership to list analysis log exports for. Currently accepts the membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [nextToken](#API_ListAnalysisLogExports_RequestSyntax) **   <a name="API-ListAnalysisLogExports-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [status](#API_ListAnalysisLogExports_RequestSyntax) **   <a name="API-ListAnalysisLogExports-request-uri-status"></a>
A filter on the status of the analysis log export.
Valid Values: `IN_PROGRESS | SUCCESS | FAILED`

## Request Body
<a name="API_ListAnalysisLogExports_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAnalysisLogExports_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analysisLogExports": [
      {
         "analysisId": "string",
         "analysisLogExportId": "string",
         "analysisType": "string",
         "createTime": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnalysisLogExports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisLogExports](#API_ListAnalysisLogExports_ResponseSyntax) **   <a name="API-ListAnalysisLogExports-response-analysisLogExports"></a>
A list of analysis log exports.
Type: Array of [AnalysisLogExportSummary](API_AnalysisLogExportSummary.md) objects

 ** [nextToken](#API_ListAnalysisLogExports_ResponseSyntax) **   <a name="API-ListAnalysisLogExports-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

## Errors
<a name="API_ListAnalysisLogExports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListAnalysisLogExports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/ListAnalysisLogExports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ListAnalysisLogExports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
