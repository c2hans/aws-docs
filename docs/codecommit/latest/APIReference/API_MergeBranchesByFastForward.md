---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergeBranchesByFastForward.html
---

# MergeBranchesByFastForward
<a name="API_MergeBranchesByFastForward"></a>

Merges two branches using the fast-forward merge strategy.

## Request Syntax
<a name="API_MergeBranchesByFastForward_RequestSyntax"></a>

```
{
   "destinationCommitSpecifier": "{{string}}",
   "repositoryName": "{{string}}",
   "sourceCommitSpecifier": "{{string}}",
   "targetBranch": "{{string}}"
}
```

## Request Parameters
<a name="API_MergeBranchesByFastForward_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [destinationCommitSpecifier](#API_MergeBranchesByFastForward_RequestSyntax) **   <a name="CodeCommit-MergeBranchesByFastForward-request-destinationCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

 ** [repositoryName](#API_MergeBranchesByFastForward_RequestSyntax) **   <a name="CodeCommit-MergeBranchesByFastForward-request-repositoryName"></a>
The name of the repository where you want to merge two branches.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [sourceCommitSpecifier](#API_MergeBranchesByFastForward_RequestSyntax) **   <a name="CodeCommit-MergeBranchesByFastForward-request-sourceCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

 ** [targetBranch](#API_MergeBranchesByFastForward_RequestSyntax) **   <a name="CodeCommit-MergeBranchesByFastForward-request-targetBranch"></a>
The branch where the merge is applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_MergeBranchesByFastForward_ResponseSyntax"></a>

```
{
   "commitId": "string",
   "treeId": "string"
}
```

## Response Elements
<a name="API_MergeBranchesByFastForward_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commitId](#API_MergeBranchesByFastForward_ResponseSyntax) **   <a name="CodeCommit-MergeBranchesByFastForward-response-commitId"></a>
The commit ID of the merge in the destination or target branch.
Type: String

 ** [treeId](#API_MergeBranchesByFastForward_ResponseSyntax) **   <a name="CodeCommit-MergeBranchesByFastForward-response-treeId"></a>
The tree ID of the merge in the destination or target branch.
Type: String

## Errors
<a name="API_MergeBranchesByFastForward_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BranchDoesNotExistException **
The specified branch does not exist.
HTTP Status Code: 400

 ** BranchNameIsTagNameException **
The specified branch name is not valid because it is a tag name. Enter the name of a branch in the repository. For a list of valid branch names, use [ListBranches](API_ListBranches.md).
HTTP Status Code: 400

 ** BranchNameRequiredException **
A branch name is required, but was not specified.
HTTP Status Code: 400

 ** CommitDoesNotExistException **
The specified commit does not exist or no commit was specified, and the specified repository has no default branch.
HTTP Status Code: 400

 ** CommitRequiredException **
A commit was not specified.
HTTP Status Code: 400

 ** ConcurrentReferenceUpdateException **
The merge cannot be completed because the target branch has been modified. Another user might have modified the target branch while the merge was in progress. Wait a few minutes, and then try again.
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

 ** InvalidCommitException **
The specified commit is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** InvalidTargetBranchException **
The specified target branch is not valid.
HTTP Status Code: 400

 ** ManualMergeRequiredException **
The pull request cannot be merged automatically into the destination branch. You must manually merge the branches and resolve any conflicts.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

 ** TipsDivergenceExceededException **
The divergence between the tips of the provided commit specifiers is too great to determine whether there might be any merge conflicts. Locally compare the specifiers using `git diff` or a diff tool.
HTTP Status Code: 400

## Examples
<a name="API_MergeBranchesByFastForward_Examples"></a>

### Example
<a name="API_MergeBranchesByFastForward_Example_1"></a>

This example illustrates one usage of MergeBranchesByFastForward.

#### Sample Request
<a name="API_MergeBranchesByFastForward_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 226
X-Amz-Target: CodeCommit_20150413.MergeBranchesByFastForward
X-Amz-Date: 20190428T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "destinationCommitSpecifier": "bugfix-bug1234",
  "sourceCommitSpecifier": "main",
  "targetBranch": "main-preprod"
}
```

#### Sample Response
<a name="API_MergeBranchesByFastForward_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 1681
Date: Sun, 28 Apr 2019 22:43:13 GMT

{
    "commitId": "4f178133EXAMPLE",
    "treeId": "389765daEXAMPLE"
}
```

## See Also
<a name="API_MergeBranchesByFastForward_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/MergeBranchesByFastForward)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/MergeBranchesByFastForward)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
