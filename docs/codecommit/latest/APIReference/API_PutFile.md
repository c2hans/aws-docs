---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PutFile.html
---

# PutFile
<a name="API_PutFile"></a>

Adds or updates a file in a branch in an AWS CodeCommit repository, and generates a commit for the addition in the specified branch.

## Request Syntax
<a name="API_PutFile_RequestSyntax"></a>

```
{
   "branchName": "{{string}}",
   "commitMessage": "{{string}}",
   "email": "{{string}}",
   "fileContent": {{blob}},
   "fileMode": "{{string}}",
   "filePath": "{{string}}",
   "name": "{{string}}",
   "parentCommitId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutFile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [branchName](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-branchName"></a>
The name of the branch where you want to add or update the file. If this is an empty repository, this branch is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [commitMessage](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-commitMessage"></a>
A message about why this file was added or updated. Although it is optional, a message makes the commit history for your repository more useful.
Type: String
Required: No

 ** [email](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-email"></a>
An email address for the person adding or updating the file.
Type: String
Required: No

 ** [fileContent](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-fileContent"></a>
The content of the file, in binary object format.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 6291456.
Required: Yes

 ** [fileMode](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-fileMode"></a>
The file mode permissions of the blob. Valid file mode permissions are listed here.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

 ** [filePath](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-filePath"></a>
The name of the file you want to add or update, including the relative path to the file in the repository.
If the path does not currently exist in the repository, the path is created as part of adding the file.
Type: String
Required: Yes

 ** [name](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-name"></a>
The name of the person adding or updating the file. Although it is optional, a name makes the commit history for your repository more useful.
Type: String
Required: No

 ** [parentCommitId](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-parentCommitId"></a>
The full commit ID of the head commit in the branch where you want to add or update the file. If this is an empty repository, no commit ID is required. If this is not an empty repository, a commit ID is required.
The commit ID must match the ID of the head commit at the time of the operation. Otherwise, an error occurs, and the file is not added or updated.
Type: String
Required: No

 ** [repositoryName](#API_PutFile_RequestSyntax) **   <a name="CodeCommit-PutFile-request-repositoryName"></a>
The name of the repository where you want to add or update the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_PutFile_ResponseSyntax"></a>

```
{
   "blobId": "string",
   "commitId": "string",
   "treeId": "string"
}
```

## Response Elements
<a name="API_PutFile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [blobId](#API_PutFile_ResponseSyntax) **   <a name="CodeCommit-PutFile-response-blobId"></a>
The ID of the blob, which is its SHA-1 pointer.
Type: String

 ** [commitId](#API_PutFile_ResponseSyntax) **   <a name="CodeCommit-PutFile-response-commitId"></a>
The full SHA ID of the commit that contains this file change.
Type: String

 ** [treeId](#API_PutFile_ResponseSyntax) **   <a name="CodeCommit-PutFile-response-treeId"></a>
The full SHA-1 pointer of the tree information for the commit that contains this file change.
Type: String

## Errors
<a name="API_PutFile_Errors"></a>

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

 ** DirectoryNameConflictsWithFileNameException **
A file cannot be added to the repository because the specified path name has the same name as a file that already exists in this repository. Either provide a different name for the file, or specify a different path for the file.
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

 ** FileContentRequiredException **
The file cannot be added because it is empty. Empty files cannot be added to the repository with this API.
HTTP Status Code: 400

 ** FileContentSizeLimitExceededException **
The file cannot be added because it is too large. The maximum file size is 6 MB, and the combined file content change size is 7 MB. Consider making these changes using a Git client.
HTTP Status Code: 400

 ** FileNameConflictsWithDirectoryNameException **
A file cannot be added to the repository because the specified file name has the same name as a directory in this repository. Either provide another name for the file, or add the file in a directory that does not match the file name.
HTTP Status Code: 400

 ** FilePathConflictsWithSubmodulePathException **
The commit cannot be created because a specified file path points to a submodule. Verify that the destination files have valid file paths that do not point to a submodule.
HTTP Status Code: 400

 ** FolderContentSizeLimitExceededException **
The commit cannot be created because at least one of the overall changes in the commit results in a folder whose contents exceed the limit of 6 MB. Either reduce the number and size of your changes, or split the changes across multiple folders.
HTTP Status Code: 400

 ** InvalidBranchNameException **
The specified reference name is not valid.
HTTP Status Code: 400

 ** InvalidDeletionParameterException **
The specified deletion parameter is not valid.
HTTP Status Code: 400

 ** InvalidEmailException **
The specified email address either contains one or more characters that are not allowed, or it exceeds the maximum number of characters allowed for an email address.
HTTP Status Code: 400

 ** InvalidFileModeException **
The specified file mode permission is not valid. For a list of valid file mode permissions, see [PutFile](#API_PutFile).
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

 ** SameFileContentException **
The file was not added or updated because the content of the file is exactly the same as the content of that file in the repository and branch that you specified.
HTTP Status Code: 400

## Examples
<a name="API_PutFile_Examples"></a>

### Example
<a name="API_PutFile_Example_1"></a>

This example illustrates one usage of PutFile.

#### Sample Request
<a name="API_PutFile_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.PutFile
X-Amz-Date: 20180126T224019Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "branchName": "MyFeatureBranch",
   "commitMessage": "I'm adding this file to fix a bug Mary found.",
   "email": "maria_garcia@example.com",
   "fileContent": QSBCaW5hcnkgTGFyToEXAMPLE=,
   "fileMode": "NORMAL",
   "filePath": "ExampleSolution.py",
   "name": "Maria Garcia",
   "parentCommitId": "4c925148EXAMPLE",
   "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_PutFile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Fri, 26 Jan 2018 22:40:19 GMT

{
   "blobId": "2eb4af3bEXAMPLE",
   "commitId": "317f8570EXAMPLE",
   "treeId": "347a3408EXAMPLE"
}
```

## See Also
<a name="API_PutFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/PutFile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/PutFile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PutFile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/PutFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PutFile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/PutFile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/PutFile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/PutFile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/PutFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PutFile)
