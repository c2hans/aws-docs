---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateSourceControlFromJob.html
---

# UpdateSourceControlFromJob
<a name="API_UpdateSourceControlFromJob"></a>

Synchronizes a job to the source control repository. This operation takes the job artifacts from the AWS Glue internal stores and makes a commit to the remote repository that is configured on the job.

This API supports optional parameters which take in the repository information.

## Request Syntax
<a name="API_UpdateSourceControlFromJob_RequestSyntax"></a>

```
{
   "AuthStrategy": "{{string}}",
   "AuthToken": "{{string}}",
   "BranchName": "{{string}}",
   "CommitId": "{{string}}",
   "Folder": "{{string}}",
   "JobName": "{{string}}",
   "Provider": "{{string}}",
   "RepositoryName": "{{string}}",
   "RepositoryOwner": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSourceControlFromJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthStrategy](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-AuthStrategy"></a>
The type of authentication, which can be an authentication token stored in AWS Secrets Manager, or a personal access token.
Type: String
Valid Values: `PERSONAL_ACCESS_TOKEN | AWS_SECRETS_MANAGER`
Required: No

 ** [AuthToken](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-AuthToken"></a>
The value of the authorization token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [BranchName](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-BranchName"></a>
An optional branch in the remote repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [CommitId](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-CommitId"></a>
A commit ID for a commit in the remote repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Folder](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-Folder"></a>
An optional folder in the remote repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [JobName](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-JobName"></a>
The name of the AWS Glue job to be synchronized to or from the remote repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Provider](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-Provider"></a>
 The provider for the remote repository. Possible values: GITHUB, AWS\_CODE\_COMMIT, GITLAB, BITBUCKET.
Type: String
Valid Values: `GITHUB | GITLAB | BITBUCKET | AWS_CODE_COMMIT`
Required: No

 ** [RepositoryName](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-RepositoryName"></a>
The name of the remote repository that contains the job artifacts. For BitBucket providers, `RepositoryName` should include `WorkspaceName`. Use the format `<WorkspaceName>/<RepositoryName>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [RepositoryOwner](#API_UpdateSourceControlFromJob_RequestSyntax) **   <a name="Glue-UpdateSourceControlFromJob-request-RepositoryOwner"></a>
The owner of the remote repository that contains the job artifacts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_UpdateSourceControlFromJob_ResponseSyntax"></a>

```
{
   "JobName": "string"
}
```

## Response Elements
<a name="API_UpdateSourceControlFromJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobName](#API_UpdateSourceControlFromJob_ResponseSyntax) **   <a name="Glue-UpdateSourceControlFromJob-response-JobName"></a>
The name of the AWS Glue job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_UpdateSourceControlFromJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSourceControlFromJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateSourceControlFromJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateSourceControlFromJob)
