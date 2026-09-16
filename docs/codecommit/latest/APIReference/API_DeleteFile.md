---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteFile.html
---

# DeleteFile
<a name="API_DeleteFile"></a>

Deletes a specified file from a specified branch. A commit is created on the branch that contains the revision. The file still exists in the commits earlier to the commit that contains the deletion.

## Request Syntax
<a name="API_DeleteFile_RequestSyntax"></a>

```
{
   "branchName": "{{string}}",
   "commitMessage": "{{string}}",
   "email": "{{string}}",
   "filePath": "{{string}}",
   "keepEmptyFolders": {{boolean}},
   "name": "{{string}}",
   "parentCommitId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [branchName](#API_DeleteFile_RequestSyntax) **   <a name="CodeCommit-DeleteFile-request-branchName"></a>
The name of the branch where the commit that deletes the file is made.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [commitMessage](#API_DeleteFile_RequestSyntax) **   <a name="CodeCommit-DeleteFile-request-commitMessage"></a>
The commit message you want to include as part of deleting the file. Commit messages are limited to 256 KB. If no message is specified, a default message is used.
Type: String
Required: No

 ** [email](#API_DeleteFile_RequestSyntax) **   <a name="CodeCommit-DeleteFile-request-email"></a>
The email address for the commit that deletes the file. If no email address is specified, the email address is left blank.
Type: String
Required: No

 ** [filePath](#API_DeleteFile_RequestSyntax) **   <a name="CodeCommit-DeleteFile-request-filePath"></a>
The fully qualified path to the file that to be deleted, including the full name and extension of that file. For example, /examples/file.md is a fully qualified path to a file named file.md in a folder named examples.
Type: String
Required: Yes

 ** [keepEmptyFolders](#API_DeleteFile_RequestSyntax) **   <a name="CodeCommit-DeleteFile-request-keepEmptyFolders"></a>
If a file is the only object in the folder or directory, specifies whether to delete the folder or directory that contains the file. By default, empty folders are deleted. This includes empty folders that are part of the directory structure. For example, if the path to a file is dir1/dir2/dir3/dir4, and dir2 and dir3 are empty, deleting the last file in dir4 also deletes the empty folders dir4, dir3, and dir2.
Type: Boolean
Required: No

 ** [name](#API_DeleteFile_RequestSyntax) **   <a name="CodeCommit-DeleteFile-request-name"></a>
The name of the author of the commit that deletes the file. If no name is specified, the user's ARN is used as the author name and committer name.
Type: String
Required: No

 ** [parentCommitId](#API_DeleteFile_RequestSyntax) **   <a name="CodeCommit-DeleteFile-request-parentCommitId"></a>
The ID of the commit that is the tip of the branch where you want to create the commit that deletes the file. This must be the HEAD commit for the branch. The commit that deletes the file is created from this commit ID.
Type: String
Required: Yes

 ** [repositoryName](#API_DeleteFile_RequestSyntax) **   <a name="CodeCommit-DeleteFile-request-repositoryName"></a>
The name of the repository that contains the file to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteFile_ResponseSyntax"></a>

```
{
   "blobId": "string",
   "commitId": "string",
   "filePath": "string",
   "treeId": "string"
}
```

## Response Elements
<a name="API_DeleteFile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [blobId](#API_DeleteFile_ResponseSyntax) **   <a name="CodeCommit-DeleteFile-response-blobId"></a>
The blob ID removed from the tree as part of deleting the file.
Type: String

 ** [commitId](#API_DeleteFile_ResponseSyntax) **   <a name="CodeCommit-DeleteFile-response-commitId"></a>
The full commit ID of the commit that contains the change that deletes the file.
Type: String

 ** [filePath](#API_DeleteFile_ResponseSyntax) **   <a name="CodeCommit-DeleteFile-response-filePath"></a>
The fully qualified path to the file to be deleted, including the full name and extension of that file.
Type: String

 ** [treeId](#API_DeleteFile_ResponseSyntax) **   <a name="CodeCommit-DeleteFile-response-treeId"></a>
The full SHA-1 pointer of the tree information for the commit that contains the delete file change.
Type: String

## Errors
<a name="API_DeleteFile_Errors"></a>

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

 ** CommitMessageLengthExceededException **
The commit message is too long. Provide a shorter string.
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

 ** FileDoesNotExistException **
The specified file does not exist. Verify that you have used the correct file name, full path, and extension.
HTTP Status Code: 400

 ** InvalidBranchNameException **
The specified reference name is not valid.
HTTP Status Code: 400

 ** InvalidEmailException **
The specified email address either contains one or more characters that are not allowed, or it exceeds the maximum number of characters allowed for an email address.
HTTP Status Code: 400

 ** InvalidParentCommitIdException **
The parent commit ID is not valid. The commit ID cannot be empty, and must match the head commit ID for the branch of the repository where you want to add or update a file.
HTTP Status Code: 400

 ** InvalidPathException **
The specified path is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** NameLengthExceededException **
The user name is not valid because it has exceeded the character limit for author names.
HTTP Status Code: 400

 ** ParentCommitDoesNotExistException **
The parent commit ID is not valid because it does not exist. The specified parent commit ID does not exist in the specified branch of the repository.
HTTP Status Code: 400

 ** ParentCommitIdOutdatedException **
The file could not be added because the provided parent commit ID is not the current tip of the specified branch. To view the full commit ID of the current head of the branch, use [GetBranch](API_GetBranch.md).
HTTP Status Code: 400

 ** ParentCommitIdRequiredException **
A parent commit ID is required. To view the full commit ID of a branch in a repository, use [GetBranch](API_GetBranch.md) or a Git command (for example, git pull or git log).
HTTP Status Code: 400

 ** PathRequiredException **
The folderPath for a location cannot be null.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_DeleteFile_Examples"></a>

### Example
<a name="API_DeleteFile_Example_1"></a>

This example illustrates one usage of DeleteFile.

#### Sample Request
<a name="API_DeleteFile_Example_1_Request"></a>

```
POST / HTTP/1.1
    Host: codecommit.us-east-1.amazonaws.com
    Accept-Encoding: identity
    Content-Length: 182
    X-Amz-Target: CodeCommit_20150413.DeleteFile
    X-Amz-Date: 20180914T223454Z
    User-Agent: aws-cli/1.15.9 Python/2.7.11 Darwin/16.7.0 botocore/1.10.9
    Content-Type: application/x-amz-json-1.1
    Authorization: AWS4-HMAC-SHA256 Credential=AKIAEXAMPLE/20180914/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=0be88b13EXAMPLE

{
      "branchName": "main",
      "repositoryName": "MyDemoRepo",
      "parentCommitId": "c5709475EXAMPLE",
      "filePath": "README.md"
}
```

#### Sample Response
<a name="API_DeleteFile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
    x-amzn-RequestId: 66c7bf89-EXAMPLE
    Content-Type: application/x-amz-json-1.1
    Content-Length: 182
    Date: Fri, 14 Sep 2018 22:34:56 GMT
    Connection: keep-alive

{
    "blobId":"559b44fEXAMPLE",
    "commitId":"353cf655EXAMPLE",
    "filePath":"README.md",
    "treeId":"6bc824cEXAMPLE"
}
```

## See Also
<a name="API_DeleteFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/DeleteFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DeleteFile)
