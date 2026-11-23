---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListProjects.html
---

# ListProjects

Lists the account's projects. Results are paginated: when the response includes `nextToken`, pass it in the next request to fetch the following page. Page size is 1-100, default 20. By default every project is returned regardless of status; set `statusFilter` to list only active or only archived projects.

## Request Syntax
<a name="API_ListProjects_RequestSyntax"></a>

```
GET /projects?maxResults={{maxResults}}&nextToken={{nextToken}}&statusFilter={{statusFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProjects_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListProjects_RequestSyntax) **   <a name="bedrock-ListProjects-request-uri-maxResults"></a>
The maximum number of projects to return in one response, from 1 to 100. The default is 20.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListProjects_RequestSyntax) **   <a name="bedrock-ListProjects-request-uri-nextToken"></a>
Continuation token from a previous ListProjects response.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [statusFilter](#API_ListProjects_RequestSyntax) **   <a name="bedrock-ListProjects-request-uri-statusFilter"></a>
Returns only the projects in this lifecycle status. When absent, no status filtering is applied and every project is returned. New lifecycle states extend the `ProjectStatus` enum, and with it this filter, compatibly.
Valid Values: `active | archived`

## Request Body
<a name="API_ListProjects_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProjects_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "projectSummaries": [
      {
         "archivedAt": "string",
         "arn": "string",
         "createdAt": "string",
         "dataRetention": {
            "mode": "string"
         },
         "id": "string",
         "name": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListProjects_ResponseSyntax) **   <a name="bedrock-ListProjects-response-nextToken"></a>
Continuation token; present only when more results exist. Pass it in the next request to fetch the following page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [projectSummaries](#API_ListProjects_ResponseSyntax) **   <a name="bedrock-ListProjects-response-projectSummaries"></a>
The projects returned for this page, including their details and data retention settings.
Type: Array of [ProjectSummary](API_ProjectSummary.md) objects

## Errors
<a name="API_ListProjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ListProjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListProjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListProjects)
