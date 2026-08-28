---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteBranch.html
---

# DeleteBranch
<a name="API_DeleteBranch"></a>

Deletes a branch from a repository, unless that branch is the default branch for the repository.

## Request Syntax
<a name="API_DeleteBranch_RequestSyntax"></a>

```
{
   "branchName": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteBranch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [branchName](#API_DeleteBranch_RequestSyntax) **   <a name="CodeCommit-DeleteBranch-request-branchName"></a>
The name of the branch to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [repositoryName](#API_DeleteBranch_RequestSyntax) **   <a name="CodeCommit-DeleteBranch-request-repositoryName"></a>
The name of the repository that contains the branch to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteBranch_ResponseSyntax"></a>

```
{
   "deletedBranch": {
      "branchName": "string",
      "commitId": "string"
   }
}
```

## Response Elements
<a name="API_DeleteBranch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deletedBranch](#API_DeleteBranch_ResponseSyntax) **   <a name="CodeCommit-DeleteBranch-response-deletedBranch"></a>
Information about the branch deleted by the operation, including the branch name and the commit ID that was the tip of the branch.
Type: [BranchInfo](API_BranchInfo.md) object

## Errors
<a name="API_DeleteBranch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BranchNameRequiredException **
A branch name is required, but was not specified.
HTTP Status Code: 400

 ** DefaultBranchCannotBeDeletedException **
The specified branch is the default branch for the repository, and cannot be deleted. To delete this branch, you must first set another branch as the default branch.
HTTP Status Code: 400

 ** EncryptionIntegrityChecksFailedException **
An encryption integrity check failed.
HTTP Status Code: 500

 ** EncryptionKeyAccessDeniedException **
An encryption key could not be accessed.
HTTP Status Code: 400

 ** EncryptionKeyDisabledException **
The encryption key is disabled.
HTTP Status Code: 400

 ** EncryptionKeyNotFoundException **
No encryption key was found.
HTTP Status Code: 400

 ** EncryptionKeyUnavailableException **
The encryption key is not available.
HTTP Status Code: 400

 ** InvalidBranchNameException **
The specified reference name is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_DeleteBranch_Examples"></a>

### Example
<a name="API_DeleteBranch_Example_1"></a>

This example illustrates one usage of DeleteBranch.

#### Sample Request
<a name="API_DeleteBranch_Example_1_Request"></a>

```
HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 57
X-Amz-Target: CodeCommit_20150413.DeleteBranch
X-Amz-Date: 20151028T224659Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "branchName": "MyNewBranch"
}
```

#### Sample Response
<a name="API_DeleteBranch_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 88
Date: Wed, 28 Oct 2015 22:47:03 GMT

{
  "deletedBranch": {
    "branchName": "MyNewBranch",
    "commitId": "317f8570EXAMPLE"
  }
}
```

## See Also
<a name="API_DeleteBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/DeleteBranch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DeleteBranch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
