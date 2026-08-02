---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositories.html
---

# ListRepositories
<a name="API_ListRepositories"></a>

 Returns a list of [RepositorySummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html) objects. Each `RepositorySummary` contains information about a repository in the specified AWS account and that matches the input parameters.

## Request Syntax
<a name="API_ListRepositories_RequestSyntax"></a>

```
POST /v1/repositories?max-results={{maxResults}}&next-token={{nextToken}}&repository-prefix={{repositoryPrefix}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRepositories_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListRepositories_RequestSyntax) **   <a name="codeartifact-ListRepositories-request-uri-maxResults"></a>
 The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListRepositories_RequestSyntax) **   <a name="codeartifact-ListRepositories-request-uri-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [repositoryPrefix](#API_ListRepositories_RequestSyntax) **   <a name="codeartifact-ListRepositories-request-uri-repositoryPrefix"></a>
 A prefix used to filter returned repositories. Only repositories with names that start with `repositoryPrefix` are returned.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`

## Request Body
<a name="API_ListRepositories_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRepositories_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "repositories": [
      {
         "administratorAccount": "string",
         "arn": "string",
         "createdTime": number,
         "description": "string",
         "domainName": "string",
         "domainOwner": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRepositories_ResponseSyntax) **   <a name="codeartifact-ListRepositories-response-nextToken"></a>
 If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [repositories](#API_ListRepositories_ResponseSyntax) **   <a name="codeartifact-ListRepositories-response-repositories"></a>
 The returned list of [RepositorySummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html) objects.
Type: Array of [RepositorySummary](API_RepositorySummary.md) objects

## Errors
<a name="API_ListRepositories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The operation did not succeed because of an unauthorized access attempt.
HTTP Status Code: 403

 ** InternalServerException **
 The operation did not succeed because of an error that occurred inside AWS CodeArtifact.
HTTP Status Code: 500

 ** ThrottlingException **
 The operation did not succeed because too many requests are sent to the service.
 ** retryAfterSeconds **
 The time period, in seconds, to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
 The operation did not succeed because a parameter in the request was sent with an invalid value.
 ** reason **

HTTP Status Code: 400

## See Also
<a name="API_ListRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/ListRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/ListRepositories)
