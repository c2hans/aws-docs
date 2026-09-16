---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateBranch.html
---

# CreateBranch
<a name="API_CreateBranch"></a>

Creates a branch in a repository and points the branch to a commit.

**Note**
Calling the create branch operation does not set a repository's default branch. To do this, call the update default branch operation.

## Request Syntax
<a name="API_CreateBranch_RequestSyntax"></a>

```
{
   "branchName": "{{string}}",
   "commitId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateBranch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [branchName](#API_CreateBranch_RequestSyntax) **   <a name="CodeCommit-CreateBranch-request-branchName"></a>
The name of the new branch to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [commitId](#API_CreateBranch_RequestSyntax) **   <a name="CodeCommit-CreateBranch-request-commitId"></a>
The ID of the commit to point the new branch to.
Type: String
Required: Yes

 ** [repositoryName](#API_CreateBranch_RequestSyntax) **   <a name="CodeCommit-CreateBranch-request-repositoryName"></a>
The name of the repository in which you want to create the new branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Elements
<a name="API_CreateBranch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateBranch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BranchNameExistsException **
Cannot create the branch with the specified name because the commit conflicts with an existing branch with the same name. Branch names must be unique.
HTTP Status Code: 400

 ** BranchNameRequiredException **
A branch name is required, but was not specified.
HTTP Status Code: 400

 ** CommitDoesNotExistException **
The specified commit does not exist or no commit was specified, and the specified repository has no default branch.
HTTP Status Code: 400

 ** CommitIdRequiredException **
A commit ID was not specified.
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

 ** InvalidCommitIdException **
The specified commit ID is not valid.
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
<a name="API_CreateBranch_Examples"></a>

### Example
<a name="API_CreateBranch_Example_1"></a>

This example illustrates one usage of CreateBranch.

#### Sample Request
<a name="API_CreateBranch_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 113
X-Amz-Target: CodeCommit_20150413.CreateBranch
X-Amz-Date: 20151028T221237Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "commitId": "317f8570EXAMPLE",
  "repositoryName": "MyDemoRepo",
  "branchName": "MyNewBranch"
}
```

#### Sample Response
<a name="API_CreateBranch_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Wed, 28 Oct 2015 22:12:40 GMT
```

## See Also
<a name="API_CreateBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/CreateBranch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/CreateBranch)
