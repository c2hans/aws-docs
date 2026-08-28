---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSourceRepositories.html
---

# ListSourceRepositories
<a name="API_ListSourceRepositories"></a>

Retrieves a list of source repositories in a project.

## Request Syntax
<a name="API_ListSourceRepositories_RequestSyntax"></a>

```
POST /v1/spaces/{{spaceName}}/projects/{{projectName}}/sourceRepositories HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSourceRepositories_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectName](#API_ListSourceRepositories_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositories-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_ListSourceRepositories_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositories-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_ListSourceRepositories_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListSourceRepositories_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositories-request-maxResults"></a>
The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a `NextToken` element, which you can use to obtain additional results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListSourceRepositories_RequestSyntax) **   <a name="codecatalyst-ListSourceRepositories-request-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

## Response Syntax
<a name="API_ListSourceRepositories_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdTime": "string",
         "description": "string",
         "id": "string",
         "lastUpdatedTime": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSourceRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListSourceRepositories_ResponseSyntax) **   <a name="codecatalyst-ListSourceRepositories-response-items"></a>
Information about the source repositories.
Type: Array of [ListSourceRepositoriesItem](API_ListSourceRepositoriesItem.md) objects

 ** [nextToken](#API_ListSourceRepositories_ResponseSyntax) **   <a name="codecatalyst-ListSourceRepositories-response-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String

## Errors
<a name="API_ListSourceRepositories_Errors"></a>

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
<a name="API_ListSourceRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/ListSourceRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ListSourceRepositories)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
