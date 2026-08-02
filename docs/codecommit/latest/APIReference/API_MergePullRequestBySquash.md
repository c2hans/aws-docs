---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergePullRequestBySquash.html
---

# MergePullRequestBySquash
<a name="API_MergePullRequestBySquash"></a>

Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the squash merge strategy. If the merge is successful, it closes the pull request.

## Request Syntax
<a name="API_MergePullRequestBySquash_RequestSyntax"></a>

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
   "email": "{{string}}",
   "keepEmptyFolders": {{boolean}},
   "pullRequestId": "{{string}}",
   "repositoryName": "{{string}}",
   "sourceCommitId": "{{string}}"
}
```

## Request Parameters
<a name="API_MergePullRequestBySquash_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [authorName](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-authorName"></a>
The name of the author who created the commit. This information is used as both the author and committer for the commit.
Type: String
Required: No

 ** [commitMessage](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-commitMessage"></a>
The commit message to include in the commit information for the merge.
Type: String
Required: No

 ** [conflictDetailLevel](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-conflictDetailLevel"></a>
The level of conflict detail to use. If unspecified, the default FILE\_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE\_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.
Type: String
Valid Values: `FILE_LEVEL | LINE_LEVEL`
Required: No

 ** [conflictResolution](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-conflictResolution"></a>
If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.
Type: [ConflictResolution](API_ConflictResolution.md) object
Required: No

 ** [conflictResolutionStrategy](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-conflictResolutionStrategy"></a>
Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.
Type: String
Valid Values: `NONE | ACCEPT_SOURCE | ACCEPT_DESTINATION | AUTOMERGE`
Required: No

 ** [email](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-email"></a>
The email address of the person merging the branches. This information is used in the commit information for the merge.
Type: String
Required: No

 ** [keepEmptyFolders](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-keepEmptyFolders"></a>
If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a .gitkeep file is created for empty folders. The default is false.
Type: Boolean
Required: No

 ** [pullRequestId](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-pullRequestId"></a>
The system-generated ID of the pull request. To get this ID, use [ListPullRequests](API_ListPullRequests.md).
Type: String
Required: Yes

 ** [repositoryName](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-repositoryName"></a>
The name of the repository where the pull request was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [sourceCommitId](#API_MergePullRequestBySquash_RequestSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-request-sourceCommitId"></a>
The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.
Type: String
Required: No

## Response Syntax
<a name="API_MergePullRequestBySquash_ResponseSyntax"></a>

```
{
   "pullRequest": {
      "approvalRules": [
         {
            "approvalRuleContent": "string",
            "approvalRuleId": "string",
            "approvalRuleName": "string",
            "creationDate": number,
            "lastModifiedDate": number,
            "lastModifiedUser": "string",
            "originApprovalRuleTemplate": {
               "approvalRuleTemplateId": "string",
               "approvalRuleTemplateName": "string"
            },
            "ruleContentSha256": "string"
         }
      ],
      "authorArn": "string",
      "clientRequestToken": "string",
      "creationDate": number,
      "description": "string",
      "lastActivityDate": number,
      "pullRequestId": "string",
      "pullRequestStatus": "string",
      "pullRequestTargets": [
         {
            "destinationCommit": "string",
            "destinationReference": "string",
            "mergeBase": "string",
            "mergeMetadata": {
               "isMerged": boolean,
               "mergeCommitId": "string",
               "mergedBy": "string",
               "mergeOption": "string"
            },
            "repositoryName": "string",
            "sourceCommit": "string",
            "sourceReference": "string"
         }
      ],
      "revisionId": "string",
      "title": "string"
   }
}
```

## Response Elements
<a name="API_MergePullRequestBySquash_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pullRequest](#API_MergePullRequestBySquash_ResponseSyntax) **   <a name="CodeCommit-MergePullRequestBySquash-response-pullRequest"></a>
Returns information about a pull request.
Type: [PullRequest](API_PullRequest.md) object

## Errors
<a name="API_MergePullRequestBySquash_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommitMessageLengthExceededException **
The commit message is too long. Provide a shorter string.
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

 ** FolderContentSizeLimitExceededException **
The commit cannot be created because at least one of the overall changes in the commit results in a folder whose contents exceed the limit of 6 MB. Either reduce the number and size of your changes, or split the changes across multiple folders.
HTTP Status Code: 400

 ** InvalidCommitIdException **
The specified commit ID is not valid.
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

 ** InvalidPathException **
The specified path is not valid.
HTTP Status Code: 400

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
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

 ** MultipleConflictResolutionEntriesException **
More than one conflict resolution entries exists for the conflict. A conflict can have only one conflict resolution entry.
HTTP Status Code: 400

 ** NameLengthExceededException **
The user name is not valid because it has exceeded the character limit for author names.
HTTP Status Code: 400

 ** PathRequiredException **
The folderPath for a location cannot be null.
HTTP Status Code: 400

 ** PullRequestAlreadyClosedException **
The pull request status cannot be updated because it is already closed.
HTTP Status Code: 400

 ** PullRequestApprovalRulesNotSatisfiedException **
The pull request cannot be merged because one or more approval rules applied to the pull request have conditions that have not been met.
HTTP Status Code: 400

 ** PullRequestDoesNotExistException **
The pull request ID could not be found. Make sure that you have specified the correct repository name and pull request ID, and then try again.
HTTP Status Code: 400

 ** PullRequestIdRequiredException **
A pull request ID is required, but none was provided.
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

 ** RepositoryNotAssociatedWithPullRequestException **
The repository does not contain any pull requests with that pull request ID. Use GetPullRequest to verify the correct repository name for the pull request ID.
HTTP Status Code: 400

 ** TipOfSourceReferenceIsDifferentException **
The tip of the source branch in the destination repository does not match the tip of the source branch specified in your request. The pull request might have been updated. Make sure that you have the latest changes.
HTTP Status Code: 400

 ** TipsDivergenceExceededException **
The divergence between the tips of the provided commit specifiers is too great to determine whether there might be any merge conflicts. Locally compare the specifiers using `git diff` or a diff tool.
HTTP Status Code: 400

## Examples
<a name="API_MergePullRequestBySquash_Examples"></a>

### Example
<a name="API_MergePullRequestBySquash_Example_1"></a>

This example illustrates one usage of MergePullRequestBySquash.

#### Sample Request
<a name="API_MergePullRequestBySquash_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.MergePullRequestBySquash
X-Amz-Date: 20190428T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestId": "47",
   "repositoryName": "MyDemoRepo",
   "sourceCommitId": "99132ab0EXAMPLE",
   "authorName": "Mary Major"
   "email": "mary_major@example.com",
   "commitMessage": "Merging this pull request after code review and acceptance tests passed."
}
```

#### Sample Response
<a name="API_MergePullRequestBySquash_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Sun, 28 Apr 2019 22:43:13 GMT

{
    "pullRequest": {
        "approvalRules": [
            {
                "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
                "approvalRuleId": "dd8b17fe-EXAMPLE",
                "approvalRuleName": "2-approver-rule-for-main",
                "creationDate": 1571356106.936,
                "lastModifiedDate": 571356106.936,
                "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major",
                "originApprovalRuleTemplate": {
                    "approvalRuleTemplateId": "dd8b17fe-EXAMPLE",
                    "approvalRuleTemplateName": "2-approver-rule-for-main"
                },
                "ruleContentSha256": "4711b576EXAMPLE"
            }
        ],
        "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
        "clientRequestToken": "",
        "creationDate": 1508530823.142,
        "description": "Review the latest changes and updates to the global variables",
        "lastActivityDate": 1508887223.155,
        "pullRequestId": "47",
        "pullRequestStatus": "CLOSED",
        "pullRequestTargets": [
            {
                "destinationCommit": "9f31c968EXAMPLE",
                "destinationReference": "refs/heads/main",
                "mergeMetadata": {
                    "isMerged": true,
                    "mergedBy": "arn:aws:iam::123456789012:user/Mary_Major"
                },
                "repositoryName": "MyDemoRepo",
                "sourceCommit": "99132ab0EXAMPLE",
                "sourceReference": "refs/heads/variables-branch"
            }
        ],
        "title": "Consolidation of global variables"
    }
}
```

## See Also
<a name="API_MergePullRequestBySquash_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/MergePullRequestBySquash)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/MergePullRequestBySquash)
