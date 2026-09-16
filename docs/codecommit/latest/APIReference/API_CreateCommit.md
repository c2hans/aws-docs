---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateCommit.html
---

# CreateCommit
<a name="API_CreateCommit"></a>

Creates a commit for a repository on the tip of a specified branch.

## Request Syntax
<a name="API_CreateCommit_RequestSyntax"></a>

```
{
   "authorName": "{{string}}",
   "branchName": "{{string}}",
   "commitMessage": "{{string}}",
   "deleteFiles": [
      {
         "filePath": "{{string}}"
      }
   ],
   "email": "{{string}}",
   "keepEmptyFolders": {{boolean}},
   "parentCommitId": "{{string}}",
   "putFiles": [
      {
         "fileContent": {{blob}},
         "fileMode": "{{string}}",
         "filePath": "{{string}}",
         "sourceFile": {
            "filePath": "{{string}}",
            "isMove": {{boolean}}
         }
      }
   ],
   "repositoryName": "{{string}}",
   "setFileModes": [
      {
         "fileMode": "{{string}}",
         "filePath": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCommit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [authorName](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-authorName"></a>
The name of the author who created the commit. This information is used as both the author and committer for the commit.
Type: String
Required: No

 ** [branchName](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-branchName"></a>
The name of the branch where you create the commit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [commitMessage](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-commitMessage"></a>
The commit message you want to include in the commit. Commit messages are limited to 256 KB. If no message is specified, a default message is used.
Type: String
Required: No

 ** [deleteFiles](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-deleteFiles"></a>
The files to delete in this commit. These files still exist in earlier commits.
Type: Array of [DeleteFileEntry](API_DeleteFileEntry.md) objects
Required: No

 ** [email](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-email"></a>
The email address of the person who created the commit.
Type: String
Required: No

 ** [keepEmptyFolders](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-keepEmptyFolders"></a>
If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a ..gitkeep file is created for empty folders. The default is false.
Type: Boolean
Required: No

 ** [parentCommitId](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-parentCommitId"></a>
The ID of the commit that is the parent of the commit you create. Not required if this is an empty repository.
Type: String
Required: No

 ** [putFiles](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-putFiles"></a>
The files to add or update in this commit.
Type: Array of [PutFileEntry](API_PutFileEntry.md) objects
Required: No

 ** [repositoryName](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-repositoryName"></a>
The name of the repository where you create the commit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [setFileModes](#API_CreateCommit_RequestSyntax) **   <a name="CodeCommit-CreateCommit-request-setFileModes"></a>
The file modes to update for files in this commit.
Type: Array of [SetFileModeEntry](API_SetFileModeEntry.md) objects
Required: No

## Response Syntax
<a name="API_CreateCommit_ResponseSyntax"></a>

```
{
   "commitId": "string",
   "filesAdded": [
      {
         "absolutePath": "string",
         "blobId": "string",
         "fileMode": "string"
      }
   ],
   "filesDeleted": [
      {
         "absolutePath": "string",
         "blobId": "string",
         "fileMode": "string"
      }
   ],
   "filesUpdated": [
      {
         "absolutePath": "string",
         "blobId": "string",
         "fileMode": "string"
      }
   ],
   "treeId": "string"
}
```

## Response Elements
<a name="API_CreateCommit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commitId](#API_CreateCommit_ResponseSyntax) **   <a name="CodeCommit-CreateCommit-response-commitId"></a>
The full commit ID of the commit that contains your committed file changes.
Type: String

 ** [filesAdded](#API_CreateCommit_ResponseSyntax) **   <a name="CodeCommit-CreateCommit-response-filesAdded"></a>
The files added as part of the committed file changes.
Type: Array of [FileMetadata](API_FileMetadata.md) objects

 ** [filesDeleted](#API_CreateCommit_ResponseSyntax) **   <a name="CodeCommit-CreateCommit-response-filesDeleted"></a>
The files deleted as part of the committed file changes.
Type: Array of [FileMetadata](API_FileMetadata.md) objects

 ** [filesUpdated](#API_CreateCommit_ResponseSyntax) **   <a name="CodeCommit-CreateCommit-response-filesUpdated"></a>
The files updated as part of the commited file changes.
Type: Array of [FileMetadata](API_FileMetadata.md) objects

 ** [treeId](#API_CreateCommit_ResponseSyntax) **   <a name="CodeCommit-CreateCommit-response-treeId"></a>
The full SHA-1 pointer of the tree information for the commit that contains the commited file changes.
Type: String

## Errors
<a name="API_CreateCommit_Errors"></a>

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

 ** FileContentAndSourceFileSpecifiedException **
The commit cannot be created because both a source file and file content have been specified for the same file. You cannot provide both. Either specify a source file or provide the file content directly.
HTTP Status Code: 400

 ** FileContentSizeLimitExceededException **
The file cannot be added because it is too large. The maximum file size is 6 MB, and the combined file content change size is 7 MB. Consider making these changes using a Git client.
HTTP Status Code: 400

 ** FileDoesNotExistException **
The specified file does not exist. Verify that you have used the correct file name, full path, and extension.
HTTP Status Code: 400

 ** FileEntryRequiredException **
The commit cannot be created because no files have been specified as added, updated, or changed (PutFile or DeleteFile) for the commit.
HTTP Status Code: 400

 ** FileModeRequiredException **
The commit cannot be created because no file mode has been specified. A file mode is required to update mode permissions for a file.
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
The specified file mode permission is not valid. For a list of valid file mode permissions, see [PutFile](API_PutFile.md).
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

 ** MaximumFileEntriesExceededException **
The number of specified files to change as part of this commit exceeds the maximum number of files that can be changed in a single commit. Consider using a Git client for these changes.
HTTP Status Code: 400

 ** NameLengthExceededException **
The user name is not valid because it has exceeded the character limit for author names.
HTTP Status Code: 400

 ** NoChangeException **
The commit cannot be created because no changes will be made to the repository as a result of this commit. A commit must contain at least one change.
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

 ** PutFileEntryConflictException **
The commit cannot be created because one or more files specified in the commit reference both a file and a folder.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

 ** RestrictedSourceFileException **
The commit cannot be created because one of the changes specifies copying or moving a .gitkeep file.
HTTP Status Code: 400

 ** SamePathRequestException **
The commit cannot be created because one or more changes in this commit duplicate actions in the same file path. For example, you cannot make the same delete request to the same file in the same file path twice, or make a delete request and a move request to the same file as part of the same commit.
HTTP Status Code: 400

 ** SourceFileOrContentRequiredException **
The commit cannot be created because no source files or file content have been specified for the commit.
HTTP Status Code: 400

## Examples
<a name="API_CreateCommit_Examples"></a>

### Example
<a name="API_CreateCommit_Example_1"></a>

This example illustrates one usage of CreateCommit.

#### Sample Request
<a name="API_CreateCommit_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.CreateCommit
X-Amz-Date: 201801219T224019Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "repositoryName": "MyDemoRepo",
   "branchName": "MyFeatureBranch",
   "parentCommitId": "4c925148EXAMPLE",
   "commitMessage": "I'm creating this commit to update a variable name in a number of files.",
   "authorName": "Saanvi Sarkar"
   "email": "saanvi_sarkar@example.com",
   "keepEmptyFolders": false,
   "putFiles": [
     {
       "filePath": "file1.py",
       "fileMode": "EXECUTABLE",
       "fileContent": "bucket_name = sys.argv[1] region = sys.argv[2]"
     },
     {
       "filePath": "file2.txt",
       "fileMode": "NORMAL",
       "fileContent": "//Adding a comment to explain the variable changes in file1.py"
     },
     {
       "filePath": "images/image1.png",
       "fileMode": "NORMAL",
       "sourceFile": {
         "filePath": "pictures/picture.png",
         "isMove": true
       }
     }
   ],
   "deleteFiles": [
     {
       "filePath": "ExampleSolution.py"
     }
   ]
}
```

#### Sample Response
<a name="API_CreateCommit_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Fri, 19 Dec 2018 22:40:19 GMT

{
   "commitId": "317f8570EXAMPLE",
   "treeId": "347a3408EXAMPLE",
   "filesAdded": [
        {
        "absolutePath": "images/image1.png",
        "blobId": "d68ba6ccEXAMPLE",
        "fileMode": "NORMAL"
        }
    ],
    "filesUpdated": [
        {
        "absolutePath": "file1.py",
        "blobId": "0a4d55a8EXAMPLE",
        "fileMode": "EXECUTABLE"
        },
        {
        "absolutePath": "file2.txt",
        "blobId": "915766bbEXAMPLE",
        "fileMode": "NORMAL"
        }
    ],
    "filesDeleted": [
        {
        "absolutePath": "ExampleSolution.py",
        "blobId": "4f9cebe6aEXAMPLE",
        "fileMode": "EXECUTABLE"
        },
        {
        "absolutePath": "pictures/picture.png",
        "blobId": "fb12a539EXAMPLE",
        "fileMode": "NORMAL"
        }
    ]
}
```

## See Also
<a name="API_CreateCommit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/CreateCommit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/CreateCommit)
