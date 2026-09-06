---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSourceRepositoryBranches.html
---

# ListSourceRepositoryBranches
<a name="API_ListSourceRepositoryBranches"></a>

Retrieves a list of branches in a specified source repository.

## Request Syntax
<a name="API_ListSourceRepositoryBranches_RequestSyntax"></a>

```
POST /v1/spaces/{{spaceName}}/projects/{{projectName}}/sourceRepositories/{{sourceRepositoryName}}/branches HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSourceRepositoryBranches_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectName](#API_ListSourceRepositoryBranches_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositoryBranches-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [sourceRepositoryName](#API_ListSourceRepositoryBranches_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositoryBranches-request-uri-sourceRepositoryName"></a>
The name of the source repository.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`
Required: Yes

 ** [spaceName](#API_ListSourceRepositoryBranches_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositoryBranches-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_ListSourceRepositoryBranches_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListSourceRepositoryBranches_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositoryBranches-request-maxResults"></a>
The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a `NextToken` element, which you can use to obtain additional results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListSourceRepositoryBranches_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositoryBranches-request-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

## Response Syntax
<a name="API_ListSourceRepositoryBranches_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "headCommitId": "string",
         "lastUpdatedTime": "string",
         "name": "string",
         "ref": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSourceRepositoryBranches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListSourceRepositoryBranches_ResponseSyntax) **   <a name="codecatalyst-ListSourceRepositoryBranches-response-items"></a>
Information about the source branches.
Type: Array of [ListSourceRepositoryBranchesItem](API_ListSourceRepositoryBranchesItem.md) objects

 ** [nextToken](#API_ListSourceRepositoryBranches_ResponseSyntax) **   <a name="codecatalyst-ListSourceRepositoryBranches-response-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String

## Errors
<a name="API_ListSourceRepositoryBranches_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## See Also
<a name="API_ListSourceRepositoryBranches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ListSourceRepositoryBranches)
