---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateUnreferencedMergeCommit.html
---

# CreateUnreferencedMergeCommit
<a name="API_CreateUnreferencedMergeCommit"></a>

Creates an unreferenced commit that represents the result of merging two branches using a specified merge strategy. This can help you determine the outcome of a potential merge. This API cannot be used with the fast-forward merge strategy because that strategy does not create a merge commit.

**Note**
This unreferenced merge commit can only be accessed using the GetCommit API or through git commands such as git fetch. To retrieve this commit, you must specify its commit ID or otherwise reference it.

## Request Syntax
<a name="API_CreateUnreferencedMergeCommit_RequestSyntax"></a>

```
{
   "authorName": "{{string}}",
   "commitMessage": "{{string}}",
   "conflictDetailLevel": "{{string}}",
   "conflictResolution": {
      "deleteFiles": [
         {
            "filePath": "{{string}}"
         }
      ],
      "replaceContents": [
         {
            "content": {{blob}},
            "fileMode": "{{string}}",
            "filePath": "{{string}}",
            "replacementType": "{{string}}"
         }
      ],
      "setFileModes": [
         {
            "fileMode": "{{string}}",
            "filePath": "{{string}}"
         }
      ]
   },
   "conflictResolutionStrategy": "{{string}}",
   "destinationCommitSpecifier": "{{string}}",
   "email": "{{string}}",
   "keepEmptyFolders": {{boolean}},
   "mergeOption": "{{string}}",
   "repositoryName": "{{string}}",
   "sourceCommitSpecifier": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateUnreferencedMergeCommit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [authorName](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-authorName"></a>
The name of the author who created the unreferenced commit. This information is used as both the author and committer for the commit.
Type: String
Required: No

 ** [commitMessage](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-commitMessage"></a>
The commit message for the unreferenced commit.
Type: String
Required: No

 ** [conflictDetailLevel](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-conflictDetailLevel"></a>
The level of conflict detail to use. If unspecified, the default FILE\_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE\_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.
Type: String
Valid Values: `FILE_LEVEL | LINE_LEVEL`
Required: No

 ** [conflictResolution](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-conflictResolution"></a>
If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.
Type: [ConflictResolution](API_ConflictResolution.md) object
Required: No

 ** [conflictResolutionStrategy](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-conflictResolutionStrategy"></a>
Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.
Type: String
Valid Values: `NONE | ACCEPT_SOURCE | ACCEPT_DESTINATION | AUTOMERGE`
Required: No

 ** [destinationCommitSpecifier](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-destinationCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

 ** [email](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-email"></a>
The email address for the person who created the unreferenced commit.
Type: String
Required: No

 ** [keepEmptyFolders](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-keepEmptyFolders"></a>
If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If this is specified as true, a .gitkeep file is created for empty folders. The default is false.
Type: Boolean
Required: No

 ** [mergeOption](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-mergeOption"></a>
The merge option or strategy you want to use to merge the code.
Type: String
Valid Values: `FAST_FORWARD_MERGE | SQUASH_MERGE | THREE_WAY_MERGE`
Required: Yes

 ** [repositoryName](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-repositoryName"></a>
The name of the repository where you want to create the unreferenced merge commit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [sourceCommitSpecifier](#API_CreateUnreferencedMergeCommit_RequestSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-request-sourceCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateUnreferencedMergeCommit_ResponseSyntax"></a>

```
{
   "commitId": "string",
   "treeId": "string"
}
```

## Response Elements
<a name="API_CreateUnreferencedMergeCommit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commitId](#API_CreateUnreferencedMergeCommit_ResponseSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-response-commitId"></a>
The full commit ID of the commit that contains your merge results.
Type: String

 ** [treeId](#API_CreateUnreferencedMergeCommit_ResponseSyntax) **   <a name="CodeCommit-CreateUnreferencedMergeCommit-response-treeId"></a>
The full SHA-1 pointer of the tree information for the commit that contains the merge results.
Type: String

## Errors
<a name="API_CreateUnreferencedMergeCommit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommitDoesNotExistException **
The specified commit does not exist or no commit was specified, and the specified repository has no default branch.
HTTP Status Code: 400

 ** CommitMessageLengthExceededException **
The commit message is too long. Provide a shorter string.
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

 ** FileContentSizeLimitExceededException **
The file cannot be added because it is too large. The maximum file size is 6 MB, and the combined file content change size is 7 MB. Consider making these changes using a Git client.
HTTP Status Code: 400

 ** FileModeRequiredException **
The commit cannot be created because no file mode has been specified. A file mode is required to update mode permissions for a file.
HTTP Status Code: 400

 ** FolderContentSizeLimitExceededException **
The commit cannot be created because at least one of the overall changes in the commit results in a folder whose contents exceed the limit of 6 MB. Either reduce the number and size of your changes, or split the changes across multiple folders.
HTTP Status Code: 400

 ** InvalidCommitException **
The specified commit is not valid.
HTTP Status Code: 400

 ** InvalidConflictDetailLevelException **
The specified conflict detail level is not valid.
HTTP Status Code: 400

 ** InvalidConflictResolutionException **
The specified conflict resolution list is not valid.
HTTP Status Code: 400

 ** InvalidConflictResolutionStrategyException **
The specified conflict resolution strategy is not valid.
HTTP Status Code: 400

 ** InvalidEmailException **
The specified email address either contains one or more characters that are not allowed, or it exceeds the maximum number of characters allowed for an email address.
HTTP Status Code: 400

 ** InvalidFileModeException **
The specified file mode permission is not valid. For a list of valid file mode permissions, see [PutFile](API_PutFile.md).
HTTP Status Code: 400

 ** InvalidMergeOptionException **
The specified merge option is not valid for this operation. Not all merge strategies are supported for all operations.
HTTP Status Code: 400

 ** InvalidPathException **
The specified path is not valid.
HTTP Status Code: 400

 ** InvalidReplacementContentException **
Automerge was specified for resolving the conflict, but the replacement type is not valid or content is missing.
HTTP Status Code: 400

 ** InvalidReplacementTypeException **
Automerge was specified for resolving the conflict, but the specified replacement type is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** ManualMergeRequiredException **
The pull request cannot be merged automatically into the destination branch. You must manually merge the branches and resolve any conflicts.
HTTP Status Code: 400

 ** MaximumConflictResolutionEntriesExceededException **
The number of allowed conflict resolution entries was exceeded.
HTTP Status Code: 400

 ** MaximumFileContentToLoadExceededException **
The number of files to load exceeds the allowed limit.
HTTP Status Code: 400

 ** MaximumItemsToCompareExceededException **
The number of items to compare between the source or destination branches and the merge base has exceeded the maximum allowed.
HTTP Status Code: 400

 ** MergeOptionRequiredException **
A merge option or stategy is required, and none was provided.
HTTP Status Code: 400

 ** MultipleConflictResolutionEntriesException **
More than one conflict resolution entries exists for the conflict. A conflict can have only one conflict resolution entry.
HTTP Status Code: 400

 ** NameLengthExceededException **
The user name is not valid because it has exceeded the character limit for author names.
HTTP Status Code: 400

 ** PathRequiredException **
The folderPath for a location cannot be null.
HTTP Status Code: 400

 ** ReplacementContentRequiredException **
USE\_NEW\_CONTENT was specified, but no replacement content has been provided.
HTTP Status Code: 400

 ** ReplacementTypeRequiredException **
A replacement type is required.
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
<a name="API_CreateUnreferencedMergeCommit_Examples"></a>

### Example
<a name="API_CreateUnreferencedMergeCommit_Example_1"></a>

This example illustrates one usage of CreateUnreferencedMergeCommit.

#### Sample Request
<a name="API_CreateUnreferencedMergeCommit_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 312
X-Amz-Target: CodeCommit_20150413.CreateUnReferencedMergeCommit
X-Amz-Date: 20190428T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "sourceCommitSpecifier": "bugfix-bug1234",
  "destinationCommitSpecifier": "main",
  "mergeOption": "THREE_WAY_MERGE",
  "authorName": "Maria Garcia",
  "email": "maria_garcia@example.com",
  "commitMessage": "Testing the merge of this bugfix branch to main."
}
```

#### Sample Response
<a name="API_CreateUnreferencedMergeCommit_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 220
Date: Sun, 28 Apr 2019 22:43:13 GMT

{
    "commitId": "4f178133EXAMPLE",
    "treeId": "389765daEXAMPLE"
}
```

## See Also
<a name="API_CreateUnreferencedMergeCommit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/CreateUnreferencedMergeCommit)
