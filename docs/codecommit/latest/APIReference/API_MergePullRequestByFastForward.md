---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergePullRequestByFastForward.html
---

# MergePullRequestByFastForward
<a name="API_MergePullRequestByFastForward"></a>

Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the fast-forward merge strategy. If the merge is successful, it closes the pull request.

## Request Syntax
<a name="API_MergePullRequestByFastForward_RequestSyntax"></a>

```
{
   "pullRequestId": "{{string}}",
   "repositoryName": "{{string}}",
   "sourceCommitId": "{{string}}"
}
```

## Request Parameters
<a name="API_MergePullRequestByFastForward_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pullRequestId](#API_MergePullRequestByFastForward_RequestSyntax) **   <a name="CodeCommit-MergePullRequestByFastForward-request-pullRequestId"></a>
The system-generated ID of the pull request. To get this ID, use [ListPullRequests](API_ListPullRequests.md).
Type: String
Required: Yes

 ** [repositoryName](#API_MergePullRequestByFastForward_RequestSyntax) **   <a name="CodeCommit-MergePullRequestByFastForward-request-repositoryName"></a>
The name of the repository where the pull request was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [sourceCommitId](#API_MergePullRequestByFastForward_RequestSyntax) **   <a name="CodeCommit-MergePullRequestByFastForward-request-sourceCommitId"></a>
The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.
Type: String
Required: No

## Response Syntax
<a name="API_MergePullRequestByFastForward_ResponseSyntax"></a>

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
<a name="API_MergePullRequestByFastForward_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pullRequest](#API_MergePullRequestByFastForward_ResponseSyntax) **   <a name="CodeCommit-MergePullRequestByFastForward-response-pullRequest"></a>
Information about the specified pull request, including the merge.
Type: [PullRequest](API_PullRequest.md) object

## Errors
<a name="API_MergePullRequestByFastForward_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidCommitIdException **
The specified commit ID is not valid.
HTTP Status Code: 400

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** ManualMergeRequiredException **
The pull request cannot be merged automatically into the destination branch. You must manually merge the branches and resolve any conflicts.
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

 ** ReferenceDoesNotExistException **
The specified reference does not exist. You must provide a full commit ID.
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

## Examples
<a name="API_MergePullRequestByFastForward_Examples"></a>

### Example
<a name="API_MergePullRequestByFastForward_Example_1"></a>

This example illustrates one usage of MergePullRequestByFastForward.

#### Sample Request
<a name="API_MergePullRequestByFastForward_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.MergePullRequestByFastForward
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestId": "47",
   "repositoryName": "MyDemoRepo",
   "sourceCommitId": "99132ab0EXAMPLE"
}
```

#### Sample Response
<a name="API_MergePullRequestByFastForward_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Wed, 25 Oct 2017 20:20:13 GMT

{
    "pullRequest": {
        "approvalRules": [
            {
                "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 1,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
                "approvalRuleId": "dd8b17fe-EXAMPLE",
                "approvalRuleName": "I want one approver for this pull request",
                "creationDate": 1571356106.936,
                "lastModifiedDate": 571356106.936,
                "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major",
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
<a name="API_MergePullRequestByFastForward_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/MergePullRequestByFastForward)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/MergePullRequestByFastForward)
