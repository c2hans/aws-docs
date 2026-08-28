---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestStatus.html
---

# UpdatePullRequestStatus
<a name="API_UpdatePullRequestStatus"></a>

Updates the status of a pull request.

## Request Syntax
<a name="API_UpdatePullRequestStatus_RequestSyntax"></a>

```
{
   "pullRequestId": "{{string}}",
   "pullRequestStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePullRequestStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pullRequestId](#API_UpdatePullRequestStatus_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestStatus-request-pullRequestId"></a>
The system-generated ID of the pull request. To get this ID, use [ListPullRequests](API_ListPullRequests.md).
Type: String
Required: Yes

 ** [pullRequestStatus](#API_UpdatePullRequestStatus_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestStatus-request-pullRequestStatus"></a>
The status of the pull request. The only valid operations are to update the status from `OPEN` to `OPEN`, `OPEN` to `CLOSED` or from `CLOSED` to `CLOSED`.
Type: String
Valid Values: `OPEN | CLOSED`
Required: Yes

## Response Syntax
<a name="API_UpdatePullRequestStatus_ResponseSyntax"></a>

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
<a name="API_UpdatePullRequestStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pullRequest](#API_UpdatePullRequestStatus_ResponseSyntax) **   <a name="CodeCommit-UpdatePullRequestStatus-response-pullRequest"></a>
Information about the pull request.
Type: [PullRequest](API_PullRequest.md) object

## Errors
<a name="API_UpdatePullRequestStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** InvalidPullRequestStatusException **
The pull request status is not valid. The only valid values are `OPEN` and `CLOSED`.
HTTP Status Code: 400

 ** InvalidPullRequestStatusUpdateException **
The pull request status update is not valid. The only valid update is from `OPEN` to `CLOSED`.
HTTP Status Code: 400

 ** PullRequestDoesNotExistException **
The pull request ID could not be found. Make sure that you have specified the correct repository name and pull request ID, and then try again.
HTTP Status Code: 400

 ** PullRequestIdRequiredException **
A pull request ID is required, but none was provided.
HTTP Status Code: 400

 ** PullRequestStatusRequiredException **
A pull request status is required, but none was provided.
HTTP Status Code: 400

## Examples
<a name="API_UpdatePullRequestStatus_Examples"></a>

### Example
<a name="API_UpdatePullRequestStatus_Example_1"></a>

This example illustrates one usage of UpdatePullRequestStatus.

#### Sample Request
<a name="API_UpdatePullRequestStatus_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.UpdatePullRequestStatus
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestStatus": "CLOSED",
   "pullRequestId": "47"
}
```

#### Sample Response
<a name="API_UpdatePullRequestStatus_Example_1_Response"></a>

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
                "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
                "approvalRuleId": "dd8b17fe-EXAMPLE",
                "approvalRuleName": "2-approvers-needed-for-this-change",
                "creationDate": 1571356106.936,
                "lastModifiedDate": 571356106.936,
                "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major",
                "ruleContentSha256": "4711b576EXAMPLE"
            }
        ],
        "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
        "clientRequestToken": "",
        "creationDate": 1508530823.165,
        "description": "Updated the pull request to remove unused global variable.",
        "lastActivityDate": 1508372423.12,
        "pullRequestId": "47",
        "pullRequestStatus": "CLOSED",
        "pullRequestTargets": [
            {
                "destinationCommit": "9f31c968EXAMPLE",
                "destinationReference": "refs/heads/main",
                "mergeMetadata": {
                    "isMerged": false,
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
<a name="API_UpdatePullRequestStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdatePullRequestStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdatePullRequestStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
