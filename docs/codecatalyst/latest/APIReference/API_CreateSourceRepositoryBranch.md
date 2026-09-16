---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateSourceRepositoryBranch.html
---

# CreateSourceRepositoryBranch
<a name="API_CreateSourceRepositoryBranch"></a>

Creates a branch in a specified source repository in Amazon CodeCatalyst.

**Note**
This API only creates a branch in a source repository hosted in Amazon CodeCatalyst. You cannot use this API to create a branch in a linked repository.

## Request Syntax
<a name="API_CreateSourceRepositoryBranch_RequestSyntax"></a>

```
PUT /v1/spaces/{{spaceName}}/projects/{{projectName}}/sourceRepositories/{{sourceRepositoryName}}/branches/{{name}} HTTP/1.1
Content-type: application/json

{
   "headCommitId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSourceRepositoryBranch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateSourceRepositoryBranch_RequestSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-request-uri-name"></a>
The name for the branch you're creating.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [projectName](#API_CreateSourceRepositoryBranch_RequestSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [sourceRepositoryName](#API_CreateSourceRepositoryBranch_RequestSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-request-uri-sourceRepositoryName"></a>
The name of the repository where you want to create a branch.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`
Required: Yes

 ** [spaceName](#API_CreateSourceRepositoryBranch_RequestSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_CreateSourceRepositoryBranch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [headCommitId](#API_CreateSourceRepositoryBranch_RequestSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-request-headCommitId"></a>
The commit ID in an existing branch from which you want to create the new branch.
Type: String
Required: No

## Response Syntax
<a name="API_CreateSourceRepositoryBranch_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "headCommitId": "string",
   "lastUpdatedTime": "string",
   "name": "string",
   "ref": "string"
}
```

## Response Elements
<a name="API_CreateSourceRepositoryBranch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [headCommitId](#API_CreateSourceRepositoryBranch_ResponseSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-response-headCommitId"></a>
The commit ID of the tip of the newly created branch.
Type: String

 ** [lastUpdatedTime](#API_CreateSourceRepositoryBranch_ResponseSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-response-lastUpdatedTime"></a>
The time the branch was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp

 ** [name](#API_CreateSourceRepositoryBranch_ResponseSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-response-name"></a>
The name of the newly created branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [ref](#API_CreateSourceRepositoryBranch_ResponseSyntax) **   <a name="codecatalyst-CreateSourceRepositoryBranch-response-ref"></a>
The Git reference name of the branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateSourceRepositoryBranch_Errors"></a>

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
<a name="API_CreateSourceRepositoryBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/CreateSourceRepositoryBranch)
